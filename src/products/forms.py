from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    title       =forms.CharField(widget=forms.TextInput(attrs={"placeholder":"your title"}))
    email       =forms.EmailField()
    description =forms.CharField(required=False,widget=forms.Textarea(
        attrs={
            "class":"new_class",
            "id":"desp_id",
            "rows":20,
            "cols":120,
        }
    )
    )
    price       =forms.DecimalField(initial=199.90)
    class Meta:
        model=Product
        fields=[
            'title',
            'description',
            'price',
        ]
    def clean_title(self,*args,**kwargs):
        title=self.cleaned_data.get("title")
        if not "golap" in title:
            raise forms.ValidationError("this is not a valid title")
        return title
    def clean_email(self,*args,**kwargs):
        email=self.cleaned_data.get("email")
        if not email.endswith("edu"):
            raise forms.ValidationError("this is not a valid email")
        return email


class RawProductForm(forms.Form):
    title       =forms.CharField(widget=forms.TextInput(attrs={"placeholder":"your title"}))
    description =forms.CharField(required=False,widget=forms.Textarea(
        attrs={
            "class":"new_class",
            "id":"desp_id",
            "rows":20,
            "cols":120,
        }
    )
    )
    price       =forms.DecimalField(initial=199.90)