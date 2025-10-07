from django.urls import path
from main.views import show_main, show_xml, show_json, show_xml_by_id, show_json_by_id, register, login_user, logout_user, get_items_json, create_item_ajax, update_item_ajax, delete_item_ajax, item_detail


app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('get-items-json/', get_items_json, name='get_items_json'),
    path('create-item-ajax/', create_item_ajax, name='create_item_ajax'),
    path('update-item-ajax/<int:id>/', update_item_ajax, name='update_item_ajax'),
    path('delete-item-ajax/<int:id>/', delete_item_ajax, name='delete_item_ajax'),
    path('item/<int:id>/', item_detail, name='item_detail'),

]