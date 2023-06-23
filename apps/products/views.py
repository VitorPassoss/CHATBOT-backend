from rest_framework.views import APIView
from rest_framework.response import Response
from apps.products.models.product import Product
from apps.products.models.supplier import Supplier
from apps.products.serializers import ProductSerializer, SupplierSerializer
from rest_framework import status
from rest_framework.exceptions import NotFound
from django.shortcuts import get_object_or_404

class ProductHandler(APIView):
    serializer_class = ProductSerializer
    def get(self, request, pk=None):
        all_products = Product.objects.all()
        product_serializer = ProductSerializer(all_products, many=True).data
        return Response(product_serializer, status=status.HTTP_200_OK)
    
    def post(self, request):
        product_data = request.data
        if 'supplie_fk' in product_data and isinstance(product_data['supplie_fk'], dict):
            supplier_data = product_data['supplie_fk']
            supplier_serializer = SupplierSerializer(data=supplier_data)
            if supplier_serializer.is_valid():
                supplier_serializer.save()
                product_data['supplie_fk'] = supplier_serializer.data
            else:
                return Response(supplier_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        product_serializer = self.serializer_class(data=product_data)
        if product_serializer.is_valid():
            product_serializer.save()
            return Response(product_serializer.data, status=status.HTTP_201_CREATED)
        return Response(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        saved_product = get_object_or_404(Product.objects.all(), pk=pk)
        product_serializer = self.serializer_class(instance=saved_product, data=request.data, partial=True)

        if product_serializer.is_valid():
            product_serializer.save()
            return Response(product_serializer.data, status=status.HTTP_200_OK)
        return Response(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        product = get_object_or_404(Product.objects.filter(pk=pk))
        product.delete()
        return Response({"message": f"Product with id {pk} has been deleted."}, status=status.HTTP_204_NO_CONTENT)



class SupplieHandler(APIView):
    serializer_class = SupplierSerializer
    def get(self, request, pk=None):
        all_supplie = Supplier.objects.all()
        supplie_serializer = SupplierSerializer(all_supplie, many=True).data
        return Response(supplie_serializer, status=status.HTTP_200_OK)

    def post(self, request, pk=None):
        supplie_serializer = self.serializer_class(data=request.data)
        if supplie_serializer.is_valid():
            supplie_serializer.save()
            return Response(supplie_serializer.data, status=status.HTTP_201_CREATED)
        return Response(supplie_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        saved_supplie= get_object_or_404(Supplier.objects.all(), pk=pk)
        supplie_serializer = self.serializer_class(instance=saved_supplie, data=request.data, partial=True)

        if supplie_serializer.is_valid():
            supplie_serializer.save()
            return Response(supplie_serializer.data, status=status.HTTP_200_OK)
        return Response(supplie_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        supplie = get_object_or_404(Supplier.objects.all(), pk=pk)
        supplie.delete()
        return Response({"message": f"supplie with id {pk} has been deleted."}, status=status.HTTP_204_NO_CONTENT)

    