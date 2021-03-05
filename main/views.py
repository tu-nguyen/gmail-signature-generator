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
        styleform = StyleForm(request.POST, prefix = 'styleform_pre')
        dataform = DataForm(request.POST, prefix = 'dataform_pre')

        if styleform.is_valid():
            test = styleform.cleaned_data['template_style']
            print(test)
            test = styleform.cleaned_data['primary_color']
            print(test)
            return HttpResponseRedirect('..')
        elif dataform.is_valid():
            test = dataform.cleaned_data['first_name']
            print(test)
            return HttpResponseRedirect('..')
        else:
            return self.form_invalid(styleform, dataform, **kwargs)

    def form_invalid(self, styleform, dataform, **kwargs):
        styleform.prefix='styleform_pre'
        dataform.prefix='dataform_pre'
        print("fail")
        return self.render_to_response({'styleform': StyleForm(prefix='styleform_pre'), 'dataform': DataForm(prefix='dataform_pre')})


