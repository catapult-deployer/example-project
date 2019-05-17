class Recipe:
    def __init__(self, storage, paths):
        self.storage = storage
        self.paths = paths

    def after_configuring(self, bullet):
        bullet.local('npm install')
        bullet.local('npm run build')
