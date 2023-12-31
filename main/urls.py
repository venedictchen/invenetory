from django.urls import path
from main.views import show_main,add_item_ajax,delete_item_ajax,create_item_flutter,show_data_user
from main.views import show_main, create_item, show_xml, show_json, show_xml_by_id, show_json_by_id,show_html
from main.views import register,login_user,logout_user,increase_item_amount,decrease_item_amount,delete_item
app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-item', create_item, name='create_item'),
    path('xml/',show_xml,name='show_xml'),
    path('html/',show_html,name='show_html'),
    path('json/',show_json,name='show_json'),
    path('xml/<int:id>/',show_xml_by_id,name='show_xml_by_id'),
    path('json/<int:id>/',show_json_by_id,name='show_json_by_id'),
    path('register/',register,name='register'),
    path('login/',login_user,name='login'),
    path('logout/',logout_user,name='logout'),
    path('increase_item_amount/<int:id>/',increase_item_amount,name='increase_item_amount'),
    path('decrease_item_amount/<int:id>/',decrease_item_amount,name='decrease_item_amount'),
    path('delete_item/<int:id>/',delete_item,name='delete_item'),
    path('delete_item_ajax/<int:id>/',delete_item_ajax,name='delete_item_ajax'),
    path('add-item-ajax/', add_item_ajax, name='add_item_ajax'),
    path('create-flutter/', create_item_flutter, name='create_item_flutter'),
    path('user_data/',show_data_user,name='show_data_user'),
    
]