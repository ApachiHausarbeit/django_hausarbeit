from django.forms import ModelForm
from minimalistic_blog.models import Blog, Comment

""" ModelForm die den Feldern die Klasse form-control hinzufügt. """
class BootstrapModelForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(BootstrapModelForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })


""" BlogForm """
class BlogForm(BootstrapModelForm):
    class Meta:
        model = Blog
        exclude = ('author', 'created_at',)


""" CommentForm """
class CommentForm(BootstrapModelForm):
    class Meta:
        model = Blog
        exclude = ('author', 'blog',)
