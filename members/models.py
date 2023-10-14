import hashlib
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Users(models.Model):
    username = models.CharField(max_length=250, default="", null=True, blank=True)
    password = models.CharField(max_length=500, default="", null=True, blank=True)
    email = models.CharField(max_length=250, default="", null=True, blank=True)
    Aadharnumber = models.CharField(max_length=100, default="", null=True, blank=True)
    User_type =  models.CharField(max_length=100, default="", null=True, blank=True)
    CreatedBy = models.BooleanField(default=False, null=False, blank=False)
    CreatedDate = models.DateTimeField(null=True)
    UpdatedBy = models.IntegerField(null=True)
    UpdatedDate = models.DateTimeField(null=True)
    DeletedBy = models.IntegerField(null=True)
    DeletedDate = models.DateTimeField(null=True)


class Account_Detils(models.Model):
    username = models.CharField(max_length=250, default="", null=True, blank=True)
    user_id = models.CharField(max_length=250, default="", null=True, blank=True)
    cripto_amount = models.CharField(max_length=100, default="", null=True, blank=True)
    CreatedDate = models.DateTimeField(null=True)

class Block(models.Model):
    index = models.PositiveIntegerField()
    timestamp = models.DateTimeField()
    previous_hash = models.CharField(max_length=64)
    data = models.DecimalField(max_digits=10, decimal_places=2)
    nonce = models.PositiveIntegerField()  # For PoW
    hash = models.CharField(max_length=64)
    
    
    @property
    def save(self, *args, **kwargs):
        if not self.previous_hash:
            try:
                last_block = Block.objects.get(index=self.index - 1)
                self.previous_hash = last_block.hash
            except Block.DoesNotExist:
                self.previous_hash = ''

        # Calculate the hash for this block (replace with your actual hash computation)
        self.hash = self.compute_hash()

        super(Block, self).save(*args, **kwargs)


    def compute_hash(self):
        # Replace this with your actual hash computation (using a cryptographic hash function)
        data = f"{self.index}{self.timestamp}{self.data}{self.previous_hash}".encode()
        # Compute the hash (replace with your hash algorithm)
        return hashlib.sha256(data).hexdigest()
    
    
    
class chat_messagers(models.Model):
    userid = models.ForeignKey(User, on_delete=models.CASCADE)  # Associate messages with users
    messages = models.TextField()
    user_name = models.CharField()
    times = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.time}"