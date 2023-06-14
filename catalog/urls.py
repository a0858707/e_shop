from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.main_page),
    path('about', views.about_page),
    path('contact', views.contact_page),
    path('category/<int:pk>', views.get_category_products),
    path('product/<str:name>/<int:pk>', views.get_exact_products),
    path('add-product-to-cart/<int:pk>', views.add_pr_to_cart),
    path('cart', views.get_user_cart),
    path('del_item/<int:pk>', views.delete_from_user_cart),
    path('send_to_tg', views.complere_order),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #Добавить изображения
