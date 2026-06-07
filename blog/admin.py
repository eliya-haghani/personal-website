from django.contrib import admin
from blog.models import post, Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(post)
class PostAdmin(admin.ModelAdmin):
    # به جای خود category، از تابعی که در پایین تعریف کردیم (get_categories) استفاده می‌کنیم
    list_display = ('title', 'status', 'publishd_date', 'author', 'img', 'get_categories')
    
    # استفاده از فیلدست برای دسته‌بندی بهتر
    fieldsets = (
        ('اطلاعات اصلی', {
            # فیلد category را اینجا اضافه کردیم تا در فرم ویرایش نمایش داده شود
            'fields': ('title', 'content', 'status', 'publishd_date', 'author', 'img', 'category')
        }),
        ('تنظیمات سئو (SEO)', {
            'fields': ('meta_title', 'meta_description'),
            'classes': ('collapse',), 
        }),
    )

    # این تابع را برای نمایش نام دسته‌بندی‌ها در لیست اصلی ادمین اضافه کردیم
    def get_categories(self, obj):
        return ", ".join([cat.name for cat in obj.category.all()])
    
    # تغییر نام سرستون در پنل ادمین
    get_categories.short_description = 'دسته بندی‌ها'
