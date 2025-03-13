from django import forms


class SearchForm(forms.Form):
    search = forms.CharField(required=False, widget=forms.TextInput(attrs={
        "type": "search",
        "class": "form-control w-100",
        "placeholder": "Поиск..."
    }))