from django import forms
from django.forms import ModelForm
from .models import Fundacion, Producto, Cliente


class ProductosForm(forms.ModelForm):

    class Meta:
        model = Producto
        fields = "__all__"


class FormularioCliente(ModelForm):
    class Meta:
        model = Cliente
        fields = "__all__"


class FormFundacion(ModelForm):
    class Meta:
        model = Fundacion
        fields = "__all__"
