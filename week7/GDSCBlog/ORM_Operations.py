import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "GDSCBlog.settings")
django.setup()

from BlogApp.models import Postt
from CommentApp.models import Comment

post1 = Postt.objects.create(
    Title='Seize',
    Content='We will explore all about our day today struggle to survive in this nothing but cruel world.',
    Category='solution'
)

post2 = Postt.objects.create(
    Title="Capture",
    Content="well in my next post we will talk about what causes this kinda misery",
    Category="Cause"
)

post3 = Postt.objects.create(
    Title="Shake",
    Content="now we is the time to discuss for the solution",
    Category="solution"
)

# displaying value
category = "solution"
post_by_category = Postt.objects.filter(Category=category)
print(f"Posts in category {category} are:")
for post in post_by_category:
    print(post.Title)

# updating content
post_to_update = Postt.objects.get(Title="Shake")
post_to_update.Content = "The solution has arrived even though we are not aware."
post_to_update.save()

# deleting post
# post_to_delete = Postt.objects.get(Title="Cause ")
# post_to_delete.delete()



comment1 = Comment.objects.create(
    Content=" i am lostttt",
    Author="Zion",
    PublishedDate="2024-02-26",
    Post=post1
)

comment2 = Comment.objects.create(
    Content="thats right either we stop stressing or we die soonnnnn",
    Author="Tsiyon",
    PublishedDate="2024-02-26",
    Post=post2
)
 
comment3=Comment.objects.create(
    Content=" i don't really care about anything tbh😂😂",
    Author="Abel",
    PublishedDate="2024-2-28",
    Post=post1
    )


# displaying comment in specific post
comments_by_post = Comment.objects.filter(Post=post1)
print(f"Comments in post {post1.Title}: ")
for comment in comments_by_post:
    print(comment.Content)

comment_to_update = Comment.objects.get(id=1)  #
comment_to_update.Content = "Updated content"
comment_to_update.save()


# # deleting comment
# to_be_deleted=Comment.objects.get(Content="who cares lets just live our life")
# to_be_deleted.delete()
# # or
# comment1.delete()

post_to_delete = Postt.objects.get(Title="Seize ")
associated_comments = Comment.objects.filter(Post=post_to_delete)

for comment in associated_comments:
    comment.delete()

post_to_delete.delete()
