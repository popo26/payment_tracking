from django.contrib import admin
from .models import Todo, Repay

# Register your models here.

class RepayInline(admin.TabularInline):
    model = Repay
    can_delete = False

@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ['date', 'text', 'amount', 'whose_account_to_repay']
    list_per_page = 10
    inlines = [RepayInline]


