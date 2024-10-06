from django.db import models

class Equipment(models.Model):
    EQUIPMENT_TYPES = [
        ('Robot', 'Robot'),
        ('Manufacturing', 'Manufacturing'),
        ('Quality Control', 'Quality Control'),
    ]

    equipment_type = models.CharField(max_length=50, choices=EQUIPMENT_TYPES)
    model = models.CharField(max_length=100)
    installation_date = models.DateField()
    status = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.model} ({self.get_equipment_type_display()})'

class Data(models.Model):
    equipment = models.ForeignKey(Equipment, related_name='data', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    temperature = models.FloatField()
    speed = models.FloatField()
    pressure = models.FloatField()

    def __str__(self):
        return f'{self.equipment} - {self.timestamp}'

class Alert(models.Model):
    equipment = models.ForeignKey(Equipment, related_name='alerts', on_delete=models.CASCADE)
    description = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Alert for {self.equipment}: {self.description}'
