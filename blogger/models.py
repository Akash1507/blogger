from django.db import models
from django.conf import settings
from django.db.models import Q
from django.utils import timezone

User = settings.AUTH_USER_MODEL


class PostQuerySet(models.QuerySet):
    def published(self):
        now = timezone.now()
        return self.filter(postPublishDate=now)

    def search(self, query):
        lookup = (
                    Q(title__icontains=query) |
                    Q(content__icontains=query) |
                    Q(slug__icontains=query) |
                    Q(user__first_name__icontains=query) |
                    Q(user__last_name__icontains=query) |
                    Q(user__username__icontains=query)
                    )

        return self.filter(lookup)


class PostManager(models.Manager):
    def get_queryset(self):
        return PostQuerySet(self.model, using=self._db)

    def published(self):
        return self.get_queryset().published()

    def search(self, query=None):
        if query is None:
            return self.get_queryset().none()
        return self.get_queryset().published().search(query)


class Post(models.Model):
    postUser        = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL)
    postTitle       = models.CharField(max_length=120)
    postUrl         = models.SlugField(unique=True)
    postContent     = models.TextField(null=True, blank=True)
    postImage       = models.ImageField(upload_to='image/', blank=True, null=True)
    postPublishDate = models.DateTimeField(auto_now=False, auto_now_add=False, null=True, blank=True)
    postTimeStamp   = models.DateTimeField(auto_now_add=True)
    PostUpdated     = models.DateTimeField(auto_now=True)

    objects = PostManager()

    class Meta:
        ordering = ['-postTimeStamp', '-postPublishDate', '-PostUpdated']

    def get_absolute_url(self):
        return f"/post/{self.postUrl}"

    def get_edit_url(self):
        return f"{self.get_absolute_url()}/edit"

    def get_delete_url(self):
        return f"{self.get_absolute_url()}/delete"

    def __str__(self):
        return self.postTitle