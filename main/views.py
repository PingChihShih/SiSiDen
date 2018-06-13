from django.shortcuts import render
from .models import Item, SingleOrder
from .forms import SingleOrderForm, TableForm

# Create your views here.

temp_match = {
	"iced": "正常冰",
	"little-iced": "少冰",
	"cool": "去冰",
	"hot": "熱",
}
sugar_match = {
	"normal": "正常糖",
	"little": "少糖",
	"no": "無糖",
}

def order(request):
	# item: 顯示的物品名稱和敘述
	# single_order: 從單一個form get的資訊
	# form: 單一個form
	item = Item()
	single_order = SingleOrder()
	item = Item.objects.get(pk=1)

	if request.method == 'POST':
		form = SingleOrderForm(request.POST)
		if form.is_valid():
			single_order.name = item.name
			single_order.temp = form.cleaned_data['temp']
			single_order.sugar = form.cleaned_data['sugar']
			single_order.count = form.cleaned_data['count']
			single_order.order_id = 1
			single_order.save()
			print("Order Saved!")

	form = SingleOrderForm()
	arg = {'item': item, 'form': form}
	return render(request, 'order.html', arg)

def check(request):
	target_order_id = 1

	try:
		SingleOrder.objects.get(pk=request.POST['order_id']).delete()
	except:
		pass

	orders = SingleOrder.objects.filter(order_id=target_order_id, status='unsent')
	for single_order in orders:
		single_order.temp = temp_match[single_order.temp]
		single_order.sugar = sugar_match[single_order.sugar]

	# TODO table UI and Certification
	form = TableForm()
	number_of_list = len(orders)
	arg = {'order': orders,
		   'number_of_list': number_of_list,
		   'form': form}
	return render(request, 'check.html', arg)

def result(request):
	target_order_id = 1
	if request.method == 'POST':
		print("Order Success!")
		new_orders = SingleOrder.objects.filter(order_id=target_order_id, status='unsent')
		new_orders.update(status='unconfirmed')

	orders = SingleOrder.objects.filter(order_id=target_order_id, status='unconfirmed')
	for single_order in orders:
		single_order.temp = temp_match[single_order.temp]
		single_order.sugar = sugar_match[single_order.sugar]

	ack_msg = ""
	# TODO check if the order is done

	number_of_list = len(orders)
	arg = {'order': orders,
		   'number_of_list': number_of_list,
		   'ack_msg': ack_msg}
	return render(request, 'result.html', arg)
