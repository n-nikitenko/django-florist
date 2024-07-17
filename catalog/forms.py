from django.core.exceptions import ValidationError
from django.forms import ModelForm, BooleanField, BaseInlineFormSet
from django.forms.utils import ErrorList

from catalog.models import Product, Version

FORBIDDEN_WORDS = [
    "казино",
    "криптовалюта",
    "крипта",
    "биржа",
    "дешево",
    "бесплатно",
    "обман",
    "полиция",
    "радар",
]


class StyleFormMixin:
    error_css_class = "text-danger form-control is-invalid"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.error_class = RedFontErrorList
        for _, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs["class"] = "form-check-input"
            else:
                field.widget.attrs["class"] = "form-control"
            if field.required:
                field.label += " *"


class RedFontErrorList(ErrorList):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.error_class += " text-danger"


class BaseVersionFormSet(BaseInlineFormSet):

    def clean(self):
        super().clean()
        if any(self.errors):
            return self.errors
        has_active = False
        for form in self.forms:
            if self.can_delete and self._should_delete_form(form):
                continue
            is_current = form.cleaned_data.get("is_current")
            if has_active and is_current:
                raise ValidationError("Может быть только одна текущая версия")
            has_active = is_current


class ProductForm(StyleFormMixin, ModelForm):

    def __cleaned_field_or_error(self, field_name, error_message):
        field = self.cleaned_data[field_name]
        if any(word.lower() in field.lower() for word in FORBIDDEN_WORDS):
            raise ValidationError(error_message)
        return field

    def clean_title(self):
        return self.__cleaned_field_or_error(
            "title", "В наименовании товара нельзя использовать запрещенные слова"
        )

    def clean_description(self):
        return self.__cleaned_field_or_error(
            "description", "В описании товара нельзя использовать запрещенные слова"
        )

    class Meta:
        model = Product
        fields = ["title", "description", "preview", "price", "category"]


class VersionForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Version
        fields = "__all__"
