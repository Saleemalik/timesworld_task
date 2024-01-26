from django.shortcuts import render, redirect

# Create your views here.


from django.views.generic.base import View, TemplateView
from .models import User
from django.contrib import auth
from django.http.response import JsonResponse 


class LoginPageView(View):
    def get(self, request):
        return render(request, 'login.html')
    
    def post(self, request):
        email = request.POST['email']

        password = request.POST['password']
        

    
        user = auth.authenticate(email=email, password=password)


        if user is not None:
            auth.login(request, user)
            
            return JsonResponse('true', safe=False)
            
        else:
            return JsonResponse('false', safe=False)


class RegistrationPageView(TemplateView):

     def get(self, request):
        return render(request, 'register.html')
     
     def post(self, request):
        username = request.POST['username']
        email = request.POST['email']
        mobile_number = request.POST['mobile_number']
        country = request.POST['country']
        nationality = request.POST['nationality']
        role = request.POST['role']
        password = request.POST['password']

        if User.objects.filter(username = username).exists():  
            data = {
                'mode': 'error',
                'field': 'username', 
                'message' :  'username taken',
            }
            return JsonResponse(data)
        elif User.objects.filter(email = email).exists():
            data = {
                'mode': 'error',
                'field': 'email',
                'message' :  'email taken',
            }
            return JsonResponse(data)
        else:
            user = User.objects.create_user(username=username, password=password, email=email, mobile_number=mobile_number, country=country, nationality=nationality, role=role )
            user.save()
        data = {
            'mode': 'success',
            'message' :  'successfully added',
        }
        return JsonResponse(data)

class AdminPageView(View):
    def get(self, request):
        if request.user.is_authenticated and request.user.role == 'admin':
            return render(request, 'admin.html', {'user': request.user})
        else:
            return redirect('access-denied')

class EditorPageView(View):
    def get(self, request):
        if request.user.is_authenticated and request.user.role == 'editor':
            return render(request, 'editor.html', {'user': request.user})
        return redirect('access-denied')

class StaffPageView(View):
    def get(self, request):
        if request.user.is_authenticated and request.user.role == 'staff':
            return render(request, 'staff.html', {'user': request.user})
        return redirect('access-denied')

class StudentPageView(View):
    def get(self, request):
        if request.user.is_authenticated and request.user.role == 'student':
            return render(request, 'student.html', {'user': request.user})
        return redirect('access-denied')


def logout(request):
    auth.logout(request)
    return redirect("/")

def home(request):
    return redirect(f"{request.user.role}/")
