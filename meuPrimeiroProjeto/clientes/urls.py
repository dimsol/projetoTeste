from django.urls import path
from .views import person_list
from .views import persons_new
from .views import person_update
from .views import person_delete

urlpatterns = [
    path('list/', person_list, name="person_list"),
    path('new/', persons_new, name="persons_new"),
    path('update/<int:id>/', person_update, name="person_update"),
    path('delete/<int:id>/', person_delete, name="person_delete"),
]
