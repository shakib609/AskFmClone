from django.db.models import Count


def get_total_likes(user):
    total_likes = user.asked_to_questions.aggregate(
        likes=Count('like')).get('likes')
    return total_likes
