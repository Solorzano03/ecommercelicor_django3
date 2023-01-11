from django.db import models

# Create your models here.

class Category(models.Model):

    name   = models.CharField(max_length = 100, verbose_name="Nombre")

    created= models.DateTimeField(auto_now_add = True, verbose_name='Fecha de Creación' ) 

    updated= models.DateTimeField(auto_now     = True, verbose_name='Fecha de Edición' ) 

    class Meta:

        verbose_name="categoría"

        verbose_name_plural="categorías"

        ordering= ["-created"]

    def __str__(self):

        return self.name
class product (models.Model):
    categoria =models.ForeignKey('Category',on_delete=models.SET_NULL, null=True)
    marca =models.CharField(verbose_name="Marca", max_length=150, null=True, blank=True)
    imagen=models.ImageField(verbose_name="imagen",upload_to="imagen" ,null=True, blank=True)
    precio=models.DecimalField(verbose_name="precio",decimal_places=2 , max_digits=5, null=True, blank=True)

    def __str__(self):
        return f"{self.categoria.name}/{self.marca}"

    class Meta:

        verbose_name="producto"

        verbose_name_plural="productos"

    