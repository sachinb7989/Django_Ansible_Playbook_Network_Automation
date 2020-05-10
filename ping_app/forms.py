from django import forms


class MyForm(forms.Form):
    Device_List = [
        ('R1', 'R1'),
        ('R2', 'Router2'),
        ('R3', 'Router3'),
        ('R4', 'Router4'),
        ('R5', 'Router5')
    ]
    hostname = forms.CharField(label='Enter Hostname', max_length=20, widget=forms.Select(choices=Device_List))
    Command = forms.CharField(label='Enter Command', max_length=100)
