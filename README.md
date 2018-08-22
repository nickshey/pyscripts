# Python Scripts
I am using an Anaconda environment and my main IDE is Spyder, which is part of the Anaconda package. Most of packages I use within my scripts are included in the Anaconda package. For any packages not included, you can run `conda install <package name>` to add it to your environment.
```bash
python -V
Python 3.6.3 :: Anaconda custom (64-bit)
```

### twitterViz
This script takes in a twitter handle as a command line parameter and generates a Plotly graph that shows your favorites and retweets in a stacked bar graph. I took out all of the tweets that a user retweeted, because that is not the user's original content so it is not representative of how well your original tweets do graphically. If you just want to see what this looks like, check out [my stats](https://plot.ly/~nickshey/26/favorites-vs-retweets/#/). If you have a lot of tweets, this script is gonna take a while because the Twitter API is pretty slow. Also, due to Tweepy's constraints, all of your tweets may not be represented if you have too many.
```python
python twitterViz.py <Twitter username>
```

### getLyrics
This script links to your Spotify account using Spotify's API and returns the lyrics to the current song you are listening to using the Genius API. (You'll need to set up a credentials file with access tokens for the APIs)
```bash
python getLyrics.py
```

### powellBot
I was bored one day so I made a script using pyautogui that just opens up Chrome and pulls up a pic of my ECE professor. Epitome of hardcoding.
```bash
python powellBot.py
```

### mapit
This script takes in a street address as a command line argument and opens up a Google Maps page with directions to that address
```bash
python mapit.py <street address>
```

### lucky
This script takes in a Google search as a command line parameter and opens up the first 5 pages that show up for that search
```bash
python lucky.py <search term>
```

### ResistorCapacitorRatios
Simple script to find working resistor and capacitor values for a certain time constant
```bash
python ResistorCapacitorRatios.py
```

### SoccerTeams
Made to help my friends and I find random teams in the top 5 leagues of Europe to root for
```bash
python SoccerTeams.py
```
