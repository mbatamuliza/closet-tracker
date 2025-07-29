from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from .models import ClothingItem
from .forms import ClothingItemForm, SignUpForm




def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})
            

# HOME PAGE VIEW

def home(request):
    return render(request, 'home.html')


class ClothingItemList(LoginRequiredMixin, ListView):
    model = ClothingItem
    template_name = 'wardrobe/clothingitem_list.html'
    context_object_name = 'clothing_items'


    def get_queryset(self):
        return ClothingItem.objects.filter(user=self.request.user)
    

class ClothingItemDetail(LoginRequiredMixin, DetailView):
    model = ClothingItem
    template_name = 'wardrobe/clothingitem_detail.html'
    context_object_name = 'clothing_item'

    

class ClothingItemCreate(LoginRequiredMixin, CreateView):
    model = ClothingItem
    form_class = ClothingItemForm
    template_name = 'wardrobe/clothingitem_form.html'
    success_url = '/items/'


    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    
class ClothingItemUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = ClothingItem
    form_class = ClothingItemForm
    template_name = 'wardrobe/clothingitem_form.html'
    success_url ='/items'

    def test_func(self):
        item = self.get_object()
        return item.user == self.request.user
    

class ClothingItemDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = ClothingItem
    template_name = 'wardrobe/clothingitem_confirm_delete.html'
    success_url = '/items/'

    def test_func(self):
        item = self.get_object()
        return item.user == self.request.user
    

