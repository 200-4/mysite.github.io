from django.http import HttpResponse

def index(request):
    return HttpResponse('hello,you are at polls app index')

# Create your views here.

