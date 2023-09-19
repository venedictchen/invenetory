from django.forms import ModelForm,TextInput
from main.models import Item

class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ["name", "amount", "description","code","price"]