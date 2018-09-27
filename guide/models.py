from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name="Автор")
    title = models.CharField(verbose_name="Заголовок", max_length=200)
    pic = models.ImageField(verbose_name="Изображение", upload_to='images/', default='images/None/no-img.jpg')
    preview_text = models.CharField(verbose_name="Превью текст", max_length=200, blank=True, null=True)
    text = models.TextField(verbose_name="Детальный текст")
    created_date = models.DateTimeField(verbose_name="Дата создания", default=timezone.now)
    published_date = models.DateTimeField(verbose_name="Дата публикации", blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Slider(models.Model):
    title = models.CharField(verbose_name="Заголовок", max_length=200)
    pic = models.ImageField(verbose_name="Изображение", upload_to='images/', default='images/None/no-img.jpg')
    preview_text = models.CharField(verbose_name="Превью текст", max_length=200, blank=True, null=True)
    handle = models.SlugField(verbose_name="Символьный код", unique=True, max_length=200)
    sort = models.IntegerField(verbose_name="Сортировка", blank=True, null=True)
    link = models.CharField(verbose_name="Ссылка", max_length=500, blank=True, null=True)
    name_button = models.CharField(verbose_name="Название кнопки", max_length=200, blank=True, null=True)
    created_date = models.DateTimeField(verbose_name="Дата создания", default=timezone.now)
    published_date = models.DateTimeField(verbose_name="Дата публикации", blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(verbose_name="Заголовок", max_length=200)
    pic = models.ImageField(verbose_name="Изображение", upload_to='images/', default='images/None/no-img.jpg')
    preview_text = models.CharField(verbose_name="Превью текст", max_length=200, blank=True, null=True)
    text = models.TextField(verbose_name="Детальный текст", blank=True, null=True)
    handle = models.SlugField(verbose_name="Символьный код", unique=True, max_length=200)
    created_date = models.DateTimeField(verbose_name="Дата создания", default=timezone.now)
    published_date = models.DateTimeField(verbose_name="Дата публикации", blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Kitchen(models.Model):
    title = models.CharField(verbose_name="Кухня", max_length=200)
    handle = models.CharField(verbose_name="Символьный код", max_length=200)

    def __str__(self):
        return self.title


class Country(models.Model):
    title = models.CharField(verbose_name="Страна", max_length=200)
    handle = models.CharField(verbose_name="Символьный код", max_length=200)

    def __str__(self):
        return self.title


class City(models.Model):
    country = models.ForeignKey('guide.Country', on_delete=models.CASCADE)
    title = models.CharField(verbose_name="Город", max_length=200)
    handle = models.SlugField(verbose_name="Символьный код", unique=True, max_length=200)

    def __str__(self):
        return self.title


class Synagogue(models.Model):
    title = models.CharField(verbose_name="Заголовок", max_length=200)
    pic = models.ImageField(verbose_name="Изображение", upload_to='images/', default='images/None/no-img.jpg', blank=True, null=True)
    preview_text = models.CharField(verbose_name="Превью текст", max_length=200, blank=True, null=True)
    text = models.TextField(verbose_name="Детальный текст", blank=True, null=True)
    handle = models.SlugField(verbose_name="Символьный код", unique=True, max_length=200)
    country = models.ForeignKey('guide.Country', on_delete=models.CASCADE, verbose_name="Страна")
    city = models.ForeignKey('guide.City', on_delete=models.CASCADE, verbose_name="Город")
    address = models.CharField(verbose_name="Адрес", max_length=200, blank=True, null=True)
    subway = models.CharField(verbose_name="Метро", max_length=200, blank=True, null=True)
    created_date = models.DateTimeField(verbose_name="Дата создания", default=timezone.now)
    published_date = models.DateTimeField(verbose_name="Дата публикации", blank=True, null=True)
    working_hours = models.CharField(verbose_name="График работы", max_length=200, blank=True, null=True)
    lat = models.CharField(verbose_name="Широта", max_length=200, blank=True, null=True)
    lng = models.CharField(verbose_name="Долгота", max_length=200, blank=True, null=True)
    site = models.CharField(verbose_name="Официальный сайт", max_length=700, blank=True, null=True)
    parking_space = models.BooleanField(verbose_name="Парковка", default=False)
    wifi = models.BooleanField(verbose_name="Wi-Fi", default=False)
    is_restaurant = models.BooleanField(verbose_name="Есть ресторан?", default=False)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class PhotoSynagogue(models.Model):
    synagogue = models.ForeignKey('guide.Synagogue', on_delete=models.CASCADE)
    image = models.ImageField(verbose_name="Изображение", upload_to='images/', default='images/None/no-img.jpg', blank=True, null=True)


class PhoneSynagogue(models.Model):
    synagogue = models.ForeignKey('guide.Synagogue', on_delete=models.CASCADE)
    title = models.CharField(verbose_name="Номер телефона", max_length=200, blank=True, null=True)


class EmailSynagogue(models.Model):
    synagogue = models.ForeignKey('guide.Synagogue', on_delete=models.CASCADE)
    title = models.CharField(verbose_name="Почта", max_length=200, blank=True, null=True)


class Restaurant(models.Model):
    title = models.CharField(verbose_name="Заголовок", max_length=200)
    pic = models.ImageField(verbose_name="Изображение", upload_to='images/', default='images/None/no-img.jpg', blank=True, null=True)
    preview_text = models.CharField(verbose_name="Превью текст", max_length=200, blank=True, null=True)
    text = models.TextField(verbose_name="Детальный текст", blank=True, null=True)
    handle = models.SlugField(verbose_name="Символьный код", unique=True, max_length=200)
    country = models.ForeignKey('guide.Country', on_delete=models.CASCADE, verbose_name="Страна")
    city = models.ForeignKey('guide.City', on_delete=models.CASCADE, verbose_name="Город")
    address = models.CharField(verbose_name="Адрес", max_length=200, blank=True, null=True)
    subway = models.CharField(verbose_name="Метро", max_length=200, blank=True, null=True)
    created_date = models.DateTimeField(verbose_name="Дата создания", default=timezone.now)
    published_date = models.DateTimeField(verbose_name="Дата публикации", blank=True, null=True)
    working_hours = models.CharField(verbose_name="График работы", max_length=200, blank=True, null=True)
    kitchens = models.ManyToManyField(Kitchen, verbose_name="Кухни")
    average_account_min = models.CharField(verbose_name="Средний счет (минимальный)", max_length=200, blank=True, null=True)
    average_account_max = models.CharField(verbose_name="Средний счет (максимальный)", max_length=200, blank=True, null=True)
    lat = models.CharField(verbose_name="Широта", max_length=200, blank=True, null=True)
    lng = models.CharField(verbose_name="Долгота", max_length=200, blank=True, null=True)
    site = models.CharField(verbose_name="Официальный сайт", max_length=700, blank=True, null=True)
    bank_cards = models.BooleanField(verbose_name="Банковские карты", default=False)
    parking_space = models.BooleanField(verbose_name="Парковка", default=False)
    wifi = models.BooleanField(verbose_name="Wi-Fi", default=False)
    banquets = models.BooleanField(verbose_name="Банкеты", default=False)
    delivery = models.BooleanField(verbose_name="Доставка", default=False)
    business_lunch = models.BooleanField(verbose_name="Бизнес-ланч", default=False)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Photo(models.Model):
    restaurant = models.ForeignKey('guide.Restaurant', on_delete=models.CASCADE)
    image = models.ImageField(verbose_name="Изображение", upload_to='images/', default='images/None/no-img.jpg', blank=True, null=True)


class Phone(models.Model):
    restaurant = models.ForeignKey('guide.Restaurant', on_delete=models.CASCADE)
    title = models.CharField(verbose_name="Номер телефона", max_length=200, blank=True, null=True)


class Email(models.Model):
    restaurant = models.ForeignKey('guide.Restaurant', on_delete=models.CASCADE)
    title = models.CharField(verbose_name="Почта", max_length=200, blank=True, null=True)
