import twitter

api = twitter.Api()

api = twitter.Api(consumer_key='inset your key here',
                      consumer_secret='insert your key here',
                      access_token_key='insert your key here',
                      access_token_secret='insert your key here')



print("welcome to twitter app. what you want to do?")
random_stater = ["A ", "The "]
random_second = ["Box ", "Apple ", "Bluebird ", "North Korean "]
random_third = ["walked ", "jumped ", "ran ", "flew "]
random_fourth = ["herself ", "himself ", "themself "]
random_fith = ["to the White House.", "to the chippy", "to the pub", "to the off lincese."]

print("welcome to twitter app. what you want to do?")
while True:
    print("A: Send status message. B: Make a new friend! C: Send a random message!")
    user_action = raw_input(": ")

    if user_action == "A":
        text_to_send = raw_input("Type in message: ")

        status = api.PostUpdate(text_to_send)
        time.sleep(1)
        print(status.text)


    elif user_action == "B":
        print("not working")
        time.sleep(1)


    elif user_action == "C":
        one = (random.choice(random_stater))
        two = (random.choice(random_second))
        three = (random.choice(random_third))
        four = (random.choice(random_fourth))
        five =  (random.choice(random_fith))
        status = api.PostUpdate(one + two + three + four + five)
        print(status.text)
        time.sleep(1)


    elif user_action != "A" or user_action != "B" or user_action != "C":
        print("That is not an option. Please choose something else.")
        time.sleep(1)

