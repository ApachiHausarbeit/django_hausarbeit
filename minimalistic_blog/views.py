# -*- coding: utf-8 -*-
from django.views.generic import ListView, TemplateView, FormView, DeleteView, UpdateView

from minimalistic_blog.models import Blog, Comment
from minimalistic_blog.forms import BlogForm, CommentForm
from minimalistic_blog.auth import LoginRequiredMixin, logout_view

""" Einen bestimmten Artikel und dessen Kommentare anzeigen lassen. """
class ArticleTemplateView(TemplateView):
    template_name = "article.html"

    def get_context_data(self, **kwargs):
        context = super(ArticleTemplateView, self).get_context_data(**kwargs)
        context["article"] = Blog.objects.get(id=kwargs["id"])
        context["comments"] = Comment.objects.filter(blog=kwargs["id"])
        return context


""" Alle existierenden Artikel auflisten. """
class ArticleListView(ListView):
    model = Blog
    template_name = "article_list.html"

    def get_context_data(self, **kwargs):
        context = super(ArticleListView, self).get_context_data(**kwargs)
        context["articles"] = Blog.objects.all().order_by("-created_at")
        return context


""" Einen neuen Artikel erstellen. """
class ArticleFormView(LoginRequiredMixin, FormView):
    template_name = "simple_form.html"
    form_class = BlogForm
    success_url = "/blog/"

    def form_valid(self, form, *args, **kwargs):
        form.instance.author = self.request.user
        form.save()
        return super(ArticleFormView, self).form_valid(form)


""" Einen Artikel löschen. """
class ArticleDeleteView(LoginRequiredMixin, DeleteView):
    model = Blog
    template_name = "delete_confirmation.html"
    success_url = "/blog/"

    def get_object(self, queryset=None):
        """ Das Objekt holen und vor dem löschen sicher stellen,
        dass es dem request.user gehört."""
        obj = super(ArticleDeleteView, self).get_object()
        if not obj.author == self.request.user:
            raise Http404
        return obj


""" Einen Artikel aktualisieren. """
class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    model = Blog
    form_class = BlogForm
    template_name = "simple_form.html"

    def form_valid(self, form):
        self.obj = form.save(commit=False)
        if self.request.user.is_authenticated():
            self.obj.author = self.request.user
        self.obj.save()
        form.save_m2m()
        return super(ArticleUpdateView, self).form_valid(form)

    def get_success_url(self):
        return "/blog/article/%s/" % self.kwargs['pk']


""" Einen Kommentar erstellen. """
class CommentFormView(LoginRequiredMixin, FormView):
    template_name = "simple_form.html"
    form_class = CommentForm

    def form_valid(self, form, *args, **kwargs):
        form.instance.author = self.request.user
        form.instance.blog_id = self.kwargs['id']
        form.save()
        return super(CommentFormView, self).form_valid(form)

    def get_success_url(self):
        return "/blog/article/%s/" % self.kwargs['id']


""" Einen Kommentar löschen. """
class CommentDeleteView(LoginRequiredMixin, DeleteView):
    model = Comment
    template_name = "delete_confirmation.html"

    def get_object(self, queryset=None):
        """ Das Objekt holen und vor dem löschen sicher stellen,
        dass es dem request.user gehört. """
        obj = super(CommentDeleteView, self).get_object()
        if not obj.author == self.request.user:
            raise Http404
        return obj

    def get_success_url(self):
        return "/blog/article/%s/" % self.kwargs['id']


""" Einen Kommentar aktualisieren. """
class CommentUpdateView(LoginRequiredMixin, UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = "simple_form.html"

    def form_valid(self, form):
        self.obj = form.save(commit=False)
        if self.request.user.is_authenticated():
            self.obj.author = self.request.user
        self.obj.save()
        form.save_m2m()
        return super(CommentUpdateView, self).form_valid(form)

    def get_success_url(self):
        return "/blog/article/%s/" % self.kwargs['id']

