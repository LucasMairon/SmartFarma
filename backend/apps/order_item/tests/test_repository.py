from django.test import TestCase
from apps.order_item.repository import OrderItemRepository
from apps.order_item.models import OrderItem


class OrderItemRepositoryTestCase(TestCase):

    def setUp(self):
        self.cart = ...
        self.product = ...
        self.order_item_data = {
            'quantity': 1,
            'product': 1,
            'cart': 1,
        }
        self.order_item = OrderItem.objects.create(**self.order_item_data)

    def test_create_order_item_for_OrderItemRepository_is_success(self):
        order_item = OrderItemRepository.create_instance(self.order_item_data)
        self.assertIsInstance(order_item, OrderItem)

    def test_verify_is_data_is_correct_in_order_item_for_OrderItemRepository(self):
        order_item = OrderItemRepository.create_instance(self.order_item_data)
        self.assertEqual(order_item.name, self.order_item_data['name'])
        self.assertEqual(order_item.price, self.order_item_data['price'])
        self.assertEqual(order_item.available_quantity,
                         self.order_item_data['available_quantity'])
        self.assertEqual(order_item.description,
                         self.order_item_data['description'])
        self.assertEqual(order_item.brand, self.order_item_data['brand'])
        self.assertEqual(order_item.maker, self.order_item_data['maker'])
        self.assertEqual(order_item.weight, self.order_item_data['weight'])
        self.assertEqual(order_item.ean, self.order_item_data['ean'])

    def test_list_all_order_items_for_OrderItemRepository_is_success(self):
        order_items = OrderItemRepository.get_all_instances()
        self.assertEqual(order_items.count(), 1)

    def test_get_order_item_by_id_for_OrderItemRepository_is_success(self):
        order_item = OrderItemRepository.get_instance_by_id(self.order_item.id)
        self.assertEqual(order_item, self.order_item)

    def test_update_order_item_for_OrderItemRepository_is_success(self):
        OrderItemRepository.update_instance(
            self.order_item.id, {'name': 'novo nome'})
        order_item = OrderItemRepository.get_instance_by_id(self.order_item.id)
        self.assertEqual(order_item.name, 'novo nome')

    def test_delete_order_item_for_OrderItemRepository_is_success(self):
        OrderItemRepository.delete_instance(self.order_item.id)
        order_items = OrderItemRepository.get_all_instances()
        self.assertEqual(order_items.count(), 0)
