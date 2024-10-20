from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils.translation import gettext as _

from account.models import MyUser

class Book(models.Model):
    name = models.CharField(max_length=16, verbose_name=_('Book Name'))
    bookmark_count = models.IntegerField(default=0)
    summary_of_story = models.TextField(verbose_name=_('summary of story'))

    def __str__(self):
        return self.name


class Rating(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE,
                             related_name='ratings')
    rating = models.IntegerField(validators=[MinValueValidator(1),
                                             MaxValueValidator(5)],
                                 null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'book')

    def __str__(self):
        return f'{self.user} rated {self.book} with {self.rating}'


class Comment(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    text = models.TextField(max_length=500, null=True, blank=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE,
                             related_name='comments')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} commented {self.book} with {self.text}'


class Bookmark(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE,
                             related_name='bookmarks')
    created_at = models.DateTimeField(auto_now_add=True)




