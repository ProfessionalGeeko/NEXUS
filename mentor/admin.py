from django.contrib import admin
from mentor.models import *

# Register your models here.
admin.site.register(MentorInfo)
admin.site.register(MenteeInfo)
admin.site.register(User)
admin.site.register(Post)
admin.site.register(Comment)