from django.db import models


class ForeignDrugUser(models.Model):
    years = models.IntegerField()
    personnel = models.IntegerField()
    percent = models.DecimalField(max_digits=5, decimal_places=1)

    class Meta:
        verbose_name_plural = "최근 5년간 국내 외국인 마약류 사범 현황"

    def __str__(self):
        return f'{self.years}:{self.personnel}:{self.percent}'
    
class ForeignDrugUserNation(models.Model):
    country = models.CharField(max_length=100)
    population = models.IntegerField()
    percent = models.DecimalField(max_digits=5, decimal_places=1)

    class Meta:
        verbose_name_plural = "국내 외국인 마약사범 국적별 현황"

    def __str__(self):
        return f'{self.country}:{self.population}:{self.percent}'
# Create your models here.
