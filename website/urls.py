from . import views
from django.urls import path

urlpatterns = [
    path('', views.home,name ='home'),
    path('gradio_app/', views.gradio_app, name='gradio_app'),
    path('predict/',views.predict, name = 'predict')
    
   
]
