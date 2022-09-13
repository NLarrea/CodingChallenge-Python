 # Reto #19
 # CONVERSOR TIEMPO
 # Fecha publicación enunciado: 09/05/22
 # Fecha publicación resolución: 16/05/22
 # Dificultad: FACIL
 #
 # Enunciado: Crea una función que reciba días, horas, minutos y segundos (como enteros) y retorne su resultado en milisegundos.
 #
 # Información adicional:
 # - Usa el canal de nuestro discord (https://mouredev.com/discord) "🔁reto-semanal" para preguntas, dudas o prestar ayuda a la comunidad.
 # - Puedes hacer un Fork del repo y una Pull Request al repo original para que veamos tu solución aportada.
 # - Revisaré el ejercicio en directo desde Twitch el lunes siguiente al de su publicación.
 # - Subiré una posible solución al ejercicio el lunes siguiente al de su publicación.

def timeToMillis(days,hours,mins,secs):
    daysToMillis = days * 24 * 60 * 60 * 1000
    hoursToMillis = hours * 60 * 60 * 1000
    minsToMillis = mins * 60 * 1000
    secsToMillis = secs * 1000
    return daysToMillis + hoursToMillis + minsToMillis + secsToMillis

print(timeToMillis(0,0,0,10))
print(timeToMillis(2,5,-45,10))
print(timeToMillis(2000000000,5,45,10))