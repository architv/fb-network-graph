from django import forms

class InputForm(forms.Form):
	access_token = forms.CharField(label='Your access token', required=True, help_text="You can get it from <a href='https://developers.facebook.com/tools/explorer'>here.</a> Mark the permission read_stream.")
	keyword = forms.CharField(max_length=30, label = 'Keyword', required=True)
