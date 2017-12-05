from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from .models import Car
from .forms import CarForm, CarUpdateForm
from django.utils import timezone
from django.urls import reverse_lazy

# https://docs.djangoproject.com/en/1.11/ref/class-based-views/generic-display/
class IndexView(TemplateView):
    template_name = 'car/index.html'

class ListView(ListView):
    template_name = 'car/car_list.html' # default : '_list.html'
    context_object_name = 'car_list' # default : 'object_list'
    queryset = Car.objects.all()

# url : pk
class DetailView(DetailView):
    template_name = 'car/car_detail.html' # default : '_detail.html'
    context_object_name = 'car' # default : 'object'
    queryset = Car.objects.all()

    def get_object(self):
        # Call the superclass
        object = super(DetailView, self).get_object()
        # Record the last accessed date
        object.last_accessed = timezone.now()
        object.save()
        # Return the object
        return object

# https://docs.djangoproject.com/en/1.11/ref/class-based-views/generic-editing/
class FormView(FormView):
    template_name = 'car/form.html'
    success_url = '/'
    form_class = CarForm

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.send_email()
        return super(FormView, self).form_valid(form)

class CreateView(CreateView):
    model = Car
    template_name_suffix = '_create_form' # default : '_form.html'
    # success_url = '/list' # or model - def get_absolute_url(self):
    fields = ['name', 'sn']

# url : pk
class UpdateView(UpdateView):
    model = Car
    template_name_suffix = '_update_form' # default : '_form.html'
    # success_url = '/list' # or model - def get_absolute_url(self):
    form_class = CarUpdateForm #fields = ['name', 'sn']

# url : pk
class DeleteView(DeleteView):
    model = Car
    template_name_suffix = '_check_delete' # default : '_confirm_delete.html'
    success_url = reverse_lazy('list')

# https://docs.djangoproject.com/en/1.11/ref/class-based-views/mixins/

# https://docs.djangoproject.com/en/1.11/topics/forms/modelforms/
