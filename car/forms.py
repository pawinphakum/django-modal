from django import forms
from django.forms import ModelForm
from .models import *
from django.utils.translation import ugettext_lazy as _
from django.core.validators import RegexValidator

CAR_NUMBER_REGEX = RegexValidator(regex=r'^\d{2}-\d{4}$', message='ต้องเป็นเลขทะเบียน รูปแบบ 10-1234')

class CarForm(ModelForm):
    message = forms.CharField(label='ข้อความ', widget=forms.Textarea)

    def send_email(self):
        # send email using the self.cleaned_data dictionary
        print(self.cleaned_data['message'])

    class Meta:
        model = Car
        fields = ['name', 'sn']
        labels = {
            'name': _('ชื่อ'),
            'sn': _('รหัส'),
        }
        widgets = {
            'sn': forms.TextInput(attrs={'placeholder':'10-1234'}),
        }
        help_texts = {
            'name': _('อะไรก็ได้ เท่ๆ'),
        }
        error_messages = {
            'name': {
                'max_length': _("This writer's name is too long."),
            },
        }

class CarUpdateForm(ModelForm):
    sn = forms.CharField(label='รหัสsss',
        validators=[CAR_NUMBER_REGEX])

    class Meta:
        model = Car
        fields = ['name', 'sn']
        labels = {
            'name': _('ชื่อ'),
        }
        error_messages = {
            'name': {
                'max_length': _("This writer's name is too long."),
            },
        }

# https://docs.djangoproject.com/en/1.11/topics/forms/modelforms/
