from django.contrib import admin
from .models import Circle,Department,Design,Division,Office,Role,Subdivision,User
# Register your models here.

class Circle_Module(admin.ModelAdmin):
    list_display = ('id','circle_code','circle_name','circle_contact','office_id')

class Department_Model(admin.ModelAdmin):
    list_display = ('id','department_name','scode','cddept')

class Design_Model(admin.ModelAdmin):
    list_display = ('id','designation','scode')

class Division_Model(admin.ModelAdmin):
    list_display = ('id','division_code','circle_code','division_name','division_contact','office_id')

class Office_Model(admin.ModelAdmin):
    list_display = ('id','office_code','office_name','office_contact','uadserver','udn','uldaprdn','display_entry','short_code','cr_short_code')

class Role_Model(admin.ModelAdmin):
    list_display = ('id','role_name')

class Subdivision_Model(admin.ModelAdmin):
    list_display = ('id','office_id','subdivision_code','subdivision_name','circle_code','division_code','subdivision_contact')

class User_Model(admin.ModelAdmin):
    list_display = ('id','subdivision_code','division_code','circle_code','office_code','department_id','design_id','role_id','uname','password','adminname','emp_no','email','phone','address','city','state','active','deactive_remarks','deactive_date','last_update_user_id','last_update_date','last_update_ip','cdeptid')

admin.site.register(Circle,Circle_Module)
admin.site.register(Department,Department_Model)
admin.site.register(Design,Design_Model)
admin.site.register(Division,Division_Model)
admin.site.register(Office,Office_Model)
admin.site.register(Role,Role_Model)
admin.site.register(Subdivision,Subdivision_Model)
admin.site.register(User,User_Model)