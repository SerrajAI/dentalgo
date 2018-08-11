from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from . import models
from django import forms
from django.forms import Textarea,ModelForm
from accounts.models import Patient,Appointment,Operation
from bootstrap_datepicker_plus import DatePickerInput, TimePickerInput
from django.forms import formset_factory
from braces.views import LoginRequiredMixin, UserFormKwargsMixin
# ***********************************************************************************************************************************************************************************************



class UserCreateForm(UserCreationForm):
    CIVILITY_CHOICES = (
        ('Mr', 'Monsieur'),
        ('Mme', 'Madame'),

    )
    # cin = forms.CharField(required=True, label="Cin")

    # civility = forms.ChoiceField(choices=CIVILITY_CHOICES, widget=forms.RadioSelect())



    class Meta:
        model = get_user_model()
        fields = ("first_name","last_name","username", "email", "password1", "password2",) #"cin","civility",



    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].label = "Username"
        self.fields["email"].label = "Email address"
        self.fields["first_name"].label = "Prenom"
        self.fields["last_name"].label = "Nom"



# ***********************************************************************************************************************************************************************************************


class PatientCreateForm(ModelForm):

    CIVILITY_CHOICES = (
        ('Mr', 'Monsieur'),
        ('Mme', 'Madame'),

    )


    civility = forms.ChoiceField(choices=CIVILITY_CHOICES, widget=forms.RadioSelect())




    class Meta:
        model = Patient
        fields = ("fullname","cin","civility","phone","assurance","profession","special","profile_picture")
        widgets = {
        #     'fullname': forms.TextInput( attrs={ 'class': 'form-control', 'placeholder': 'Fullname', 'required': True, } ),
        #     'cin': forms.TextInput( attrs={ 'class': 'form-control', 'placeholder': 'BJXXXXX', 'required': True, } ),
        #     'phone': forms.TextInput( attrs={ 'class': 'form-control',  'required': True, } ),
        #     'assurance': forms.TextInput( attrs={ 'class': 'form-control', 'placeholder': 'Assurance', } ),
        #     'profession': forms.TextInput( attrs={ 'class': 'form-control', 'placeholder': 'Profession', } ),
            'special': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description here...','cols': 80, 'rows': 10}),
        #
        #
        #
        }


# *********************************************************************************************************************************************************************************************************
class AppointmentCreateForm(UserFormKwargsMixin,ModelForm):
    model = Appointment

    



    # day = forms.TimeField(widget=forms.TimeInput(format='%H:%M'))
    # time = forms.DateField(widget=forms.widgets.DateInput(format="%d/%m/%Y"))

    # CIVILITY_CHOICES = (
    #     ('Mr', 'Monsieur'),
    #     ('Mme', 'Madame'),
    #
    # )

    # civility = forms.ChoiceField(choices=CIVILITY_CHOICES, widget=forms.RadioSelect())



    class Meta:
        model = Appointment
        fields = fields = ("patient","day","time","special","position")

        day = forms.DateField(
            widget=DatePickerInput(format='%m/%d/%Y')
        )
        widgets = {
            'day': DatePickerInput(),
            'time': TimePickerInput(),
            'special': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description here...','cols': 80, 'rows': 10}),
            }
        # def __init__( self, *args, **kwargs):
        #     super(AppointmentCreateForm, self).__init__(*args, **kwargs)
        #     self.fields['patient'] =forms.ModelChoiceField(queryset=Patient.objects.filter(created_by=request.user))
        #     # self.fields['patient'] = forms.ModelChoiceField(
            #                          queryset=Patient.objects.filter(created_by=form_user))

    #     model = Appointment
    #       #("fullname","cin","civility","phone","assurance","profession","special","profile_picture")
    #     # widgets = {
    #     #     'date': forms.DateInput(attrs={'class':'datepicker'}),
    #     #     # 'time': forms.DateInput(attrs={'class':'datepicker'}),
    #     #
    #     # }
    #     # widgets = {
    #     #     'fullname': forms.TextInput( attrs={ 'class': 'form-control', 'placeholder': 'Fullname', 'required': True, } ),
    #     #     'cin': forms.TextInput( attrs={ 'class': 'form-control', 'placeholder': 'BJXXXXX', 'required': True, } ),
    #     #     'phone': forms.TextInput( attrs={ 'class': 'form-control',  'required': True, } ),
    #     #     'assurance': forms.TextInput( attrs={ 'class': 'form-control', 'placeholder': 'Assurance', } ),
    #     #     'profession': forms.TextInput( attrs={ 'class': 'form-control', 'placeholder': 'Profession', } ),
    #     #     'special': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description here...','cols': 80, 'rows': 10}),
    #     #
    #     #
    #     #
        # }



















# ********************************************************************************************************************************************************************************************************************


class OperationCreateForm(ModelForm):
    model = Operation

    # day = forms.TimeField(widget=forms.TimeInput(format='%H:%M'))
    # time = forms.DateField(widget=forms.widgets.DateInput(format="%d/%m/%Y"))

    # CIVILITY_CHOICES = (
    #     ('Mr', 'Monsieur'),
    #     ('Mme', 'Madame'),
    #
    # )

    # civility = forms.ChoiceField(choices=CIVILITY_CHOICES, widget=forms.RadioSelect())




    class Meta:
        model = Operation
        fields = ("fullname","patient","dent","appointment","special","price","advance",)
        day = forms.DateField(
            widget=DatePickerInput(format='%m/%d/%Y')
        )
        widgets = {
            'day': DatePickerInput(),
            'time': TimePickerInput(),
            'special': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description here...','cols': 80, 'rows': 10}),
            }
    #     model = Appointment
    #       #("fullname","cin","civility","phone","assurance","profession","special","profile_picture")
    #     # widgets = {
    #     #     'date': forms.DateInput(attrs={'class':'datepicker'}),
    #     #     # 'time': forms.DateInput(attrs={'class':'datepicker'}),
    #     #
    #     # }
    #     # widgets = {
    #     #     'fullname': forms.TextInput( attrs={ 'class': 'form-control', 'placeholder': 'Fullname', 'required': True, } ),
    #     #     'cin': forms.TextInput( attrs={ 'class': 'form-control', 'placeholder': 'BJXXXXX', 'required': True, } ),
    #     #     'phone': forms.TextInput( attrs={ 'class': 'form-control',  'required': True, } ),
    #     #     'assurance': forms.TextInput( attrs={ 'class': 'form-control', 'placeholder': 'Assurance', } ),
    #     #     'profession': forms.TextInput( attrs={ 'class': 'form-control', 'placeholder': 'Profession', } ),
    #     #     'special': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description here...','cols': 80, 'rows': 10}),
    #     #
    #     #
    #     #
        # }
