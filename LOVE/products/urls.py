from django.urls import path

from .views import ( 
    product_detail_view,
    product_create_view,  
    product_create2_view, 
    product_create3_view,
    render_initial_data,
    dynamic_lookup_view,
    product_delete_view,
    product_list_view,
)

urlpatterns = [
	path('product/', product_detail_view),
    path('create/', product_create_view),
    path('create2/', product_create2_view),
    path('create3/', product_create3_view),
    path('render/', render_initial_data),
    path('p/<int:my_id>/', dynamic_lookup_view, name='productA'),
    path('products/<int:id>/delete/', product_delete_view, name='product_delete'),
    path('products/list', product_list_view, name='product_list'),

]