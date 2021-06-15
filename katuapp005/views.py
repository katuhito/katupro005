from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from .forms import HelloForm
from .models import Friend

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

   

        
        





    


