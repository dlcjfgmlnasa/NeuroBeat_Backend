# -*- coding:utf-8 -*-
from django.contrib import admin
from user.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'username',
        'gender',
        'birth',
        'attention',
        'diagnosis',
        'int_dt',
        'upt_dt'
    )
