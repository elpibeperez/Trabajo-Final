import mapscript
import Image
import random

DIRECTORIO_BASE = '/home/perez/django_test/sistema/'


class amap():
    image = None
    meta = None
    zoom = 1
    outtype = "JPEG"
    imagespath = DIRECTORIO_BASE+"maps/"
    templatepath = DIRECTORIO_BASE+"maps/"
    sizex = 400
    sizey = 300
    image_name = "image"

    def generate_layer(self,tipo, num):
        lay = mapscript.layerObj()
        lay.name = "lay1"
        lay.status = mapscript.MS_DEFAULT #defaul

#        lay.data = self.image.path
        lay.data = self.image
        if tipo == "tiff":
            lay.type = mapscript.MS_LAYER_RASTER
            self.bandset(lay, num)
        elif tipo == "polygon":
            st = mapscript.styleObj()
            #st.outlinecolor = mapscript.colorObj(100,100,100)
            st.color = mapscript.colorObj(255,255,255)
            cl = mapscript.classObj()
            cl.insertStyle(st)
            lay.type = mapscript.MS_LAYER_LINE
            lay.insertClass(cl)
        return lay

#Toma un tipo lay, te toca el tema del numero de bandas en el caso
#que se trabaje con TIFF
    def bandset(self, lay, num):
        if num == 1:
            lay.addProcessing("BANDS=1")
        elif num == 2:
            lay.addProcessing("BANDS=1,2")
        elif num == 3:
            lay.addProcessing("BANDS=1,2,3")
        return lay

    def generate_map(self, in_t, minx, miny, maxx, maxy,lay):
        map = mapscript.mapObj()
        map.name = "Map"
        map.setSize(self.sizex,self.sizey)
        map.setImageType(self.outtype)
        map.imagecolor = mapscript.colorObj(0,0,0)
        map.units = mapscript.MS_METERS
        map.extent = mapscript.rectObj(minx,miny,maxx,maxy)
        map.web = mapscript.webObj()
        map.web.template = self.templatepath
        map.web.imagepath = self.imagespath
        map.web.imageurl = "/tmp"
        map.shapepath = DIRECTORIO_BASE+"maps/"
        map.insertLayer(lay)
        return map

#Solo funciona para los formatos de imagenes soportados por Image
    def calculatey(self):
        fo = Image.open(self.image)
#        print fo.path
        x = float(fo.size[0])
        y = float(fo.size[1])
        return int((self.sizex/x)*y)

    def image_pos(self):
        fh = open(self.meta)
        lst = fh.readlines()
#aca calculo el size de los pix para x
        sizex = float(lst[0][0:len(lst[0])-2])
#aca calculo el size de los pix para y
        sizey = float(lst[3][0:len(lst[3])-2])
        minx = 	float(lst[4][0:len(lst[4])-2])
        maxy = 	float(lst[5][0:len(lst[5])-2])
        maxx = minx + self.sizex*sizex
        miny = maxy + self.sizey*sizey #(porque) sizey es negativo
        return (minx,maxx,miny,maxy)

    def draw_image(self,map):
        image_name = self.image_name \
                + str(random.randrange(999999)).zfill(6) \
                + ".jpg"
        img=map.draw()
        img.save(self.imagespath + image_name)
        return image_name

    def newmap(self, image, meta, bands=1, name="image", \
                sizex=400, tipo="tiff", out="JPEG"):
        self.image = image
        self.meta = meta
        self.outtype = out
        self.sizex =sizex
        self.sizey = self.calculatey()
        self.image_name = name
        lay = self.generate_layer("tiff", bands)
        pos = self.image_pos()
        map = self.generate_map(tipo,pos[0],pos[2],pos[1],pos[3],lay)
        return self.draw_image(map)

    def newvect(self, image, meta, minx, miny, maxx, maxy, name="vect",\
                sizex=600, sizey=600, tipo="polygon", out="JPEG"):
        self.image = image
        self.meta = meta
        self.outtype = out
        self.sizex = sizex
        self.sizey = sizey
        self.image_name = name
        lay = self.generate_layer(tipo, "")
        map = self.generate_map(tipo, minx, miny, maxx, maxy,lay)
        return self.draw_image(map)
