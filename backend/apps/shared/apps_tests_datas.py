from datetime import datetime


class Tests_datas:

    def get_user_data(self,
                      name="teste user nome",
                      email="testeuser@email.com",
                      password="teste user password",
                      cpf="80795052090",
                      date_of_birth=datetime(1990, 1, 1),
                      phone_number="teste user phone_number",
                      street="teste user street",
                      city="teste user city",
                      state="teste user state",
                      number="teste user number",
                      neighborhood="teste user neighborhood",
                      complement="teste user complement",
                      reference_point="teste user reference_point",
                      zip_code="teste user zip_code"
                      ):
        return {
            'name': name,
            'email': email,
            'password': password,
            'cpf': cpf,
            'date_of_birth': date_of_birth,
            'phone_number': phone_number,
            'street': street,
            'city': city,
            'state': state,
            'number': number,
            'neighborhood': neighborhood,
            'complement': complement,
            'reference_point': reference_point,
            'zip_code': zip_code
        }

    def get_product_data(self, name="teste product nome",
                         price=1.1,
                         available_quantity=10,
                         description="teste product description",
                         brand="teste marca",
                         maker="teste fabricante",
                         weight=10.22,
                         ean="teste codigo de barras",
                         sku="teste sku",
                         ):
        return {
            'name': name,
            'price': price,
            'available_quantity': available_quantity,
            'description': description,
            'brand': brand,
            'maker': maker,
            'weight': weight,
            'ean': ean,
            'sku': sku,
        }

    def get_cart_data(self, user_id=None, is_active=True):

        return {
            'user_id': user_id,
            'is_active': is_active
        }

    def get_order_data(self, quantity=1, product_id=None, cart_id=None):
        return {
            'quantity': quantity,
            'product_id': product_id,
            'cart_id': cart_id,
        }

    def get_purchase_data(self):
        return ...


tests_datas = Tests_datas()
