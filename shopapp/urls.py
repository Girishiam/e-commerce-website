from django.urls import path
from . import views
app_name = 'shopapp'

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('product/<pk>', views.ProductDetail.as_view(), name='productdetail'),

]
