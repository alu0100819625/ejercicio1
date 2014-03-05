#! /usr/bin/python
n= int(raw_input('Valor de n: '))
if n!=0:
 sumatorio=0
 PI=3.14159265358979323846264338327950288
 for i in range(1,n+1):
   a= float (i-1)/n
   b= float (i)/n
   xi=float(i-0.5)/n
   fxi= 4.0/(1.0+xi*xi)
   print a,b,xi,fxi
   sumatorio+=fxi
 pi= float(sumatorio)/n
 print 'El valor aproximado de PI es:', pi
 print 'El valor de PI con 35 decimales es: %1.35g' %PI
