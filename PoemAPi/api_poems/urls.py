from .views import poem_list, poem_detail
from django.urls import path

urlpatterns = [
    path('poem/', poem_list),
    path('detail/<int:pk>', poem_detail)
]
