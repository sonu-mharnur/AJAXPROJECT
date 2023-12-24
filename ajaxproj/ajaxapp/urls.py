from django.urls import path
from . import views

urlpatterns = [
    # path('postdata/',views.home,name='home'),
    path('uploadfile/', views.upload_file, name='uploadfile'),

]