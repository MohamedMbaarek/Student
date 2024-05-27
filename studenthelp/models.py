from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

class Post(models.Model):
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)
    OFFER = 'OFF'
    DEMAND = 'DEM'
    TYPE_CHOICES = [
        (OFFER, 'Offre'),
        (DEMAND, 'Demande'),
    ]
    type = models.CharField(max_length=3, choices=TYPE_CHOICES)
    date = models.DateField()
    titre = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    auteur = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts_blog', null=True)
    date_modification = models.DateTimeField(auto_now=True)
    contenu = models.TextField()
    DRAFT = 'DRA'
    PUBLISHED = 'PUB'
    STATUT_CHOICES = [
        (DRAFT, "Brouillon"),
        (PUBLISHED, "Publié")
    ]
    statut = models.CharField(max_length=3, choices=STATUT_CHOICES, default=DRAFT)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.titre

    def save(self, *args, **kwargs):
        self.slug = slugify(self.titre)
        super(Post, self).save(*args, **kwargs)

class Transport(models.Model):
    depart = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)
    heure_dep = models.TimeField()
    nbre_sieges = models.IntegerField()
    contactinfo = models.CharField(max_length=255)
    club = models.CharField(max_length=255)
    prix = models.FloatField()

    def __str__(self):
        return f"{self.depart} - {self.destination}"

class HousingPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
