from django.urls import path
from . import views
urlpatterns = [path('parameter/view/',views.ParameterViewCreate.as_view(),name='parameter-view-create'),
               path('parameters/', views.parameter_list, name='parameter_list'),
               path('parameters/update/<int:id_param>/', views.parameter_update, name='parameter_update'),
]