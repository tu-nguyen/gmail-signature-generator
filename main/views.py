from django.http import HttpResponseRedirect
# from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import StyleForm, DataForm

def _get_form(request, formcls, prefix):
    data = request.POST if prefix in request.POST else None
    return formcls(data, prefix=prefix)

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'

class CreatePageView(TemplateView):
    template_name = 'create.html'

    def get(self, request, *args, **kwargs):
        return self.render_to_response({'styleform': StyleForm(prefix='styleform_pre'), 'dataform': DataForm(prefix='dataform_pre')})

    def post(self, request, *args, **kwargs):

        # context = self.get_context_data(**kwargs)

        styleform = _get_form(request, StyleForm, 'styleform_pre')
        dataform = _get_form(request, DataForm, 'dataform_pre')
        # if styleform.is_bound and styleform.is_valid():
        #     # Process styleform and render response
        # elif dataform.is_bound and dataform.is_valid():
        #     # Process dataform and render response
        if styleform.is_bound and styleform.is_valid() and dataform.is_bound and dataform.is_valid():
            return self.render_to_response({'styleform': styleform, 'dataform': dataform})