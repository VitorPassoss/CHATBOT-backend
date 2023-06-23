from rest_framework import serializers
from apps.products.models.product import Product
from apps.products.models.supplier import Supplier


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    supplie_fk = SupplierSerializer(read_only=True)
    supplie_fk_id = serializers.PrimaryKeyRelatedField(source='supplie_fk', write_only=True, queryset=Supplier.objects.all())

    class Meta:
        model = Product
        fields = ['pk','name', 'quantity', 'supplie_fk', 'supplie_fk_id', 'weight']

    def to_internal_value(self, data):
        if 'supplie_fk' in data and isinstance(data['supplie_fk'], dict):
            supplier_data = data.pop('supplie_fk')
            supplier_serializer = SupplierSerializer(data=supplier_data)
            if supplier_serializer.is_valid():
                supplier_serializer.save()
                data['supplie_fk_id'] = supplier_serializer.instance
        return super().to_internal_value(data)

    def create(self, validated_data):
        return Product.objects.create(**validated_data)



