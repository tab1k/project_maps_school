from django import forms


class ContactForms(forms.Form):
    name = forms.CharField(
        min_length=2, # Минимальная длина
        widget=forms.TextInput(
            attrs={
                'placeholder' : 'Имя:',
            }
        )
    )

    phone_number = forms.CharField(
        min_length=13,
        widget=forms.TextInput(
            attrs= {
                'placeholder' : 'Номер телефона:',
            }
        )
    )

    subject_input = forms.CharField(
        min_length=5,
        widget=forms.TextInput(
            attrs= {
                'placeholder' : 'Предмет:'
            }
        )
    )