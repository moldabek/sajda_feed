from django.contrib import admin
from .models import Card


class CardAdmin(admin.ModelAdmin):
    # Define fields to be shown in the admin interface for each card type
    fieldsets = [
        ('General', {'fields': (
        'card_type', 'title', 'content', 'additional_info', 'content_url', 'description', 'date', 'repeat', 'repeat_days',
        'active')}),
        ('Quran Ayah', {'fields': ('arabic_text',), 'classes': ('quran-ayah',)}),
        ('Hadith', {'fields': ('name_of_narrator', ), 'classes': ('hadith',)}),
        ('Inspiring Picture', {'fields': (), 'classes': ('inspiring-picture',)}),
        ('Dhikr', {'fields': ()}),
        ('Youtube', {'fields': ('play_in_app', )}),
    ]

    def get_form(self, request, obj=None, **kwargs):
        # Customize form based on the selected type
        form = super().get_form(request, obj, **kwargs)
        if obj and obj.type:
            type_specific_fields = self.fieldsets[self.fieldsets_map[obj.type]]['fields']
            form.base_fields = {k: form.base_fields[k] for k in type_specific_fields}
        return form

    fieldsets_map = {
        'Quran Ayah': 1,
        'Hadith': 2,
        'Inspiring Picture': 3,
        'Dhikr': 4,
        'Youtube': 5,
    }


admin.site.register(Card, CardAdmin)
