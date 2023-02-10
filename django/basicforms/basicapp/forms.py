from django import forms
from django.core import validators

# own validator
def check_for_z(value):
    if value[0].lower() != 'z':
        raise forms.ValidationError('Name needs to start with Z or z!')

class FormName(forms.Form):
    name = forms.CharField(validators=[check_for_z])
    email = forms.EmailField()
    verify_email = forms.EmailField(label='Enter your email again')
    text = forms.CharField(widget=forms.Textarea)

    # hidden field to catch bots
    bot_catcher = forms.CharField(required=False, widget=forms.HiddenInput, validators=[validators.MaxLengthValidator(0)])

    # own validation...
    # usually don't do this
    # def clean_bot_catcher(self):
    #     bot_catcher = self.cleaned_data['bot_catcher']
    #     if len(bot_catcher) > 0:
    #         raise forms.ValidationError('GOTCHA BOT!')
    #     return bot_catcher

    # get all clean data and validate if emails match
    def clean(self):
        # get all clean data of the entire form
        all_clean_data = super().clean()
        email = all_clean_data['email']
        v_email = all_clean_data['verify_email']

        if email != v_email:
            raise forms.ValidationError('Emails do not match!')