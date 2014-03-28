<?php
	$data = file_get_contents("https://graph.facebook.com/870175569_10153929919780570?fields=likes.fields(pic_square,name).limit(100),comments&access_token=CAACEdEose0cBAIYeLOKY3vYcfbr0jmXBUFmKw2LTGwlYZCWz27ROZBxxKpR87K166OPFsPYql9hpUZCSRRzTlbE9T0BIScpr2J4ZAfWeYcjmIvzxOTMjl3ngA1WVu7zsiXmB5na3wm2MrkN4Sljf6jp5VXnAQIqbxrmZC9U4FZBjUkdZCyz6vXmv0HrBhIeqbQZD");
	$likes = json_decode($data);
	$real_likes = $likes->likes->data;
	$no = count($real_likes);
	for($i=0; $i<$no; $i++) {
		echo $real_likes[$i]->name;
	}
	
?>