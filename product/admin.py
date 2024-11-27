from django.contrib import admin
from .models import Genre,Book

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('designation',)}
    list_display=('designation','slug')


class BookAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('title',)}
    list_display=('title','ISBN','author','price','is_available','on_sale','discount')
    def get_readonly_fields(self, request, obj=None):
        if obj and obj.on_sale:
            return self.readonly_fields  # 'discount' is editable if 'on_sale' is True
        else:
            return ('discount',)  # 'discount' is readonly if 'on_sale' is False


admin.site.register(Genre,CategoryAdmin)
admin.site.register(Book,BookAdmin)
# Register your models here.
