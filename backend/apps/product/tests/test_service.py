from django.test import TestCase
from apps.product.service import ProductService
from apps.product.models import Product


class ProductServiceTestCase(TestCase):

    def setUp(self):
        self.product_data = {
            'name': "teste product nome",
            'price': 1.1,
            'available_quantity': 10,
            'description': "teste product description",
            'brand': "teste marca",
            'maker': "teste fabricante",
            'weight': 10.22,
            'ean': "teste codigo de barras",
            'sku': "teste sku",
        }
        self.product = Product.objects.create(**self.product_data)

    def test_create_product_for_ProductService_is_success(self):
        product = ProductService.create_instance(self.product_data)
        self.assertIsInstance(product, Product)

    def test_verify_is_data_is_correct_in_product_for_ProductService(self):
        product = ProductService.create_instance(self.product_data)
        self.assertEqual(product.name, self.product_data['name'])
        self.assertEqual(product.price, self.product_data['price'])
        self.assertEqual(product.available_quantity,
                         self.product_data['available_quantity'])
        self.assertEqual(product.description, self.product_data['description'])
        self.assertEqual(product.brand, self.product_data['brand'])
        self.assertEqual(product.maker, self.product_data['maker'])
        self.assertEqual(product.weight, self.product_data['weight'])
        self.assertEqual(product.ean, self.product_data['ean'])

    def test_list_all_products_for_ProductService_is_success(self):
        products = ProductService.list_all_instances()
        self.assertEqual(products.count(), 1)

    def test_get_product_by_id_for_ProductService_is_success(self):
        product = ProductService.retrieve_instance(self.product.id)
        self.assertEqual(product, self.product)

    def test_update_product_for_ProductService_is_success(self):
        ProductService.update_instance_and_partial_update(
            self.product.id, {'name': 'novo nome'})
        product = ProductService.retrieve_instance(self.product.id)
        self.assertEqual(product.name, 'novo nome')

    def test_delete_product_for_ProductService_is_success(self):
        ProductService.destroy_instance(self.product.id)
        products = ProductService.list_all_instances()
        self.assertEqual(products.count(), 0)
