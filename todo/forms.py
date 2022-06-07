from django import forms
from todo.models import Repay, Todo

# class TodoForm(forms.Form):
    
#     text = forms.CharField(max_length=40,
#         widget = forms.TextInput (
#             attrs={
#                 'class' : "form-control form-control-lg",
#                 'id' : "colFormLabelLg",
#                 'placeholder' : "Enter new payment info",
#             }
#         ))

#     amount = forms.FloatField(
#         widget = forms.TextInput (
#             attrs= {
#                 'class' : "form-control form-control-lg",
#                 'id' : "colFormLabelLg",
#                 'placeholder' : "Enter price. e.g, 85",
#             }
#         ))

class TodoForm(forms.ModelForm):

        
    # text = forms.CharField(max_length=40,
    #     widget = forms.TextInput (
    #         attrs={
    #             'class' : "form-control form-control-lg",
    #             'id' : "colFormLabelLg",
    #             'placeholder' : "Enter new payment info",
    #         }
    #     ))

    # amount = forms.FloatField(
    #     widget = forms.TextInput (
    #         attrs= {
    #             'class' : "form-control form-control-lg",
    #             'id' : "colFormLabelLg",
    #             'placeholder' : "Enter price. e.g, 85",
    #         }
    #     ))

    class Meta:
        model = Todo
        fields = ['text', 'amount', 'whose_account_to_repay']

class RepayForm(forms.ModelForm):

    
    class Meta:
        model = Repay
        fields = "__all__"

