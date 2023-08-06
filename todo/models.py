from django.db import models

class Todo(models.Model):
    title=models.CharField(max_length=300)
    content=models.TextField()
    priority=models.IntegerField(default=1)
    is_done=models.BooleanField()

    def __str__(self) -> str:
        return f'{self.title} / IS DONE : {self.is_done}'

    class Meta:
        db_table='todos'