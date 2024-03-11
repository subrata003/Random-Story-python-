import  random

print("Hello Reader ! This is your Story Generator.")

group=["subrata","subhankar","shibam","ananya"]

readername=input("Enter your Code Here :")
for i in range(0,len(group)):
        if readername== group[i]:
                print("Hello "+readername)

                print("Here is your story :")


                name=["Ram","Rahul","Sayan","Manab","Ratan","Dipesh","Dinesh","Souvik","Ankit","Rajib"]

                place=["Italy","Canada","South Africa","Nepal","Germany","India","Bangaladesh","United Kingdom", "America"]

                Words=["Drive in a large car.","go to meet a celebrity.","explain the books in Mystique Pages had a magical touch. ","had to meet someone.","arrive to a grand building and take a photograph."]

                like=["normal boy","old man","university student","collage student"]

                day=["a sunny day","a cold night","a cloudy day","a rainy day"]

                randomname=random.choice(name)
                randomplace=random.choice(place)
                randomwords=random.choice(Words)
                randomlike=random.choice(like)
                randomday=random.choice(day)

                story=" Once upon a time a "+ randomlike + " called "+randomname+" lived in a beautiful Country called "+randomplace+ " Where it was "+randomday+" and In this enchanting place "+randomname+" has to "+randomwords

                print(story)
                break
else:
        print("Access Denied")






