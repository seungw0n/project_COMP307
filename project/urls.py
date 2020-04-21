"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings

from django.urls import path, include

from accounts import views as accounts_views
from market import views
from payments import views as payments_views

urlpatterns = [
    url('^admin/', admin.site.urls),
    url('^$', views.home, name='home'),
    url('^cart/$', views.cart, name='cart'),
    url('^addItem/$', views.addItem, name='addItem'),
    url('^myspace/$', views.myspace, name='myspace'),
    url('^edit_profile/$', views.editProfile, name='editProfile'),
    url('^signup/$', accounts_views.signup, name='signup'),
    url('^logout/$', auth_views.LogoutView.as_view(), name='logout'),
    url('^login/$', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('chat/', include('chat.urls')),
    path('category/<str:cat>', views.category, name='category'),
    path('product/<int:product_id>', views.productPage, name='productPage'),
    path('product/add_to_cart/<int:product_id>', views.addToCart, name='addToCart'),
    path('cart/change_quantity', views.changeQuantity, name='changeQuantity'),
    path('cart/remove_from_cart', views.removeFromCart, name='removeFromCart'),
    path('', include('sendemail.urls')),
    path('product/<int:product_id>/modifyProduct/',views.modifyProduct,name='modifyProduct'),
    path('product/<int:product_id>/deleteProduct/',views.deleteProduct,name='deleteProduct'),
    # path('detail/', payments_views.detail, name='detail'),
    path('charge/', payments_views.charge, name='charge'),
    # path('checkout/', payments_views.checkout, name='checkout'),



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
