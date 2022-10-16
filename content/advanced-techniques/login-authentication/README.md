<div id="top"  align="center">

# Login Authentication

</div>



[Quotes to Scrape Login In](http://quotes.toscrape.com/login)

Check the source of the login form to get three pieces of information:

- The `url` that the form posts to. In this exampe `/login`
- The form `attributes`. In this example, they are `username`, and `password`, and `csrf_token`.


![image](https://user-images.githubusercontent.com/72005563/194976938-21fbb668-0d09-46d4-be31-c5f66aa057e4.png)


Once you've got that, you can use a `HTTPSession()` instance to make a `post` request to the `login url` with your 
login credentials as a `payload`. Making requests from a session instance is essentially the same as using requests normally,
it simply adds persistence, allowing you to store and use cookies etc.


```python
from requests_html import HTMLSession
from config import username, password


def login(user_name, pass_word, login_url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0'}

    # check the source of the login form to get the name attributes
    # of the username and password fields.
    login_data = {
        'csrf_token': '',
        'username': username,
        'password': password,
    }
    with HTMLSession() as session:
        r = session.get(login_url)
        login_data['csrf_token'] = r.html.find('input', first=True).attrs['value']
        r = session.post(login_url, data=login_data, headers=headers)
        return session


LOGIN_URL = 'http://quotes.toscrape.com/login'
SECURE_URL = 'http://quotes.toscrape.com'

session = login(username, password, LOGIN_URL)

page = session.get(SECURE_URL)
print(r.html.html)
```



<div align="right">

[[↑] Back to top](#top)

</div> 

