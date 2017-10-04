import twitter

api = twitter.Api()

api = twitter.Api(consumer_key='inset your key here',
                      consumer_secret='insert your key here',
                      access_token_key='insert your key here',
                      access_token_secret='insert your key here')



print("welcome to twitter app. what you want to say?")

text_to_send = raw_input(": ")

status = api.PostUpdate(text_to_send)

print(status.text)
