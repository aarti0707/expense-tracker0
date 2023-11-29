from django.urls import path
from .views import add_expense,expense_tracker,expense_list, expense_detail, expense_update, expense_delete,register, user_login, user_logout

urlpatterns = [
    path('', expense_tracker, name='expense_tracker'),
    path('exp_list', expense_list, name='expense_list'),
    path('expense_detail/<int:expense_id>/', expense_detail, name='expense_detail'),
    path('expense_update/<int:expense_id>/', expense_update, name='expense_update'),
    path('expense_delete/<int:expense_id>/', expense_delete, name='expense_delete'),
    path('add_expense/', add_expense, name='add_expense'),
    # Add other URL patterns as needed

    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
]
