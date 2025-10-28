"""
URL configuration for ResumeProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path

from resume.views import (
    index,
    EducationListView,
    ExperienceListView,
    ProjectListView,
    ContactDetailView,
    ContactCreateView,
)

urlpatterns = [
    path("", index, name="index"),
    path("education/", EducationListView.as_view(), name="education"),
    path("experience/", ExperienceListView.as_view(), name="experience"),
    path("projects/", ProjectListView.as_view(), name="projects"),
    path("contact/", ContactDetailView.as_view(), name="contacts"),
    path(
        "contact/message/", ContactCreateView.as_view(), name="message"
    ),
]

app_name = "resume"
