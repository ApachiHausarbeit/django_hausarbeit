# -*- coding: utf-8 -*-
from django.views.generic import ListView, TemplateView, FormView, DeleteView, UpdateView

from minimalistic_blog.models import Blog, Comment
from minimalistic_blog.forms import BlogForm, CommentForm

""" Alle existierenden Artikel auflisten. """
class ArticleListView(ListView):
    model = Blog
    def get_context_data(self, **kwargs):
        context = super(ArticleListView, self).get_context_data(**kwargs)
        context['articles'] = Blog.objects.all().order_by('-created_at')
        return context


""" Einen bestimmten Artikel und dessen Kommentare anzeigen lassen. """
class ArticleTemplateView(TemplateView):
    template_name = 'article_show.html'

    def get_context_data(self, **kwargs):
        context = super(ArticleTemplateView, self).get_context_data(**kwargs)
        context['article'] = Blog.objects.get(id=kwargs['blog_id'])
        context['comments'] = Comment.objects.filter(blog=kwargs['blog_id'])
        return context


""" Einen neuen Artikel erstellen. """
class ArticleFormView(FormView):
    template_name = "article_create_form.html"
    form_class = BlogForm
    success_url = ""

    def form_valid(self, form, *args, **kwargs):
        form.instance.author = self.request.user
        form.save()
        return super(ArticleCreateView, self).form_valid(form)


""" Einen Artikel löschen. """
class ArticleDeleteView(DeleteView):
    model = Blog
    template_name = "delete_confirmation.html"
    success_url = ""

    def get_object(self, queryset=None):
        """ Das Objekt holen und vor dem löschen sicher stellen,
        dass es dem request.user gehört."""
        obj = super(ArticleDeleteView, self).get_object()
        if not obj.author == self.request.user:
            raise Http404
        return obj


""" Einen Kommentar erstellen. """
class CommentFormView(FormView):
    template_name = "comment_create_form.html"
    form_class = CommentForm
    success_url = ""

    def form_valid(self, form, *args, **kwargs):
        form.instance.author = self.request.user
        form.save()
        return super(CommentFormView, self).form_valid(form)


""" Einen Kommentar löschen. """
class CommentDeleteView(DeleteView):
    model = Comment
    template_name = "delete_confirmation.html"
    success_url = ""

    def get_object(self, queryset=None):
        """ Das Objekt holen und vor dem löschen sicher stellen,
        dass es dem request.user gehört. """
        obj = super(CommentDeleteView, self).get_object()
        if not obj.author == self.request.user:
            raise Http404
        return obj
