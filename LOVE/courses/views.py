from django.shortcuts import render, get_object_or_404, redirect

from django.views.generic import(
	View,
)
from .models import Course
from .forms  import CourseModelForm
# Class Base View
#這是我們blog中用的class based view

# 取得指定id的物件，可用來作detail, update, delete
class CourseObjectMixin(object):
	model = Course
	lookup = 'pk'

	def get_object(self):
		pk = self.kwargs.get(self.lookup)
		obj = None # 設None原因應該是不要讓obj和id變成共享記憶體，不讓下一個物件影響上一個，所以只好預設None
		if id is not None:
			obj = get_object_or_404(self.model, id=pk)
		return obj


class CourseView(CourseObjectMixin, View):
	template_name = 'about.html'
	def get(self, request, *args, **kwargs):
		context = {'object': self.get_object()}
		return render(request, self.template_name, {}) #new_obj = CourseView()
	
# HTTP Method
# Function Base View
# 這是我們products用的function based view
def my_FunctionBaseView(request, *args, **kwargs):
	print(request.method) #GET method
	return render(request, 'about.html', {})


class CourseDetailView(CourseObjectMixin, View):
	template_name = 'courses/detail.html'
	def get(self, request, id, *args, **kwargs):
		if not id is None:
			obj = get_object_or_404(Course, id=id)
		context = {
			'object' : obj,
		} 
		return render(request, self.template_name,context)

class CourseListView(View):
	template_name = 'courses/list.html'
	queryset = Course.objects.all()
	
	def get(self, request, *args, **kwargs):
		context = {'object_list': self.queryset}
		queryset = Course.objects.all()
		return render(request, self.template_name, context)

	

class MyListView(CourseListView):
	queryset = Course.objects.all()
#跟上者同效果。

class CourseCreateView(View):
	template_name = 'courses/create.html'

	#因為是在class底下，所以會是CourseCreateView.get(CourseCreateView)
	#第一個參數就是self，class自我本身，第一個參數一定要是self，不然無法做別的動作 
	#進入create頁面
	def get(self, request, *args, **kwargs):
		form = CourseModelForm()
		context = {'form':form}
		return render(request, self.template_name, context) #new_obj = CourseView()
	
	#按下save後儲存此格式，post適用於save時候
	def post(self, request, *args, **kwargs):
		form = CourseModelForm(request.POST)
		if form.is_valid():
			form.save()
		form = CourseModelForm() #讓儲存後，裡面的文字域被清空
		context = {'form':form}
		return render(request, self.template_name, context)

class CourseUpdateView(CourseObjectMixin, View):
	template_name = 'courses/update.html'
	# def get_object(self):
	# 	id = self.kwargs.get('id')
	# 	obj = None #這行code功用是update後，在list頁面確實被更新，不然只有detail頁面更新
	# 	if id is not None: #這行if code還不知道意義在哪
	# 		obj = get_object_or_404(Course, id=id)
	# 	return obj

	def get(self, request, *args, **kwargs):
		obj = self.get_object()
		if obj is not None:
			form = CourseModelForm(instance=obj)
			#丟入參數instance，進入頁面會顯示目前的物件data
			context = {'form':form, 'object':obj}
		return render(request, self.template_name, context) #new_obj = CourseView()
	
	#按下save後儲存此格式，post適用於save時候
	def post(self, request, *args, **kwargs):
		obj = self.get_object()
		if obj is not None:
			form =CourseModelForm(request.POST, instance=obj) 
			#第一個參數是輸入的data到後端，也像是要用記性的方式POST一樣
			#第二個參數是輸入後的data要取代那個id的object，換句話說，如果沒有第二個的參數save後不是取代原本的，而是新建一個object
			if form.is_valid():
				form.save()
		form = CourseModelForm() #讓儲存後，裡面的文字域被清空
		context = {'form':form}

		return render(request, self.template_name, context)

class CourseDeleteView(CourseObjectMixin, View):
	template_name = 'courses/delete.html'
	# def get_object(self):
	# 	id = self.kwargs.get('id')
	# 	obj = None #這行code功用是update後，在list頁面確實被更新，不然只有detail頁面更新
	# 	if id is not None: #這行if code還不知道意義在哪
	# 		obj = get_object_or_404(Course, id=id)
	# 	return obj

	def get(self, request, *args, **kwargs):
		context = {} #由於context內容在條件式裡面，不會被定義到
		obj = self.get_object()
		if obj is not None: 
			context = {'object':obj}
		return render(request, self.template_name, context) #new_obj = CourseView()
	
	#按下save後儲存此格式，post適用於save時候
	def post(self, request, *args, **kwargs):
		context = {}
		obj = self.get_object()
		if obj is not None:
			obj.delete()
			context['object'] = None
			return redirect('/courses/')
		return render(request, self.template_name, context)

	


