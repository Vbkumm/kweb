from django import forms
from main.models import (TestimonialsModel,
                         ClientModel)


class TestimonialForm(forms.ModelForm):

    class Meta:
        model = TestimonialsModel
        fields = ['testimonials_author', 'author_picture', 'author_job', 'testimonials_description']


class ClientForm(forms.ModelForm):

    class Meta:
        model = ClientModel
        fields = ['client_company', 'company_picture']

