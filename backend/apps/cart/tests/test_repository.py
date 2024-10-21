from django.test import TestCase
from apps.cart.repository import CartRepository
from apps.cart.models import Cart
from django.contrib.auth import get_user_model
from apps.shared.apps_tests_datas import tests_datas
from apps.users.service import UserService


User = get_user_model()


class CartRepositoryTestCase(TestCase):

    def setUp(self):
        self.user = UserService.create_instance(tests_datas.get_user_data())
        self.cart = Cart.objects.create(
            **tests_datas.get_cart_data(user_id=self.user.id))

    def test_create_cart_for_CartRepository_is_success(self):
        cart = CartRepository.create_instance(
            tests_datas.get_cart_data(user_id=self.user.id))
        self.assertIsInstance(cart, Cart)

    def test_verify_is_data_is_correct_in_cart_for_CartRepository(self):
        data = tests_datas.get_cart_data(user_id=self.user.id)
        cart = CartRepository.create_instance(data)
        self.assertEqual(cart.user.id, data['user_id'])
        self.assertEqual(cart.is_active, data['is_active'])

    def test_list_all_carts_for_CartRepository_is_success(self):
        carts = CartRepository.get_all_instances()
        self.assertEqual(carts.count(), 1)

    def test_get_cart_by_id_for_CartRepository_is_success(self):
        cart = CartRepository.get_instance_by_id(self.cart.id)
        self.assertEqual(cart, self.cart)

    def test_update_cart_for_CartRepository_is_success(self):
        CartRepository.update_instance(
            self.cart.id, {'is_active': False})
        cart = CartRepository.get_instance_by_id(self.cart.id)
        self.assertEqual(cart.is_active, False)

    def test_delete_cart_for_CartRepository_is_success(self):
        CartRepository.delete_instance(self.cart.id)
        carts = CartRepository.get_all_instances()
        self.assertEqual(carts.count(), 0)
