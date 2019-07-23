from django import forms

class PostAdminForm(forms.ModelForm):
    #desc 摘要
    desc = forms.CharField(widget=forms.Textarea,label='摘要',required=False)
