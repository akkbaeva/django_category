from django import forms

from category.models import Comment, TVShow


class CommentForm(forms.ModelForm):
    show = forms.ModelChoiceField(widget=forms.HiddenInput(),
                                  disabled=True,
                                  required=False,
                                  queryset=TVShow.objects.all())

    class Meta:
        model = Comment
        fields = [
            'text',
            'show'
        ]