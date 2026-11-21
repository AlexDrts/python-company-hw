from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView

from .forms import FeedbackForm


class FeedbackContextMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active'] = 'contacts'
        return context


class FeedbackView(FeedbackContextMixin, FormView):
    template_name = 'feedback/feedback.html'
    form_class = FeedbackForm
    success_url = reverse_lazy('feedback:thanks')

    def form_valid(self, form):
        messages.success(self.request, f"Thank you, {form.cleaned_data['name']}! We will reply to {form.cleaned_data['email']} soon.")
        return super().form_valid(form)


class ThanksView(FeedbackContextMixin, TemplateView):
    template_name = 'feedback/thanks.html'
