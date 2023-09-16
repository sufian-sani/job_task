from django.views import generic
from product.models import Product,Variant, ProductVariantPrice

class ProductList(generic.ListView):
    # model = Product
    template_name = 'products/list.html'
    # context_object_name = "book_list"
    def get_queryset(self):
        self.product = Product.objects.all()
        # self.productWithVariantPrice = ProductVariantPrice.objects.filter(product=[i for i in self.product])
        self.productWithVariantPrice = ProductVariantPrice.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['varient_list'] = ProductVariantPrice.objects.all()
        import pdb;pdb.set_trace()
        return context