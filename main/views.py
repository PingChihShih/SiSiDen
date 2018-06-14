from django.shortcuts import render
from .models import Item, SingleOrder
from .forms import SingleOrderForm, TableForm

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
status_match = {
	"unsent": "未下單",
	"unconfirmed": "未確認",
	"confirmed": "已確認(待處理)",
	"making": "製作中",
	"payed": "已付款",
}

table = 13

def login(request):
	return render(request, 'login.html', {'form': TableForm()})

def order(request):
	global table
	# item: 顯示的物品名稱和敘述
	# single_order: 從單一個form get的資訊
	# form: 單一個form

	items = Item.objects.all()
	item3s = []
	n = len(items)//3 + 1 if ((len(items)%3) != 0) else 0
	for i in range(n):
		item3s.append(items[i*3:(i+1)*3])

	if request.method == 'POST':
		# get info about table
		try:
			tform = TableForm(request.POST)
			print(tform) # no this line not work, but not important...
			table = tform.cleaned_data['table']
		except:
			pass

		form = SingleOrderForm(request.POST)
		if form.is_valid():
			single_order = SingleOrder()
			try:
				single_order.name = Item.objects.get(pk=request.POST['item_id']).name
				print("[NAME]", single_order.name)
			except:
				pass
			single_order.temp = form.cleaned_data['temp']
			single_order.sugar = form.cleaned_data['sugar']
			single_order.count = form.cleaned_data['count']
			single_order.order_id = table
			single_order.save()

	forms = []
	for i in range(14):
		forms.append(SingleOrderForm())
	form = forms[0]

	arg = {'form': form,
		   'item3s': item3s,
		   'table': table}

	return render(request, 'order.html', arg)

def check(request):
	global table

	# delete single_order
	try:
		SingleOrder.objects.get(pk=request.POST['order_id']).delete()
	except:
		pass

	# show list of unsent single_order
	orders = SingleOrder.objects.filter(order_id=table, status='unsent')
	for single_order in orders:
		single_order.temp = temp_match[single_order.temp]
		single_order.sugar = sugar_match[single_order.sugar]

	form = TableForm()
	number_of_list = len(orders)
	arg = {'order': orders,
		   'number_of_list': number_of_list,
		   'form': form,
		   'table': table}
	return render(request, 'check.html', arg)

def result(request):
	global table
	if request.method == 'POST':
		print("Order Success!")
		new_orders = SingleOrder.objects.filter(order_id=table, status='unsent')
		new_orders.update(status='unconfirmed')

	orders = SingleOrder.objects.filter(order_id=table, status='unconfirmed')
	for single_order in orders:
		single_order.temp = temp_match[single_order.temp]
		single_order.sugar = sugar_match[single_order.sugar]
		single_order.status = status_match[single_order.status]

	number_of_list = len(orders)
	arg = {'order': orders,
		   'number_of_list': number_of_list,}
	return render(request, 'result.html', arg)

def manage(request):
	ranges = [i+1 for i in range(13)]
	range5 = []
	n = len(ranges)//5 + 1 if ((len(ranges)%5) != 0) else 0
	for i in range(n):
		range5.append(ranges[i*5:(i+1)*5])

	r = []
	if request.method == 'POST':
		# get table number
		for i in range(13):
			try:
				print(request.POST[str(i+1)])
				table = i+1
			except:
				pass
		r = SingleOrder.objects.filter(order_id=table).exclude(status="payed").exclude(status="unsent")
		number_of_list = len(r)
		arg = {'order': r,
			   'show_table': table,
			   'number_of_list': number_of_list}
		return render(request, 'manage_result.html', arg)

	arg = {'range5': range5,}
	return render(request, 'manage_table.html', arg)
