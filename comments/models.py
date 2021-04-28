from django.db import models
from products.models import Product
from accounts.models import UserAccount


class Comment(models.Model):
    """User to be able to comment on each product"""

    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    comment = models.TextField()
    comment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{} commented on {} - {}'.format(
            self.user, self.comment, self.comment_date)
