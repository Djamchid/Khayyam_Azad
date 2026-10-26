"""Attach imported Latin combining marks using a separate OpenType GPOS 'mark' feature."""
from fontTools.ttLib import TTFont
from fontTools.ttLib.tables import otTables as ot
import unicodedata

def anchor(x,y):
    a=ot.Anchor();a.Format=1;a.XCoordinate=int(x);a.YCoordinate=int(y);return a

def update(path):
    f=TTFont(path)
    cmap=f.getBestCmap()
    pairs={v:u for u,v in cmap.items() if v.startswith('kaLatin_')}
    marks=sorted((n for n,u in pairs.items() if unicodedata.category(chr(u)).startswith('M')),key=f.getGlyphID)
    bases=sorted((n for n,u in pairs.items() if not unicodedata.category(chr(u)).startswith('M')),key=f.getGlyphID)
    if not marks:return f
    glyf=f['glyf']
    def bounds(n):
        g=glyf[n];g.recalcBounds(glyf)
        return g.xMin,g.yMin,g.xMax,g.yMax
    def cl(u):
        return 1 if unicodedata.combining(chr(u)) in (202,216,218,220,222,224,226,228) else 0
    classes={n:cl(pairs[n]) for n in marks}
    st=ot.MarkBasePos();st.Format=1
    st.MarkCoverage=ot.Coverage();st.MarkCoverage.glyphs=marks
    st.BaseCoverage=ot.Coverage();st.BaseCoverage.glyphs=bases
    st.ClassCount=2
    ma=ot.MarkArray();ma.MarkCount=len(marks);ma.MarkRecord=[]
    for n in marks:
        xmin,ymin,xmax,ymax=bounds(n)
        rec=ot.MarkRecord();rec.Class=classes[n]
        rec.MarkAnchor=anchor((xmin+xmax)/2,ymax if classes[n]==1 else ymin)
        ma.MarkRecord.append(rec)
    st.MarkArray=ma
    ba=ot.BaseArray();ba.BaseCount=len(bases);ba.BaseRecord=[]
    for n in bases:
        xmin,ymin,xmax,ymax=bounds(n)
        rec=ot.BaseRecord()
        x=f['hmtx'][n][0]/2
        rec.BaseAnchor=[anchor(x,ymax+65),anchor(x,ymin-65)]
        ba.BaseRecord.append(rec)
    st.BaseArray=ba
    look=ot.Lookup();look.LookupType=4;look.LookupFlag=0;look.SubTable=[st];look.SubTableCount=1
    table=f['GPOS'].table;li=len(table.LookupList.Lookup)
    table.LookupList.Lookup.append(look);table.LookupList.LookupCount+=1
    ft=ot.Feature();ft.FeatureParams=None;ft.LookupListIndex=[li];ft.LookupCount=1
    fr=ot.FeatureRecord();fr.FeatureTag='mark';fr.Feature=ft
    fi=len(table.FeatureList.FeatureRecord)
    table.FeatureList.FeatureRecord.append(fr);table.FeatureList.FeatureCount+=1
    sr=next((a for a in table.ScriptList.ScriptRecord if a.ScriptTag=='latn'),None)
    if sr is None:
        sr=ot.ScriptRecord();sr.ScriptTag='latn';sr.Script=ot.Script()
        sr.Script.DefaultLangSys=ot.LangSys()
        sr.Script.DefaultLangSys.LookupOrder=None
        sr.Script.DefaultLangSys.ReqFeatureIndex=0xFFFF
        sr.Script.DefaultLangSys.FeatureIndex=[]
        sr.Script.DefaultLangSys.FeatureCount=0
        sr.Script.LangSysRecord=[];sr.Script.LangSysCount=0
        table.ScriptList.ScriptRecord.append(sr)
        table.ScriptList.ScriptRecord.sort(key=lambda r:r.ScriptTag)
        table.ScriptList.ScriptCount+=1
    sr.Script.DefaultLangSys.FeatureIndex.append(fi)
    sr.Script.DefaultLangSys.FeatureCount+=1
    gdef=f['GDEF'].table
    if gdef.GlyphClassDef:
        for n in marks:gdef.GlyphClassDef.classDefs[n]=3
    f.save(path)
    print('Latin mark positioning feature built:',len(marks),'marks',len(bases),'base glyphs')
    return TTFont(path)

f=update('fonts/KhayyamAzad-Regular.ttf')
f.flavor='woff2'
f.save('fonts/KhayyamAzad-Regular.woff2')
