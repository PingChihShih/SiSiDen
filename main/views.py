from django.shortcuts import render
from .models import Item, SingleOrder
from .forms import SingleOrderForm

# Create your views here.

def order(request):
	item = Item()
	single_order = SingleOrder()
	item.name = "豪郝喝咖啡"
	item.description = "豪郝喝~~~"
	form = SingleOrderForm()

	if request.method == 'POST':
		form = SingleOrderForm(request.POST)
		if form.is_valid():
			single_order.name = item.name
			single_order.temp = form.cleaned_data['single']


	arg = {'item': item, 'form': form}
	return render(request, 'order.html', arg)

def result(request):
	return render(request, 'result.html')
