from django.db import models  
class Funcionario(models.Model):  
    fid = models.CharField(max_length=20)  
    fname = models.CharField(max_length=100)  
    fposition = models.CharField(max_length=30)  
    femail = models.EmailField()  
    fcontact = models.CharField(max_length=15)  
    class Meta:  
        db_table = "funcionario"  
