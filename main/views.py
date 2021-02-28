from django.http import HttpResponseRedirect
# from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import StyleForm, DataForm
from django.views.generic.edit import FormView

def _get_form(request, formcls, prefix):
    data = request.POST if prefix in request.POST else None
    return formcls(data, prefix=prefix)

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'

class CreatePageView(FormView):
    template_name = 'create.html'

    def get(self, request, *args, **kwargs):
        styleform = StyleForm(auto_id=True)
        styleform.prefix = 'styleform_pre'
        dataform = DataForm(auto_id=True)
        dataform.prefix = 'dataform_pre'
        return self.render_to_response({'styleform': styleform, 'dataform': dataform})

    def post(self, request, *args, **kwargs):
        styleform = _get_form(request, StyleForm, 'styleform_pre')
        dataform = _get_form(request, DataForm, 'dataform_pre')


        # if style_form.is_valid(): #and data_form.is_valid():
        #     ### do something
        #     print("success")
        #     return HttpResponseRedirect('..')
        print(dataform.errors)
        if dataform.is_valid():
            ### do something
            print("success2")
            return HttpResponseRedirect('..')
        else:
            return self.form_invalid(styleform, dataform, **kwargs)

    def form_invalid(self, styleform, dataform, **kwargs):
        styleform.prefix='styleform_pre'
        dataform.prefix='dataform_pre'
        print("fail")
        return self.render_to_response({'styleform': StyleForm(prefix='styleform_pre'), 'dataform': DataForm(prefix='dataform_pre')})


