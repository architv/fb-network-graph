import urllib, json
from django.shortcuts import render, render_to_response, redirect
from main.forms import InputForm
from django.http import HttpResponse, HttpResponseRedirect

def main(request):
    if request.method == 'POST': # If the form has been submitted
        input_form = InputForm(request.POST)
        if input_form.is_valid():
            cd = input_form.cleaned_data
            actoken = cd['access_token']
            keyword = cd['keyword']
            print actoken
            print keyword
            url = "https://graph.facebook.com/search?q="+keyword+"&type=post&fields=likes.fields(name).limit(200),comments,message&limit=5&access_token="+actoken
            fetch = urllib.urlopen(url).read()
            data = json.loads(fetch)
            #print data
            nodes = "[{ group:'nodes', data: { id:'"+keyword+"' , name:'"+keyword+"'  } },"
            edges = ""
            for meta in data["data"]:
                if "likes" in meta:
                    for beta in meta["likes"]["data"]:
                        nodes += "{ group:'nodes', data: { id: '"+beta['id']+"' , name: '"+beta['id']+"'  } },"
                        edges += "{ group:'edges', data: { source:'"+keyword+"' , target: '"+beta['id']+"' } },"
                if "comments" in meta:
                    for beta in meta["comments"]["data"]:
                        nodes += "{ group:'nodes', data: { id: '"+beta['from']['id']+"' , name: '"+beta['from']['id']+"'  } },"
                        edges += "{ group:'edges', data: { source:'"+keyword+"' , target: '"+beta['from']['id']+"' } },"
            edges += " ]"
            #print nodes
            #print edges
            total = nodes + edges
            #print total
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

"""def getData(request):
    with open('data.txt','r+') as data:
        content = data.read()
        print content
    return render(request,'data.html',{
            'content':content,
        })"""