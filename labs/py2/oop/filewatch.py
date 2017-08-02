import os
import time

class FileWatcher(object):
	def __init__(self, path_of_file_to_watch):
		self.path = path_of_file_to_watch
		self.subscribers = set()
		# self.observe_file_size()

	def register(self, who):
		self.subscribers.add(who)

	def unregister(self, who):
		self.subscribers.discard(who)

	def observe_file_size(self):
		size = os.stat(self.path).st_size
		time.sleep(5)
		while True:
			new_size = os.stat(self.path).st_size
			if new_size > size:
				print "New size is {}".format(new_size)
				for subscriber in self.subscribers:
					subscriber.update(new_size)
				size = new_size
			else: print "No changes"
			time.sleep(5)

class FileObserver(object):
	def __init__(self, name):
		self.name = name

	def update(self, message):
		print('{} noticed that the file is now {} bytes'.format(self.name, message))

bob = FileObserver("bob")
john = FileObserver("john")
stacy = FileObserver("stacy")

watcher = FileWatcher("/Users/fichel/Documents/Training/courseware-btb/labs/py2/oop/filewatch-lab.txt")
watcher.register(bob)
watcher.register(john)
watcher.register(stacy)

watcher.observe_file_size()