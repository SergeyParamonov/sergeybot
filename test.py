import praw
import os

UA = 'made for testing, contact me at sergey.paramonov@phystech.edu'

r = praw.Reddit(UA)


client_id     = os.environ['BOTID']
client_secret = os.environ['REDDITSECRET']
redirect_uri  = 'http://127.0.0.1:65010/authorize_callback'

r.set_oauth_app_info(client_id     = client_id,
                      client_secret = client_secret,
                      redirect_uri  = redirect_uri)

# url = r.get_authorize_url('uniqueKey', 'identity read submit', True)
# import webbrowser
# webbrowser.open(url)

#access_information = r.get_access_information('put key here')
r.set_access_credentials(**access_information)
print(access_information['refresh_token'])
#authenticated_user = r.get_me()
#r.login('templatebot', os.environ['TEMPLATEBOTPASS'], disable_warning=True)
#print(authenticated_user.name, authenticated_user.link_karma)
#r.refresh_access_information(access_information['refresh_token'])




