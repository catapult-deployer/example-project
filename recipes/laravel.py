class Recipe:
    def __init__(self, storage, paths):
        self.storage = storage
        self.paths = paths

    def after_configuring(self, bullet):
        bullet.console("local composer install")
        bullet.local("composer install")

    def after_releasing(self, bullet):
        bullet.remote("all", "composer install")

    def after_maintaining(self, bullet):
        bullet.console("maintain composer install")
        bullet.remote("maintain", "composer install")

        bullet.console("maintain clear cache")
        bullet.remote("maintain", "./artisan cache:clear")
        bullet.remote("maintain", "./artisan config:clear")
        bullet.remote("maintain", "./artisan config:cache")

        bullet.console("maintain migrate")
        bullet.maintain([
            "./artisan migrate"
        ])

    def after_installing(self, bullet):
        bullet.remote("all", "./artisan cache:clear")
        bullet.remote("all", "./artisan config:clear")
        bullet.remote("all", "./artisan config:cache")

