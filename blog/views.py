from django.shortcuts import render, get_object_or_404, redirect
from .models import Livre,Lieu
from .forms import MoveForm
from django.contrib import messages

def livre_list(request):
    livres = Livre.objects.filter()
    lieux = Lieu.objects.all()
    return render(request, 'blog/livre_list.html', {'livres':livres, 'lieux':lieux})

def livre_detail(request, id_livre):
    livre = get_object_or_404(Livre, id_livre=id_livre)
    lieu_actuel=livre.lieu
    form = MoveForm()
    message = ''

    if request.method == "POST":
        form = MoveForm(request.POST, instance=livre)
        if form.is_valid():
            livre = form.save(commit=False)
            nouveau_lieu=livre.lieu

            if nouveau_lieu.id_lieu == "Lecture":
                if nouveau_lieu.disponibilité == "disponible":
                    lieu_actuel.disponibilité = "disponible"
                    lieu_actuel.save()
                    nouveau_lieu.disponibilité = "occupé"
                    nouveau_lieu.save()
                    livre.statut = "emprunté"
                    livre.save()
                    return redirect('livre_list')
                else:
                    message = messages.error(request, "Le lieu lecture est déjà occupé. Déplacement impossible.")
            
            elif nouveau_lieu.id_lieu == "Bibliothèque":
                nouveau_lieu.disponibilité = "disponible"
                nouveau_lieu.save()
                lieu_actuel.disponibilité = "disponible"
                lieu_actuel.save()
                livre.statut = "disponible"
                livre.save()
                return redirect('livre_list')
            
            elif nouveau_lieu.id_lieu == "Coin enfant":
                nouveau_lieu.disponibilité = "disponible"
                nouveau_lieu.save()
                lieu_actuel.disponibilité = "disponible"
                lieu_actuel.save()
                livre.statut = "emprunté"
                livre.save()
                return redirect('livre_list')
        else:
            message = messages.error(request, "Le formulaire n'est pas valide. Veuillez vérifier les champs.")
    else:
        form = MoveForm(instance=livre)
    return render(request,'blog/livre_detail.html',{'livre': livre, 'lieu': lieu_actuel, 'form': form, 'message':message})


