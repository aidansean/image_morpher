<?php
$title = 'Image morpher' ;
$stylesheets = array('style.css') ;
$js_scripts  = array('functions.js') ;
include($_SERVER['FILE_PREFIX'] . '/_core/preamble.php') ;
?>
  <div class="right">
    <h3>Image morpher</h3>
      <div class="blurb">
		<p>This page morphs images.  You're welcome.</p>
		<img id="img_morphing" src="images/edith1.jpg" width="750px" height="497px" alt=""/>
	  </div>
    </div>

<?php foot() ; ?>
