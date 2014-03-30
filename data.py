import urllib, json
print "You need to get access token first with the following permissions: read_stream"
actoken = raw_input("Enter your access token: ")
postid = raw_input("Please enter the id of the post: ")
url = "https://graph.facebook.com/"+postid+"?fields=likes.fields(pic_square,name).limit(100),comments&access_token="+actoken
fetch = urllib.urlopen(url).read()
data = json.loads(fetch)
nodes = "[{ group:'nodes', data: { id:'"+postid+"' , name:'fbpost'  } },"
edges = ""
for meta in data['likes']['data']:
	nodes += "{ group:'nodes', data: { id: '"+meta['id']+"' , name: '"+meta['name']+"'  } },"
	edges += "{ group:'edges', data: { source:'"+postid+"' , target: '"+meta['id']+"' } },"
edges += " ]"
total = nodes + edges
with open('data.txt','w+') as js:
	js.write(total)