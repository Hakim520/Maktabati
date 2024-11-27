from django.contrib.auth import logout
from django.shortcuts import redirect

def logout_view(request):
    logout(request)
    return redirect('store')  # Redirect to the homepage or any other page after logout

