from django import forms

class owned_char_list(forms.Form):
    albedo = forms.CheckboxInput(label='Albedo')