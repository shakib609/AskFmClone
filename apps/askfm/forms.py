from django import forms


class QuestionForm(forms.Form):
    question_text = forms.CharField(
        widget=forms.Textarea,
        max_length=300,
        label='Ask something!',
        required=True
    )
    anonymous = forms.BooleanField(
        widget=forms.CheckboxInput,
        label='Ask Anonymously',
        required=False
    )

    def clean_question_text(self):
        question_text = self.cleaned_data.get('question_text')
        if question_text:
            question_text = question_text.strip()
        return question_text
