from django import forms

class FormularioContacto(forms.Form):
   
   nombre=forms.CharField(label='Nombre',required=True, max_length='40')
   
   email=forms.CharField(label='Email',required=True)
   
   comentario=forms.CharField(label='Comentario', widget=forms.Textarea)