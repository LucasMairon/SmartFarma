from datetime import datetime
from django.test import TestCase
from django.contrib.auth import get_user_model
from apps.shared.apps_tests_datas import tests_datas
from apps.cart.models import Cart
from apps.purchase.models import Purchase
from apps.purchase.repository import PurchaseRepository
from apps.users.service import UserService

User = get_user_model()


class PurchaseRepositoryTestCase(TestCase):

    def setUp(self):
        self.user = UserService.create_instance(
            tests_datas.get_user_data())
        self.cart = Cart.objects.create(
            **tests_datas.get_cart_data(user_id=self.user.id))
        self.cart2 = Cart.objects.create(
            **tests_datas.get_cart_data(user_id=self.user.id))
        self.purchase = Purchase.objects.create(
            **tests_datas.get_purchase_data(
                user_id=self.user.id,
                cart_id=self.cart.id
            )
        )

    def test_create_purchase_for_PurchaseRepository_is_success(self):
        purchase = PurchaseRepository.create_instance(
            tests_datas.get_purchase_data(
                user_id=self.user.id, cart_id=self.cart2.id)
        )
        self.assertIsInstance(purchase, Purchase)

    def test_verify_is_data_is_correct_in_purchase_for_PurchaseRepository(self):
        data = tests_datas.get_purchase_data(
            user_id=self.user.id, cart_id=self.cart2.id)
        purchase = PurchaseRepository.create_instance(data)
        self.assertEqual(purchase.total_price, data['total_price'])
        self.assertEqual(purchase.payment_method, data['payment_method'])
        self.assertEqual(purchase.street, data['street'])
        self.assertEqual(purchase.city, data['city'])
        self.assertEqual(purchase.state, data['state'])
        self.assertEqual(purchase.number, data['number'])
        self.assertEqual(purchase.neighborhood, data['neighborhood'])
        self.assertEqual(purchase.complement, data['complement'])
        self.assertEqual(purchase.reference_point, data['reference_point'])
        self.assertEqual(purchase.zip_code, data['zip_code'])
        self.assertEqual(purchase.status, data['status'])
        self.assertEqual(purchase.user.id, data['user_id'])
        self.assertEqual(purchase.cart.id, data['cart_id'])

    def test_list_all_purchases_for_PurchaseRepository_is_success(self):
        purchases = PurchaseRepository.get_all_instances()
        self.assertEqual(purchases.count(), 1)

    def test_get_purchase_by_id_for_PurchaseRepository_is_success(self):
        purchase = PurchaseRepository.get_instance_by_id(self.purchase.id)
        self.assertEqual(purchase, self.purchase)

    def test_update_purchase_for_PurchaseRepository_is_success(self):
        PurchaseRepository.update_instance(
            self.purchase.id, {'city': 'nova city nome'})
        purchase = PurchaseRepository.get_instance_by_id(self.purchase.id)
        self.assertEqual(purchase.city, 'nova city nome')

    def test_delete_purchase_for_PurchaseRepository_is_success(self):
        PurchaseRepository.delete_instance(self.purchase.id)
        purchases = PurchaseRepository.get_all_instances()
        self.assertEqual(purchases.count(), 0)
