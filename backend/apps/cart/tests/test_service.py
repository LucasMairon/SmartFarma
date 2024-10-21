from django.test import TestCase
from apps.cart.service import CartService
from apps.cart.models import Cart
from apps.users.service import UserService
from apps.shared.apps_tests_datas import tests_datas


class CartServiceTestCase(TestCase):

    def setUp(self):
        self.user = UserService.create_instance(tests_datas.get_user_data())
        self.cart = Cart.objects.create(
            **tests_datas.get_cart_data(user_id=self.user.id))

    def test_create_cart_for_CartService_is_success(self):
        cart = CartService.create_instance(
            tests_datas.get_cart_data(user_id=self.user.id))
        self.assertIsInstance(cart, Cart)

    def test_verify_is_data_is_correct_in_cart_for_CartService(self):
        cart = CartService.create_instance(
            tests_datas.get_cart_data(user_id=self.user.id))
        self.assertEqual(cart.user.id, self.user.id)
        self.assertEqual(cart.is_active, True)

    def test_list_all_carts_for_CartService_is_success(self):
        carts = CartService.list_all_instances()
        self.assertEqual(carts.count(), 1)

    def test_get_cart_by_id_for_CartService_is_success(self):
        cart = CartService.retrieve_instance(self.cart.id)
        self.assertEqual(cart, self.cart)

    def test_update_cart_for_CartService_is_success(self):
        CartService.update_instance_and_partial_update(
            self.cart.id, {'is_active': False})
        cart = CartService.retrieve_instance(self.cart.id)
        self.assertEqual(cart.is_active, False)

    def test_delete_cart_for_CartService_is_success(self):
        CartService.destroy_instance(self.cart.id)
        carts = CartService.list_all_instances()
        self.assertEqual(carts.count(), 0)
