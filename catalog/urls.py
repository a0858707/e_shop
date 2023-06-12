from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page),
    path('about', views.about_page),
    path('contact', views.contact_page),
    path('category/<int:pk>', views.get_category_products),
    path('product/<str:name>/<int:pk>', views.get_exact_products),
    path('add-product-to-cart/<int:pk>', views.add_pr_to_cart),
    path('user_cart/', views.get_user_cart),
    path('user_cart/del_item/<int:pk>', views.delete_from_user_cart),



]
