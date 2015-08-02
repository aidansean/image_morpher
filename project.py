from project_module import project_object, image_object, link_object, challenge_object

p = project_object('image_morpher', 'Image morpher')
p.domain = 'http://www.aidansean.com/'
p.path = 'image_morpher'
p.preview_image    = image_object('%s/images/project.jpg'   %p.path, 150, 250)
p.preview_image_bw = image_object('%s/images/project_bw.jpg'%p.path, 150, 250)
p.folder_name = 'aidansean'
p.github_repo_name = 'image_morpher'
p.mathjax = False
p.tags = 'Frivolous'
p.technologies = 'canvas,HTML,JavaScript'
p.links.append(link_object(p.domain, 'image_morpher/', 'Live page'))
p.introduction = '<tt>*.gif</tt> images have been around for a long time, but this is something a bit different.  It takes an array of images and changes between them randomly with random intervals of time.'
p.overview = '''The canvas is used to load images and switch between them.  The time interval is determined randomly, and images are selected at random, so this differs from the traditional .gif images in a fundamental way.'''
