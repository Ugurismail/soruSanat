from django.shortcuts import render
import json
from .models import Soru

def ana_sayfa(request):
    sorular = Soru.objects.all()
    nodes = [{"id": soru.id, "label": soru.baslik} for soru in sorular]
    edges = []  # Eğer bağlantılarınız varsa buraya ekleyin
    context = {
        'sorular': sorular,
        'nodes': json.dumps(nodes),
        'edges': json.dumps(edges),
    }
    return render(request, 'ana_sayfa.html', context)

def soru_detay(request, soru_id):
    soru = get_object_or_404(Soru, id=soru_id)
    alt_sorular = soru.alt_sorular.all()
    sorular_recursive = Soru.objects.all()
    if request.method == "POST":
        form = SoruForm(request.POST)
        if form.is_valid():
            yeni_soru = form.save(commit=False)
            yeni_soru.ust_soru = soru
            yeni_soru.save()
            return redirect('soru_detay', soru_id=soru.id)
    else:
        form = SoruForm()
    return render(request, 'sorular/soru_detay.html', {
        'soru': soru,
        'alt_sorular': alt_sorular,
        'form': form,
        'sorular_recursive': sorular_recursive,
        'current_soru_id': soru_id
    })
