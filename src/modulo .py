def aproximacion (fin):
  s=0.0
  for j in range (1,fin+1):
    xi= float ((j-0.5)/fin)
    fxi= float (4.0/(1.0+(xi**2)))
    s=s+fxi
    r=s/fin
  return r
if__name__=="__main__":
 fin=int (raw_input('Introduzca el numero de intervalos'))
 veces=int (raw_input('Introduzca el numero de veces'))
 l=[]
 for i in range(1,veces+1):
   m=aproximacion(fin*i)
   print m
   l=l+[m]
 print l
 