from django import forms


class QuizForm(forms.Form):
    Q1_CHOICES = [
        (True, 'Instrumenty finansowe emitowane przez państwo, aby pozyskać środki na swoje projekty lub funkcjonowanie'),
        (False, 'Instrumenty finansowe emitowane przez korporacje, aby sfinansować swoje inwestycje')
    ]
    Q2_CHOICES = [
        (True, 'Tak'),
        (False, 'Nie')
    ]
    Q3_CHOICES = [
        (True, 'Ryzyko niewypłacalności państwa'),
        (False, 'Ryzyko inflacji')
    ]
    Q4_CHOICES = [
        (True, 'Obligacje indeksowane inflacją'),
        (False, 'Obligacje stałoprocentowe')
    ]
    Q5_CHOICES = [
        (True, 'Kupon'),
        (False, 'Nominał')
    ]
    Q6_CHOICES = [
        (True, 'Instrumenty niskiego ryzyka'),
        (False, 'Instrumenty wysokiego ryzyka')
    ]
    Q7_CHOICES = [
        (True, 'Narodowy Bank Polski'),
        (False, 'Ministerstwo Finansów')
    ]
    Q8_CHOICES = [
        (True, 'Stopy referencyjnej NBP'),
        (False, 'Inflacji')
    ]
    Q9_CHOICES = [
        (True, 'COI (4-letnie) i EDO (10-letnie)'),
        (False, 'OTS (3 miesiące) i TOS (3 lata)')
    ]
    Q10_CHOICES = [
        (True, 'Sfinansowanie projektów rządowych i funkcjonowanie państwa'),
        (False, 'Sfinansowanie działalności banków centralnych')
    ]

    Q1 = forms.ChoiceField(label='Pytanie 1: Co to są obligacje skarbowe?', choices=Q1_CHOICES, widget=forms.RadioSelect)
    Q2 = forms.ChoiceField(label='Pytanie 2: Czy zakup obligacji skarbowych detalicznych wiąże się z prowizją w przypadku Pekao lub PKO?', choices=Q2_CHOICES, widget=forms.RadioSelect)
    Q3 = forms.ChoiceField(label='Pytanie 3: Jakie jest główne ryzyko związane z obligacjami skarbowymi?', choices=Q3_CHOICES, widget=forms.RadioSelect)
    Q4 = forms.ChoiceField(label='Pytanie 4: Który rodzaj obligacji skarbowych zazwyczaj oferuje stałe oprocentowanie?', choices=Q4_CHOICES, widget=forms.RadioSelect)
    Q5 = forms.ChoiceField(label='Pytanie 5: Jak nazywa się kwota główna, którą inwestor otrzymuje po wykupie obligacji skarbowych?', choices=Q5_CHOICES, widget=forms.RadioSelect)
    Q6 = forms.ChoiceField(label='Pytanie 6: Obligacje skarbowe są uważane za:', choices=Q6_CHOICES, widget=forms.RadioSelect)
    Q7 = forms.ChoiceField(label='Pytanie 7: Który organ w Polsce emituje obligacje skarbowe?', choices=Q7_CHOICES, widget=forms.RadioSelect)
    Q8 = forms.ChoiceField(label='Pytanie 8: Obligacje zmiennoprocentowe mają oprocentowanie uzależnione od:', choices=Q8_CHOICES, widget=forms.RadioSelect)
    Q9 = forms.ChoiceField(label='Pytanie 9: Które obligacje skarbowe są indeksowane inflacją?', choices=Q9_CHOICES, widget=forms.RadioSelect)
    Q10 = forms.ChoiceField(label='Pytanie 10: Jaki jest główny cel emisji obligacji skarbowych przez państwo?', choices=Q10_CHOICES, widget=forms.RadioSelect)



class QuizForm2(forms.Form):
    Q1_CHOICES = [
        (True, 'Papiery wartościowe emitowane przez spółki akcyjne, reprezentujące udział w kapitale zakładowym przedsiębiorstwa'),
        (False, 'Papiery wartościowe emitowane przez państwo, reprezentujące udział w jego długach')
    ]
    Q2_CHOICES = [
        (True, 'Obligatariusze'),
        (False, 'Akcjonariusze')
    ]
    Q3_CHOICES = [
        (True, 'London Metal Exchange'),
        (False, 'New York Stock Exchange (NYSE)')
    ]
    Q4_CHOICES = [
        (True, 'Zapewnienie płynności, odkrywanie cen, regulacje i nadzór'),
        (False, 'Kredytowanie inwestorów, udzielanie pożyczek, zarządzanie aktywami')
    ]
    Q5_CHOICES = [
        (True, 'Dochody uzyskane z wypłaty dywidend przez spółki'),
        (False, 'Wzrost wartości akcji, który można zrealizować poprzez ich sprzedaż')
    ]
    Q6_CHOICES = [
        (True, 'Część zysków spółki wypłacana regularnie akcjonariuszom'),
        (False, 'Opłaty pobierane przez giełdę za transakcje kupna-sprzedaży')
    ]
    Q7_CHOICES = [
        (True, 'Gotówkowe i akcyjne'),
        (False, 'Zmiennoprocentowe i stałoprocentowe')
    ]
    Q8_CHOICES = [
        (True, 'Brak ryzyka finansowego'),
        (False, 'Łatwa dywersyfikacja')
    ]
    Q9_CHOICES = [
        (True, 'Wahania cen, ryzyko spółki, czynniki zewnętrzne'),
        (False, 'Brak możliwości sprzedaży akcji, stałe oprocentowanie')
    ]
    Q10_CHOICES = [
        (True, 'Ponieważ wartość akcji zawsze rośnie szybciej niż inflacja'),
        (False, 'Ponieważ wartość akcji może rosnąć szybciej niż inflacja, a firmy mogą zwiększać swoje przychody')
    ]

    Q1 = forms.ChoiceField(label='Pytanie 1: Co to są akcje?', choices=Q1_CHOICES, widget=forms.RadioSelect)
    Q2 = forms.ChoiceField(label='Pytanie 2: Kto jest współwłaścicielem firmy posiadając akcje?', choices=Q2_CHOICES, widget=forms.RadioSelect)
    Q3 = forms.ChoiceField(label='Pytanie 3: Która giełda jest przykładem giełdy papierów wartościowych?', choices=Q3_CHOICES, widget=forms.RadioSelect)
    Q4 = forms.ChoiceField(label='Pytanie 4: Jakie są główne funkcje giełdy?', choices=Q4_CHOICES, widget=forms.RadioSelect)
    Q5 = forms.ChoiceField(label='Pytanie 5: Czym są zyski kapitałowe?', choices=Q5_CHOICES, widget=forms.RadioSelect)
    Q6 = forms.ChoiceField(label='Pytanie 6: Czym są dywidendy?', choices=Q6_CHOICES, widget=forms.RadioSelect)
    Q7 = forms.ChoiceField(label='Pytanie 7: Jakie są rodzaje dywidend?', choices=Q7_CHOICES, widget=forms.RadioSelect)
    Q8 = forms.ChoiceField(label='Pytanie 8: Która z poniższych jest zaletą inwestowania w akcje?', choices=Q8_CHOICES, widget=forms.RadioSelect)
    Q9 = forms.ChoiceField(label='Pytanie 9: Jakie jest ryzyko związane z akcjami?', choices=Q9_CHOICES, widget=forms.RadioSelect)
    Q10 = forms.ChoiceField(label='Pytanie 10: Dlaczego inwestowanie w akcje może stanowić ochronę przed inflacją?', choices=Q10_CHOICES, widget=forms.RadioSelect)


class QuizForm3(forms.Form):
    Q1_CHOICES = [
        (True, 'Fundusz notowany na giełdzie'),
        (False, 'Fundusz inwestycyjny zarządzany przez bank')
    ]
    Q2_CHOICES = [
        (True, 'ETF umożliwia inwestowanie w cały indeks jednym kliknięciem'),
        (False, 'ETF wymaga analizy każdej spółki przed zakupem')
    ]
    Q3_CHOICES = [
        (True, 'ETF są wolne od ryzyka rynkowego'),
        (False, 'ETF podlegają mechanizmom rynkowym jak inne instrumenty giełdowe')
    ]
    Q4_CHOICES = [
        (True, 'ETF są zarządzane aktywnie przez ekspertów'),
        (False, 'ETF są notowane na giełdzie i mają niższe koszty zarządzania')
    ]
    Q5_CHOICES = [
        (True, 'Commodity ETF'),
        (False, 'Equity ETF')
    ]
    Q6_CHOICES = [
        (True, 'Equity ETF'),
        (False, 'Bond ETF')
    ]
    Q7_CHOICES = [
        (True, 'SPDR Gold Shares'),
        (False, 'Invesco Dynamic Pharmaceuticals ETF (PJP)')
    ]
    Q8_CHOICES = [
        (True, 'Śledzi wartość waluty lub koszyka walut'),
        (False, 'Śledzi ceny towarów, takich jak złoto czy ropa')
    ]
    Q9_CHOICES = [
        (True, 'Fundusze, które posiadają fizycznie towary'),
        (False, 'Fundusze, które angażują się w transakcje na instrumentach pochodnych towarów')
    ]
    Q10_CHOICES = [
        (True, 'Gwarantuje szybki zysk w krótkim okresie'),
        (False, 'W dłuższej perspektywie, inwestycje mogą zyskać na wartości')
    ]

    Q1 = forms.ChoiceField(label='Pytanie 1: Co to jest ETF?', choices=Q1_CHOICES, widget=forms.RadioSelect)
    Q2 = forms.ChoiceField(label='Pytanie 2: Czym ETF różni się od bezpośredniego kupna akcji?', choices=Q2_CHOICES, widget=forms.RadioSelect)
    Q3 = forms.ChoiceField(label='Pytanie 3: Jakie ryzyko związane jest z inwestowaniem w ETF?', choices=Q3_CHOICES, widget=forms.RadioSelect)
    Q4 = forms.ChoiceField(label='Pytanie 4: Czym różni się ETF od TFI?', choices=Q4_CHOICES, widget=forms.RadioSelect)
    Q5 = forms.ChoiceField(label='Pytanie 5: Który rodzaj ETF śledzi indeks giełdowy?', choices=Q5_CHOICES, widget=forms.RadioSelect)
    Q6 = forms.ChoiceField(label='Pytanie 6: Który rodzaj ETF śledzi koszyk obligacji?', choices=Q6_CHOICES, widget=forms.RadioSelect)
    Q7 = forms.ChoiceField(label='Pytanie 7: Jaki jest przykład sektorowego ETF?', choices=Q7_CHOICES, widget=forms.RadioSelect)
    Q8 = forms.ChoiceField(label='Pytanie 8: Czym charakteryzuje się walutowy ETF?', choices=Q8_CHOICES, widget=forms.RadioSelect)
    Q9 = forms.ChoiceField(label='Pytanie 9: Czym są ETF-y na towary?', choices=Q9_CHOICES, widget=forms.RadioSelect)
    Q10 = forms.ChoiceField(label='Pytanie 10: Dlaczego warto rozważyć inwestowanie w ETF na indeks SP500?', choices=Q10_CHOICES, widget=forms.RadioSelect)
