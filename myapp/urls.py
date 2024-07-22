from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('insert',views.insertData,name="insertDaata"),
    path('update/<id>', views.updateData, name="updateData"),
    path('delete/<id>', views.deleteData, name="deleteData"),

    path('login', views.handlelogin, name="handlelogin"),
    path('logout', views.handlelogout, name="handlelogout"),
    path('signup', views.handlesignup, name="handlesignup"),
]