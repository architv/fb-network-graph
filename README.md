fb-network-graph
================================
       
Usage:
----------
**fb-network-graph**  crawls any public [facebook](https://www.facebook.com/) post using the [FB graph api](https://developers.facebook.com/docs/graph-api/) for a "keyword" and then plots a graph for the likes and comments for the keyword.

	$ python data.py

    access token: (Your access token from [here](https://developers.facebook.com/tools/explorer) with permission for read_stream.
    post id: (id of the post whose graph is to be drawn)
    
    After this open index.html

todo:
------
*  Draw the graph for all posts which contain a particular keyword.
*  Grab the access token by itself.

