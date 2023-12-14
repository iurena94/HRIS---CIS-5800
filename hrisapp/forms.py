from django.forms import ModelForm, DateInput
from .models import Event, Request, Feedback, Message
from django import forms

class EventForm(ModelForm):
  class Meta:
    model = Event
    # datetime-local is a HTML5 input type, format to make date time show on fields
    widgets = {
      'start_time': DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
      'end_time': DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
    }
    fields = '__all__'
    exclude = ['From']

  def __init__(self, *args, **kwargs):
    super(EventForm, self).__init__(*args, **kwargs)
    # input_formats parses HTML5 datetime-local input to datetime field
    self.fields['start_time'].input_formats = ('%Y-%m-%dT%H:%M',)
    self.fields['end_time'].input_formats = ('%Y-%m-%dT%H:%M',)

# request form for employees
class RequestForm(ModelForm):
  content = forms.CharField(widget=forms.Textarea(attrs={'row':'20','cols':'60','placeholder':"Enter content here", 'type':'text'}),)
  class Meta:
    model = Request
    fields = '__all__'
    exclude = ['From']

    def __init__(self, *args, **kwargs):
      super(RequestForm, self).__init__(*args, **kwargs)

# feedback form for all users
class FeedbackForm(ModelForm):
  topic = forms.CharField(widget=forms.TextInput(attrs={'placeholder':"Enter topic here", 'type':'text'}),)
  content = forms.CharField(widget=forms.Textarea(attrs={'row':'20','cols':'60','placeholder':"Enter content here", 'type':'text'}),)
  class Meta:
    model = Feedback
    fields = '__all__'
    exclude = ['From']

    def __init__(self, *args, **kwargs):
      super(FeedbackForm, self).__init__(*args, **kwargs)

# message form for all users
class MessageForm(ModelForm):
  subject = forms.CharField(widget=forms.TextInput(attrs={'placeholder':"Enter Subject here", 'type':'text'}),)
  content = forms.CharField(widget=forms.Textarea(attrs={'row':'20','cols':'60','placeholder':"Enter content here", 'type':'text'}),)
  class Meta:
    model = Message
    fields = '__all__'

    def __init__(self, *args, **kwargs):
      super(MessageForm, self).__init__(*args, **kwargs)