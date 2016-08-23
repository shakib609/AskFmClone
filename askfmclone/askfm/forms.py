from django import forms
# from django.core import validators

# from .models import Answer


# class AnswerForm(forms.Form):
#     answer = forms.Textarea(widget=forms.TextInput,
#                             required=True)

#     def clean_answer(self):
#         answer = self.cleaned_data.get('answer')

#         if answer:
#             answer = answer.strip()
#         return answer


class QuestionForm(forms.Form):
    question_text = forms.CharField(
        widget=forms.Textarea,
        max_length=300,
        label='Ask something!',
        required=True
    )
    anonymous = forms.BooleanField(
        widget=forms.CheckboxInput,
        label='Ask Anonymously'
    )

    def clean_question_text(self):
        question_text = self.cleaned_data.get('question_text')
        if question_text:
            question_text = question_text.strip()
        return question_text
