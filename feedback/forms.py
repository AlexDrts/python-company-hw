from django import forms


class FeedbackForm(forms.Form):
    TOPICS = [
        ('project', 'New project'),
        ('support', 'Support'),
        ('career', 'Career'),
        ('other', 'Other'),
    ]

    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Your name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'you@example.com'}))
    topic = forms.ChoiceField(choices=TOPICS)
    message = forms.CharField(
        min_length=10,
        widget=forms.Textarea(attrs={'rows': 5, 'placeholder': 'Tell us about your question or project'}),
    )
