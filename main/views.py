from django.shortcuts import render
from .models import Item, SingleOrder
from .forms import SingleOrderForm, TableForm
from django.http import HttpResponseForbidden
from django.core.exceptions import PermissionDenied

from django.contrib import auth
from django.shortcuts import redirect

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
	if request.method == 'POST':
		user = auth.authenticate(username=request.POST['table'], password=request.POST['password'])
		print(request.POST['table'], request.POST['password'])
		print(user)
		if user:
			auth.login(request, user)
			if user.is_superuser:
				return redirect('manage')
			return redirect('order')

	return render(request, 'login.html', {'form': TableForm()})

def order(request):
	if not request.user.is_active:
		print(request.user)
		return redirect('login')
	else:
		print(request.user)
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
			single_order.order_id = request.user.username
			single_order.save()

	forms = []
	for i in range(14):
		forms.append(SingleOrderForm())
	form = forms[0]

	arg = {'form': form,
		   'item3s': item3s,
		   'table': request.user.username}

	return render(request, 'order.html', arg)

def check(request):
	if not request.user.is_active:
		return redirect('login')
	# delete single_order
	try:
		SingleOrder.objects.get(pk=request.POST['order_id']).delete()
	except:
		pass

	# show list of unsent single_order
	orders = SingleOrder.objects.filter(order_id=request.user.username, status='unsent')
	for single_order in orders:
		single_order.temp = temp_match[single_order.temp]
		single_order.sugar = sugar_match[single_order.sugar]

	form = TableForm()
	number_of_list = len(orders)
	arg = {'order': orders,
		   'number_of_list': number_of_list,
		   'form': form,
		   'table': request.user.username}
	return render(request, 'check.html', arg)

def result(request):
	if not request.user.is_active:
		return redirect('login')

	if request.method == 'POST':
		print("Order Success!")
		new_orders = SingleOrder.objects.filter(order_id=request.user.username, status='unsent')
		new_orders.update(status='unconfirmed')

	orders = SingleOrder.objects.filter(order_id=request.user.username).exclude(status='unsent')
	for single_order in orders:
		single_order.temp = temp_match[single_order.temp]
		single_order.sugar = sugar_match[single_order.sugar]
		single_order.status = status_match[single_order.status]

	number_of_list = len(orders)
	arg = {'order': orders,
		   'number_of_list': number_of_list,
		   'table': request.user.username}
	return render(request, 'result.html', arg)

def manage(request):
	if not request.user.is_superuser:
		raise PermissionDenied

	ranges = [i+1 for i in range(13)]
	range5 = []
	n = len(ranges)//5 + 1 if ((len(ranges)%5) != 0) else 0
	for i in range(n):
		range5.append(ranges[i*5:(i+1)*5])
	new_notify = []
	# notify new orders
	for i in range(1, 13):
		if SingleOrder.objects.filter(order_id=i, status='confirmed'):
			new_notify.append(i)


	r = []
	table = 0
	update = False
	if request.method == 'POST':
		# get table number
		try:
			if request.POST['table_no']:
				print("MODE: status confirmed")
				update = True
				table = request.POST['table_no']
		except:
			pass
		if not update:
			print("MODE: select table")
			for i in range(13):
				try:
					print(request.POST[str(i+1)])
					table = i+1
				except:
					pass
		r = SingleOrder.objects.filter(order_id=table).exclude(status="payed").exclude(status="unsent")
		if update:
			print("Table", table, "order updated")
			r.filter(status="unconfirmed").update(status='confirmed')
		for single_order in r:
			single_order.temp = temp_match[single_order.temp]
			single_order.sugar = sugar_match[single_order.sugar]
			single_order.status = status_match[single_order.status]
		number_of_list = len(r)
		arg = {'order': r,
			   'table': table,
			   'number_of_list': number_of_list,
			   'unconfirmed': "未確認"}
		return render(request, 'manage_result.html', arg)

	arg = {'range5': range5, 'new_notify': new_notify}
	return render(request, 'manage_table.html', arg)
