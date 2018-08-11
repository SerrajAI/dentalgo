from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

# python manage.py migrate --run-syncdb --------------------- delete migration files then db and then sync it with this



#python manage.py flush  clear db



class Doctor(models.Model):
    # CIVILITY_CHOICES = (
    #     ('Mr', 'Monsieur'),
    #     ('Mme', 'Madame'),
    #
    # )
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # cin = models.CharField(max_length=200, )
    # civility = models.CharField(choices = CIVILITY_CHOICES,max_length=10,null=True, blank=True, )


    # def __str__(self):
    #     return "@{}".format(self.user.username)




class Patient(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    # parent = models.ForeignKey('admin.User', null=True)
    CIVILITY_CHOICES = (
        ('Mr', 'Mr.'),
        ('Mme', 'Mme.'),

    )
    fullname = models.CharField(max_length=200,unique=True, )
    created_by = models.ForeignKey(User,related_name='patients',on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True,null=True, blank=True,)
    cin = models.CharField(max_length=200,unique=True, )
    civility = models.CharField(choices = CIVILITY_CHOICES,max_length=10,null=True, blank=True, )
    phone =  models.CharField(max_length=20,default="06",unique=True, )
    assurance = models.CharField(max_length=200,default="Aucune")
    profession = models.CharField(max_length=200,default="Aucune")
    special = models.CharField(max_length=2000,default="Aucune")
    profile_picture=models.ImageField(upload_to='pics/%Y/%m/%d/', blank=True, null=True)



    @property
    def profile_picture_url(self):
        if self.profile_picture and hasattr(self.profile_picture, 'url'):
            return self.photo.profile_picture

    def get_absolute_url(self):
        return reverse("accounts:detail",kwargs={'pk':self.pk})

    def __str__(self):
        return str(self.civility)+" "+(self.fullname)
        class Meta:
            ordering = ['-fullname']



# class School(models.Model):
#     name = models.CharField(max_length=256)
#     principal = models.CharField(max_length=256)
#     location = models.CharField(max_length=256)
#
#     def __str__(self):
#         return self.name
#
#     def get_absolute_url(self):
#         return reverse("accounts:detail",kwargs={'pk':self.pk})
#
# class Student(models.Model):
#     name = models.CharField(max_length=256)
#     age = models.PositiveIntegerField()
#     school = models.ForeignKey(School,related_name='students',on_delete=models.CASCADE)
#
#     def __str__(self):
#         return self.name

class Appointment(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    # parent = models.ForeignKey('admin.User', null=True)
    # CIVILITY_CHOICES = (
    #     ('Mr', 'Mr.'),
    #     ('Mme', 'Mme.'),
    #
    # )
    # fullname = models.CharField(max_length=200, )

    # operation = models.ForeignKey(Operation,related_name='app_operations',on_delete=models.CASCADE,null=True)
    # cin = models.CharField(max_length=200, )
    # civility = models.CharField(choices = CIVILITY_CHOICES,max_length=10,null=True, blank=True, )
    # phone =  models.CharField(max_length=20,default="06" )
    created_by = models.ForeignKey(User,related_name='appointments',on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient,related_name='appointments',on_delete=models.CASCADE)
    day = models.DateField(blank=True, null=True)
    time = models.TimeField(blank=True, null=True)
    special = models.CharField(max_length=2000,default="06")
    position = models.IntegerField(null=True, blank=True,)

    # profile_picture=models.ImageField(upload_to='pics/%Y/%m/%d/', blank=True, null=True)
    # @property
    # def profile_picture_url(self):
    #     if self.profile_picture and hasattr(self.profile_picture, 'url'):
    #         return self.photo.profile_picture

    def get_absolute_url(self):
        return reverse("accounts:detailapp",kwargs={'pk':self.pk})

    def __str__(self):
        return str(self.day) +" "+ str(self.time) +" "+ str(self.patient) +" (an-mois-jour)"


    # def __str__(self):
    #     return self.fullname
    #     class Meta:
    #         ordering = ['-fullname']

class Operation(models.Model):
    OP_NAME_CHOICES = (
        ('detartrage', 'detartrage'),
        ('extraction', 'extraction'),

    )
    DENT_CHOICES = (
        ('11', '11'),
        ('12', '12'),
        ('13', '13'),
        ('14', '14'),
        ('15', '15'),
        ('16', '16'),
        ('17', '17'),
        ('18', '18'),

        ('21', '21'),
        ('22', '22'),
        ('23', '23'),
        ('24', '24'),
        ('25', '25'),
        ('26', '26'),
        ('27', '27'),
        ('28', '28'),

        ('31', '31'),
        ('32', '32'),
        ('33', '33'),
        ('34', '34'),
        ('35', '35'),
        ('36', '36'),
        ('37', '37'),
        ('38', '38'),

        ('41', '41'),
        ('42', '42'),
        ('43', '43'),
        ('44', '44'),
        ('45', '45'),
        ('46', '46'),
        ('47', '47'),
        ('48', '48'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('1+2', '1+2'),
        ('3+4', '3+4'),
        ('tout', 'tout'),






    )

    # patient = models.ForeignKey(Patient,related_name='pat_operations',on_delete=models.CASCADE,null=True)
    # appointment = models.ForeignKey(Appointment,related_name='app_operations',on_delete=models.CASCADE,null=True)
    created_by = models.ForeignKey(User,related_name='operations',on_delete=models.CASCADE)
    fullname = models.CharField(choices = OP_NAME_CHOICES,max_length=200,null=True, blank=True, )
    patient = models.ForeignKey(Patient,related_name='operations',on_delete=models.CASCADE)
    appointment = models.ForeignKey(Appointment,related_name='operations',on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=6, decimal_places=2,null=True, blank=True,)
    advance = models.DecimalField(max_digits=6, decimal_places=2,null=True, blank=True,)
    rest = models.DecimalField(max_digits=6, decimal_places=2,null=True, blank=True,)
    day = models.DateTimeField(blank=True, null=True)
    time = models.TimeField(blank=True, null=True)
    special = models.CharField(max_length=2000,null=True, blank=True,default="06")
    dent  = models.CharField(choices = DENT_CHOICES,max_length=10,blank=True, null=True)


    def save(self, *args, **kwargs):
        self.rest = self.price - self.advance
        super(Operation, self).save(*args, **kwargs) # Call the "real" save() method.
    def __str__(self):
        return self.fullname

    def get_absolute_url(self):
        return reverse("accounts:detailop",kwargs={'pk':self.pk})
