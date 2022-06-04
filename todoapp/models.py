from django.db import models

# Create your models here.
class Todo(models.Model):
    PRIOTRY = [
        ('FS','FullStack'),
        ('DS','DataScience'),
        ('AWS','Amazon Web Service')
    ]
    location = [
        ("TR", "Turkey"),
        ("ABD", "America"),
        ("BUL", "Bulgaristan")
    ]
    first_name = models.CharField(max_length=30)
    branche = models.CharField(max_length=20,choices=PRIOTRY,default='FS')
    Location = models.CharField(max_length=30,choices=location,default='TR')
    created_at = models.DateTimeField(auto_now_add=True)  #! şimdiki gün.
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} - {self.Location} - {self.branche} - {self.created_at} - {self.update_at}"
        
    class Meta:
        verbose_name_plural = 'Todos'  #! adını değiştirir.
        #db_table = 'student_table'  #! db table adı degısır, tekrar migrations yapmalısın.