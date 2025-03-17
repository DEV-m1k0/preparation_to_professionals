from django import forms


class SearchForm(forms.Form):
    search = forms.CharField(required=False, widget=forms.TextInput(attrs={
        "type": "search",
        "class": "form-control w-100",
        "placeholder": "Поиск..."
    }))

class VCardForm(forms.Form):
    full_name = forms.CharField(widget=forms.TextInput(attrs={
        "type": "hidden"
    }))