from django.db import models
from django.urls import reverse

TRANSACTIONS = (
    ('B', 'Bought'),
    ('S', 'Sold')
)

# Create your models here.

class Record(models.Model):
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    release_date = models.DateField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("detail", kwargs={"record_id": self.id})

class Market(models.Model):
    date = models.DateField('date')
    transaction = models.CharField(
        max_length=1,
        choices=TRANSACTIONS,
        default=TRANSACTIONS[0][0]
    )

    record = models.ForeignKey(Record, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_transaction_display()} on {self.date}"
    
    class Meta:
        ordering = ['-date']