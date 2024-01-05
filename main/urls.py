from django.urls import path
from . import views
from .views import ItemListView
app_name = 'main'

urlpatterns = [
    path('', ItemListView.as_view(), name = 'index'),
    path('signup', views.signup, name =  'signup'),
    path('profile', views.profile, name = 'profile'),
    path('additem', views.additem, name = 'additem'),
    path('<int:pk>/viewitem', views.viewitem, name = 'viewitem'),
    path('<int:pk>/edititem', views.edititem, name = 'edititem'),
    path('<int:pk>/deleteitem', views.deleteitem, name = 'deleteitem'),
    path('addtocart/<int:pk>/', views.addtocart, name = 'addtocart'),
    path('viewcart', views.viewcart, name = 'viewcart'),

]
