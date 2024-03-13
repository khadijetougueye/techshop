from django.shortcuts import redirect, render
from .models import Product, Commande
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Product

# Create your views here.
def index(request):
    product_object =Product.objects.all()
    item_name= request.GET.get('item-name')
    if item_name !='' and item_name is not None:
        product_object = Product.objects.filter(title__icontains=item_name)
    paginator = Paginator(product_object, 4)
    page = request.GET.get('page')
    product_object = paginator.get_page(page)
    return render(request, 'shop/index.html', { 'product_object': product_object})

def detail(request, myid):
    product_object = Product.objects.get(id=myid)
    return render(request, 'shop/detail.html', {'product': product_object})

@login_required
def checkout(request):
    if request.method == "POST":
        items = request.POST.get('items')
        total = request.POST.get('total')
        nom = request.POST.get('nom')
        email = request.POST.get('email')
        address = request.POST.get('address')
        tel = request.POST.get('tel')
        ville = request.POST.get('ville')
        pays = request.POST.get('pays')
        zipcode = request.POST.get('zipcode')
        com = Commande(items=items, total=total, nom=nom, email=email, address=address, tel=tel, ville=ville, pays=pays, zipcode=zipcode)
        com.save()

        # Nettoyer le panier après la commande
        if 'panier' in request.session:
            del request.session['panier']

        return redirect('confirmation')
    return render(request, 'shop/checkout.html')
def confirmation(request):
    info = Commande.objects.all()[:1]
    for item in info:
        nom = item.nom
    return render(request, 'shop/confirmation.html' , {'name':nom})

def products(request):
    # Récupérer tous les produits depuis la base de données
    all_products = Product.objects.all()

    # Passer la liste des produits au contexte de rendu
    return render(request, 'shop/products.html', {'products': all_products})

def load_products(request):
    # votre logique pour charger les produits
    return render(request, 'votre_template.html', {'data': vos_données})