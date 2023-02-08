from django.shortcuts import render
from socialgram.models import PostModel,MyUser
from socialgram.form import RegistrationForm,LoginForm,PostForm
from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView,FormView,TemplateView,ListView,DetailView
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
# Create your views here.



class SignUpView(CreateView):
    model=MyUser
    template_name="Registration.html"
    form_class=RegistrationForm
    success_url=reverse_lazy('signup')
    
    
class LoginView(FormView):
    form_class=LoginForm
    template_name="login.html"
    def post(self,request,*args,**kwargs):
        form=LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            user=authenticate(request,username=username,password=pwd)
            if user:
                login(request,user=user)
                messages.success="login success"
                return redirect("home")
            else:
                messages.error="login failed"
                return redirect("signin")
            
            
class HomeView(ListView):
    model=PostModel
    template_name="home.html"
    context_object_name='posts'
    def get_queryset(self):
        return PostModel.objects.all().exclude(user=self.request.user)
    
    
class UserDashboardView(ListView):
    model=PostModel
    context_object_name="myposts"
    template_name='userdashboard.html'
    def get_queryset(self):
        return PostModel.objects.filter(user=self.request.user)

def add_like(request, *args, **kwargs):
    pid=kwargs.get("id")
    post=PostModel.objects.get(id=pid)
    post.like.add(request.user)
    post.save()
    return redirect('home')


class PostAddView(CreateView):
    model=PostModel
    form_class=PostForm
    template_name='addpost.html'
    success_url=reverse_lazy('home')
    def form_valid(self, form):
        form.instance.user=self.request.user
        return super().form_valid(form)
    
def signout(request, *args, **kwargs):
    logout(request)
    return redirect('signin')


class PostDetailView(DetailView):
    model=PostModel
    template_name="postdetail.html"
    pk_url_kwarg="id"
    context_object_name="post"
    