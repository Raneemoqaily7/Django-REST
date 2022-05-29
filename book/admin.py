from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin


from .models import CustomUser
from .forms import CustomUserChangeForm ,CustomUserCreationForm


@admin.register(CustomUser)

class CustomUserAdmin (UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model =CustomUser
    list_display=["email" , "username" , "phone_number" , "address"]
    fieldsets = UserAdmin.fieldsets+(

        ("contact number" , {"fields":("phone_number", )}),
        ("Address Info" , {"fields":("address", )}),
    )


