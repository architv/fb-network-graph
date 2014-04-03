fb-network-graph
================================

Dependencies:
-------------
*  Python 2.7
*  Django 1.6.1
       
Usage:
----------
**fb-network-graph**  crawls any public [Facebook](https://www.facebook.com/) post using the [FB graph api](https://developers.facebook.com/docs/graph-api/) for a "keyword" and then plots a graph for the likes and comments for the keyword.

Change the directory to wherever the files are stored and then run the following command

	$ python manage.py runserver
	
	After this open http://localhost:8000/main/

    access token: (Your access token from https://developers.facebook.com/tools/explorer with permission for read_stream)
    keyword: (the keyword you want to search for)

todo:
------
*  Improve the aesthetics.

