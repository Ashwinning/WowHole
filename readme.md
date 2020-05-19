# WowHole
This project helps us track quote tweets for 'Wow', tweeted by [@fnthawar](https://twitter.com/fnthawar/status/1261787165719232514)

![](https://i.snipboard.io/yp1vTK.jpg)

It could be used to track quote tweets for any tweet for that matter.

## How does it work?

- We use the [Twitter API](https://developer.twitter.com/en/docs) to [search]() for tweets, and [recursively](https://en.wikipedia.org/wiki/Recursion_(computer_science)) create a tree of all the tweets.
- We save every tweet in the `tweets/` subdirectory with the filename format `{id}.json`.
- Then, we go through all of our saved tweets and create a CSV file, storing information about the tweets, and all the relationships/references (`refs`) of 'who quoted whom'.
- We upload this CSV file to draw.io, to let it handle all the heavylifting of drawing our hierarchy tree and displaying data.

## How to use it

Clone this repository or download the source code
> We use `pipenv` to manage dependencies : https://pipenv.pypa.io/en/latest/ and `tweepy`, the beautiful python library which helps us interact with the Twitter API : http://www.tweepy.org/  

Get into the pipenv environment
```bash
pipenv shell
```
> `app.py` uses Tweepy as a dependency to authenticate us with the Twitter API, then starts recursively searching for the entire chain of quoted tweets, and starts saving them to the `tweets/` folder

Create a file next to `app.py` called `config.py` and populate it with the following code, and replace the strings with your twitter credentials.
```python
consumer_key = 'consumer_key'
consumer_secret = 'consumer_secret'
access_token = 'access_token'
access_token_secret = 'access_token_secret'
```

If a `tweets` subdirectory does not already exist next to app.py, please create it manually

Run:
```bash
python app.py
```
> To avoid hitting twitter [rate limits](https://developer.twitter.com/en/docs/tweets/search/api-reference/get-search-tweets#resource-information), this will only call the twitter search function once every 5 seconds, and may take a very long time to save all tweets depending upon how popular your tweethole is.

Once your app.py function stops running, run:
```bash
python generateHierarchy.py
```

> This won't take too long to run. `generateHierarchy.py` goes through all the tweets in the `tweets/` folder, and creates a file called `data.csv`, which contains all the quote-tweets and their relationships. `data.csv` can now be uploaded to draw.io

> Draw.io offers _not the nicest_ way, to [upload a CSV file and create a diagram out of it](https://drawio-app.com/automatically-create-draw-io-diagrams-from-csv-files/). While it may _not be the nicest_, it is still extremely powerful and saves us a lot of coding and hassle, plus gives us a _pleasant_ visual interface to edit & publish things!

Go to draw.io

Insert a CSV by going to `Arrange -> Insert -> Advanced -> CSV`
![](https://i.snipboard.io/DH4BUY.jpg)

Replace the default code with the template from `layout.csv`

Now copy the contents from `data.csv` and paste them into the box below the contents which were just pasted from `layout.csv`.

⏳ Wait for draw.io to generate our chart.

> Draw.io might throw some errors about invalid characters, like `'`, `"`, `\`, etc., which it won't accept. When this happens, it'll throw a line number and surrounding text as well. You may `Ctrl / Cmd + F` to find the surrounding text and then replace the offending characters. 

Once, the items appear, use `Ctrl / Cmd + A` to select all items, and then you can play around with the various layout settings which draw.io provides under `Arrange -> Layout`.
![](https://i.snipboard.io/HVKgNG.jpg)



