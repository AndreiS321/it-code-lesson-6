from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("index", views.index),
    path("workers_list", views.workers_list),
    path("add_worker", views.add_worker),
    path("delete_worker/<int:worker_id>", views.delete_worker, name="delete_worker"),
    path("worker_of_month", views.worker_of_month),
]
