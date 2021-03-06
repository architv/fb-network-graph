import requests
from django.shortcuts import render
from main.forms import InputForm
from django.http import HttpResponseRedirect

def main(request):
    if request.method == 'POST': # If the form has been submitted
        input_form = InputForm(request.POST)
        if input_form.is_valid():
            cd = input_form.cleaned_data
            keyword = cd['keyword']
            url = "https://graph.facebook.com/search?q="+keyword+"&type=post&fields=likes.fields(name).limit(10),comments,message&limit=5&access_token=1434923293417681|3e2c59074ce5b2d34436fe6ee90dfa63"
            fetch = requests.get(url)
            data = fetch.json()
            nodes = "[{ group:'nodes', data: { id:'"+keyword+"' , name:'"+keyword+"',gweight: '12', gheight: '12', faveColor: '#6FB1FC', mColor: '#6FB1FC', size: 8  } },"
            edges = ""
            for meta in data["data"]:
                if "likes" in meta:
                    for beta in meta["likes"]["data"]:
                        nodes += "{ group:'nodes', data: { id: '"+beta['id']+"' , name: '"+beta['id']+"', gweight: '2', gheight: '2', faveColor: '#736F6E', mColor: '#736F6E', size: 2 } },"
                        edges += "{ group:'edges', data: { source:'"+keyword+"' , target: '"+beta['id']+"', mColor: '#98AFC7' } },"
                if "comments" in meta:
                    for beta in meta["comments"]["data"]:
                        nodes += "{ group:'nodes', data: { id: '"+beta['from']['id']+"' , name: '"+beta['from']['id']+"', gweight: '2', gheight: '2', faveColor: '#736F6E', mColor: '#736F6E', size: 2  } },"
                        edges += "{ group:'edges', data: { source:'"+keyword+"' , target: '"+beta['from']['id']+"', mColor:'#52D017' } },"
            edges += " ]"
            total = nodes + edges
            with open('data.txt','w+') as js:
                js.write(total)
            return HttpResponseRedirect('/graph/')
        else:
            input_form = InputForm(request.POST)
            return render(request, 'index.html', {
                'input_form': input_form,
            })
    else:
        input_form = InputForm()
        return render(request, 'index.html', {
            'input_form': input_form,
        })

def graph(request):
    with open('data.txt','r+') as data:
        content = data.read()
    return render(request,'graph.html',{
            'content':content,
        })