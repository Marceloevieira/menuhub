from django.views.generic import ListView, DetailView
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from menus.forms import MenuItemForm, RestaurantForm

from menus.models import MenuItem, Restaurant

# Create your views here.


@login_required
def index(request):
    return render(request, "home.html")


class RestaurantListView(LoginRequiredMixin, ListView):
    template_name = "restaurants/list.html"
    context_object_name = "restaurant_list"

    def get_queryset(self):
        return Restaurant.objects.all()


class ResturantDetailView(LoginRequiredMixin, DetailView):
    model = Restaurant
    template_name = "restaurants/detail.html"


@login_required
def restaurants_create(request):
    if request.method == 'POST':
        form = RestaurantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('app-restaurant-list')
    form = RestaurantForm()

    return render(request, 'restaurants/create.html', {'form': form})


@login_required
def restaurants_edit(request, pk, template_name='restaurants/edit.html'):
    restaurant = get_object_or_404(Restaurant, pk=pk)
    form = RestaurantForm(request.POST or None, instance=restaurant)
    if form.is_valid():
        form.save()
        return redirect('app-restaurant-list')
    return render(request, template_name, {'form': form})


@login_required
def restaurants_delete(request, pk, template_name='restaurants/confirm_delete.html'):
    restaurant = get_object_or_404(Restaurant, pk=pk)
    form = RestaurantForm(request.POST or None, instance=restaurant)
    if request.method == 'POST':
        restaurant.delete()
        return redirect('app-restaurant-list')
    return render(request, template_name, {'form': form})


# menu-itens
@login_required
def menu_itens_create(request, fk):
    restaurant = get_object_or_404(Restaurant, pk=fk)
    if request.method == 'POST':
        form = MenuItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('app-restaurant-detail', fk)
    form = MenuItemForm(initial={'restaurant': restaurant, })

    return render(request, 'menu-itens/create.html', {'form': form})


@login_required
def menu_itens_edit(request, fk, pk, template_name='menu-itens/edit.html'):
    restaurant = get_object_or_404(Restaurant, pk=fk)
    menuitem = get_object_or_404(MenuItem, pk=pk)
    form = MenuItemForm(request.POST or None, instance=menuitem)
    if form.is_valid():
        form.save()
        return redirect('app-restaurant-detail', fk)
    return render(request, template_name, {'form': form})


@login_required
def menu_itens_delete(request, fk, pk, template_name='menu-itens/confirm_delete.html'):
    restaurant = get_object_or_404(Restaurant, pk=fk)
    menuitem = get_object_or_404(MenuItem, pk=pk)
    form = MenuItemForm(request.POST or None, instance=menuitem)
    if request.method == 'POST':
        menuitem.delete()
        return redirect('app-restaurant-detail', fk)
    return render(request, template_name, {'form': form})
