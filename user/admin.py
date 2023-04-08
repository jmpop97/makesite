from django.contrib import admin
from .models import UserModel

class TimeDisplay(admin.ModelAdmin):
    list_display = ('username','email','password','created_at','updated_at')
    fields =('username','email','password','created_at','updated_at')
    readonly_fields = ('created_at','updated_at')

# Register your models here.
admin.site.register(UserModel,TimeDisplay) # 이 코드가 나의 UserModel을 Admin에 추가 해 줍니다py