from django.shortcuts import render

# Create your views here.
def order(request):
	return render(request, 'order.html')

def result(request):
	return render(request, 'result.html')
