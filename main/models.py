from django.db import models


class Todo(models.Model):
    STATUS_CHOICES=[
        ["new","New"],
        ["in_progress","In_progress"],
        ["finished","Finished"],
    ]
    title=models.CharField(max_length=150)
    desc=models.TextField(null=True,blank=True)
    time=models.DateTimeField()
    status=models.CharField(max_length=50,choices=STATUS_CHOICES)
    
    class Meta:
        verbose_name="Todo"
        verbose_name_plural="Todo"
    def __str__(self):
        return f"{self.title}"[:50]