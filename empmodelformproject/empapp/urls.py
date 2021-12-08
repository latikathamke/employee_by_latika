from django.urls import path
from empapp import views


urlpatterns = [
    path('home/',views.home),
    path('add/',views.add_employee),
    path('read/',views.read_employee),
    path('detail/<int:id>/',views.detail_employee),
    path('update/<int:id>/',views.update_employee),
    path('delete/<int:id>/',views.delete_employee),
    path('search/',views.search),
    path('search_result/',views.search_result, name='search_result'),
]