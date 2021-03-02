from django.urls import path
from . import views
from rest_framework_swagger.views import get_swagger_view
schema_view = get_swagger_view(title='employee')
urlpatterns = [
    #path('login/', views.LoginAPIView.as_view()),
    path('employeelist/', views.EmployeelistView.as_view()),
    path('create/', views.EmployeecreateView.as_view()),
    path('details/', views.EmployeedetailView.as_view()),
    path('update/', views.EmployeeupdateView.as_view()),
    #path('swaggerapi/', schema_view),
]