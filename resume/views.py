from django.shortcuts import render
from django.views import generic

from resume.models import Education, Job, Project, Contact, Skill


# Create your views here.
def index(request):
    return render(request, "resume/index.html")


class EducationListView(generic.ListView):
    model = Education


class SkillListView(generic.ListView):
    model = Skill


class ExperienceListView(generic.ListView):
    model = Job


class ProjectListView(generic.ListView):
    model = Project


class ContactDetailView(generic.DetailView):
    model = Contact


class ContactCreateView(generic.CreateView):
    model = Contact
