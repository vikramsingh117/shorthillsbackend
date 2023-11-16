from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt
from .views import get_csrf_token  # Import your view function

from django.urls import reverse
from django.http import HttpResponse
from django.middleware.csrf import get_token



urlpatterns = [
    path('add-product/', views.add_product, name='add_product'),
    path('get-csrf-token/', csrf_exempt(get_csrf_token), name='get_csrf_token'),
    path('get-products/', views.get_products, name='get_products'),
    path('edit-product/<int:product_id>/', views.edit_product, name='edit_product'), 
    path('upload-file/', views.upload_image, name='upload_image'),

]



def get_base_url(request):
    base_url = request.build_absolute_uri('/')
    return HttpResponse(f"Base URL: {base_url}")
