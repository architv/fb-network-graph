from django import forms

class InputForm(forms.Form):
	keyword = forms.CharField(max_length=30, label = 'Keyword', required=True, widget=forms.TextInput(attrs={'placeholder': 'Keyword to search', 'class':'form-control input-lg', 'tabindex':'2'}))
