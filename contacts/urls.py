# contacts/urls.py

from django.urls import path
from .views import contact_list, add_contact, edit_contact, delete_contact

urlpatterns = [
    path('', contact_list, name='contact_list'),
    path('add/', add_contact, name='add_contact'),
    path('edit/<int:pk>/', edit_contact, name='edit_contact'),
    path('delete/<int:pk>/', delete_contact, name='delete_contact'),
]




# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.contact_list, name='contact_list'),
#     path('add/', views.add_contact, name='add_contact'),
#     path('<pk>/', views.contact_detail, name='contact_detail'),
#     path('<pk>/edit/', views.edit_contact, name='edit_contact'),
#     path('<pk>/delete/', views.delete_contact, name='delete_contact'),
#     path('search/', views.search_contacts, name='search_contacts'),
# ]




# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.home, name='home'),
#     path('add/', views.add_contact, name='add_contact'),
#     path('<int:pk>/', views.contact_detail, name='contact_detail'),
#     path('<int:pk>/edit/', views.edit_contact, name='edit_contact'),
#     path('<int:pk>/delete/', views.delete_contact, name='delete_contact'),
# ]


