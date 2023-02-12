from django.shortcuts import render
from django.http import HttpResponse
from basic_app import models
from django.urls import reverse_lazy
from django.views.generic import (View, TemplateView,DetailView, 
                                ListView, CreateView, UpdateView, 
                                DeleteView)

# Create your views here.

# def index(request):
#     return render(request, "basic_app/index.html")

# BASIC CLASS BASED VIEW
# class CBView(View):
#     def get(self, request):
#         return HttpResponse("CBV are nice!")

class IndexView(TemplateView):
    template_name = "index.html"

    # how to inject data (context)
    def get_context_data(self, **kwargs: any) -> dict[str, any]:
        context = super().get_context_data(**kwargs)
        context["inject_me"] = "Basic Injection!"
        return context

# get provided with every object in this list!
# ListView will handle everything else
class SchoolListView(ListView):
    # make own context name
    context_object_name = "schools"
    # school_list - returned automatically if no context name defined
    model = models.School
    

class SchoolDetailView(DetailView):
    context_object_name = "school_details" # default - school
    model = models.School
    template_name = "basic_app/school_details.html"

class SchoolCreateView(CreateView):
    fields = ('name', 'principal', 'location')
    model = models.School

class SchoolUpdateView(UpdateView):
    fields = ('name', 'principal')
    model = models.School

class SchoolDeleteView(DeleteView):
    model = models.School
    success_url = reverse_lazy("basic_app:school_list")