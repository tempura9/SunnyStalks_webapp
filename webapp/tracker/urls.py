from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("grocer/add",views.addGrocer),
    path("edit/<int:id>",views.editGrocer),
    path("grocer/all",views.grocerList),
    path("purchase/add",views.groceryPurchase),
    path("compare",views.compareGrocers),
]