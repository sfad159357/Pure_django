from django.urls import path
from .views import (
	ArticleListView,
	ArticleDetailView,
	ArticleCreateView,
	ArticleUpdateView,
	ArticleDeleteView,


)

app_name = 'Blog'
urlpatterns = [
	path('', ArticleListView.as_view(), name='article_list'),
	# 注意，ArticleListView是class，不是function，不能直接丟入此參數，透過.as_view()形成一個函式。
	path('<int:akb48>', ArticleDetailView.as_view(), name='article_detail'),
	#在class基礎上的View基本上要輸入的標籤變數是<int:pk>，而不是<int:id>，pk意思是primary key的意思，不是id，作為辨識每個網頁的no.。
	path('create/', ArticleCreateView.as_view(), name='article_create'),
	path('<int:akb48>/update/', ArticleUpdateView.as_view(), name='article_update'),
	path('<int:akb48>/delete/', ArticleDeleteView.as_view(), name='article_delete'),
	# path('class', CourseView.as_view(template_name='contact.html'), name='class_view'),
	# path('func', my_FunctionBaseView, name='func_view'),
]