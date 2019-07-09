from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    #增加条件qq号必须是数字
    def clean_qq(self):
        cleaned_data = self.cleaned_data['qq']
        if not cleaned_data.isdigit():
            #我们可以使用raise语句自己触发异常
            #一旦执行了raise语句，raise后面的语句将不能执行
            raise forms.ValidationError('必须是数字！')
        return int(cleaned_data)
    class Meta:
        model = Student
        fields = [
            'name','sex','profession','email','qq',
            'phone'
        ]



    