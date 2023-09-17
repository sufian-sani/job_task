from django.views import generic
from product.models import Product,Variant, ProductVariantPrice, ProductVariant
from django.db.models import Q

class ProductList(generic.ListView):
    # model = Product
    template_name = 'products/list.html'
    # context_object_name = "book_list"
    def get_queryset(self):
        self.product = Product.objects.all()
        # self.productWithVariantPrice = ProductVariantPrice.objects.filter(product=[i for i in self.product])
        # import pdb;pdb.set_trace()
        self.productVariantPrice = ProductVariantPrice.objects.all()

        #varient_group start
        # self.product_variantlist = ProductVariant.objects.all().values_list('variant_title')
        self.variant = Variant.objects.all()
        self.product_variantlist = ProductVariant.objects.all()
        self.varient_group = {}
        for i in self.variant:
            self.varient_title_name = []
            for j in self.product_variantlist:
                if i == j.variant:
                    self.varient_title_name.append(j.variant_title)
                    # print(i.title)
                    # print(j.variant_title)
                self.varient_title_name=list(set(self.varient_title_name))
                # i.__dict__.update({i.title:self.varient_title_name})
                self.varient_group.update({i.title:self.varient_title_name})
        import pdb;pdb.set_trace()
        
        #varient_group end
        # product_list = {}

        for i in self.product:
            self.product_varient = []
            for j in self.productVariantPrice:
                if i == j.product:
                    self.product_varient.append(j)
                    # import pdb;pdb.set_trace()
                    # i.updates.key()
                    # print(i.add_to_class(self.product_list))
                # i=i.__dict__
            i.__dict__.update({'products':self.product_varient})
            # print(self.product_varient)
                    # pass
            # product_list.update(i)
        # import pdb;pdb.set_trace()
        


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.request.GET.get('title'):
            title = self.request.GET.get('title')
            self.product=self.product.filter(title__icontains=title)
            # import pdb;pdb.set_trace()
            for i in self.product:
                self.product_varient = []
                for j in self.productVariantPrice:
                    if i == j.product:
                        self.product_varient.append(j)
                        # import pdb;pdb.set_trace()
                        # i.updates.key()
                        # print(i.add_to_class(self.product_list))
                    # i=i.__dict__
                i.__dict__.update({'products':self.product_varient})

        if self.request.GET.get('variant'):
            variant = self.request.GET.get('variant')
            self.productVariantPrice = self.productVariantPrice.filter(Q(product_variant_one__variant_title=variant) | Q(product_variant_two__variant_title=variant) | Q(product_variant_three__variant_title=variant))
            for i in self.product:
                self.product_varient = []
                for j in self.productVariantPrice:
                    if i == j.product:
                        self.product_varient.append(j)
                        # self.product = self.product.filter(id=i.id)
                        # print(self.product)
                i.__dict__.update({'products':self.product_varient})
                if not i.products:
                    self.product = self.product.exclude(id=i.id)

            for i in self.product:
                self.product_varient = []
                for j in self.productVariantPrice:
                    if i == j.product:
                        self.product_varient.append(j)
                i.__dict__.update({'products':self.product_varient})

        if self.request.GET.get('price_from') and self.request.GET.get('price_to'):
            price_from = self.request.GET.get('price_from')
            price_to = self.request.GET.get('price_to')
            self.productVariantPrice = self.productVariantPrice.filter(price__range=(price_from,price_to))
            for i in self.product:
                self.product_varient = []
                for j in self.productVariantPrice:
                    if i == j.product:
                        self.product_varient.append(j)
                        # self.product = self.product.filter(id=i.id)
                        # print(self.product)
                i.__dict__.update({'products':self.product_varient})
                if not i.products:
                    self.product = self.product.exclude(id=i.id)

            for i in self.product:
                self.product_varient = []
                for j in self.productVariantPrice:
                    if i == j.product:
                        self.product_varient.append(j)
                i.__dict__.update({'products':self.product_varient})

        if self.request.GET.get('date'):
            date = self.request.GET.get('date')
            self.product=self.product.filter(created_at__date=date)

            for i in self.product:
                self.product_varient = []
                for j in self.productVariantPrice:
                    if i == j.product:
                        self.product_varient.append(j)
                        # import pdb;pdb.set_trace()
                        # i.updates.key()
                        # print(i.add_to_class(self.product_list))
                    # i=i.__dict__
                i.__dict__.update({'products':self.product_varient})
        
        # import pdb;pdb.set_trace()

        # context['product_variantlist'] = list(set(self.product_variantlist))
        context['product_variantlist'] = self.varient_group
        # import pdb;pdb.set_trace()
        context['product_list'] = self.product
        return context