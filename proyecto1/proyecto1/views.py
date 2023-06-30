from django.template import loader
from django.http import HttpResponse



def startpage(self):
    
    plantilla = loader.get_template("startpage.html")
    document = plantilla.render()
    return HttpResponse(document)