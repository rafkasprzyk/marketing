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



class QuizForm2(forms.Form):
    Q1_CHOICES = [
        (True, 'Chodzi o samą sprzedaż produktu klientom'),
        (False, 'Skupiamy się na samym kształtowaniu wizerunku marki oraz edukacji rynku na temat naszego produktu')
    ]
    Q2_CHOICES = [
        (True, 'Współpraca z osobami mającymi wpływ na opinie innych w celu promocji marki'),
        (False, 'Wysyłanie spersonalizowanych e-maili do klientów')
    ]
    Q3_CHOICES = [
        (True, 'Skupia się na cyklu życia klienta, od pozyskania do utrzymania'),
        (False, 'Skupia się na wykorzystaniu influencer marketingu')
    ]
    Q4_CHOICES = [
        (True, 'Sprzedaż osobista '),
        (False, 'Reklama telewizyjna')
    ]
    Q5_CHOICES = [
        (True, 'Prawda'),
        (False, 'Fałsz')
    ]
    Q6_CHOICES = [
        (True, 'Systemem znaków, za pomocą którego wyrażany jest przekaz'),
        (False, 'Kanałem, przez który przekaz jest dostarczany')
    ]
    Q7_CHOICES = [
        (True, 'Tak'),
        (False, 'Nie')
    ]
    Q8_CHOICES = [
        (True, 'Płatną formą reklamy internetowej'),
        (False, 'Nieformalną komunikacją między konsumentami na temat produktu lub usługi')
    ]
    Q9_CHOICES = [
        (True, 'Tak'),
        (False, 'Nie')
    ]
    Q10_CHOICES = [
        (True, 'Tak'),
        (False, 'Nie')
    ]

    Q1 = forms.ChoiceField(label='Pytanie 1: W pojęciu komunikacja marketingowa', choices=Q1_CHOICES, widget=forms.RadioSelect)
    Q2 = forms.ChoiceField(label='Pytanie 2: Czym jest influencer marketing?', choices=Q2_CHOICES, widget=forms.RadioSelect)
    Q3 = forms.ChoiceField(label='Pytanie 3: Czym charakteryzuje się model RACE? ', choices=Q3_CHOICES, widget=forms.RadioSelect)
    Q4 = forms.ChoiceField(label='Pytanie 4: Która forma komunikacji marketingowej jest przykładem modelu interpersonalnego?', choices=Q4_CHOICES, widget=forms.RadioSelect)
    Q5 = forms.ChoiceField(label='Pytanie 5: Model AIDA opisuje etapy, przez które przechodzi konsument przed podjęciem decyzji zakupowej', choices=Q5_CHOICES, widget=forms.RadioSelect)
    Q6 = forms.ChoiceField(label='Pytanie 6: Czym jest kod w komunikacji marketingowej?', choices=Q6_CHOICES, widget=forms.RadioSelect)
    Q7 = forms.ChoiceField(label='Pytanie 7: Czy tradycyjne formy komunikacji marketingowej obejmują strony internetowe i blogi?', choices=Q7_CHOICES, widget=forms.RadioSelect)
    Q8 = forms.ChoiceField(label='Pytanie 8: Czym jest marketing szeptany?', choices=Q8_CHOICES, widget=forms.RadioSelect)
    Q9 = forms.ChoiceField(label='Pytanie 9: Czy model RACE koncentruje się na jednorazowej transakcji z klientem?', choices=Q9_CHOICES, widget=forms.RadioSelect)
    Q10 = forms.ChoiceField(label='Pytanie 10: Czy reklama prasowa jest przykładem tradycyjnej formy komunikacji marketingowej?', choices=Q10_CHOICES, widget=forms.RadioSelect)


class QuizForm3(forms.Form):
    Q1_CHOICES = [
        (True, 'Zwiększenie udziału w istniejących rynkach z istniejącymi produktami'),
        (False, 'Wejście na nowe rynki z istniejącymi produktami')
    ]
    Q2_CHOICES = [
        (True, 'Ekspansja geograficzna'),
        (False, 'Konkurencyjne ceny')
    ]
    Q3_CHOICES = [
        (True, 'Dywersyfikacja powiązana i dywersyfikacja niepowiązana'),
        (False, 'Dywersyfikacja geograficzna i dywersyfikacja demograficzna')
    ]
    Q4_CHOICES = [
        (True, 'Stać się producentem o najniższych kosztach w branży '),
        (False, 'Stać się liderem innowacji w branży')
    ]
    Q5_CHOICES = [
        (True, 'Dogłębne badania rynku'),
        (False, 'Fuzje i przejęcia')
    ]
    Q6_CHOICES = [
        (True, 'Apple wprowadzające nowe wersje iPhone'),
        (False, 'Starbucks wchodzący na rynek chiński')
    ]
    Q7_CHOICES = [
        (True, 'Agresywne kampanie marketingowe'),
        (False, 'Tworzenie nowych linii produktów')
    ]
    Q8_CHOICES = [
        (True, 'CRM koncentruje się na zwiększeniu satysfakcji i lojalności klientów'),
        (False, 'Strategia retencji klientów koncentruje się na utrzymaniu istniejących klientów')
    ]
    Q9_CHOICES = [
        (True, 'Marketing treści'),
        (False, 'Spersonalizowane kampanie marketingowe')
    ]
    Q10_CHOICES = [
        (True, 'Zbudowanie i utrzymanie silnej marki'),
        (False, 'Zwiększenie udziału w rynku na istniejących rynkach')
    ]

    Q1 = forms.ChoiceField(label='Pytanie 1: Co jest głównym celem strategii penetracji rynku?', choices=Q1_CHOICES, widget=forms.RadioSelect)
    Q2 = forms.ChoiceField(label='Pytanie 2: Która z poniższych taktyk nie jest związana ze strategią rozwoju rynku?', choices=Q2_CHOICES, widget=forms.RadioSelect)
    Q3 = forms.ChoiceField(label='Pytanie 3: Jakie są dwa rodzaje dywersyfikacji w strategii dywersyfikacji?', choices=Q3_CHOICES, widget=forms.RadioSelect)
    Q4 = forms.ChoiceField(label='Pytanie 4: Co jest głównym celem strategii przywództwa kosztowego?', choices=Q4_CHOICES, widget=forms.RadioSelect)
    Q5 = forms.ChoiceField(label='Pytanie 5: Która taktyka nie jest typowa dla strategii koncentracji?', choices=Q5_CHOICES, widget=forms.RadioSelect)
    Q6 = forms.ChoiceField(label='Pytanie 6: Który przykład najlepiej ilustruje strategię rozwoju produktu?', choices=Q6_CHOICES, widget=forms.RadioSelect)
    Q7 = forms.ChoiceField(label='Pytanie 7: Jaką taktykę stosuje Coca-Cola w strategii penetracji rynku?', choices=Q7_CHOICES, widget=forms.RadioSelect)
    Q8 = forms.ChoiceField(label='Pytanie 8: Jaka jest główna różnica między strategią zarządzania relacjami z klientami (CRM) a strategią retencji klientów?', choices=Q8_CHOICES, widget=forms.RadioSelect)
    Q9 = forms.ChoiceField(label='Pytanie 9: Która taktyka jest charakterystyczna dla strategii marketingu cyfrowego?', choices=Q9_CHOICES, widget=forms.RadioSelect)
    Q10 = forms.ChoiceField(label='Pytanie 10: Co jest celem strategii wartości marki?', choices=Q10_CHOICES, widget=forms.RadioSelect)
