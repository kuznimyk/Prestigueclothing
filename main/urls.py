from django.urls import path
from . import views
from .views import ItemListView
app_name = 'main'

urlpatterns = [
    path('', ItemListView.as_view(), name = 'index'),
    path('login/', views.login_view, name = 'login'),
    path('signup', views.signup, name =  'signup'),
    path('profile', views.profile, name = 'profile'),
    path('additem', views.additem, name = 'additem'),
    path('<int:pk>/viewitem', views.viewitem, name = 'viewitem'),
    path('<int:pk>/edititem', views.edititem, name = 'edititem'),
    path('<int:pk>/deleteitem', views.deleteitem, name = 'deleteitem'),
    path('addtocart/<int:pk>/', views.addtocart, name = 'addtocart'),
    path('viewcart', views.viewcart, name = 'viewcart'),
    path('logout/', views.logout_view, name = 'logout'),
    path('about/', views.about, name = 'about'),
    path('contact/', views.contact, name = 'contact'),
    path('investors', views.investors, name = 'investors'),
]
