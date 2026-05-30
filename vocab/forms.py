from django import forms
from .models import Mot

class MotForm(forms.ModelForm):

    class Meta:
        model = Mot
        fields = [
            "terme",
            "definition",
            "categorie"
        ]

        widgets = {
            "terme": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Entrez le terme"
                }
            ),

            "definition": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 4,
                    "placeholder": "Entrez la définition"
                }
            ),

            "categorie": forms.Select(
                attrs={
                    "class": "form-select"
                }
            ),
        }

        error_messages = {
            'terme': {
                'required': "Champ requis.",
                'max_length': "Votre titre est trop long (maximum 100 caractères).",
            },
            'definition': {
                'required': "Champ requis.",
            },
            'categorie': {
                'required': "Champ requis.",
            },
        }