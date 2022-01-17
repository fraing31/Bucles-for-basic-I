
#Básico: imprime todos los números enteros del 0 al 150.

for e in range(0, 151):
    print( e )

#Múltiplos de cinco: imprime todos los múltiplos de 5 entre 5 y 1,000.

for cin in range(0, 1001, 5):
    print( cin )

#Contar, a la manera del Dojo: imprime números enteros del 1 al 100. Si es divisible por 5, 
# imprime "Coding” en su lugar. Si es divisible por 10, imprime "Coding Dojo".

for countDojo in range(1, 101):
    if (countDojo % 10 == 0) and (countDojo % 5 == 0):
        print("Coding Dojo")
    elif (countDojo % 5 == 0) and not (countDojo % 10 == 0):
        print("Coding")
    else: 
        print(countDojo)

#Whoa. Es un gran idiota: agrega los enteros impares del 0 al 500,000, e imprime la suma final.

add = 0

for e in range(0,50) :
    if ( e % 2 > 0 ):
        add = add + e
print( add )


#Cuenta regresiva de a 4: imprime números positivos comenzando desde el 2018, en cuenta regresiva de 4 en 4.

reFour = 218
while reFour > 0:
    print( reFour )
    reFour = reFour - 4  


#Contador flexible: establece tres variables: lowNum, highNum, mult. Comenzando en lowNum y pasando por highNum, 
# imprime solo los enteros que sean múltiplos de mult. Por ejemplo, si lowNum=2, highNum=9 y mult=3. 
# El bucle debe imprimir 3, 6, 9 (en líneas sucesivas). 

lowNum = 30
hightNum = 45
mult = 5

for countFlex in range(lowNum, hightNum+1,):
    if ( countFlex % mult == 0):
        print(countFlex)





