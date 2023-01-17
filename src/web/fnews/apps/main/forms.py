from django import forms
from crispy_forms.layout import Layout
from crispy_forms.helper import FormHelper
from crispy_forms.bootstrap import InlineRadios

MODEL_CHOICES = ((0, 'Simple (Text-Only) Model'),
              (1, 'Feature-Rich Model'))

class MLForm(forms.Form):
    model_selection = forms.ChoiceField(choices=MODEL_CHOICES, widget=forms.RadioSelect)
    text = forms.CharField(label="Source text:")

    def __init__(self, *args, **kwargs):
        super(MLForm, self).__init__(*args, **kwargs)
        helper = self.helper = FormHelper()
        helper.layout = Layout(
            InlineRadios('model_selection')
        )

