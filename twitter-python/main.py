import twitter

api = twitter.Api()

api = twitter.Api(consumer_key='inset your key here',
                      consumer_secret='insert your key here',
                      access_token_key='insert your key here',
                      access_token_secret='insert your key here')

random_stater = ["A ", "The "]
random_second = ["Box ", "Apple ", "Bluebird ", "North Korean ", "Donnie Trump ", "Theresa May "]
random_third = ["walked ", "jumped ", "ran ", "flew "]
random_fourth = ["herself ", "himself ", "themself "]
random_fith = ["to the White House.", "to the chippy", "to the pub", "to the off licence."]

print("welcome to twitter app. what you want to do?")
while True:
    print("A: Send status message! B: Make a new friend! C: Send a random message! D: List friends! E: See a User's id!")
    user_action = raw_input(": ")

    if user_action == "A":
        text_to_send = raw_input("Type in message: ")

        status = api.PostUpdate(text_to_send)
        time.sleep(1)
        print(status.text)


    elif user_action == "B":
        print("What is the user id of the person you want to follow? The uid must be perfect, or it wont work!")
        user_follow = raw_input(": ")
        api.CreateFriendship(user_follow)
        friend_list = api.GetFriends()

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

    elif user_action == "D":
        friend_list_2 = api.GetFriends()
        print(friend_list_2)

    elif user_action == "E":
        print(" ")
        #working on it


    elif user_action != "A" or user_action != "B" or user_action != "C" or user_action != "D" or user_action != "E":
        print("That is not an option. Please choose something else.")
        time.sleep(1)
