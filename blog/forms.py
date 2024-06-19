from django.forms import ModelForm

from blog.models import Article


class ArticleForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(ArticleForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            if visible.field.label != 'Признак публикации':
                visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Article
        fields = ["title", "content", "preview", "is_published"]
