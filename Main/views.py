from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from .models import Expense
from .forms import ExpenseForm
from django.contrib.auth.decorators import login_required

@login_required
def add_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('expense_list')  # Assuming you have a view named 'expense_list'
    else:
        form = ExpenseForm()

    return render(request, 'add_expense.html', {'form': form})


# #baseroute
# def expense_homepage(request):
#     return redirect('/login')
#     expenses = Expense.objects.all()
#     return render(request, 'expense_tracker.html', {'expenses': expenses})

@login_required
def expense_tracker(request):
    expenses = Expense.objects.all()
    return render(request, 'expense_tracker.html', {'expenses': expenses})

@login_required
def expense_list(request):
    expenses = Expense.objects.all()
    return render(request, 'expense_list.html', {'expenses': expenses})

@login_required
def expense_detail(request, expense_id):
    expense = get_object_or_404(Expense, id=expense_id)
    return render(request, 'expense_detail.html', {'expense': expense})

@login_required
def expense_update(request, expense_id):
    expense = get_object_or_404(Expense, id=expense_id)

    if request.method == 'POST':
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('expense_list')

    else:
        form = ExpenseForm(instance=expense)

    return render(request, 'expense_form.html', {'form': form, 'action': 'Update'})

@login_required
def expense_delete(request, expense_id):
    expense = get_object_or_404(Expense, id=expense_id)

    if request.method == 'POST':
        expense.delete()
        return redirect('expense_list')

    return render(request, 'expense_confirm_delete.html', {'expense': expense})



def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('expense_tracker')  # Redirect to the expense tracker page after registration
    else:
        form = UserCreationForm()

    return render(request, 'registration/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('expense_tracker')  # Redirect to the expense tracker page after login
    else:
        form = AuthenticationForm()

    return render(request, 'registration/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('expense_tracker')  # Redirect to the expense tracker page after logout