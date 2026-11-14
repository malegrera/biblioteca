from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("catalogo/", views.catalogo, name="catalogo"),
    path("libros/<int:libro_id>/", views.detalle_libro, name="detalle_libro"),
    path(
    "login/",
    auth_views.LoginView.as_view(template_name="login.html"),
    name="login"
    ),
    path(
    "logout/",
    auth_views.LogoutView.as_view(next_page="inicio"),
    name="logout"
    ),
    path("mis-prestamos/", views.mis_prestamos, name="mis_prestamos"),
    path(
    "api/libros/",
    views.LibroListAPIView.as_view(),
    name="api_libros"
    ),
    path("api/libros/<int:pk>/", views.LibroDetailAPIView.as_view(), name="api_detalle_libro"),
]