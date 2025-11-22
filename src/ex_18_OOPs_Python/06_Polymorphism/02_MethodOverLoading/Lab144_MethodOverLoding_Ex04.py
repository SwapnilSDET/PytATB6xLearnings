# In case of method overloading,
# when a function is available with same name but with additional parameters
# - then the function with max parameters will be used.

class Browser:

    def make_http_request(self, url): # This will become redundant
        print("Hi, Lets make the HTTP request without auth", url)

    def make_http_request(self, url, auth=None): # This will be in use due to extra parameters
        print("Hi, Lets make the HTTP request with auth", url, auth)

t = Browser()
t.make_http_request("google.com","admin")