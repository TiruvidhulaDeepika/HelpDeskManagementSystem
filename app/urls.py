from django.urls import path, include
from .views import *
urlpatterns = [
    path("index", index, name="index"),
    path("register", register, name="register"),
    path("", loginpage, name="loginpage"),
    path("login_view", login_view, name="login_view"),
    path("registration", registration, name="registration"),
    path("raise_ticket", raise_ticket, name="raise_ticket"),
    path("raised", Raised, name="raised"),
    path("success", success, name="success"),
    path("showuser", showuser, name="show_user"),
    path("faq", faq, name="faq"),
    path("show", show, name="show"),
    path("detailed/<int:pk>", Detailed, name="detailed"),
    path("logout", signout, name="logout")
]