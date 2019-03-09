from django.contrib import admin
from users.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):

    list_display = ('pk', 'picture', 'user', 'phone_number', 'website')
    list_display_links = ('pk', 'user', 'phone_number')
    search_fields = (
        'user__email',
        'user__user_name',
        'user__first_name',
        'user__last_name',
        'phone_number')

    list_filter = (
        'user__is_active',
        'user__is_staff',
        'created',
        'modified')
