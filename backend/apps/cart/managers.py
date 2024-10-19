from django.db.models import Manager


class ManagerCart(Manager):

    def get_or_create(self, user):
        queryset_carrinho = self.get_queryset().filter(user=user, is_active=True)
        if queryset_carrinho.exists():
            return queryset_carrinho.first()
        return Carrinho.objects.create(user=user)
