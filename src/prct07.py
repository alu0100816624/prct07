import modulo
t_uplas=(10,100,1000,10000,100000,1000000)
l=[]
for i in range(len(t_uplas)):
  m=modulo.aproximacion(t_uplas[i])
  l=l+[m]
print l
#El numero maximo de la t_upla es 6 y se producen errores a partir de 8. Los elemenotos de la t_upla sí se pueden definir en notación científica. .pyc permite a python ejecutar archivos de otros formatos.