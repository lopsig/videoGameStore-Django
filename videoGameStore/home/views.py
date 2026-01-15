from django.shortcuts import render

#Vista pagina principal
def index(request):
    #toma el request y el HTML que se quiere mostrar
    return render(request, 'home/index.html')

#vist pagina de contacto
def contact(request):
    return render(request, 'home/contact.html')
