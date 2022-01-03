# from django.db import models
# from django.contrib.auth.models import User

# class Profile(models.Model):
#     # name = models.CharField(max_length=255)
#     # created_at = models.DateTimeField(auto_now_add=True)
#     # created_by = models.OneToOneField(User, related_name='user', on_delete=models.CASCADE)
#     # balance=models.DecimalField(max_digits=10,decimal_places=2,default=0.0)
#     user=models.OneToOneField(User,on_delete=models.CASCADE,default=0)
   
    
#     def __str__(self):
#         return f'{self.user.username} Profile'

# # class Profile(models.Model):
# #     user = models.OneToOneField(User, on_delete=models.CASCADE)
# #     image = models.ImageField(default='default.jpg', upload_to='profile_pics')

# #     def __str__(self):
# #         return f'{self.user.username} Profile'


from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'