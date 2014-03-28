<?php
	$data = file_get_contents("https://graph.facebook.com/870175569_10153929919780570?fields=likes.fields(pic_square,name).limit(100),comments&access_token=access_token_here"); //change the access token here
	$likes = json_decode($data);
	$real_likes = $likes->likes->data;
	$no = count($real_likes);
	for($i=0; $i<$no; $i++) {
		echo $real_likes[$i]->name;
	}
	
?>