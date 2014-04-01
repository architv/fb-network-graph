import urllib, json
print "You need to get access token first with the following permissions: read_stream"
actoken = raw_input("Enter your access token: ")
keyword = raw_input("Please enter the keyword of the post: ")
url = "https://graph.facebook.com/search?q="+keyword+"&type=post&fields=likes.fields(name).limit(200),comments,message&limit=5&access_token="+actoken
fetch = urllib.urlopen(url).read()
data = json.loads(fetch)
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
total = nodes + edges
with open('data.txt','w+') as js:
	js.write(total)