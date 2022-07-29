from django  import forms

class choice(forms.Form):
    choice1=[('cse','cse'),('Info',"Info"),('Pharmacy',"Pharmacy"),('eee',"eee"),('mechanical',"mechanical")]
    ch = forms.ChoiceField(choices = choice1)

    