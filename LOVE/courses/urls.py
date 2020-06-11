from django.urls import path
from .views import (
	CourseView,
	CourseDetailView,
	# my_FunctionBaseView,
	CourseListView,
	MyListView,
	CourseCreateView,
	CourseUpdateView,
	CourseDeleteView,
)


app_name = 'courses'
urlpatterns = [
# path('class', CourseView.as_view(template_name='contact.html'), name='class_view'),
	# path('func', my_FunctionBaseView, name='func_view'),
	path('class', CourseView.as_view(template_name='contact.html'), name='class_view'),
	path('<int:id>', CourseDetailView.as_view(), name='courses_detail'),
	path('', CourseListView.as_view(), name='course_list'),
	path('list1', MyListView.as_view(), name='course_list1'),
	path('create/', CourseCreateView.as_view(), name='course_create'),
	path('<int:id>/update/', CourseUpdateView.as_view(), name='course_update'),
	path('<int:id>/delete/', CourseDeleteView.as_view(), name='course_delete')
	# /delete後面一定要再加個/，不然按yes後，會出現找不到頁面
]