def aproximacion (fin):
  s=0.0
  for j in range (1,fin+1):
    xi= float ((j-0.5)/fin)
    fxi= float (4.0/(1.0+(xi**2)))
    s=s+fxi
    r=s/fin
  return r
if __name__=='__main__':
 import sys
 if(len(sys.argv)==3):
   n=int(sys.argv[1])
   veces=int(sys.argv[2])
 else:
    print"Debe introducir n(intervalos) y veces(de ejecucion). Por defecto seran 6 intervalos y 6 ejecuciones"
    n=6
    veces=6
 l=[]
 for i in range(1,veces+1):
     m=aproximacion(n)
     l=l+[m]
 print l
 