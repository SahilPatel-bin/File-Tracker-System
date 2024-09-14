from django.db import models

# Create your models here.
class User_Registration(models.Model):
    username = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    moblie_No = models.BigIntegerField()
    password = models.CharField(max_length=30)

    class Meta:
        db_table = 'user_registration_master'

class Feedback(models.Model):
    user_id = models.IntegerField()
    rating = models.IntegerField()
    message = models.TextField()
    date = models.DateField()

    class Meta:
        db_table = 'feedback_master'

class Admin_Registration(models.Model):
    userName = models.CharField(max_length=51)
    email = models.CharField(max_length=50)
    moblie_No = models.BigIntegerField()
    password = models.CharField(max_length=30)
    
    class Meta:
        db_table = 'Admin_Registration_Master'

class Circle(models.Model):
    circle_code = models.IntegerField(unique=True,default=0)
    circle_name = models.CharField(max_length=50)
    circle_contact = models.CharField(max_length=50)
    office_id = models.IntegerField(default=0)

    class Meta:
        db_table = 'Circle_Master'

class Department(models.Model):
    department_name = models.CharField(max_length=50)
    scode = models.CharField(max_length=10)
    cddept = models.CharField(max_length=1,default='N')

    class Meta:
        db_table = 'Department_Master'

class Design(models.Model):
    designation = models.CharField(max_length=30)
    scode =  models.CharField(max_length=10)

    class Meta:
        db_table = 'Design_Master'

class Division(models.Model):
    division_code = models.IntegerField(unique=True)
    circle_code = models.IntegerField()
    division_name = models.CharField(max_length=50)
    division_contact = models.CharField(max_length=50,null=True,default='NULL')
    office_id = models.IntegerField()

    class Meta:
        db_table = 'Division_Master'

class Office(models.Model):
    office_code = models.IntegerField(default=0)
    office_name = models.CharField(max_length=50)
    office_contact = models.CharField(max_length=50)
    uadserver = models.CharField(max_length=30)
    udn = models.CharField(max_length=50)
    uldaprdn = models.CharField(max_length=20)
    display_entry = models.IntegerField(default=0)
    short_code = models.CharField(max_length=3)
    cr_short_code = models.CharField(max_length=7)

    class Meta:
        db_table = 'Office_Master'

class Role(models.Model):
    role_name = models.CharField(max_length=15)

    class Meta:
        db_table = 'Role_Master'

class Subdivision(models.Model):
    office_id = models.IntegerField(default=0)
    subdivision_code = models.IntegerField(default=0)
    subdivision_name = models.CharField(max_length=50)
    circle_code =  models.IntegerField(default=0)
    division_code = models.IntegerField(default=0)
    subdivision_contact = models.CharField(max_length=50,default='NULL')

    class Meta:
        db_table = 'Subdivision_Master'

class User(models.Model):
    subdivision_code = models.IntegerField(default='0')
    division_code = models.IntegerField(default='0')
    circle_code =  models.IntegerField(default='0')
    office_code = models.IntegerField(default='5')
    department_id = models.IntegerField(default='0')
    design_id = models.IntegerField(default='0')
    role_id = models.IntegerField(default='0')
    uname = models.CharField(max_length=50)
    password = models.CharField(max_length=20)
    adminname = models.CharField(max_length=50)
    emp_no = models.CharField(max_length=10,null=True,default="null")
    email = models.CharField(max_length=100,null=True,default="null")
    phone = models.CharField(max_length=10,null=True,default="0")
    address = models.TextField(null=True,default="null")
    city = models.CharField(max_length=15,null=True,default="null")
    state = models.CharField(max_length=15,null=True,default="null")
    active = models.CharField(max_length=1,default='Y')
    deactive_remarks = models.CharField(max_length=100,null=True,default='null')
    deactive_date = models.DateTimeField(null=True,default=0)
    last_update_user_id = models.CharField(max_length=50,default='null',null=True)
    last_update_date = models.DateTimeField()
    last_update_ip = models.CharField(max_length=20,null=True,default='null')
    cdeptid = models.SmallIntegerField(default='0')

    class Meta:
        db_table = 'User_Master'

class File_Create(models.Model):
    scode = models.CharField(max_length=10)
    sid = models.IntegerField()
    dept_id = models.SmallIntegerField()
    design_id = models.SmallIntegerField()
    file_name = models.CharField(max_length=100)
    file_title = models.CharField(max_length=500)
    file_desc = models.TextField(null=True,default='null')
    file_created_date = models.DateTimeField()
    file_put_user_id = models.IntegerField()
    file_put_uname = models.CharField(max_length=50)
    file_status = models.CharField(max_length=10,default='create',null=True)
    file_status_remarks = models.TextField(null=True,default='null')
    file_status_date = models.DateTimeField()
    last_update_user_id = models.IntegerField(null=True,default='null')
    last_update_date = models.TimeField()
    last_update_ip = models.CharField(max_length=20,null=True,default='null')
    document = models.FileField(null=True)

    class Meta:
        db_table = 'File_Create'

class Notification(models.Model):
    file_id = models.IntegerField()
    file_name = models.CharField(max_length=100)
    sender_user_id = models.IntegerField(null=True,default='null')
    sender_uname = models.CharField(max_length=50,null=True,default='null')
    sender_date = models.DateTimeField()
    receive_user_id = models.IntegerField(null=True,default='0')
    receive_uname = models.CharField(max_length=50,null=True,default='null')
    action = models.CharField(max_length=20,null=True,default='null')
    action_read_date = models.DateTimeField()
    action_remarks = models.CharField(max_length=500,null=True,default='null')
    action_date = models.DateTimeField()
    last_update_user_id = models.IntegerField(null=True,default='0')
    last_update_date = models.DateTimeField()
    last_updated_ip = models.CharField(max_length=20,null=True,default='null')

    class Meta:
        db_table = 'Notification'