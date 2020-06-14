# coding=UTF-8<code>

from django.shortcuts import render, get_object_or_404, redirect

from .models import Product

from .forms import ProductForm, RawProductForm

from django.http import Http404
# Create your views here.
def product_detail_view(request, pk):
	obj = Product.objects.get(id=pk)
	#context = {
	#		'tilte' : obj.tilte,
	#		'description': obj.description
	#	} 沒有效率


	context = {
			'obj' : obj
		} #利用字典直接將物件設為變數，其屬性直接obj.xxx

	return render(request,"product/detail.html",context)

def product_create_view(request):
	form = ProductForm(request.POST or None)
	if form.is_valid():
		form.save()
		form = ProductForm() # 將表格內容的數字清空
 
	context = {
			'form' : form
		} 
	return render(request,"product2/create3.html",context)

def product_create2_view(request):
	if request.method	 == "POST":
		new_tilte = request.POST.get('tilte')
		print(new_tilte)

	context = {}
	return render(request, "product2/create2.html")

def product_create3_view(request):
	form2 = RawProductForm()

	if request.method == "POST":
		form2 = RawProductForm(request.POST) #裡頭沒有輸入參數：reqest.POST，data不會被輸入到後台
		if form2.is_valid():
			print(form2.cleaned_data) 
			# 經過valid合格後就是cleaned_data
			# cleaned_data在django.form模組中底下某模組的某類某屬性
			Product.objects.create(**form2.cleaned_data) #.create()裡面只能輸入一個參數，在前投加上兩個**就能突破限制，本來裡面的變數有3個參數。
			# 呼喚這個物件的create()方法，會在django內建網頁實體地創造出product頁面連結。
		else:
			print(form2.errors)
	context = {
		"form" : form2 
	}
	return render(request,'product2/create3.html',context)

def render_initial_data(request): # initial data和editing data都能儲存在實體頁面裡
	initial_data = {
		"description": "render_initial_description",
	}	
	obj = Product.objects.get(id=27) #一開始登入頁面輸入域中就會呈現product(id=27)的data
	form = ProductForm(request.POST or None, initial=initial_data, instance=obj)
	if form.is_valid():
		form.save()
	context = {
		'form': form
	}
	return render(request, "product2/create3.html", context)

def dynamic_lookup_view(request, my_id):
	#  obj = Product.objects.get(id=my_id)

	#第一種可取得物件和顯示404，比較簡潔。
	obj = get_object_or_404(Product, id=my_id)
	# 第二種方法:
	# try:
	# 	obj = Product.objects.get(id=my_id)
	# except Product.DoesNotExist:
	# 	raise Http404
	context = {
		"obj" : obj
	}
	return render(request, "product/detail.html", context)

def product_delete_view(request, id):
	obj = get_object_or_404(Product, id=id)
	if request.method == "POST": 
	#如果沒有這個if的動作，obj.delete()會執行於GET request，也就是只要一訪問網頁就是GET request，就馬上執行delete()的動作。
		obj.delete()
		return redirect('../../list') 
		#刪除完進行回傳url，首先刪除delete/，再來刪掉id/，來到127.0.0.1:8000/products/list。
	
	context = {
		'obj': obj
	}
	return render(request, "product2/delete.html", context)

def product_list_view(request):
	queryset = Product.objects.all() # list or objects
	
	context = {
		"obj_list": queryset
	}
	
	return render(request, "product2/list.html", context)









