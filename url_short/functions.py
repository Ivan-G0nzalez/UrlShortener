import shortuuid
from .models import Url

class ValidUrls:
    def __init__(self, url):
        self.url = url
    
    def start_with_http_or_https(self):
        return self.url.startswith(('http://', 'https://'))

class ValidName:
    def __init__(self, name):
        self.name = name

    def ensure_length(self):
      
        if len(self.name) < 6:
            needed = 6 - len(self.name)
            self.name += shortuuid.ShortUUID().random(length=needed)

    def confirm_that_it_does_not_exist(self):
        if Url.objects.filter(shortcode=self.name).exists():
            return False
        return True

    def execute_validation(self):
        self.ensure_length()
        if self.confirm_that_it_does_not_exist():
           
            return self.name
        