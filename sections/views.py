from django.urls import reverse
from django.views.generic import TemplateView

from .data import SECTIONS
from .entities import EXECUTIVES, PRINCIPLES


class SectionMixin:
    section = None

    def get_section(self):
        return SECTIONS[self.section]

    def get_subsections(self):
        return [
            {**data, 'slug': slug, 'url': reverse('sections:subsection', args=[self.section, slug])}
            for slug, data in self.get_section()['subsections'].items()
        ]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'active': self.section,
            'section': self.get_section(),
            'section_url': reverse(f'sections:{self.section}'),
            'subsections': self.get_subsections(),
        })
        return context


class SectionView(SectionMixin, TemplateView):
    def get_template_names(self):
        return [f'{self.section}.html']


class ManagementView(SectionView):
    section = 'management'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['company'] = {
            'name': 'Company',
            'executives': EXECUTIVES,
            'principles': PRINCIPLES,
            'contacts': {'email': 'info@example.com', 'phone': '10000000000'},
        }
        return context


class SubsectionView(SectionMixin, TemplateView):
    template_name = 'sections/subsection.html'

    def get(self, request, *args, **kwargs):
        self.section = kwargs['section']
        if self.section not in SECTIONS or kwargs['slug'] not in self.get_section()['subsections']:
            return NotFoundView.as_view()(request)
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        slug = kwargs['slug']
        context.update({
            'subsection': self.get_section()['subsections'][slug],
            'active_subsection': slug,
        })
        return context


class NotFoundView(TemplateView):
    template_name = '404.html'

    def dispatch(self, request, *args, **kwargs):
        context = self.get_context_data(path=request.path)
        return self.render_to_response(context, status=404)
