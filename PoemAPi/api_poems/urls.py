
from .views import poem_list, poem_detail, PoemAPIView, PoemDetails, GenericAPIView
from django.urls import path

urlpatterns = [
    # path('poem/', poem_list),
    path('poem/', PoemAPIView.as_view()),
    # path('detail/<int:pk>', poem_detail)
    path('detail/<int:id>', PoemDetails.as_view()),
    path('generic/detail/<int:id>/', GenericAPIView.as_view()),
    path('generic/poem/', GenericAPIView.as_view()),
]
