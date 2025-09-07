from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views
from .views import CustomSignupView
from allauth.account.views import LoginView
urlpatterns = [
    path('listuniv/', views.home, name='listofuniversities'),
    path('university/<int:pk>/', views.university_detail, name='university_detail'),
path('university/<int:pk>/register/', views.university_register, name='university_register'),
# path('ajax/load-course-options/', views.get_course_options, name='ajax_load_course_options'),
path('compare/', views.compare_colleges, name='compare_colleges'),
    # path('ajax/get-course-options/', views.get_course_options, name='get_course_options'),
path('',views.landing, name='landing'),
     # path('login/', views.login, name='login'),
     path('accounts/', include('allauth.urls')),
    path('accounts/signup/', CustomSignupView.as_view(), name='account_signup'),
    path('accounts/login/', LoginView.as_view(), name='account_login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page='listuniv'), name='logout'),
path('heartbeat/', views.heartbeat, name='heartbeat'),
    path('my-wishlists/', views.my_wishlists, name='my_wishlists'),
    path('wishlist/add/', views.add_to_wishlist, name='add_to_wishlist'),
    path('wishlist/remove/', views.remove_from_wishlist, name='remove_from_wishlist'),
    ]


