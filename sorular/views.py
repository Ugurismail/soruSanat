from django.shortcuts import render, get_object_or_404, redirect
from .models import Soru
from .forms import SoruForm
from django.http import JsonResponse

def ana_sayfa(request):
    sorular = Soru.objects.all()
    ilk_soru = sorular.first()
    nodes = [{"id": soru.id, "label": soru.baslik} for soru in sorular]
    edges = [{"from": soru.ust_soru.id, "to": soru.id} for soru in sorular if soru.ust_soru]
    return render(request, 'sorular/ana_sayfa.html', {'ilk_soru': ilk_soru, 'nodes': nodes, 'edges': edges})

def soru_detay(request, soru_id):
    sorular = Soru.objects.all()
    soru = get_object_or_404(Soru, id=soru_id)
    bagli_sorular = soru.alt_sorular.all()
    nodes = [{"id": s.id, "label": s.baslik} for s in sorular]
    edges = [{"from": s.ust_soru.id, "to": s.id} for s in sorular if s.ust_soru]
    if request.method == "POST":
        form = SoruForm(request.POST)
        if form.is_valid():
            yeni_soru = form.save(commit=False)
            yeni_soru.ust_soru = soru
            yeni_soru.save()
            return redirect('soru_detay', soru_id=soru.id)
    else:
        form = SoruForm()
    editable = request.GET.get('edit', False)
    return render(request, 'sorular/soru_detay.html', {'soru': soru, 'bagli_sorular': bagli_sorular, 'form': form, 'editable': editable, 'nodes': nodes, 'edges': edges})

def arama(request):
    query = request.GET.get('q', '')
    if query:
        results = Soru.objects.filter(baslik__icontains=query).values('id', 'baslik')
        return JsonResponse(list(results), safe=False)
    return JsonResponse([], safe=False)