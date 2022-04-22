from django import forms

#comment :D
class owned_char_list(forms.Form):
    albedo = forms.CheckboxInput(label='Albedo')