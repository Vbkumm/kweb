from main.models import (TestimonialsModel,
                         ClientModel)
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import (UpdateView, CreateView,
                                  DeleteView, ListView)
from main.form import (TestimonialForm, ClientForm)
from django.urls import reverse


# Create your views here.


def my_view(request):
    testimonials = TestimonialsModel.objects.all()
    clients = ClientModel.objects.all()

    return render(request, 'home.html', {'testimonials': testimonials, 'clients': clients})


@method_decorator(login_required, name='dispatch')
class TestimonialCreateView(SuccessMessageMixin, CreateView):
    model = TestimonialsModel
    template_name = 'main/testimonial_add.html'
    form_class = TestimonialForm
    context_object_name = 'testimonials'
    success_message = "Depoimento adicionado com sucesso!"

    def get_success_url(self, *args, **kwargs):
        return reverse("main:testimonial_list_view")


class TestimonialsListView(ListView):
    model = TestimonialsModel
    queryset = TestimonialsModel.objects.all()
    template_name = 'main/testimonial_list_view.html'
    context_object_name = 'testimonials'


@method_decorator(login_required, name='dispatch')
class TestimonialUpdateView(SuccessMessageMixin, UpdateView):
    template_name = 'main/testimonial_update.html'
    model = TestimonialsModel
    form_class = TestimonialForm
    success_message = "Alterações feitas com sucesso!"

    def get_success_url(self, *args, **kwargs):
        return reverse("main:testimonial_list_view")


@method_decorator(login_required, name='dispatch')
class TestimonialDeleteView(DeleteView):
    template_name = 'main/testimonial_delete.html'
    model = TestimonialsModel
    success_message = "Depoimento deletado com sucesso!"

    def get_success_url(self, *args, **kwargs):
        return reverse("main:testimonial_list_view")


@method_decorator(login_required, name='dispatch')
class ClientCreateView(SuccessMessageMixin, CreateView):
    model = ClientModel
    template_name = 'main/client_add.html'
    form_class = ClientForm
    context_object_name = 'clients'
    success_message = "Cliente adicionado com sucesso!"

    def get_success_url(self, *args, **kwargs):
        return reverse("main:client_list_view")


class ClientListView(ListView):
    model = ClientModel
    queryset = ClientModel.objects.all()
    template_name = 'main/client_list_view.html'
    context_object_name = 'clients'


@method_decorator(login_required, name='dispatch')
class ClientUpdateView(SuccessMessageMixin, UpdateView):
    template_name = 'main/client_update.html'
    model = ClientModel
    form_class = ClientForm
    success_message = "Alterações feitas com sucesso!"

    def get_success_url(self, *args, **kwargs):
        return reverse("main:client_list_view")


@method_decorator(login_required, name='dispatch')
class ClientDeleteView(DeleteView):
    template_name = 'main/client_delete.html'
    model = ClientModel
    success_message = "Cliente deletado com sucesso!"

    def get_success_url(self, *args, **kwargs):
        return reverse("main:client_list_view")

