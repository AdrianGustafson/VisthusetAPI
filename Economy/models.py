from django.db import models
from datetime import date, datetime
from django.contrib.auth.models import User
from django.dispatch.dispatcher import receiver
from django.db.models.signals import post_save
'''
TODO:
* Gör det möjligt att räkna ut lön, skatt och antal arbetade timmar för varje anställd
    - Ge digitalt lönebesked
* Gör formulär för admin att kunna lägga in antalet timmar de anställda jobbat
    - Uppdaterar automatiskt hours_worked

'''
class Employee(models.Model):
    user = models.OneToOneField(
        User,
        limit_choices_to = {'is_staff' : True},
        null = True,
        blank = True,
        verbose_name='anställd'
        )
    first_name = models.CharField(max_length=25, default=None, verbose_name='förnamn')
    last_name = models.CharField(max_length=25, default=None, verbose_name='efternamn')
    person_number = models.IntegerField(null= True, verbose_name= 'Personnummer')
    wage = models.DecimalField(verbose_name= 'Lön',
        max_digits=6, decimal_places=2, null= True, blank=True)
    
    hours_worked = models.DecimalField(verbose_name='arbetade timmar',
        max_digits=6, decimal_places=2, default = 0)
    
    tax = models.DecimalField(max_digits=4, decimal_places=2, default=33.0,
                              help_text='Preliminärskatt att dra från lönen',
                              verbose_name='preliminärskatt')
    
    drawTax = models.BooleanField(default=True, verbose_name='Dra preliminärskatt',
                                  help_text='skall preliminärskatt dras från lönen?')
    
    ArbAvg = models.DecimalField(max_digits=3, decimal_places=2, default=0.25)
    
    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)
    
    def get_full_name(self):
        return "%s %s" % (self.user.first_name, self.user.last_name)
    
    def update_hours_worked(self, hours):
        self.hours_worked += hours
        return self.hours_worked
    
    def reset_hours_worked(self):
        self.hours_worked = 0
        return self.hours_worked
    
    class Meta:
        verbose_name = 'anställd'
        verbose_name_plural = 'anställda'
   
class WorkingHours(models.Model):
    employee = models.ForeignKey(
        Employee,
        null=True,
        verbose_name='anställd'
        )
    date = models.DateField(verbose_name='datum')
    startTime = models.TimeField(verbose_name='starttid')
    endTime = models.TimeField(verbose_name='sluttid')
    added = models.DateTimeField(default=datetime.now, verbose_name= 'Tillagd')
    
    class Meta:
        verbose_name='arbetstimme'
        verbose_name_plural='arbetstimmar'
        unique_together = ['employee', 'date']

# Modell för att lägga in dagskassor
class Dagskassa(models.Model):
    date = models.DateField(default= date.today, verbose_name='datum')
    
    cash = models.DecimalField(
        max_digits = 7, decimal_places = 2, default=0, verbose_name='kontanter')
    
    card = models.DecimalField(
        max_digits = 7, decimal_places = 2, default=0, verbose_name='kort')
    
    cafeSales = models.DecimalField(
        max_digits = 7, decimal_places = 2, default=0, verbose_name='café')
    
    iceCreamSales = models.DecimalField(
        max_digits = 7, decimal_places = 2, default=0, verbose_name='glass')
    
    foodShopSales = models.DecimalField(
        max_digits = 7, decimal_places = 2, default=0, verbose_name='gårdsbutik')
    
    bikeSales = models.DecimalField(
        max_digits = 7, decimal_places = 2, default=0, verbose_name='cyklar')
    
    booksSales = models.DecimalField(
        max_digits = 7, decimal_places = 2, default=0, verbose_name='böcker')
    
    other12Sales = models.DecimalField(
        max_digits = 7, decimal_places = 2, default=0, verbose_name='övrigt 12%')
    
    other25Sales = models.DecimalField(
        max_digits = 7, decimal_places = 2, default=0, verbose_name='övrigt 25%')
    
    signature = models.ForeignKey(Employee,
        on_delete=models.CASCADE,
        verbose_name='Signatur'
        )
    
    comment = models.CharField(max_length = 150, null=True, verbose_name='kommentar')
    class Meta:
        verbose_name = 'dagskassa'
        verbose_name_plural = 'dagskassor'
        ordering = ('date', )
        unique_together = ['date', 'cash', 'card', 'signature']
