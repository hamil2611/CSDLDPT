from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.index,name="search"),
    path('solvesearch/',views.Search,name="solvesearch"),
    path('autoupdate/',views.auto_createidf,name="autoupdate"),
    path('autotrongso/',views.auto_createFileWeight,name="autotrongso"),
    path('viewdocument/',views.viewdocument,name="adddocument"),
    path('addfile/',views.addfile,name="addfile"),
    path('readfile/',views.readfile,name="readfile"),

]