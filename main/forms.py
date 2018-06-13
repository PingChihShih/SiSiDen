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
        ("normal", "正常糖"),
        ("little", "少糖"),
        ("no", "無糖"),
    )
    sugar = forms.CharField(widget=forms.Select(choices=sugar_choices))
    count = forms.IntegerField(
        widget=forms.NumberInput(attrs={'name': 'count',
                                        'value': '0',
                                        'width': '20',
                                        'class': 'number-input'}))

class TableForm(forms.Form):
    table = forms.CharField(max_length=3,
        widget=forms.TextInput(attrs={'id': 'table_id',
                                      'placeholder':'請輸入桌號',
                                      'class': 'centered-input'}))
    password = forms.CharField(max_length=16,
        widget=forms.TextInput(attrs={'id': 'password',
                                      'placeholder':'請輸入密碼',
                                      'class': 'centered-input'}))
