from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

from .models import Author, Quote, Tag
from .forms import AuthorForm, QuoteForm, UserRegisterForm
from django.core.paginator import Paginator
import requests
from bs4 import BeautifulSoup

from django.views.generic import TemplateView, ListView

def home(request):
    return render(request, 'quotes/home.html')

class HomeView(TemplateView):
    template_name = 'quotes/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['authors'] = Author.objects.all()
        context['quotes'] = Quote.objects.all()
        return context

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request, 'quotes/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'quotes/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('home')

@login_required
def add_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AuthorForm()
    return render(request, 'quotes/add_author.html', {'form': form})

@login_required
def add_quote(request):
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = QuoteForm()
    return render(request, 'quotes/add_quote.html', {'form': form})


@login_required
def scrape(request):
    url = "http://quotes.toscrape.com"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    quotes = soup.find_all('div', class_='quote')
    for quote in quotes:
        text = quote.find('span', class_='text').get_text()
        author_name = quote.find('small', class_='author').get_text()
        tags = [tag.get_text() for tag in quote.find_all('a', class_='tag')]

        author, created = Author.objects.get_or_create(name=author_name)
        quote_obj, created = Quote.objects.get_or_create(text=text, author=author)

        for tag_name in tags:
            tag, created = Tag.objects.get_or_create(name=tag_name)
            quote_obj.tags.add(tag)

    return redirect('login')


def author_list(request):
    authors = Author.objects.all()
    paginator = Paginator(authors, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'quotes/author_list.html', {'page_obj': page_obj})

# class AuthorListView(ListView):
#     model = Author
#     template_name = 'quotes/author_list.html'
#     context_object_name = 'page_obj'
#     paginate_by = 10

#     def get_queryset(self):
#         return Author.objects.all()

def author_detail(request, pk):
    author = get_object_or_404(Author, pk=pk)
    quotes = Quote.objects.filter(author=author)
    return render(request, 'quotes/author_detail.html', {'author': author, 'quotes': quotes})

# class AuthorDetailView(TemplateView):
#     template_name = 'quotes/author_detail.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['author'] = get_object_or_404(Author, pk=kwargs['pk'])
#         context['quotes'] = Quote.objects.filter(author=context['author'])
#         return context

def quote_list(request):
    quotes = Quote.objects.all()
    paginator = Paginator(quotes, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'quotes/quote_list.html', {'page_obj': page_obj})


def quotes_by_tag(request, tag_name):
    tag = get_object_or_404(Tag, name=tag_name)
    quotes = Quote.objects.filter(tags=tag)
    paginator = Paginator(quotes, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'quotes/quotes_by_tag.html', {'page_obj': page_obj, 'tag': tag})
