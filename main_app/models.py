from django.db import models
from django.urls import reverse

REASONS = (
    ('P', 'Personal Gain'),
    ('A', 'Against Avengers'),
    ('S', 'Showing Off...Again')
)

# Create your models here.
class Stone(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'stone_id': self.id})

class Use(models.Model):
  date = models.DateField('Date Used')
  reason = models.CharField(
    max_length=1,
        choices=REASONS,
        default=REASONS[0][0]
  )
  
  stone = models.ForeignKey(Stone, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.get_reason_display()} on {self.date}"

  class Meta:
    ordering = ['-date']
