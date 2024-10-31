from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path("", TemplateView.as_view(template_name="pages/home.html"), name="home"),
    path(
        "about/",
        TemplateView.as_view(template_name="pages/about.html"),
        name="about",
    ),
    path("users/", include("bloodhound.users.urls", namespace="users")),
    path("accounts/", include("allauth.urls")),
    path("admin/", admin.site.urls),
]
