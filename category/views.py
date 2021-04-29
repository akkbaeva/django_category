from django.views.decorators.csrf import csrf_exempt

from category.forms import CommentForm
from category.models import Category, TVShow, Comment
from django.http import HttpResponse
# Create your views here.
from django.views.generic import ListView, DetailView


class CategoryListView(ListView):
    model = Category
    template_name = 'category/category_list.html'

    def get_queryset(self):
        return Category.objects.all()


class CategoryDetailView(DetailView):
    model = Category
    template_name = 'category/category_detail.html'


class TVShowListView(ListView):
    model = TVShow
    template_name = 'show/tvshow_list.html'

    def get_queryset(self):
        return TVShow.objects.all()


class TVShowDetailListView(DetailView):
    model = TVShow
    template_name = 'show/tvshowdetail_list.html'
    extra_context = {'form': CommentForm()}

    @csrf_exempt
    def post(self, request, *args, **kwargs):
        if request.user:
            show_id = kwargs['pk']
            show = TVShow.objects.get(pk=show_id)
            form = CommentForm(request.POST, initial={'show': show})
            if form.is_valid():
                form.save()
        return self.get(request, *args, **kwargs)


class CommentListView(ListView):
    model = Comment
    template_name = 'comment/comment_list.html'
