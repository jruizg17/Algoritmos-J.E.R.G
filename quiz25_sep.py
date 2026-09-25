#merge sort de una funcion que busca ciertos productos por encima de cierto precio para aplicar un descuento
#n es la cantidad de productos que esten en la lista con sus respectivos precios O(logn)
#se ejecuta mas veces al tener que revisar mas elementos tambien existiria la posibilidad de dividir la lista en mas listas por lo que pasa a ser O(nlogn)
#se invocan mas procesos dentro de la misma funcion, se aplican 2 mas aparte del principal
#listas enlazadas y arreglos dinamicos
#el codigo que elegi solo toma datos y no genera ningun tipo de proceso, por lo que el codigo en las 3 funciones es O(1) haciendo que la complejidad del codigo sea costante, osea 0
#en el mejor caso ningun producto supera el precio por lo que no siguen haciendo la siguiente funcion
#el peor caso es muchos precios superan el limite y tiene que invocar todas las funciones del codigo sin embargo ninguna complejidad en las funciones supera la complejidad O(1)
