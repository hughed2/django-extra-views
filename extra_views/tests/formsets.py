from django.forms.formsets import BaseFormSet
from django import forms

COUNTRY_CHOICES = (
    ('gb', 'Great Britain'),
    ('us', 'United States'),
    ('ca', 'Canada'),
    ('au', 'Australia'),
    ('nz', 'New Zealand'),
)


class AddressFormSet(BaseFormSet):
    def add_fields(self, form, index):
        super(AddressFormSet, self).add_fields(form, index)
        form.fields['county'] = forms.ChoiceField(choices=COUNTRY_CHOICES,initial='gb')
        