# Spotflock Studio SDK (Python)

[![](https://studio.spotflock.com/static/img/logo-high.png)](https://studio.spotflock.com)
Spotflock Studio renders a comprehensive spectrum of solutions that can be accessed by users on-demand from our pool of transformational technologies.

### Installation

Spotflock Studio SDK requires Python 3.5 + . Go to https://studio.spotflock.com and create an app. On creation of an app, you will get an API Key.

```sh
import studio
client = studio.StudioClient('API Key')
response = c.sentiment_analysis('I am feeling good.')
print(response)
```

For more details, visit https://studio.spotflock.com