from django import forms

class SingleOrderForm(forms.Form):
    temp_choices = (
        ("iced", "正常冰"),
        ("little-iced", "少冰"),
        ("cool", "去冰"),
        ("hot", "熱"),
    )
    temp = forms.CharField(widget=forms.Select(choices=temp_choices))
    sugar_choices = (
        ("normal-sugar", "正常糖"),
        ("little-sugar", "少糖"),
        ("no-sugar", "無糖"),
    )
    sugar = forms.CharField(widget=forms.Select(choices=sugar_choices))
    count = forms.CharField(max_length=30,
        widget=forms.NumberInput(attrs={'name': 'count',
                                        'value': '0',
                                        'width': '20',
                                        'class': 'number-input'}))
