from django import forms


class QuizForm(forms.Form):
    TRUE_FALSE_CHOICES = [
        (True, 'Prawda'),
        (False, 'Fałsz')
    ]

    Q1 = forms.ChoiceField(label='Pytanie 1: Public Relations (PR) to to samo co reklama.', choices=TRUE_FALSE_CHOICES, widget=forms.RadioSelect)
    Q2 = forms.ChoiceField(label='Pytanie 2: Jednym z celów public relations jest budowanie pozytywnego wizerunku firmy.', choices=TRUE_FALSE_CHOICES, widget=forms.RadioSelect)
    Q3 = forms.ChoiceField(label='Pytanie 3: Relacje z mediami to jedyny obszar działania public relations.', choices=TRUE_FALSE_CHOICES, widget=forms.RadioSelect)
    Q4 = forms.ChoiceField(label='Pytanie 4: W ramach public relations ważne jest monitorowanie opinii publicznej na temat firmy.', choices=TRUE_FALSE_CHOICES, widget=forms.RadioSelect)
    Q5 = forms.ChoiceField(label='Pytanie 5: Public relations to działania skierowane wyłącznie do klientów.', choices=TRUE_FALSE_CHOICES, widget=forms.RadioSelect)
    Q6 = forms.ChoiceField(label='Pytanie 6: Działania PR nie obejmują zarządzania sytuacjami kryzysowymi.', choices=TRUE_FALSE_CHOICES, widget=forms.RadioSelect)
    Q7 = forms.ChoiceField(label='Pytanie 7: Public relations może wpływać na decyzje inwestorów.', choices=TRUE_FALSE_CHOICES, widget=forms.RadioSelect)
    Q8 = forms.ChoiceField(label='Pytanie 8: Rzecznictwo to jeden z elementów public relations.', choices=TRUE_FALSE_CHOICES, widget=forms.RadioSelect)
    Q9 = forms.ChoiceField(label='Pytanie 9: W dzisiejszych czasach media społecznościowe nie odgrywają ważnej roli w public relations.', choices=TRUE_FALSE_CHOICES, widget=forms.RadioSelect)
    Q10 = forms.ChoiceField(label='Pytanie 10: Public relations nie jest potrzebne małym firmom.', choices=TRUE_FALSE_CHOICES, widget=forms.RadioSelect)
