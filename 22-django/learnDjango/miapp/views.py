from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
"""
MVC = Modelo Vista controlador -> Acciones(metodos)
MVT = Modelo Template Vista -> Acciones(metodos)
"""

#menú de navegación
layout = """
<h1>Sitio web con Django</h1>

<ul>
    <li>
        <a href="/">Inicio</a>
    </li>
    <li>
        <a href="/hola-mundo">Hola mundo</a>
    </li>
    <li>
        <a href="/pagina-pruebas">Página de pruebas</a>
    </li>
    <li>
        <a href="/contacto-dos">Contacto</a>
    </li>
</ul>


"""

def index(request):

    """
    html = ""
        <h1>Inicio</h1>
        <p>Años hasta el 2050</p>
        <ul>
    ""

    year = 2021

    while year <= 2050:
        if year % 2 == 0:
            html += f"<li>{year}</li>"
        year +=1

    html += "</ul>"
    """

    year = 2021
    hasta = range(year, 2051)

    nombre = 'Isabel Blanco'

    lenguajes = ['TypeScript','Python', 'C#','C++']

    return render(request,'index.html', {
        'title': 'Inicio',
        'mi_variable': 'Soy un dato que esta en la vista',
        'nombre' : nombre,
        'lenguajes' : lenguajes,
        'years': hasta
    })

def hola_mundo(request):
    return render(request, 'hola_mundo.html')

def pagina(request, redirigir=0):

    if redirigir == 1:
        return redirect('/contacto/', nombre="Isabel", apellidos="Blanco")

    return render(request,'pagina.html', {
        'texto': 'Lista de la compra',
        'lista': ['Zanahorias', 'lechuga', 'Tofu', 'Seitan']
    })

def contacto(request, nombre="", apellidos=""):

    html = ""

    if nombre and apellidos:
        html += "<p>El nombre completo es: </p>"
        html += f"<h3>{nombre} {apellidos}</h3>"
    
    return HttpResponse(layout+f"<h2>Contacto</h2>"+html)