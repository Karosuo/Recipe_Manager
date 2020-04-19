from django.db import models


# Create your models here.
class RecipeSteps(models.Model):
    StepName = models.CharField(max_length=150)
    StepDescription = models.CharField(max_length=250)

    class Meta:
        db_table = "RecipeSteps"


class Tag(models.Model):
    Name = models.CharField(max_length=150, unique=True)

    class Meta:
      db_table = "Tag"


class MeasureUnit(models.Model):
    UnitName = models.CharField(max_length=100, unique=True)

    class Meta:
        db_table = "MeasureUnit"


class Recipe(models.Model):
    Name = models.CharField(max_length=100, unique=True)
    DayPosition = models.IntegerField(default=0) #By default put them on the dawn position, 1 is like breakfast, 2 second meal and so on
    FK_Tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    FK_Steps = models.ForeignKey(RecipeSteps, on_delete=models.CASCADE)

    class Meta:
        db_table = "Recipe"


class Ingredient(models.Model):
    Name = models.CharField(max_length=150, unique=True)
    FK_MUnit = models.ForeignKey(MeasureUnit, on_delete=models.CASCADE)

    class Meta:
        db_table = "Ingredient"


class Recipe_has_Ingredients(models.Model):
    FK_Recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    FK_Ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    MUnitQty = models.FloatField()
    PCS = models.FloatField(default=0) #Some of the items can't be measured in pcs, so zero is ok, this is just a support field

    class Meta:
        db_table = "Recipe_has_Ingredients"


class Profile(models.Model):
    ProfileName = models.CharField(max_length=100, unique=True)
    ProfileOwner = models.CharField(max_length=150, default="")

    class Meta:
        db_table = "Profile"


class Profile_has_Recipe(models.Model):
    MONDAY = "monday"
    TUESDAY = "tuesday"
    WEDNESDAY = "wednesday"
    THURSDAY = "thursday"
    FRIDAY = "friday"
    SATURDAY = "saturday"
    SUNDAY = "sunday"

    WEEKDAYS = (
        (MONDAY, "Lunes"),
        (TUESDAY, "Martes"),
        (WEDNESDAY, "Miercoles"),
        (THURSDAY, "Jueves"),
        (FRIDAY, "Viernes"),
        (SATURDAY, "Sabado"),
        (SUNDAY, "Domingo"),
    )
    FK_Recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    FK_Profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    WeekdayName = models.CharField(max_length=50, default=MONDAY, choices=WEEKDAYS)

    class Meta:
        db_table = "Profile_has_Recipe"


class Packages(models.Model):
    Name = models.CharField(max_length=150, unique=True)
    TotalCapacity = models.FloatField(default=0)
    FK_Ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)

    class Meta:
        db_table = "Packages"


class PackagesInventory(models.Model):
    FK_Package = models.ForeignKey(Packages, on_delete=models.CASCADE)
    ExistingPackagesQty = models.FloatField(default=0) #The number of remaining packages, if it's 1.5, means one a half packages


class AisleTag(models.Model):
    Name = models.CharField(max_length=150, unique=True)

    class Meta:
        db_table = "AisleTag"

