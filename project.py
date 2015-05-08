from project_module import project_object, image_object, link_object, challenge_object

p = project_object('image_morpher', 'Image morpher')
p.domain = 'http://www.aidansean.com/'
p.path = 'image_morpher'
p.preview_image_ = image_object('http://placekitten.com.s3.amazonaws.com/homepage-samples/408/287.jpg', 408, 287)
p.github_repo_name = 'image_morpher'
p.mathjax = False
p.links.append(link_object(p.domain, 'image_morpher/', 'Live page'))
p.introduction = '*.gif images have been around for a long time, but this is something a bit different.  It takes an array of images and changes between them randomly with random intervals of time.'
p.overview = '''The canvas is used to load images and switch between them.  The time interval is determined randomly, and images are selected at random, so this differs from the traditional .gif images in a fundamental way.'''
