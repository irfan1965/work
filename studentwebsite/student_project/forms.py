from django import forms
class FirstName(forms.Form):
    Roll_Number = forms.CharField(label='Your name', max_length=100)
class Branch(forms.Form):
    choice1=[('cse','cse'),('Info',"Info"),('Pharmacy',"Pharmacy"),('eee',"eee"),('mechanical',"mechanical")]
    ch=forms.ChoiceField(choices=choice1)
# class Regis(ModelForm):
#     username = forms.CharField(max_length=100)
#     password = forms.CharField(widget=PasswordInput)
#     email = forms.CharField(widget=EmailInput)
#     discord_id = forms.CharField(max_length=100, label='Discord ID')
#     zoom_id = forms.CharField(max_length=100, label='Zoom ID')
#      class Meta:
#         model = Person
#         fields = ["username", "password", "birthdate", "email", "discord_id", "zoom_id"]



class ByChoice(forms.Form):
    choice1=[('Roll_Number',"Roll_Number"),('branch',"branch"),("registration","registration")]
    ch=forms.ChoiceField(choices=choice1,widget=forms.RadioSelect)
