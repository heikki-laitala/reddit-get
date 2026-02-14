# Reddit Get
![Reddit-Get Integration](https://github.com/mikelane/reddit-get/workflows/Reddit-Get%20Integration/badge.svg)
[![codecov](https://codecov.io/gh/mikelane/reddit-get/branch/main/graph/badge.svg)](https://codecov.io/gh/mikelane/reddit-get)

This is a Python CLI that will pull posts from Reddit. In order to use this CLI, you'll need to set up a
Reddit app of your own so that you can authenticate into Reddit with your own credentials. Never fear,
this process is pretty straight forward.

## Installation

Requires Python 3.11 or later.

```shell
# Install directly from GitHub
pip install git+https://github.com/heikki-laitala/reddit-get.git

# Or from a local clone
pip install /path/to/reddit-get

# Or editable install for development
pip install -e /path/to/reddit-get
```

After installation, the `reddit-get` command is available in your shell. You also need to set up Reddit API credentials — see below.

### Create a Reddit Application

1. Navigate to https://reddit.com/prefs/apps
1. Click `create an app`
1. You should see something like this:

    ![create an app form](assets/create_an_app_form.png)

1. You can then fill this form out with some values like these (choose whatever you like):

    ![create an app form filled](assets/create_an_app_form_filled.png)

After that, you'll need to find the `client_id` and `client_secret` for your new app and insert those into 
a configuration file on your system.

### Adding a Reddit-Get Config File

1. Create a file in your home directory called `.redditgetrc` (currently this is the default name and is 
   only configurable when you call the script each time, so this name is probably for the best for now)
1. Make your reddit config file look like this:

    ```toml
   [reddit-get]
   client_id = "<your client id here>"
   client_secret = "<your client secret here>"
   user_agent = "<anything, e.g. My super awesome cli app by u/pm_me_myour_apps>" 
   username = "<your reddit username>"
   password = "<your reddit password>"
   ```

Once this is set up, you should be good to go.

## Commands

### `post` — Get post titles

Fetch post titles from a subreddit with customizable sorting, time filtering, and output formatting.

```shell
$ reddit-get post --subreddit showerthoughts --post_sorting top --limit 10 --time_filter all
```

Example output:

```
#### The Top Posts for All Time from r/showerthoughts
- Whoever created the tradition of not seeing the bride in the wedding dress beforehand saved countless husbands everywhere from hours of dress shopping and will forever be a hero to all men.
- We laugh at dogs getting excited when they hear a bark on TV, but if TV was a nonstop stream of unintelligible noises and then someone suddenly spoke to you in your language, you'd be pretty fucking startled too.
- When you're a kid, you don't realize you're also watching your mom and dad grow up.
```

For more options:

```shell
$ reddit-get post --help
```

### `post-count` — Count posts on a date

Count how many posts were made in a subreddit on a specific date. Fetches up to 1000 recent posts and filters by date, so this works best for recent dates.

```shell
$ reddit-get post-count --subreddit showerthoughts --date 2025-01-15
```

Example output:

```
r/showerthoughts had 42 post(s) on 2025-01-15
```

### `stats` — Get subreddit statistics

Retrieve metadata and statistics for a subreddit.

```shell
$ reddit-get stats --subreddit showerthoughts
```

Example output:

```
Subreddit: r/showerthoughts
Subscribers: 25,000,000
Active Users: 10,000
Type: public
NSFW: No
Created: 2011-07-18
Description: A subreddit for sharing those miniature epiphanies you have...
```

### `config-location` — Show config file path

```shell
$ reddit-get config-location
```

---

Enjoy! This is early stages, so I'll be adding more features as time goes on.
