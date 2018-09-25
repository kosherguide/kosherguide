from django.contrib import admin
from .models import Post, Category, Slider, Synagogue, Kitchen, Photo, Phone, Email, Country, City, Restaurant, \
    PhotoSynagogue, PhoneSynagogue, EmailSynagogue

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Kitchen)
admin.site.register(Slider)


class CityInline(admin.StackedInline):
    model = City
    extra = 1
    verbose_name = "Город"
    verbose_name_plural = "Города"


class CountryAdmin(admin.ModelAdmin):
    inlines = [CityInline]

    def save_model(self, request, obj, form, change):
        obj.save()


admin.site.register(Country, CountryAdmin)


class PhotoInline(admin.StackedInline):
    model = Photo
    extra = 1
    verbose_name = "Изображение"
    verbose_name_plural = "Изображения"


class PhoneInline(admin.StackedInline):
    model = Phone
    extra = 1
    verbose_name = "Телефон"
    verbose_name_plural = "Номера телефонов"


class EmailInline(admin.StackedInline):
    model = Email
    extra = 1
    verbose_name = "Почта"
    verbose_name_plural = "Электронные почты"


class RestaurantAdmin(admin.ModelAdmin):
    inlines = [PhotoInline, PhoneInline, EmailInline]

    def save_model(self, request, obj, form, change):
        obj.save()


admin.site.register(Restaurant, RestaurantAdmin)


class PhotoSynagogueInline(admin.StackedInline):
    model = PhotoSynagogue
    extra = 1
    verbose_name = "Изображение"
    verbose_name_plural = "Изображения"


class PhoneSynagogueInline(admin.StackedInline):
    model = PhoneSynagogue
    extra = 1
    verbose_name = "Телефон"
    verbose_name_plural = "Номера телефонов"


class EmailSynagogueInline(admin.StackedInline):
    model = EmailSynagogue
    extra = 1
    verbose_name = "Почта"
    verbose_name_plural = "Электронные почты"


class SynagogueAdmin(admin.ModelAdmin):
    inlines = [PhotoSynagogueInline, PhoneSynagogueInline, EmailSynagogueInline]

    def save_model(self, request, obj, form, change):
        obj.save()


admin.site.register(Synagogue, SynagogueAdmin)
