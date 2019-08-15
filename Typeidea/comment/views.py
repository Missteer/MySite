from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic import TemplateView
# Create your views here.
from .forms import CommentForm

class CommentView(TemplateView):
    http_method_names = ['post']
    template_name = 'comment/result.html'

    def post(self,request,*args,**kwargs):
        comment_form = CommentForm(request.POST)
        target = request.POST.get('target')

        if comment_form.is_valid():
            '''Django之form组件is_valid校验机制 '''
            isinstance = comment_form.save(commit=False)
            isinstance.target = target
            isinstance.save()
            succeed = True
            return redirect(target)
        else:
            succeed = False

        context = {
            'succeed':succeed,
            'form':comment_form,
            'target':target,
        }
        return  self.render_to_response(context)




