from django.urls import path
from . import views

urlpatterns = [
    path('', views.class_list, name='class_list'),
    path('<int:pk>/', views.class_detail, name='class_detail'),
    path('create/', views.class_create, name='class_create'),
    path('<int:pk>/edit/', views.class_edit, name='class_edit'),
    path('<int:pk>/delete/', views.class_delete, name='class_delete'),
    path('<int:pk>/add-students/', views.class_add_students, name='class_add_students'),
    path('<int:class_pk>/remove-student/<int:student_pk>/', views.class_remove_student, name='class_remove_student'),
]
