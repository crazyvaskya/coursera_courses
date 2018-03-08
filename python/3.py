import sys
a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])

D = b*b-4*a*c

if D < 0 or a==0:
    print('ALARM')
else:

    x1= (-b + D**0.5)/(2*a)
    x2= (-b - D**0.5)/(2*a)

    print ('x1=', x1)
    print ('x2=', x2)