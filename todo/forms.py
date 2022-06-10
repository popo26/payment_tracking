from django import forms
from todo.models import Repay, Todo


class TodoForm(forms.ModelForm):
  
    text = forms.CharField(max_length=40,
        widget = forms.TextInput (
            attrs={
                'class' : "form-control form-control-md",
                'id' : "colFormLabelLg",
                'placeholder' : "e.g. Uber",
            }
        ))

    amount = forms.FloatField(
        widget = forms.TextInput (
            attrs= {
                'class' : "form-control form-control-md",
                'id' : "colFormLabelLg",
                'placeholder' : "e.g. 85",
            }
        ))

    whose_account_to_repay = forms.CharField(max_length=100,
        widget = forms.TextInput (
            attrs= {
                'class' : "form-control form-control-md",
                'id' : "colFormLabelLg",
                'placeholder' : "e.g. Mum",
            }
        ))

    class Meta:
        model = Todo
        fields = ['text', 'amount', 'whose_account_to_repay']

class RepayForm(forms.ModelForm):

    repay = forms.FloatField(
        widget = forms.TextInput (
            attrs= {
                'class' : "form-control form-control-md",
                'id' : "colFormLabelLg",
                'placeholder' : "e.g. 85",
            }
        ))

    class Meta:
        model = Repay
        fields = ['repay', 'todo']

  


