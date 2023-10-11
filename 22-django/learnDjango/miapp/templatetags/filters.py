from django import template

register = template.Library()

#funcionalidad previa para decorar#
@register.filter(name='saludo')
def saludo(value):

    largo = ''
    if len(value) >= 8:
        largo = "Tú nombre es demasiado largo"

    return f"<h1 style='background:pink;color:black;'>Bienvenida, {value}</h1>"+largo