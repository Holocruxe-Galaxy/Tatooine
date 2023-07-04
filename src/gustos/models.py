from django.db import models


class meal_type(models.Model):
    id_meal_type = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class meal(models.Model):
    id_meal = models.AutoField(primary_key=True)
    type = models.ForeignKey(meal_type, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class user(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class user_meal(models.Model):
    id_user_meal = models.AutoField(primary_key=True)
    id_user = models.ForeignKey(user, on_delete=models.CASCADE)
    id_meal = models.ForeignKey(meal, on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return f"{self.id_user} - {self.id_meal} ({self.date})"
