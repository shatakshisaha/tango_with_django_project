from django import forms
from rango.models import Page, Category, UserProfile
from django.contrib.auth.models import User


class CategoryForm(forms.ModelForm):
    """Form to add a new category."""
    name = forms.CharField(
        max_length=Category.NAME_MAX_LENGTH,
        help_text="Please enter the category name."
    )
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Category
        fields = ('name',)


class PageForm(forms.ModelForm):
    """Form to add a new page to a category."""
    title = forms.CharField(
        max_length=Page.TITLE_MAX_LENGTH,
        help_text="Please enter the title of the page."
    )
    url = forms.URLField(
        max_length=Page.URL_MAX_LENGTH,
        help_text="Please enter the URL of the page."
    )
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    class Meta:
        model = Page
        exclude = ('category',)

    def clean(self):
        """Ensure URLs start with 'http://' or 'https://'."""
        cleaned_data = super().clean()
        url = cleaned_data.get('url')

        if url and not url.startswith(('http://', 'https://')):
            cleaned_data['url'] = f'http://{url}'

        return cleaned_data

class UserForm(forms.ModelForm):
    # Password field with a PasswordInput widget to hide the input
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        # Specifies which model this form is for and which fields to include
        model = User
        fields = ('username', 'email', 'password',)
        
class UserProfileForm(forms.ModelForm):
    class Meta:
        # Specifies the model for the profile form and the fields to include
        model = UserProfile
        fields = ('website', 'picture',)

