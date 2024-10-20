from django.db.models import Count, Avg
from rest_framework import serializers
from book.models import Book, Comment, Rating


class CommentListSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.email')
    class Meta:
        model = Comment
        fields = ('text', 'user', 'created_at')


class UserCommentRatingSerializer(serializers.Serializer):
    rating = serializers.IntegerField(allow_null=True, required=False)
    text = serializers.CharField(allow_null=True, required=False)

    def to_representation(self, instance):
        return {
            'rating': instance.get('rating', None),
            'text': instance.get('comment', None)
        }

    def update(self, instance, validated_data):

        comment_text = validated_data.get('text', None)
        if comment_text is not None:
            comment, created = Comment.objects.get_or_create(
                user=instance['user'],
                book=instance['book'],
                defaults={'text': comment_text}
            )
            if not created:
                comment.text = comment_text
                comment.save()

        rating_value = validated_data.get('rating', None)
        if rating_value is not None:
            rating, created = Rating.objects.get_or_create(
                user=instance['user'],
                book=instance['book'],
                defaults={'rating': rating_value}
            )
            if not created:
                rating.rating = rating_value
                rating.save()

        return instance


class UserCommentRateDetailSerializer(serializers.ModelSerializer):
    comments = serializers.SerializerMethodField()
    class Meta:
        model = Rating
        fields = ('user', 'created_at', 'rating', 'comments')

    def get_comments(self, obj):
        instance = Rating.objects.filter(book=obj.book)
        return CommentListSerializer(instance, many=True).data

class BookDetailSerializer(serializers.ModelSerializer):
    user_comments_ratings = serializers.SerializerMethodField()
    rating_count = serializers.SerializerMethodField()
    comment_count = serializers.SerializerMethodField()
    rating_distribution = serializers.SerializerMethodField()
    average_rating = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = ('name', 'summary_of_story','user_comments_ratings',
                  'rating_count', 'comment_count', 'rating_distribution',
                  'average_rating')

    def get_user_comments_ratings(self, obj):
        user_comments_ratings = []
        for comment in obj.comments.all():
            rating = Rating.objects.filter(user=comment.user, book=obj).first()
            user_comments_ratings.append({
                'user': comment.user.email,
                'text': comment.text,
                'rating': rating.rating if rating else None
            })
        return user_comments_ratings

    def get_rating_count(self, obj):
        return Rating.objects.filter(book=obj).count()

    def get_comment_count(self, obj):
        return Comment.objects.filter(book=obj).count()

    def get_rating_distribution(self, obj):
        rating_distribution = Rating.objects.filter(book=obj).values(
            'rating').annotate(count=Count('user')).order_by('rating')
        distribution_dict = {i: 0 for i in range(1,6)}

        for entry in rating_distribution:
            distribution_dict[entry['rating']] = entry['count']

        return distribution_dict

    def get_average_rating(self, obj):
        average_rating = Rating.objects.filter(book=obj).aggregate(Avg('rating'))
        return average_rating


class BookListsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'name', 'bookmark_count')

