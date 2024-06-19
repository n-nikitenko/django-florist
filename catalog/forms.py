from django.forms import ModelForm

from catalog.models import Product


class ProductForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Product
        fields = ["title", "description", "preview", "price", "category"]
