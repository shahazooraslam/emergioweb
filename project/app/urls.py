from django.urls import path,include
from . import views

urlpatterns = [
    
    path("",views.Home,name="index/"),
    path("courses/",views.Courses,name="courses/"),
    path("career/",views.Career,name="career/"),
    path("contact/",views.Contact,name="contact/"),
    path("signup/",views.signup,name="signup/"),
    path("signin/",views.signin,name="signin/"),
    path("accounts/login/",views.signin,name="signin/"),
    path("logout/",views.logoutview,name="logout/"),
    path("pdf/",views.pdf,name="pdf/"),
    path("searchvenues/",views.searchvenues,name="search-venues"),
    path("apply/",views.apply,name="apply/"),
    

]
