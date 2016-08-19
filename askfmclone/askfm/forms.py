from django import forms
from .models import Answer


class AnswerForm(forms.Form):
    answer = forms.Textarea(widget=forms.TextInput,
                            required=True)

    def clean_answer(self):
        answer = self.cleaned_data.get('answer')

        if answer:
            answer = answer.strip
        return answer
