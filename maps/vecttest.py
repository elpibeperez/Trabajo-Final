import map
mp = map.amap()
#mp.newvect("../imagenes/Mapas/Argentina.shp","", -8218228.769375612, -6128083.940903781, -4034538.5206617708, -2424383.204701764)
minx = -65.798047	#-73.566667
miny = -35.011637 	#-55.05
maxx = -61.730606	#-53.633333
maxy = -29.524866 	#-22.766667

l = minx-maxx
if(l<0):
    l = -l
a = miny-maxy
if(a<0):
    a = -a
y = 500*a/l
print (y,a,l)
mp.newvect("../imagenes/Mapas/Argentina.shp","", minx,miny,maxx,maxy,sizex=500, sizey = int(y))

