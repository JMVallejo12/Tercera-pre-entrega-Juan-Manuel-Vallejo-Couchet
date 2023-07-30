from django import forms

class Formulario_Suscriptor(forms.Form):
    nombre = forms.CharField(label="Nombre:", max_length=50, required= True)
    apellido = forms.CharField(label="Apellido:", max_length=50, required=True)
    edad = forms.IntegerField(label="Edad:",required=True)
    sexos = ((1,"Masculino"),(2,"Femenino"))
    sexo = forms.ChoiceField(label="Sexo:",choices=sexos,required=True)
    direccion = forms.CharField(label="Direccion:",max_length=50,required=True)
    tarjeta = forms.IntegerField(label="Tarjeta:",required=True)

class Formulario_Personajes(forms.Form):
    nombre = forms.CharField(label="Nombre:", max_length=50,required=True)
    apellido = forms.CharField(label="Apellido", max_length=50,required=True)
    nombrePersonaje = forms.CharField(label="Nombre Personaje:", max_length=50,required=True)
    apellidoPersonaje = forms.CharField(label="Apellido Personaje:", max_length=50,required=True)


class Formulario_Temporada(forms.Form):
    nombreTemporada = forms.CharField(label="Nombre:",max_length=50,required=True)
    numeroCapitulos = forms.IntegerField(label="Nro. Capítulos", required=True)
    fechaEmision = forms.CharField(label="Fecha emisión:",max_length=50,required=True)

