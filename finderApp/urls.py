from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('signup', views.signup, name="signup"),
    path('login', views.login, name="login"),
    path('logout', views.logout, name="logout"),
    # path('(?P<todo_id>[0-9]+)/done/', views.done, name='done'),
    # path('(?P<todo_id>[0-9]+)/delete/', views.delete, name='delete'),

    path('lawyers', views.lawyer_list, name="lawyer_list"),
    path('lawyers/<int:pk>', views.lawyer_detail, name="lawyer_detail"),
    path('lawyers/new', views.lawyer_create, name="lawyer_create"),
    path('lawyers/<int:pk>/edit', views.lawyer_edit, name="lawyer_edit"),
	path('lawyers/<int:pk>/delete', views.lawyer_delete, name="lawyer_delete"),
]
