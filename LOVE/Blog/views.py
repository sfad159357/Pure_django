from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.views.generic import(
	CreateView,
	DetailView,
	ListView,
	UpdateView,
	DeleteView,
	View,
	)

from .models import Article
from .forms import ArticleForm

# 有ListView這django內建模組，也不用return render(...)
class ArticleListView(ListView):
	queryset = Article.objects.all()
	template_name = 'blog/article_list.html'
	# 透過這個才能跟前端的樣式網頁做連結

class ArticleDetailView(DetailView):
	# 過濾obj的id > 1的網頁，如果訪客訪問no.1的網頁，就會出現404，page not found。
	queryset = Article.objects.filter(id__gt=1)
	template_name = 'blog/article_detail.html'

	# 這個function是DetailView模組內建的函式，而ListView沒有
	# 這個函式的用意是為了讓此url的path('<int:id>')標籤裡頭可以輸入的是"id"。
	# 但我把它改成<int:akb48>，比較不會混淆。
	# 所謂的self，不是網頁實體的物件，而是訪客訪問的request data。
	def get_object(self):
		id = self.kwargs.get("akb48")
	# 	#這裏kwargs.get("xx")對照url裡path('<int:xx>')
		return get_object_or_404(Article, id=id)
		# 這裡返回給訪客的是，將一個網址no.對照成物件的no.
		# 實體出來後會到template前端html樣板進行呈現
		# 若沒有對應的no.，就會產生404，page not found.

class ArticleCreateView(CreateView):
	queryset = Article.objects.all()
	template_name = 'blog/article_create.html'
	form_class = ArticleForm
	
	#
	def form_valid(self, form):
		print(form.cleaned_data)
		return super().form_valid(form)

	# create完物件後，網址立馬跳http://127.0.0.1:8000+"XXX"
	def get_success_url(self):
		return '/blog'


class ArticleUpdateView(UpdateView):
	queryset = Article.objects.all()
	template_name = 'blog/article_create.html'
	form_class = ArticleForm
	
	#
	def form_valid(self, form):
		print(form.cleaned_data)
		return super().form_valid(form)

	# create完物件後，網址立馬跳http://127.0.0.1:8000+"XXX"
	def get_success_url(self):
		return "/blog"

	def get_object(self):
		id = self.kwargs.get("akb48")
	# 	#這裏kwargs.get("xx")對照url裡path('<int:xx>')
		return get_object_or_404(Article, id=id)

class ArticleDeleteView(DeleteView):
	# 過濾obj的id > 1的網頁，如果訪客訪問no.1的網頁，就會出現404，page not found。
	queryset = Article.objects.all()
	template_name = 'blog/article_delete.html'

	def get_object(self):
		id = self.kwargs.get("akb48")
	# 	#這裏kwargs.get("xx")對照url裡path('<int:xx>')
		return get_object_or_404(Article, id=id)

	def get_success_url(self):
		return "/blog"



