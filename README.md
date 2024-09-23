# Python Tweet Generator
Fake tweet screenshot generator made in python using the `selenium` library. Customizable infomation fields and easy implementation into other scripts. As of writing this is in very early beta and lacks a lot of features, I will be improving and optimising this in the future.

\
<img src="https://raw.githubusercontent.com/reckedpr/python-tweet/refs/heads/main/images/tweet-preview.png" width="90%" alt="Fake @elonmusk tweet">

## Features
- Edit name and handle
- Easy to change pfp
- Compatible with discord api wrappers
- Easy implementation into projects

## How to use
### 1. Clone or Download the repo
```bash
git clone https://github.com/reckedpr/python-menu
```
#### OR:
![Static Badge](https://img.shields.io/badge/download%20repo-29903b?style=for-the-badge&logoColor=white&link=https%3A%2F%2Fgithub.com%2Freckedpr%2Fpython-menu%2Farchive%2Frefs%2Fheads%2Fmain.zip)

### 2. Open `tweetGenerator.py`
```python
# Command usage

generateTweet(handle, name, tweet_text, avatar)
```
All parameters are to be strings, avatar must refer to a direct image link

#### Example:

```python
generateTweet(
    'elonmusk',
    'Elon Fucking Musk',
    'reckedpr is an absolute legend, holy shit',
    'https://d1kd6h2y8iq4lp.cloudfront.net/avatars/elonmusk'
)
```

