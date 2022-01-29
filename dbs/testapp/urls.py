from django.urls import path,include
from testapp import views

urlpatterns = [
    path("home/",views.home,name="home"),
    path("login/",views.login,name="login"),
    path("signin/",views.signin,name="signin"),
    path("cus/",views.cus,name="cus"),
]

