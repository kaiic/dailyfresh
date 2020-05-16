from django import HttpResponse


def index(request):
	return HttpResponse('index')


