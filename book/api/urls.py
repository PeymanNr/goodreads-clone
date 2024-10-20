from django.urls import path
from book.api.views import BookListAPIView, BookDetailAPIView, \
    CommentRatingCreateUpdateAPIView

urlpatterns = [
    path('list/', BookListAPIView.as_view(), name='book-list'),
    path('detail/<int:book_id>/', BookDetailAPIView.as_view(),
         name='book_detail'),
    path('<int:book_id>/comment-rating/',
         CommentRatingCreateUpdateAPIView.as_view(), name='comment-rating')
]