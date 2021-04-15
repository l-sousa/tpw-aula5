from django import forms
from app.models import *


class BookQueryForm(forms.Form):
    name = forms.CharField(label='Search Book by Title:', max_length=100)


class BookQueryAuthorForm(forms.Form):
    name = forms.CharField(label='Search Book by Author:', max_length=70)


class BookSearchAuthorPublisherForm(forms.Form):
    authorName = forms.CharField(
        label='Search Book by Author:', max_length=70, required=False)
    publisherName = forms.CharField(
        label='Search Book by Publisher:', max_length=70, required=False)


class InsertAuthor(forms.Form):
    name = forms.CharField(label="Name:", max_length=70)
    email = forms.EmailField(label="Email:", max_length=70)


class InsertPublisher(forms.Form):
    name = forms.CharField(label="Name:", max_length=70)
    city = forms.CharField(label="City:", max_length=70)
    country = forms.CharField(label="Country:", max_length=70)
    website = forms.URLField(label="Website:", max_length=70)


class InsertBook(forms.Form):
    authors = forms.ModelMultipleChoiceField(
        label="Authors: (can be more than one)",
        queryset=Author.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )
    publisher = forms.ModelChoiceField(queryset=Publisher.objects.all(), label="Publisher: ", )
    title = forms.CharField(label="Title: ", max_length=100)
    date = forms.DateField()


class EditAuthor(forms.Form):
    author_to_change = forms.CharField(
        widget=forms.Select(
            choices=Author.objects.all()
        )
    )

    new_name = forms.CharField(label="New Name:", max_length=70)
    new_email = forms.EmailField(label="New Email:", max_length=70)



