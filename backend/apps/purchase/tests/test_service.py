from datetime import datetime
from django.test import TestCase
from apps.users.service import UserService
from django.contrib.auth import get_user_model

User = get_user_model()


class UserServiceTestCase(TestCase):

    def setUp(self):
        self.user_data = {
            'name': "teste user nome",
            'email': "testeuser@email.com",
            'password': "teste user password",
            'cpf': "80795052090",
            'date_of_birth': datetime(1990, 1, 1),
            'phone_number': "teste user phone_number",
            'street': "teste user street",
            'city': "teste user city",
            'state': "teste user state",
            'number': "teste user number",
            'neighborhood': "teste user neighborhood",
            'complement': "teste user complement",
            'reference_point': "teste user reference_point",
            'zip_code': "teste user zip_code"
        }
        self.user = User.objects.create_user(**self.user_data)

    def test_create_user_for_UserService_is_success(self):
        data = self.user_data
        data['cpf'] = '34051546004'
        data['email'] = "teste1user@email.com"
        user = UserService.create_instance(data)
        self.assertIsInstance(user, User)

    def test_verify_is_data_is_correct_in_user_for_UserService(self):
        data = self.user_data
        data['cpf'] = '34051546004'
        data['email'] = "teste1user@email.com"
        user = UserService.create_instance(data)
        self.assertEqual(user.name, data['name'])
        self.assertEqual(user.email, data['email'])
        self.assertEqual(user.cpf, data['cpf'])
        self.assertEqual(user.date_of_birth, data['date_of_birth'])
        self.assertEqual(user.phone_number, data['phone_number'])
        self.assertEqual(user.street, data['street'])
        self.assertEqual(user.city, data['city'])
        self.assertEqual(user.state, data['state'])
        self.assertEqual(user.number, data['number'])
        self.assertEqual(user.neighborhood, data['neighborhood'])
        self.assertEqual(user.complement, data['complement'])
        self.assertEqual(user.reference_point, data['reference_point'])
        self.assertEqual(user.zip_code, data['zip_code'])

    def test_list_all_users_for_UserService_is_success(self):
        users = UserService.list_all_instances()
        self.assertEqual(users.count(), 1)

    def test_get_user_by_id_for_UserService_is_success(self):
        user = UserService.retrieve_instance(self.user.id)
        self.assertEqual(user, self.user)

    def test_update_user_for_UserService_is_success(self):
        UserService.update_instance_and_partial_update(
            self.user.id, {'name': 'novo nome'})
        user = UserService.retrieve_instance(self.user.id)
        self.assertEqual(user.name, 'novo nome')

    def test_delete_user_for_UserService_is_success(self):
        UserService.destroy_instance(self.user.id)
        users = UserService.list_all_instances()
        self.assertEqual(users.count(), 0)
