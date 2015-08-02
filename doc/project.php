<?php
include_once($_SERVER['FILE_PREFIX']."/project_list/project_object.php") ;
$github_uri   = "https://github.com/aidansean/image_morpher" ;
$blogpost_uri = "http://aidansean.com/projects/?tag=image_morpher" ;
$project = new project_object("image_morpher", "Image morpher", "https://github.com/aidansean/image_morpher", "http://aidansean.com/projects/?tag=image_morpher", "image_morpher/images/project.jpg", "image_morpher/images/project_bw.jpg", "<tt>*.gif</tt> images have been around for a long time, but this is something a bit different.  It takes an array of images and changes between them randomly with random intervals of time.", "Frivolous", "canvas,HTML,JavaScript") ;
?>