Unfortunately, this repository is no longer functioning as expected. \
Google made it so that running the token in the browser no longer bypasses the recaptcha as it used to 

This repo was intended to work as a Chrome extension however due to the above reasons this has been discontinued. 

The way this repo works is that when there is a recaptcha html element found, it will send the webpage url to the backend, which will then open up a new browser, complete the recaptcha using the google cloud speech api (if applicable), and then return the token granted to the user. The token is granted to everyone who completes the reCaptcha and it's how many popular services do this. Then, the user get's the token, and it was supposed to be used to solve the reCaptcha however they made it so that it's no longer possible to do this. 

If you are interested in running this, run 

```python3 app.py```

Then, add the JS files to a chrome extension and head over to a page that has a recaptcha and where you don't need to log in. 
