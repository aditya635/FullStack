from django.urls import path

from . import views

urlpatterns = [ 
  #  path("january",views.index),
  #    path("february",views.index1),
  path("<int:month>",views.monthly_challenges),#<> is used for dynamic paths
  path("<str:month>",views.monthly_challenge, name="dad")#value added here with str: should be used as a string
 
]