from django import forms

class SubjectForm(forms.Form):
    subject1 = forms.CharField(max_length=50, label='First subject')
    subject2 = forms.CharField(max_length=50, label='Second subject')
    subject3 = forms.CharField(max_length=50, label='Third subject')
    subject4 = forms.CharField(max_length=50, label='Fourth subject')
    subject5 = forms.CharField(max_length=50, label='Fifth subject')
    subject6 = forms.CharField(max_length=50, label='Sixth subject')
