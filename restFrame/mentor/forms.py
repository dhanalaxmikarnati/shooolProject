from django import forms

class AddStudentForm(forms.Form):
    student_email = forms.EmailField(label='Student Email')