# from .models import post

# def sidebar_latest_posts(request):
#     latest_posts = post.objects.filter(status=True).order_by("-publishd_date")[:4]
#     return {
#         "latest_posts": latest_posts,
#         "debug_sidebar_test": "HELLO_FROM_CONTEXT"
#     }