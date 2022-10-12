# Reto #23
# MÁXIMO COMÚN DIVISOR Y MÍNIMO COMÚN MÚLTIPLO
# Fecha publicación enunciado: 07/06/22
# Fecha publicación resolución: 13/06/22
# Dificultad: MEDIA
#
# Enunciado: Crea dos funciones, una que calcule el máximo común divisor (MCD) y otra que calcule el mínimo común múltiplo (mcm) de dos números enteros.
# - No se pueden utilizar operaciones del lenguaje que lo resuelvan directamente.
#
# Información adicional:
# - Usa el canal de nuestro discord (https://mouredev.com/discord) "🔁reto-semanal" para preguntas, dudas o prestar ayuda a la comunidad.
# - Puedes hacer un Fork del repo y una Pull Request al repo original para que veamos tu solución aportada.
# - Revisaré el ejercicio en directo desde Twitch el lunes siguiente al de su publicación.
# - Subiré una posible solución al ejercicio el lunes siguiente al de su publicación.

def maxComunDivisor(n1, n2):
    while n1!=0 and n2!=0:
        aux = n2
        n2 = n1 % n2
        n1 = aux
    return n1 + n2

def minComunMultiplo(n1, n2):
    return int((n1 * n2) / maxComunDivisor(n1, n2))

print(maxComunDivisor(180,56))
print(minComunMultiplo(56,180))