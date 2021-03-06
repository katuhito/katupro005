from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from .models import Friend
#from .forms import HelloForm
from .forms import FriendForm
from .forms import FindForm
from .forms import CheckForm

from django.db.models import Count, Sum, Avg, Min, Max

#ジェネリックビュー
from django.views.generic import ListView, DetailView

class FriendList(ListView):
    model = Friend

class FriendDetail(DetailView):
    model = Friend


#CURD:function base
#index2
def index(request):
    # data = Friend.objects.all()
    # data = Friend.objects.all().order_by('id')
    data = Friend.objects.all()
    re1 = Friend.objects.aggregate(Count('age'))
    re2 = Friend.objects.aggregate(Sum('age'))
    re3 = Friend.objects.aggregate(Avg('age'))
    re4 = Friend.objects.aggregate(Min('age'))
    re5 = Friend.objects.aggregate(Max('age'))

    msg = 'count:' + str(re1['age__count']) + '<br>Sum:' + str(re2['age__sum']) + '<br>Average:' + str(re3['age__avg']) + '<br>Min:' + str(re4['age__min']) + '<br>Max:' +str(re5['age__max'])

    params = {
        'title': 'Hello',
        'message': msg,
        'data': data,
    }
    return render(request, 'katuapp005/index2.html', params)

#create
def create(request):
    if (request.method == 'POST'):
        obj = Friend()
        friend = FriendForm(request.POST, instance=obj)
        friend.save()
        return redirect(to='/katuapp005/index2')
    params = {
        'title': 'Hello',
        'form': FriendForm(),
    }
    return render(request, 'katuapp005/create.html', params)

#edit
def edit(request, num):
    obj = Friend.objects.get(id=num)
    if (request.method == 'POST'):
        friend = FriendForm(request.POST, instance=obj)
        friend.save()
        return redirect(to='/katuapp005/index2')
    params = {
        'title':'Hello',
        'id':num,
        'form': FriendForm(instance=obj),
    }
    return render(request, 'katuapp005/edit.html', params)

#delete
def delete(request, num):
    friend = Friend.objects.get(id=num)
    if (request.method == 'POST'):
        friend.delete()
        return redirect(to='/katuapp005/index2')
    params = {
        'title': 'Hello',
        'id': num,
        'obj': friend,
    }
    return render(request, 'katuapp005/delete.html', params)

#find
def find(request):
    if (request.method == 'POST'):
        msg = 'search result:'
        form = FindForm(request.POST)
        find = request.POST['find']
        list = find.split()
        data = Friend.objects.all()[int(list[0]):int(list[1])]
        msg = 'Result: ' + str(data.count())
    else:
        msg = 'search words...'
        form = FindForm()
        data = Friend.objects.all()
    params = {
        'title': 'Hello',
        'message': msg,
        'form': form,
        'data': data,
    }
    return render(request, 'katuapp005/find.html', params)

#check
def check(request):
    params = {
        'title': 'Hello',
        'message':'check validation',
        'form': FriendForm(),
    }
    if (request.method == 'POST'):
        obj = Friend()
        form = FriendForm(request.POST, instance=obj)
        params['form'] = form
        if (form.is_valid()):
            params['message'] = 'OK!'
        else:
            params['message'] = 'no good.'
    return render(request, 'katuapp005/check.html', params)















# from django.shortcuts import render
# from django.http import HttpResponse
# from django.views.generic import TemplateView
# from django.shortcuts import redirect
# from .forms import HelloForm, FriendForm
# from .models import Friend
# from django.urls import reverse_lazy

# class HelloView(TemplateView):

#     def __init__(self):
#         self.params = {
#             'title':'Hello',
#             'message':'your data',
#             'form': HelloForm(),  
#             'messages':'all friends.',   
#         }

#     def get(self, request):
#         return render(request, 'katuapp005/index.html', self.params)

#     def post(self, request):
#         msg = 'あなたは、<br>' + request.POST['name'] + \
#             '(' + request.POST['age'] + \
#                 ') </b>さんです。<br>メールアドレスは<b>' + request.POST['mail'] + \
#                     '</b> ですね。'
#         self.params['message'] = msg

#         #Checkbox
#         if ('chck' in request.POST):
#             self.params['results'] = 'Checked!!'
#         else:
#             self.params['results'] = 'not checked...'

#         #Check
#         chk = request.POST['check']
#         self.params['result'] = 'you selected: "' + chk + '".'
#         self.params['form'] = HelloForm(request.POST)
#         return render(request, 'katuapp005/index.html', self.params)

# # class HelloView2(TemplateView):
# #     template_name = "katuapp005/friends.html"

# #     def __init__(self):
# #         self.params = {
# #             'title': 'Hello',
# #             'message': 'Select friends.',
# #             'form': HelloForm2(),
# #             'data': [],
# #         }

# #     def get(self, request):
# #         return render(request, 'katuapp005/friends.html', self.params)

# #     def post(self, request):
# #         # self.data = Friend.objects.all()
# #         if(request.method == 'POST'):
# #             self.num = request.POST['id']
# #             self.item = Friend.objects.get(id=self.num)
# #             self.params['data'] = [self.item]
# #             self.params['form'] = HelloForm2(request.POST)
# #         else:
# #             self.params['data'] = Friend.objects.all()
# #         return render(request, 'katuapp005/friends.html', self.params)

# class HelloView3(TemplateView):
#     template_name = "katuapp005/index2.html"

#     def __init__(self):
#         self.params = {
#             'title': 'Hello',
#             'data': Friend.objects.all(),
#         }
    
#     def get(self, request):
#         return render(request, 'katuapp005/index2.html', self.params)

#     def post(self, request):
#         self.data = Friend.objects.all()
#         return render(request, 'katuapp005/index2.html', self.params)

# class HelloView4(TemplateView):
#     template_name = "katuapp005/create.html"

#     def __init__(self):
#         self.params = {
#             'title': 'Hello',
#             'form': FriendForm(),
#         }
    
#     def get(self, request):
#         return render(request, 'katuapp005/create.html', self.params)

#     def post(self, request):
#         # if (request.method == 'POST'):
#         #     self.name = request.POST['name']
#         #     self.mail = request.POST['mail']
#         #     self.gender = 'gender' in request.POST
#         #     self.age = int(request.POST['age'])
#         #     self.birth = request.POST['birthday']
#         #     self.friend = Friend(name=self.name, mail=self.mail, gender=self.gender, age=self.age, birthday=self.birth)
#         #     self.friend.save()
#         #     return redirect(to='/katuapp005/index2')
#         if (request.method == 'POST'):
#             self.obj = Friend()
#             self.friend = FriendForm(request.POST, instance=self.obj)
#             self.friend.save()
#             return redirect(to='/katuapp005/index2')
#         return render(request, 'katuapp005/create.html', self.params)


# class HelloView5(TemplateView):
#     template_name = "katuapp005/edit.html"

#     def __init__(self):
#         self.params = {
#             'title': 'Hello',
#             'id':num,
#             'form': FriendForm(),
#             }

#     # def get_context_data(self, **kwargs):
#     #     context = super().get_context_data(**kwargs)
#     #     context['id'] = int(self.kwargs.get('id'))
#     #     return context   
    
#     def get(self, request, num):
#         return render(request, 'katuapp005/edit.html', self.params)

#     def post(self, request, num):
#         # self.num = request.POST['id']
#         self.obj = Friend.objects.get(id=num)
#         if (request.method == 'POST'):
#             self.obj = Friend()
#             self.friend = FriendForm(request.POST, instance=self.obj)
#             self.friend.save()
#             return redirect(to='/katuapp005/index2')
#         return render(request, 'katuapp005/edit.html', self.params)




   

        
        





    


