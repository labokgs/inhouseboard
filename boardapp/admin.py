from django.contrib import admin

from boardapp.models import BoardModel
from .models import BoardModel
# Register your models here.

admin.site.register(BoardModel)
