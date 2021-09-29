from django.db import models
from django.contrib.auth.models import AbstractBaseUser, AbstractUser
from django.contrib.auth.models import PermissionsMixin

class User(AbstractUser):
    is_mentor = models.BooleanField(default=False)
    is_mentee = models.BooleanField(default=False)
    first_name = models.CharField(max_length=32, blank=False)
    last_name = models.CharField(max_length=32, blank=False)
    registered = models.BooleanField(default=False)


GENDER_CHOICES =[
    ('OTHER', '......'),
    ('MALE', 'MALE'),
    ('FEMALE', 'FEMALE'),
    ]


class MentorInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='mentorof')

    dp = models.ImageField(default="default.png", null=True, blank=True)
    dob = models.CharField(max_length=15)
    gender = models.CharField(max_length=7, choices=GENDER_CHOICES, default='NONE')
    mobile = models.CharField(max_length=12)
    Qualifications = models.CharField(max_length=100)
    profession = models.CharField(max_length=50, null=True)
    followers = models.ManyToManyField(User, blank=True, related_name='mentor_followers')
    following = models.ManyToManyField(User, blank=True, related_name='mentor_following')

    def __str__(self):
        return self.user.username


class MenteeInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='menteeof')

    dp = models.ImageField(default='default.png', null=True, blank=True)
    dob = models.CharField(max_length=15)
    gender = models.CharField(max_length=7, choices=GENDER_CHOICES, default='NONE')
    mobile = models.CharField(max_length=12)
    institute = models.CharField(max_length=100)
    followers = models.ManyToManyField(User, blank=True, related_name='mentee_followers')
    following = models.ManyToManyField(User, blank=True, related_name='mentee_following')

    def __str__(self):
        return self.user.username


class Post(models.Model):
    creator = models.ForeignKey(MenteeInfo, on_delete=models.CASCADE, related_name='created_by')
    post_caption = models.CharField(max_length=100, blank=True)
    post_text = models.CharField(max_length=300, blank=True)
    post_image = models.ImageField(blank=True)
    post_video = models.FileField(blank=True)
    likes = models.ManyToManyField(MenteeInfo, related_name='liked_by', blank=True)
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.creator.user.username + ' ' + str(self.id)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_related')
    body = models.CharField(max_length=300, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    commentor = models.ForeignKey(MenteeInfo, related_name='commented_by', on_delete=models.PROTECT)

    def __str__(self):
        return self.post.creator.user.username + ' ' + str(self.post.creator.user.id)