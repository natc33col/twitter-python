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
    print("A: Send status message! B: Make a new friend! C: Send a random message! D: List friends! E: Direct message someone! F: Check for new friends! Quit to quit.")
    user_action = raw_input(": ")

    if user_action == "A":
        text_to_send = raw_input("Type in message: ")
        def send_status():
            try:
                status = api.PostUpdate(text_to_send)
                print(status.text)
            except:
                print("Sorry, the action failed.")
            time.sleep(1)
        if len(text_to_send) < 140:
            send_status()
        elif len(text_to_send) > 140:
            print("Sorry, your message is over 140 characters.")

    elif user_action == "B":
        print("What is the user id of the person you want to follow? The uid must be perfect, or it wont work!")
        user_follow = raw_input(": ")
        try:
            api.CreateFriendship(user_follow)
            friend_list = api.GetFriends()
        except:
            print("Sorry, the action failed.")
        time.sleep(1)

    elif user_action == "C":
        one = (random.choice(random_stater))
        two = (random.choice(random_second))
        three = (random.choice(random_third))
        four = (random.choice(random_fourth))
        five =  (random.choice(random_fith))
        try:
            status = api.PostUpdate(one + two + three + four + five)
            print(status.text)
        except:
            print("Sorry, the action failed.")
        time.sleep(1)

    elif user_action == "D":
        try:
            friend_list_2 = api.GetFriends()
            print(friend_list_2)
        except:
            print("Sorry, the action failed.")

    elif user_action == "E":
        print("Enter message text and recipant.")
        prvt_msg_txt = raw_input("Msg txt: ")
        msg_rcpt_id = raw_input("Rcpt uid: ")
        try:
            api.PostDirectMessage(prvt_msg_txt, msg_rcpt_id)
        except:
            print("Sorry, the action failed.")
        time.sleep(1)

    elif user_action == "F":
        print("Checking for incoming friendships...")
        try:
            isfriendexist = api.IncomingFriendship()
            if len(isfriendexist) < 0.5:
                print("No new frienship request.")
            elif len(isfriendexist) > 0.5:
                print("new friendships from:" + isfriendexist)
        except:
            print("Sorry, the action failed.")

    elif user_action == "Quit" or user_action == "quit":
        break
        
    elif user_action != "A" or user_action != "B" or user_action != "C" or user_action != "D" or user_action != "E" or user_action != "F" or user_action != "Quit" or user_action !="quit":
        print("That is not an option. Please choose something else.")
        time.sleep(1)
