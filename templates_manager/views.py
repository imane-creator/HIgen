
from django.shortcuts import render, get_object_or_404
from .models import SiteTemplate

# Liste des templates
def templates_list(request):
    templates = SiteTemplate.objects.all()
    return render(request, 'templates_manager/list_template.html', {'templates': templates})

# Détail d'un template
#def template_detail(request, pk):
#    template = get_object_or_404(SiteTemplate, pk=pk)
  #  return render(request, 'templates_manager/template_detail.html', {'template': template})
