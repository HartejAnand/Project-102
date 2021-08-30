print("Riddle game!")
print("Rules: enter your answer in all lowercase and one word only")
print("Q: I have a bed, but I don't sleep. I have a mouth, but I never eat. I always run, but I never walk. What am I?")
answer1=input("A: ")
if(answer1=="river"):
    print("Nice! Next one:")
    print("Q: The red house is made of red bricks, and the blue house is made of blue bricks. What is the greenhouse made of?")
    answer2=input("A: ")
    if(answer2=="glass"):
        print("Not that easy to trick? How about this one:")
        print("Q: What can you catch, but never throw?")
        answer3=input("A: ")
        if(answer3=="cold"):
            print("Perfect, now onto the harder ones:")
            print("Q: What can you not hold for long, but weighs less than a feather?")
            answer4=input("A: ")
            if(answer4=="breath"):
                print("Great, but how about trying to decipher notes:")
                print("Q: A man is sitting in his house when a rock breaks his window. He sees 4 kids running away: Sally Wilson, Joe Wilson, Mark Wilson, and Emma Wilson. Later the man recieves the following note:")
                print("? Wilson. They threw the stone")
                print("Who threw the stone?")
                answer5=input("A: ")
                if(answer5=="mark"):
                    print("Well, he's in trouble. Anyways...:")
                    print("Q: if !+#=$, (-*=!, %/!)=@, and @x#=^, what is $+^-!X%+&/!$  ? (enter in code)")
                    answer6=input("A: ")
                    if(answer6=="&"):
                        print("You caught on? Well, I doubt you will get this:")
                        print("Q: I have many keys, but no locks; I have space, but no rooms; you can enter, but you can't come inside. What am I?")
                        answer7=input("A: ")
                        if(answer7=="keyboard"):
                            print("Last one:")
                            print("Q: What dies as soon an you say its name?")
                            answer8=input("A: ")
                            if(answer8=="silence"):
                                print("YAY! You won. But, do you want to try the bonus riddles?")
                                yon=input("yes or no: ")
                                if(yon=="yes"):
                                    print("Ok, let's get started:")
                                    print("Q: Name the movie:  (This one may or maynot be more than 1 word)")
                                    print("🤮p=l 👁️  🐖-h 🐗b=y,a=u 👴-grand")
                                    answer8=input("A: ")
                                    if(answer8=="star wars"):
                                        print("I'm sure you won't get this one:")
                                        print("Q: what is the missing word?")
                                        print("t 🐈 📍-p t 🎩 _____ a ⚫d=l 🐟tr=ab t+🎩")
                                        answer9=input("A: ")
                                        if(answer9=="knows"):
                                            print("And you know a lot about riddles. Last one:")
                                            print("Q: Which Disney movie character is being described?")
                                            print("🤖 🗑️ 🚀")
                                            answer10=input("A: ")
                                            if(answer10=="wall-e"):
                                                print("🎉, and it doesn't take a genius to figure out what that means.")
                                                print("CONGRATULATIONS!")
                                            else:
                                                print("better rewatch your classic Disney movies")
                                        else:
                                            print("Hint: the lone 't' stand for 'the'")
                                    else:
                                        print("I'm sure you've watched at least on of these movies")
                                elif(yon=="no"):
                                    print("Aww")
                            else:
                                print("Bonus Hint: it's not a physical thing")
                        else:
                            print("I'm sure you have one of these nearby")
                    else:
                        print("Didn't catch on, try again")
                else:
                    print("Hint: try reading the note out loud")
            else:
                print("No one can hold it for long, exept magicians")
        else:
            print("But it's better to not catch one")
    else:
        print("Think it over for a sec")
else:
    print("This is a classic, I know you can do it!")