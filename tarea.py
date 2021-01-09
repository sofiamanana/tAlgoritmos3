'''
Nombre: cambios.
Input: un array arr y su tamaño n.
Return: void.
Descripcion: la funcion recorre el array, tomando pequeños segmentos de este (0..1,0..2,etc) y en la lista aux va registrando
la cantidad de elementos que estan en orden considerando que el elemento en la ultima posicion (posicion cont) no se mueve.
Si el numero en dicha posicion es el menor de la secuencia, se contara como que no hay elementos ordenados, para que cuenten
los ordenados, el elemento en la posicion cont tiene que estar dentro de alguna secuencia de orden. Por ejemplo, si se cuenta
al segmento [2,3,1], el elemento en la posicion cont es 1, y a pesar de que 2 y 3 si estan en orden, 1 no es parte, por lo que 
en la lista aux iria un 1 en la posicion cont.
'''

def cambios(arr,n):
    mayor=1 
    #Genera una lista de tamaño n, con 1 dentro de cada casilla
    aux = []
    for i in range(0,n):
        aux.append(1)
    
    for cont in range (1,n): 
        for cont2 in range(cont): 

            #Compara si el elemento en cont es mayor que el de cont2, el signo = para numero repetidos.
            if (arr[cont] >= arr[cont2]) and ((aux[cont2] + 1) > aux[cont]) : 
                aux[cont] = aux[cont2]+1

    #Busca el mayor numero en la lista aux.
    for elem in aux: 
        mayor = max(mayor,elem)     

    #Se resta n al numero mayor ya que este representa la mayor secuencia de numero ordenados, por ende el la resta
    #representaria el minimi numero de cambios que hacer en el arreglo.
    valor = n-mayor
    print(valor)

flag = True

while flag==True:
    try:

        line = input().split()
        n=int(line[0])
        lista=list(map(int,line[1:]))
        cambios(lista,n)

    except EOFError:
        flag= False

