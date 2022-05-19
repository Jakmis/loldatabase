from distutils.command.upload import upload
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

# Create your models here.
def champion_path(instance, filename):
    return "champion/" + str(instance.championName) + "/skin/" + filename

def region_icon(instance, filename):
    return "region/" + str(instance.name) + "/icon/" + filename

class Region(models.Model):
    name = models.CharField(max_length=50, verbose_name="Region name")

    icon = models.ImageField(upload_to=region_icon, blank=True, null=True, verbose_name="Icon")

    bio = models.TextField(verbose_name="Region biography", null=True, blank=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class Champion(models.Model):
    name = models.CharField(max_length=50, verbose_name="Champion name")

    title = models.CharField(max_length=50, verbose_name="Title")

    bio = models.TextField(verbose_name="Champion biography")

    quote = models.CharField(max_length=50, verbose_name="Quote")

    basicSkin = models.FileField(upload_to=champion_path, blank=True, null=True, verbose_name="Basic skin")

    releaseDate = models.DateField(help_text="Please use the following format: <em>YYYY-MM-DD</em>.", verbose_name="Champion release date")

    priceBe = models.IntegerField(help_text="Enter price of champion in Blue Essence", validators=[MaxValueValidator(6300),MinValueValidator(450)], verbose_name="Price in Blue Essence")

    regionName = models.ForeignKey(Region, on_delete=models.CASCADE, verbose_name="Region")

    ROLE = (
        ("assassin", "Assassin"),
        ("fighter", "Fighter"),
        ("mage", "Mage"),
        ("marksman", "Marksman"),
        ("support", "Support"),
        ("tank",  "Tank"),
    )

    role = models.CharField(max_length=50, choices=ROLE, help_text="Select role of a champion")

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Skin(models.Model):
    name = models.CharField(max_length=50, verbose_name="Skin name")

    releaseDate = models.DateField(help_text="Please use the following format: <em>YYYY-MM-DD</em>.", verbose_name="Skin release date")

    skin = models.ImageField(upload_to=champion_path, blank=True, null=True, verbose_name="Skin")

    priceRp = models.IntegerField(help_text="Enter price of skin in Riot Points", validators=[MaxValueValidator(3250),MinValueValidator(390)])

    championName = models.ForeignKey(Champion, on_delete=models.CASCADE, verbose_name="Champion name")

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class Ability(models.Model):
    name = models.CharField(max_length=50, verbose_name="Ability name")

    KEY = (
        ("passive", "Passive"),
        ("q", "Q"),
        ("w", "W"),
        ("e", "E"),
        ("r", "R"),
    )

    key = models.CharField(max_length=7, choices=KEY, verbose_name="Select keyboard key of an ability")

    description = models.TextField(verbose_name="Description of an ability")

    championName = models.ForeignKey(Champion, on_delete=models.CASCADE, verbose_name="Champion name")

    class Meta:
        ordering = ['name']
        verbose_name_plural = "abilities"

    def __str__(self):
        return f"{self.name}, Key: {str.upper(self.key)}, Champion: {str(self.championName)}"