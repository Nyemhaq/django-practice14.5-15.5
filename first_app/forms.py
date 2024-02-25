from django import forms 
import datetime

class studentForm(forms.Form):
    first_name = forms.CharField(initial='Your name')
    name = forms.CharField(label = 'Last Name', initial='Last Name')
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter your Title'})) 
    description = forms.CharField() 
    roll_number = forms.IntegerField(help_text = "Enter 6 digit roll number")  
    password = forms.CharField(widget = forms.PasswordInput()) 
    comment = forms.CharField(widget=forms.Textarea(attrs={'rows':3}))
    email = forms.EmailField()
    join_date = forms.DateField(widget=forms.NumberInput(attrs={'type': 'date'}))
    BIRTH_YEAR_CHOICES = ['1980', '1981', '1982']
    birth_year = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))
    value = forms.DecimalField()
    message = forms.CharField(max_length = 10,widget=forms.TextInput(attrs={'placeholder':'Write your message here...'}))
    day = forms.DateField(initial=datetime.date.today)
    FAVORITE_COLORS_CHOICES = [('blue', 'Blue'),('green', 'Green'),('black', 'Black'),]
    favorite_color = forms.ChoiceField(choices=FAVORITE_COLORS_CHOICES)
    favorite_color = forms.ChoiceField(widget=forms.RadioSelect, choices=FAVORITE_COLORS_CHOICES)
    favorite_colors = forms.MultipleChoiceField(choices=FAVORITE_COLORS_CHOICES) 
    favorite_colors = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=FAVORITE_COLORS_CHOICES,)
    img = forms.ImageField() 
    agree = forms.BooleanField()