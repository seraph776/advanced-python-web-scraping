# ∞ Infinite Scroll

Nowadays, more and more websites start to use `infinite scrolling` to replace the classic pagination. In reality, there is a pagination in an infinite scrolling page, but it is hidden in the HTML code. On a classic page, the user clicks on the next page URL whereas here, the next page is called dynamically when you visit the end area of the webpage. When user scroll to the bottom of the web pages, javascript will send HTTP request and load new items automatically. You can see `infinite scrolling` in most e-commerce website and blogs.


## Analyze the Web Page


First, visit [Quotes to Scrape - Infinite Scroll](https://quotes.toscrape.com/scroll). Open the `Developer Tools`  of our browser to help inspect the web traffic of the website. Then go to `Network` tab, and make sure `Disable Cache`, `Persisit Logs`,  and  `XHR` is selected.



![image](https://user-images.githubusercontent.com/72005563/196279322-886dbc72-f7e5-4f5a-94d3-7c5ceff7c23d.png)

> 👉 **Note**: the requests we’re interested in will be in the XHR filter.

You can see all real time requests the browser is making. As you scroll down, you can see the requests pop up in the panel. You need to find the URL that javascript used to get the data. When you select a request, you can see its information such as `URL`, `HTTP method`, and `headers`.

![image](https://user-images.githubusercontent.com/72005563/196279653-aca3ccb2-7662-49b3-97fc-9eea77597591.png)

You can also see the data is structured within a `json` reposnse object.

![image](https://user-images.githubusercontent.com/72005563/196279910-1c7af758-9cbd-44b4-a024-027ee4f7e174.png)


## Requests API endpoint

Make a requests to the URL that the javascript is requesting, and extract the data using a `json` parser. 


```python
from requests_html import HTMLSession

session = HTMLSession()

url = 'http://quotes.toscrape.com/api/quotes?page=2'

page = session.get(url)
print(page.json())

#  {'has_next': True, 'page': 2, 'quotes': [{'author': {'goodreads_link': '/author/show/82952.Marilyn_Monroe', 'name': 'Marilyn Monroe', 'slug': 'Marilyn-Monroe'}, 'tags': ['friends', 'heartbreak', 'inspirational', 'life', 'love', 'sisters'], 'text': "“This life is what you make it. No matter what, you're going to mess up sometimes, it's a universal truth. But the good part is you get to decide how you're going to mess it up. Girls will be your friends - they'll act like it anyway. But just remember, some come, some go. The ones that stay with you through everything - they're your true best friends. Don't let go of them. Also remember, sisters make the best friends in the world. As for lovers, well, they'll come and go too. And baby, I hate to say it, most of them - actually pretty much all of them are going to break your heart, but you can't give up because if you give up, you'll never find your soulmate. You'll never find that half who makes you whole and that goes for everything. Just because you fail once, doesn't mean you're gonna fail at everything. Keep trying, hold on, and always, always, always believe in yourself, because if you don't, then who will, sweetie? So keep your head high, keep your chin up, and most importantly, keep smiling, because life's a beautiful thing and there's so much to smile about.”"}, {'author': {'goodreads_link': '/author/show/1077326.J_K_Rowling', 'name': 'J.K. Rowling', 'slug': 'J-K-Rowling'}, 'tags': ['courage', 'friends'], 'text': '“It takes a great deal of bravery to stand up to our enemies, but just as much to stand up to our friends.”'}, {'author': {'goodreads_link': '/author/show/9810.Albert_Einstein', 'name': 'Albert Einstein', 'slug': 'Albert-Einstein'}, 'tags': ['simplicity', 'understand'], 'text': "“If you can't explain it to a six year old, you don't understand it yourself.”"}, {'author': {'goodreads_link': '/author/show/25241.Bob_Marley', 'name': 'Bob Marley', 'slug': 'Bob-Marley'}, 'tags': ['love'], 'text': "“You may not be her first, her last, or her only. She loved before she may love again. But if she loves you now, what else matters? She's not perfect—you aren't either, and the two of you may never be perfect together but if she can make you laugh, cause you to think twice, and admit to being human and making mistakes, hold onto her and give her the most you can. She may not be thinking about you every second of the day, but she will give you a part of her that she knows you can break—her heart. So don't hurt her, don't change her, don't analyze and don't expect more than she can give. Smile when she makes you happy, let her know when she makes you mad, and miss her when she's not there.”"}, {'author': {'goodreads_link': '/author/show/61105.Dr_Seuss', 'name': 'Dr. Seuss', 'slug': 'Dr-Seuss'}, 'tags': ['fantasy'], 'text': '“I like nonsense, it wakes up the brain cells. Fantasy is a necessary ingredient in living.”'}, {'author': {'goodreads_link': '/author/show/4.Douglas_Adams', 'name': 'Douglas Adams', 'slug': 'Douglas-Adams'}, 'tags': ['life', 'navigation'], 'text': '“I may not have gone where I intended to go, but I think I have ended up where I needed to be.”'}, {'author': {'goodreads_link': '/author/show/1049.Elie_Wiesel', 'name': 'Elie Wiesel', 'slug': 'Elie-Wiesel'}, 'tags': ['activism', 'apathy', 'hate', 'indifference', 'inspirational', 'love', 'opposite', 'philosophy'], 'text': "“The opposite of love is not hate, it's indifference. The opposite of art is not ugliness, it's indifference. The opposite of faith is not heresy, it's indifference. And the opposite of life is not death, it's indifference.”"}, {'author': {'goodreads_link': '/author/show/1938.Friedrich_Nietzsche', 'name': 'Friedrich Nietzsche', 'slug': 'Friedrich-Nietzsche'}, 'tags': ['friendship', 'lack-of-friendship', 'lack-of-love', 'love', 'marriage', 'unhappy-marriage'], 'text': '“It is not a lack of love, but a lack of friendship that makes unhappy marriages.”'}, {'author': {'goodreads_link': '/author/show/1244.Mark_Twain', 'name': 'Mark Twain', 'slug': 'Mark-Twain'}, 'tags': ['books', 'contentment', 'friends', 'friendship', 'life'], 'text': '“Good friends, good books, and a sleepy conscience: this is the ideal life.”'}, {'author': {'goodreads_link': '/author/show/276029.Allen_Saunders', 'name': 'Allen Saunders', 'slug': 'Allen-Saunders'}, 'tags': ['fate', 'life', 'misattributed-john-lennon', 'planning', 'plans'], 'text': '“Life is what happens to us while we are making other plans.”'}], 'tag': None, 'top_ten_tags': [['love', 14], ['inspirational', 13], ['life', 13], ['humor', 12], ['books', 11], ['reading', 7], ['friendship', 5], ['friends', 4], ['truth', 4], ['simile', 3]]}
```

## Load JSON string into a Dictionary

Use `json.loads` to load the json `response` string into a `diction` object:

```python
from requests_html import HTMLSession

session = HTMLSession()

url = 'http://quotes.toscrape.com/api/quotes?page=2'

page = session.get(url)
json_obj = json.loads(page.text)

data = json_obj.keys()
print(data) 

# dict_keys(['has_next', 'page', 'quotes', 'tag', 'top_ten_tags'])
```

Lets start by reading the quotes:

```python
print(data['quotes'])

# [{'author': {'goodreads_link': '/author/show/82952.Marilyn_Monroe', 'name': 'Marilyn Monroe', 'slug': 'Marilyn-Monroe'}, 'tags': ['friends', 'heartbreak', 'inspirational', 'life', 'love', 'sisters'], 'text': "“This life is what you make it. No matter what, you're going to mess up sometimes, it's a universal truth. But the good part is you get to decide how you're going to mess it up. Girls will be your friends - they'll act like it anyway. But just remember, some come, some go. The ones that stay with you through everything - they're your true best friends. Don't let go of them. Also remember, sisters make the best friends in the world. As for lovers, well, they'll come and go too. And baby, I hate to say it, most of them - actually pretty much all of them are going to break your heart, but you can't give up because if you give up, you'll never find your soulmate. You'll never find that half who makes you whole and that goes for everything. Just because you fail once, doesn't mean you're gonna fail at everything. Keep trying, hold on, and always, always, always believe in yourself, because if you don't, then who will, sweetie? So keep your head high, keep your chin up, and most importantly, keep smiling, because life's a beautiful thing and there's so much to smile about.”"}, {'author': {'goodreads_link': '/author/show/1077326.J_K_Rowling', 'name': 'J.K. Rowling', 'slug': 'J-K-Rowling'}, 'tags': ['courage', 'friends'], 'text': '“It takes a great deal of bravery to stand up to our enemies, but just as much to stand up to our friends.”'}, {'author': {'goodreads_link': '/author/show/9810.Albert_Einstein', 'name': 'Albert Einstein', 'slug': 'Albert-Einstein'}, 'tags': ['simplicity', 'understand'], 'text': "“If you can't explain it to a six year old, you don't understand it yourself.”"}, {'author': {'goodreads_link': '/author/show/25241.Bob_Marley', 'name': 'Bob Marley', 'slug': 'Bob-Marley'}, 'tags': ['love'], 'text': "“You may not be her first, her last, or her only. She loved before she may love again. But if she loves you now, what else matters? She's not perfect—you aren't either, and the two of you may never be perfect together but if she can make you laugh, cause you to think twice, and admit to being human and making mistakes, hold onto her and give her the most you can. She may not be thinking about you every second of the day, but she will give you a part of her that she knows you can break—her heart. So don't hurt her, don't change her, don't analyze and don't expect more than she can give. Smile when she makes you happy, let her know when she makes you mad, and miss her when she's not there.”"}, {'author': {'goodreads_link': '/author/show/61105.Dr_Seuss', 'name': 'Dr. Seuss', 'slug': 'Dr-Seuss'}, 'tags': ['fantasy'], 'text': '“I like nonsense, it wakes up the brain cells. Fantasy is a necessary ingredient in living.”'}, {'author': {'goodreads_link': '/author/show/4.Douglas_Adams', 'name': 'Douglas Adams', 'slug': 'Douglas-Adams'}, 'tags': ['life', 'navigation'], 'text': '“I may not have gone where I intended to go, but I think I have ended up where I needed to be.”'}, {'author': {'goodreads_link': '/author/show/1049.Elie_Wiesel', 'name': 'Elie Wiesel', 'slug': 'Elie-Wiesel'}, 'tags': ['activism', 'apathy', 'hate', 'indifference', 'inspirational', 'love', 'opposite', 'philosophy'], 'text': "“The opposite of love is not hate, it's indifference. The opposite of art is not ugliness, it's indifference. The opposite of faith is not heresy, it's indifference. And the opposite of life is not death, it's indifference.”"}, {'author': {'goodreads_link': '/author/show/1938.Friedrich_Nietzsche', 'name': 'Friedrich Nietzsche', 'slug': 'Friedrich-Nietzsche'}, 'tags': ['friendship', 'lack-of-friendship', 'lack-of-love', 'love', 'marriage', 'unhappy-marriage'], 'text': '“It is not a lack of love, but a lack of friendship that makes unhappy marriages.”'}, {'author': {'goodreads_link': '/author/show/1244.Mark_Twain', 'name': 'Mark Twain', 'slug': 'Mark-Twain'}, 'tags': ['books', 'contentment', 'friends', 'friendship', 'life'], 'text': '“Good friends, good books, and a sleepy conscience: this is the ideal life.”'}, {'author': {'goodreads_link': '/author/show/276029.Allen_Saunders', 'name': 'Allen Saunders', 'slug': 'Allen-Saunders'}, 'tags': ['fate', 'life', 'misattributed-john-lennon', 'planning', 'plans'], 'text': '“Life is what happens to us while we are making other plans.”'}]
```

Let's gather some more information:

```python
print(data['quotes'][0]['author'])
print(data['quotes'][0]['author']['name'])
print(data['quotes'][0]['text'])
print(data['quotes'][0]['tags'])

#  {'goodreads_link': '/author/show/82952.Marilyn_Monroe', 'name': 'Marilyn Monroe', 'slug': 'Marilyn-Monroe'}
#  Marilyn Monroe
#  “This life is what you make it. No matter what, you're going to mess up sometimes, it's a universal truth. But the good part is you get to decide how you're going to mess it up. Girls will be your friends - they'll act like it anyway. But just remember, some come, some go. The ones that stay with you through everything - they're your true best friends. Don't let go of them. Also remember, sisters make the best friends in the world. As for lovers, well, they'll come and go too. And baby, I hate to say it, most of them - actually pretty much all of them are going to break your heart, but you can't give up because if you give up, you'll never find your soulmate. You'll never find that half who makes you whole and that goes for everything. Just because you fail once, doesn't mean you're gonna fail at everything. Keep trying, hold on, and always, always, always believe in yourself, because if you don't, then who will, sweetie? So keep your head high, keep your chin up, and most importantly, keep smiling, because life's a beautiful thing and there's so much to smile about.”
#  ['friends', 'heartbreak', 'inspirational', 'life', 'love', 'sisters']
```
