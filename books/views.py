from django.shortcuts import render, get_object_or_404
from django.views.generic.base import View
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView, CreateView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy

from .models import Book
from .forms import ContactForm, BookCreateForm


class BookDetailView(View):
    def get(self, request, *args, **kwargs):
        book = get_object_or_404(Book, pk=kwargs['pk'])
        context = {'book': book}
        return render(request, 'books/book_detail.html', context)


# class BookCreateView(CreateView):
    # def get(self, request, *args, **kwargs):
        # context = {'form': BookCreateForm()}
        # return render(request, 'books/book-create.html', context)
    # def post(self, request, *args, **kwargs):
        # form = BookCreateForm(request.POST)
        # if form.is_valid():
            # book = form.save()
            # book.save()
            # return HttpResponseRedirect(reverse_lazy('books:detail', args=[book.id]))
        # return render(request, 'books/book-create.html', {'form': form})
class BookCreateView(CreateView):
    template_name = 'books/book-create.html'
    form_class = BookCreateForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_initial(self, *args, **kwargs):
        initial = super(BookCreateView, self).get_initial(**kwargs)
        initial['title'] = 'My Title'
        return initial

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(BookCreateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs


class ContactView(FormView):
    form_class = ContactForm
    template_name = 'books/contact-us.html'
    success_url = reverse_lazy('books:contact-us')

    def get_initial(self):
        initial = super(ContactView, self).get_initial()
        if self.request.user.is_authenticated:
            initial.update({'name': self.request.user.get_full_name()})
        return initial

    def form_valid(self, form):
        self.send_mail(form.cleaned_data)
        return super(ContactView, self).form_valid(form)

    def send_mail(self, valid_data):
        print(valid_data)
