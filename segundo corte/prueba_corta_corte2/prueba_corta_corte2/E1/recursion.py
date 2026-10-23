# ============================================================
#  Prueba corta · Segundo corte · EJERCICIO 1  (25 puntos)
#  Tema: recursion y exploracion de caminos
#  Sistema: TurnoJusto — calculo de rutas de atencion
#
#  NO MODIFIQUE el archivo pruebas_e1.py
#  Ejecute:   python3 pruebas_e1.py
# ============================================================


def suma_impares(n):
    """Devuelve la suma de todos los numeros impares desde 1 hasta n (incluido).
       Ejemplos:  suma_impares(5) -> 9     (1 + 3 + 5)
                  suma_impares(0) -> 0     (no hay impares)

       DEFECTO REPORTADO: con ciertas entradas el programa se cae.
       Revise el caso base."""
    if n == 0:
        return 0
    if n % 2 == 0:
        return suma_impares(n - 1)
    return n + suma_impares(n - 1)


def contar_caminos(f, c):
    if f==1 or c==1:
        return 1
    return contar_caminos(f - 1, c) + contar_caminos(f, c - 1)


print("suma_impares(5)=", suma_impares(5))  
print("suma_impares(0)=", suma_impares(0))  
print("suma_impares(1)=", suma_impares(1))
print("suma_impares(10)=", suma_impares(10))
print("contar_caminos(3,3)=", contar_caminos(3,3))  
print("contar_caminos(2,4)=", contar_caminos(2,4))  
print("contar_caminos(4,4)=", contar_caminos(4,4)) 
print("contar_caminos(1,9)=", contar_caminos(1,9)) 


