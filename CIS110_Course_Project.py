print("Welcome friends today I am going to tell you a story about a dog that takes a trip.")
print("In the fields down below please answer all questions.")
print("After you answer each question please hit the enter button.")
print("Lets get started! ")


breed = input(f"\n\n\nWhat breed is the dog: ")
while len(breed) == 0:
    breed = input(f"Please enter a breed to continue: ")
name = input(f"\nWhat is the name of your new friend: ")
while len(name) == 0:
    name = input(f"Please enter a name to continue: ")
city = input(f"\nWhat city does your new friend live in: ")
while len(city) == 0:
    city = input(f"Please enter a city name to continue: ")
size = input(f"\nWhat is the size of the dog. Type small, medium, or large: ")
while len(size) == 0:
    size = input(f"Please enter a size to continue. Type small, medium, or large: ")
sex = input(f"\nIs your friend a boy or girl: ")
while len(sex) == 0:
    sex = input(f"Please enter a sex to continue. Type boy or girl:  ")

if sex == "boy":
    print(f"\n\n\n\nLets Begin. ")
    print(f"\nYour name is {name} a {size} {breed}. ")
    print(f"\nOne day {name} wakes up from taking a nap. ")
    print(f"\n{name}'s parents have never let him go outside as far as the backyard. ")
    print(f"\nYou hear a knock at the door. Who could it be?")
    print(f"\nIts the delievery man of {city}!")
else:
    print(f"\n\n\n\nLets Begin. ")
    print(f"\nYour name is {name} a {size} {breed}. ")
    print(f"\nOne day {name} wakes up from taking a nap. ")
    print(f"\n{name}'s parents have never let her go outside as far as the backyard. ")
    print(f"\nYou hear a knock at the door. Who could it be?")
    print(f"\nIts the delievery man of {city}!")


choice1 = input(f"\n\n\n\nShould {name} dart out the door? Type yes or no: ")

if sex == "boy":
    if choice1 == "yes":
        print(f"\n{name} makes a break for the door.")
        print(f"{name}'s parents were busy putting packages away and didnt notice him get out.")
        print(f"He runs across the yard and jumps into the truck's back door while the truck driver does his paper work.")
        print(f"The door slams shut, and {name} is locked inside the delivery truck.")
        print(f"The truck starts up and begins to drive away.")
        print(f"After what seems like forever, the truck stops and the door opens up.")
        print(f"{name} is at the delivery depot.")
        print(f"He gets scared someone might see him and call the pound. So he darts out into {city}.")
    else:
        print(f"\n{name}'s parents put him out before they can escape.")
        print(f"He starts wondering the yard thinking what could be on the other side of this fence.")
        print(f"If he wouldn't have been so scared he might know.")
        print(f"Where would he go? What would he do?")
        print(f"He notices a hole in the fence and squeezes his body through it.")
        print(f"He runs across the yard and jumps into the truck's back door while the truck driver does his paper work.")
        print(f"The door slams shut, and {name} is locked inside the delivery truck.")
        print(f"The truck starts up and begins to drive away.")
        print(f"After what seems like forever, the truck stops and the door opens up.")
        print(f"{name} is at the delivery depot.")
        print(f"He gets scared someone might see him and call the pound so he darts out the door into {city}.")

else:
    if choice1 == "yes":
        print(f"\n{name} makes a break for the door.")
        print(f"{name}'s parents were busy putting packages away and didnt notice her get out.")
        print(f"She runs across the yard and jumps into the truck's back door while the truck driver does his paper work.")
        print(f"The door slams shut, and {name} is locked inside the delivery truck.")
        print(f"The truck starts up and begins to drive away.")
        print(f"After what seems like forever, the truck stops and the door opens up.")
        print(f"{name} is at the delivery depot.")
        print(f"She gets scared someone might see her and call the pound. So she darts out into {city}.")
    else:
        print(f"\n{name}'s parents put her out before they can escape.")
        print(f"She starts wondering the yard thinking what could be on the other side of this fence.")
        print(f"If she wouldn't have been so scared she might know.")
        print(f"Where would she go? What would she do?")
        print(f"She notices a hole in the fence and squeezes her body through it.")
        print(f"She runs across the yard and jumps into the truck's back door while the truck driver does his paper work.")
        print(f"The door slams shut, and {name} is locked inside the delivery truck.")
        print(f"The truck starts up and begins to drive away.")
        print(f"After what seems like forever, the truck stops and the door opens up.")
        print(f"{name} is at the delivery depot.")
        print(f"She gets scared someone might see her and call the pound so she darts out the door into {city}.")


choice2 = input(f"\n\n\n\n{name} see's a hotdog vendor and is hungry. Should {name} try and grab a string of hotdogs? Type yes or no: ")

if sex == "boy":
    if choice2 == "yes":
        print(f"\nHe grabs a strand of hotdogs and starts chowing down on them.")
        print(f"The hotdog vendor notices him eating them and yells to the police officer nearby.") 
        print(f"{name} gets startled, drops the hotdogs and runs.")
        print(f"The police officer is now chasing him. As the police officer is chasing him, the officer calls the pound on his walkie talkie.")
        print(f"{name} tries to cut down an alley way. But the animal control officer is waiting for him.")
        print(f"He is caught! The animal control officer takes him to the pound.")
    else:
        print(f"\n{name} decides it is too risky.")
        print(f"He runs across the street and down an alley way.")
        print(f"A police officer walks by and notices him in the alley.")
        print(f"The police officer notices {name} doesn't have a tag, it must have slipped off somewhere along the journey.")
        print(f"{name} gets scared and starts to run from the police officer.")
        print(f"The police officer yells *Hey dog stop!* ")
        print(f"The police officer is now chasing him. As the police officer is chasing him, the officer calls the pound on his walkie talkie.")
        print(f"{name} crosses the street. He tries to cut down another alley way. But the animal control officer is waiting for him.")
        print(f"He somehow manages to get by the animal control officer, and loses them.")
else:
    if choice2 == "yes":
        print(f"\nShe grabs a strand of hotdogs and starts chowing down on them.")
        print(f"The hotdog vendor notices her eating them and yells to the police officer nearby.") 
        print(f"{name} gets startled, drops the hotdogs and runs.")
        print(f"The police officer is now chasing her. As the police officer is chasing her, the officer calls the pound on his walkie talkie.")
        print(f"{name} tries to cut down an alley way. But the animal control officer is waiting for her.")
        print(f"She is caught! The animal control officer takes her to the pound.")
    else:
        print(f"\n{name} decides it is too risky.")
        print(f"She runs across the street and down an alley way.")
        print(f"A police officer walks by and notices her in the alley.")
        print(f"The police officer notices {name} doesn't have a tag, it must have slipped off somewhere along the journey.")
        print(f"{name} gets scared and starts to run from the police officer.")
        print(f"The police officer yells *Hey dog stop!* ")
        print(f"The police officer is now chasing her. As the police officer is chasing her, the officer calls the pound on his walkie talkie.")
        print(f"{name} crosses the street. She tries to cut down another alley way. But the animal control officer is waiting for her.")
        print(f"She somehow manages to get by the animal control officer, and loses them.")

if sex == "boy":
    if choice1 == "yes" and choice2 == "yes":
        print(f"\n{name}'s parents are found and called.")
        print(f"They come and pick him up.")
        print(f"On the way home they tell him *See we told you the world is a dangerous place* ")
        print(f"They get {name} home and he goes inside and lays in his bed.")
    elif choice1 == "no" and choice2 == "no":
        print(f"\n After some time of wondering around outside the city")
        print(f"{name} finally finds his way home.")
        print(f"{name}'s parents were so worried about him.")
        print(f"His parents see that even though he was gone a couple days, he made it back in one piece.")
        print(f"{name}'s parents let him go outside of the fence more often, but he had to be home before dark.")
    else:
        print(f"He lays down on the sidewalk tired, hungry, and scared.")
        print(f"An old lady driving down the road spots him.")
        print(f"She stops the car picks him up and puts him in her car.")
        print(f"She recognizes him and knows where he lives.")
        print(f"She lives in the house next door to his house.")
        print(f"She takes him to her house. Feeds, and bathes him.")
        print(f"Then takes {name} home to his family.")
        print(f"{name}'s parents were so worried about him.")
        print(f"The neighbor tells his parents they need to get him out more.")
        print(f"His parents see that even though he was gone a couple days, he made it back in one piece.")
        print(f"{name}'s parents let him go outside of the fence more often, but he had to be home before dark.")
else:
    if choice1 == "yes" and choice2 == "yes":
        print(f"\n{name}'s parents are found and called.")
        print(f"They come and pick her up.")
        print(f"On the way home they tell her *See we told you the world is a dangerous place* ")
        print(f"They get {name} home and she goes inside and lays in her bed.")
    elif choice1 == "no" and choice2 == "no":
        print(f"\n After some time of wondering around outside the city")
        print(f"{name} finally finds her way home.")
        print(f"{name}'s parents were so worried about her.")
        print(f"Her parents see that even though she was gone a couple days, she made it back in one piece.")
        print(f"{name}'s parents let her go outside of the fence more often, but she had to be home before dark.")
    else:
        print(f"She lays down on the sidewalk tired, hungry, and scared.")
        print(f"An old lady driving down the road spots her.")
        print(f"She stops the car picks her up and puts her in her car.")
        print(f"She recognizes her and knows where she lives.")
        print(f"She lives in the house next door to her house.")
        print(f"She takes her to her house. Feeds, and bathes her.")
        print(f"Then takes {name} home to her family.")
        print(f"{name}'s parents were so worried about her.")
        print(f"The neighbor tells his parents they need to get her out more.")
        print(f"Her parents see that even though she was gone a couple days, she made it back in one piece.")
        print(f"{name}'s parents let her go outside of the fence more often, but she had to be home before dark.")
print("THE END!")



    
