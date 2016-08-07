import praw
import os

def authorize():
    UA = 'made for testing, contact me at sergey.paramonov@phystech.edu'

    r = praw.Reddit(UA)

    client_id     = os.environ['BOTID']
    client_secret = os.environ['REDDITSECRET']
    redirect_uri  = 'http://127.0.0.1:65010/authorize_callback'

    r.set_oauth_app_info(client_id     = client_id,
                         client_secret = client_secret,
                         redirect_uri  = redirect_uri)

    r.refresh_access_information(os.environ['AUTHTOKEN'])

    authenticated_user = r.get_me()
    print("bot " + authenticated_user.name + " is authorized")
    return r, authenticated_user

r, user = authorize()

submissions = list(r.get_subreddit('videos').get_hot(limit=10))

print(submissions)



