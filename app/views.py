from django.template import loader
from django.http import HttpResponse

def Home(request):
    # Load the template using the path relative to the templates directory in your app folder
    template = loader.get_template("index.html")
    # Render the template with an empty context and return it as an HTTP response
    return HttpResponse(template.render({}, request))


def Signup(request):
    template = loader.get_template('signup.html')
    return HttpResponse(template.render({}, request))

def Signin(request):
    template = loader.get_template('signin.html')
    return HttpResponse(template.render({}, request))