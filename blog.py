import requests

class Blogs():

    def __init__(self):
        self.blog_api_endpoint = "https://api.npoint.io/e2c3d27dfa84356b27ef"
    
    def get_all_blog_data(self):
        response = requests.get(url=self.blog_api_endpoint)
        return response.json()