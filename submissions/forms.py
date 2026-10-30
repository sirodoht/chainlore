import uuid
from django import forms
from django.core import signing
from django.core.exceptions import ValidationError
from django.core.validators import URLValidator
from .catalog import articles

TOKEN_SALT = 'chainlore.submission'


def new_token():
    return signing.dumps(str(uuid.uuid4()), salt=TOKEN_SALT)


class SubmissionForm(forms.Form):
    article = forms.ChoiceField(label='Article', choices=[])
    section = forms.CharField(max_length=200, required=False, label='Section (optional)')
    title = forms.CharField(max_length=200, label='Suggested article title')
    claim = forms.CharField(max_length=3000, widget=forms.Textarea(attrs={'rows': 4}), label='Quoted claim')
    details = forms.CharField(max_length=5000, widget=forms.Textarea(attrs={'rows': 7}))
    correction = forms.CharField(max_length=3000, required=False, widget=forms.Textarea(attrs={'rows': 4}), label='Proposed correction (optional)')
    sources = forms.CharField(max_length=10000, required=False, widget=forms.Textarea(attrs={'rows': 3}), label='Source links (optional)', help_text='One http:// or https:// URL per line, up to 10 links.')
    email = forms.EmailField(max_length=254, required=False, label='Email for a reply (optional)', help_text='Never published. Used only to contact you about this submission.')
    website = forms.CharField(max_length=200, required=False, widget=forms.TextInput(attrs={'tabindex': '-1', 'autocomplete': 'off'}))
    form_token = forms.CharField(widget=forms.HiddenInput)

    def __init__(self, *args, kind, **kwargs):
        if kind not in ('request', 'correction'):
            raise ValueError('Unsupported submission type')
        super().__init__(*args, **kwargs)
        self.fields['article'].choices = [('', 'Select an article')] + [(slug, page['title']) for slug, page in articles().items()]
        self.fields['form_token'].initial = new_token()
        if kind == 'request':
            for field in ('article', 'section', 'claim', 'correction'):
                self.fields.pop(field)
            self.fields['details'].label = 'What should the article cover? (optional)'
            self.fields['details'].required = False
        else:
            self.fields.pop('title')
            self.fields['details'].label = 'What is incorrect, and why?'
            self.fields['sources'].required = True
            self.fields['sources'].label = 'Source links'
        for name, field in self.fields.items():
            if isinstance(field.widget, forms.Textarea):
                field.widget.attrs['maxlength'] = field.max_length

    def clean_sources(self):
        links = [line.strip() for line in self.cleaned_data.get('sources', '').splitlines() if line.strip()]
        if len(links) > 10:
            raise ValidationError('Provide no more than 10 source links.')
        validator = URLValidator(schemes=['http', 'https'])
        for link in links:
            if len(link) > 2000:
                raise ValidationError('Each URL must be at most 2,000 characters.')
            validator(link)
        return '\n'.join(links)

    def clean_form_token(self):
        try:
            value = signing.loads(self.cleaned_data['form_token'], salt=TOKEN_SALT, max_age=7200)
            return uuid.UUID(value)
        except (signing.BadSignature, ValueError, TypeError):
            raise ValidationError('This form has expired. Reload the page and submit again.')
