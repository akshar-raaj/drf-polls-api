from django import forms

from .models import Book


class ContactForm(forms.Form):
    name = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)


class BookCreateForm(forms.ModelForm):
    class Meta:
        model = Book
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(BookCreateForm, self).__init__(*args, **kwargs)

    def clean_title(self):
        title = self.cleaned_data['title']
        if Book.objects.filter(user=self.user, title=title).exists():
            raise forms.ValidationError("You have already written a book with same title.")
        return title
