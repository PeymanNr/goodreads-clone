from rest_framework import status
from rest_framework.generics import ListAPIView, RetrieveAPIView, \
    RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from account.models import MyUser
from book.api.serializers import BookListsSerializer, BookDetailSerializer, UserCommentRatingSerializer
from book.models import Book, Comment, Rating


class BookListAPIView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookListsSerializer

class BookDetailAPIView(RetrieveAPIView):
    serializer_class = BookDetailSerializer
    queryset = Book.objects.all()
    def get_object(self):
        book_id = self.kwargs.get('book_id')
        queryset = Book.objects.get(id=book_id)
        return queryset

class CommentRatingCreateUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = UserCommentRatingSerializer
    # permission_classes = [IsAuthenticated]

    def get_object(self):
        user = MyUser.objects.get(id=21)
        book_id = self.kwargs.get('book_id')
        book = Book.objects.get(id=book_id)
        comment = Comment.objects.filter(user=user, book=book).last()
        rating = Rating.objects.filter(user=user, book=book).last()

        return {
            'user': user,
            'book': book,
            'comment': comment.text if comment else None,
            'rating': rating.rating if rating else None
        }

    def update(self, request, *args, **kwargs):
        obj = self.get_object()
        serializer = self.get_serializer(obj, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                {'message': 'Comment and/or rating updated successfully!'},
                status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

