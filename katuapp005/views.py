from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.shortcuts import redirect
from .forms import HelloForm, HelloForm2, FriendForm
from .models import Friend
from django.urls import reverse_lazy

class HelloView(TemplateView):

    def __init__(self):
        self.params = {
            'title':'Hello',
            'message':'your data',
            'form': HelloForm(),  
            'messages':'all friends.',   
        }

    def get(self, request):
        return render(request, 'katuapp005/index.html', self.params)

    def post(self, request):
        msg = 'あなたは、<br>' + request.POST['name'] + \
            '(' + request.POST['age'] + \
                ') </b>さんです。<br>メールアドレスは<b>' + request.POST['mail'] + \
                    '</b> ですね。'
        self.params['message'] = msg

        #Checkbox
        if ('chck' in request.POST):
            self.params['results'] = 'Checked!!'
        else:
            self.params['results'] = 'not checked...'

        #Check
        chk = request.POST['check']
        self.params['result'] = 'you selected: "' + chk + '".'
        self.params['form'] = HelloForm(request.POST)
        return render(request, 'katuapp005/index.html', self.params)

class HelloView2(TemplateView):
    template_name = "katuapp005/friends.html"

    def __init__(self):
        self.params = {
            'title': 'Hello',
            'message': 'Select friends.',
            'form': HelloForm2(),
            'data': [],
        }

    def get(self, request):
        return render(request, 'katuapp005/friends.html', self.params)

    def post(self, request):
        # self.data = Friend.objects.all()
        if(request.method == 'POST'):
            self.num = request.POST['id']
            self.item = Friend.objects.get(id=self.num)
            self.params['data'] = [self.item]
            self.params['form'] = HelloForm2(request.POST)
        else:
            self.params['data'] = Friend.objects.all()
        return render(request, 'katuapp005/friends.html', self.params)

class HelloView3(TemplateView):
    template_name = "katuapp005/index2.html"

    def __init__(self):
        self.params = {
            'title': 'Hello',
            'data': Friend.objects.all(),
        }
    
    def get(self, request):
        return render(request, 'katuapp005/index2.html', self.params)

    def post(self, request):
        self.data = Friend.objects.all()
        return render(request, 'katuapp005/index2.html', self.params)

class HelloView4(TemplateView):
    template_name = "katuapp005/create.html"

    def __init__(self):
        self.params = {
            'title': 'Hello',
            'form': FriendForm(),
        }
    
    def get(self, request):
        return render(request, 'katuapp005/create.html', self.params)

    def post(self, request):
        # if (request.method == 'POST'):
        #     self.name = request.POST['name']
        #     self.mail = request.POST['mail']
        #     self.gender = 'gender' in request.POST
        #     self.age = int(request.POST['age'])
        #     self.birth = request.POST['birthday']
        #     self.friend = Friend(name=self.name, mail=self.mail, gender=self.gender, age=self.age, birthday=self.birth)
        #     self.friend.save()
        #     return redirect(to='/katuapp005/index2')
        if (request.method == 'POST'):
            self.obj = Friend()
            self.friend = FriendForm(request.POST, instance=self.obj)
            self.friend.save()
            return redirect(to='/katuapp005/index2')
        return render(request, 'katuapp005/create.html', self.params)


class HelloView5(TemplateView):
    template_name = "katuapp005/edit.html"
    

    def __init__(self):
        self.params = {
            'title': 'Hello',
            'id': num,
            'form': FriendForm(instance=obj),
            }
        
    
    def get(self, request, num):
        self.num = request.GET['num']
        return render(request, 'katuapp005/edit.html', self.params)

    def post(self, request, num):
        # self.num = request.POST['id']
        self.obj = Friend.objects.get(id=self.num)
        if (request.method == 'POST'):
            self.obj = Friend()
            self.friend = FriendForm(request.POST, instance=self.obj)
            self.friend.save()
            return redirect(to='/katuapp005/index2')
        return render(request, 'katuapp005/edit.html', self.params)




   

        
        





    


