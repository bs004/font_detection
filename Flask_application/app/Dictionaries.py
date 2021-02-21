# -*- coding: utf-8 -*-

Font_Mapping={'Oswald':0,'Roboto':1,'Open_Sans':2,'Ubuntu':3,'PT_Serif':4,'Dancing_Script':5,'Fredoka_One':6,'Arimo':7,'Noto_Sans':8,'Patua_One':9}
Reverse_Font_Mapping=dict([(v,k) for (k,v) in Font_mapping.items()])

def dict_return(x,y,width,height,font,confidence):
  return {"boundingBox": { "x": x, "y": y, "width": width, "height": height }, "font": font, "confidence": confidence}