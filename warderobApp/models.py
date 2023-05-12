from django.db import models
from pytils.translit import slugify
from django.contrib.auth.models import User

class Season(models.Model):
    seasonName = models.CharField("Мезгіл атауы", max_length=255)
    slug = models.SlugField(unique=True, editable=False, blank=True)

    def __str__(self):
        return f"{self.seasonName}"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.seasonName)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Мезгіл"
        verbose_name_plural = "Мезгілдер"

class Weather(models.Model):
    weatherName = models.CharField("Ауа-райы", max_length=255)
    slug = models.SlugField(unique=True, editable=False, blank=True)

    def __str__(self):
        return f"{self.weatherName}"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.weatherName)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Ауа-райы"
        verbose_name_plural = "Ауа-райы"

class Age(models.Model):
    age = models.IntegerField("Жас", blank=True, null=True)
    slug = models.SlugField(unique=True, editable=False, blank=True)

    def __str__(self):
        return f"{self.age}"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.age)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Жас"
        verbose_name_plural = "Жас"


class Style(models.Model):
    style = models.CharField("Стиль", max_length=255, blank=True, null=True)
    slug = models.SlugField(unique=True, editable=False, blank=True)

    def __str__(self):
        return f"{self.style}"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.style)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Стиль"
        verbose_name_plural = "Стиль"


class Look(models.Model):
    lookName = models.CharField("Лук атауы", max_length=255, blank=True, null=True)
    season = models.ForeignKey(Season, on_delete=models.CASCADE, verbose_name="Мезгіл", blank=True, null=True)
    weather = models.ForeignKey(Weather, on_delete=models.CASCADE, verbose_name="Ауа-райы", blank=True, null=True)
    style = models.ForeignKey(Style, on_delete=models.CASCADE, verbose_name="Стиль", blank=True, null=True)
    age = models.ForeignKey(Age, on_delete=models.CASCADE, verbose_name="Жас", blank=True, null=True)
    description = models.TextField("Сипаттамасы", blank=True, null=True)
    lookFullPhoto = models.ImageField("Луктың суреті", upload_to="images/looks/", blank=True, null=True)
    head = models.ImageField("Бас киім", upload_to="images/heads/", blank=True, null=True)
    headLink = models.CharField("Сілтеме", max_length=500, blank=True, null=True)
    eyes = models.ImageField("Көз", upload_to="images/eyes/", blank=True, null=True)
    eyesLink = models.CharField("Сілтеме", max_length=500, blank=True, null=True)
    top1 = models.ImageField("Куртка", upload_to="images/top1/", blank=True, null=True)
    top1Link = models.CharField("Сілтеме", max_length=500, blank=True, null=True)
    top2 = models.ImageField("Футболка", upload_to="images/top2/", blank=True, null=True)
    top2Link = models.CharField("Сілтеме", max_length=500, blank=True, null=True)
    hands = models.ImageField("Қол", upload_to="images/hands/", blank=True, null=True)
    handsLink = models.CharField("Сілтеме", max_length=500, blank=True, null=True)
    bottom1 = models.ImageField("Шалбар", upload_to="images/bottom1/", blank=True, null=True)
    bottom1Link = models.CharField("Сілтеме", max_length=500, blank=True, null=True)
    bottom2 = models.ImageField("Шолақ", upload_to="images/bottom2/", blank=True, null=True)
    bottom2Link = models.CharField("Сілтеме", max_length=500, blank=True, null=True)
    shoes = models.ImageField("Аяқ киім", upload_to="images/shoes/", blank=True, null=True)
    shoesLink = models.CharField("Сілтеме", max_length=500, blank=True, null=True)
    isFavorite = models.BooleanField("Таңдаулы", default=False, blank=True, null=True)
    isPopular = models.BooleanField("Таңымал", default=False, blank=True, null=True)

    def __str__(self):
        return f"{self.lookName}"

    class Meta:
        verbose_name = "Лук"
        verbose_name_plural = "Луктар"


class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    look = models.ForeignKey(Look, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} {self.look.lookName}"

    class Meta:
        verbose_name = "Fav"
        verbose_name_plural = "Fav"