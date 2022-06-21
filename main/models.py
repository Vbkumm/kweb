from django.db import models
from PIL import Image


# Create your models here.


class TestimonialsModel(models.Model):
    testimonials_author = models.CharField('Nome do autor:',max_length=150, )
    author_picture = models.ImageField('Sua foto', upload_to="img/author/", null=True, blank=True, )
    author_job = models.CharField('Cargo função na empresa:', max_length=150, )
    testimonials_description = models.CharField('Seu depoimento', max_length=800, null=True, blank=True, )

    class Meta:
        verbose_name_plural = "testimonials"
        verbose_name = "testimonial"

    def __str__(self):
        return self.testimonials_author

    def save1(self):

        super(TestimonialsModel, self).save()
        if not self.id:
            return
        else:
            if self.author_picture:

                im1 = Image.open(self.author_picture)
                (width, height) = im1.size
                if width > 400:
                    if 300 / width < 300 / height:
                        factor = 300 / height
                    else:
                        factor = 300 / width

                    size = (int(width * factor), int(height * factor))
                    im1 = im1.resize(size, Image.ANTIALIAS)
                    im1.save(self.author_picture.path, optimize=True)


class ClientModel(models.Model):
    client_company = models.CharField('Nome da empres:',max_length=150, )
    company_picture = models.ImageField('Logo da empresa', upload_to="img/author/", null=True, blank=True, )

    class Meta:
        verbose_name_plural = "clients"
        verbose_name = "client"

    def __str__(self):
        return self.client_company

    def save1(self):

        super(ClientModel, self).save()
        if not self.id:
            return
        else:
            if self.company_picture:

                im1 = Image.open(self.company_picture)
                (width, height) = im1.size
                if width > 200:
                    if 150 / width < 150 / height:
                        factor = 150 / height
                    else:
                        factor = 150 / width

                    size = (int(width * factor), int(height * factor))
                    im1 = im1.resize(size, Image.ANTIALIAS)
                    im1.save(self.company_picture.path, optimize=True)
