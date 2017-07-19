define m = Character("Me")
define n = Character("Me", color="#DDDDDD")
define f = Character(_("Ford"), color="#3BB9FF") #Deep Sky Blue
define r = Character(_("Richter"), color="#996515") #Golden Brown
define j = Character(_("Jermaine"), color="#FAF0BE") #Blonde
define y = Character(_("Royce"), color="#8F6FF") #Poiple

image bg pier = "pier.jpg"
image bg gym = "gym.jpg"
image bg buffet = "buffet.jpg"
image bg black = "black.jpg"
image r trunks = "richter_trunks.png"
image r naked = "richter_naked.png"
image f = "ford_fluff.png"
image f naked = "ford_naked.png"
image j = "ford_fluff.png"

default pierchat_flag = False
default gym_start = False
default gym1_rack = False
default gym1_machines = False
default j_lastbf = False
default buffet_start = False
default buffet1_eat = False
default buffet1_eat_seconds = False
default buffet1_bar = False

label start:

    scene bg pier

    "{i}They say the definition of madness is doing the same thing and expecting a different result.{/i}"

    "{i}Without doing anything drastic, I figure a change of scenery is a good first step.{/i}"

    "{i}Change things up a bit, try and inject something different into my day.{/i}"

    "{i}My dad used to take me to a place like this when I was little.{/i}"

    "{i}If it was warmer than today, the ice cream van would show up.{/i}"

    "{i}I was always on my best behaviour in case that happened!{/i}"

    pause 2

    "{i}It's nice, but I'm still feeling a bit flat.{/i}"

    "{i}I'm not sure what I expected.{/i}"

    "{i}Might as well walk to the end and \"pier\" out, hurr hurr.{/i}"

    pause 2

    "{i}That cute couple sure have it figured out. Hand in hand, completely content in this moment.{/i}"

    "{i}But the size of that guy, heavens to Betsy! What a gigantic hunk! My heart's fluttering!{/i}"

    menu:

        "{i}Do... do I talk to him?{/i}"

        "{i}Can't hurt to say hi!{/i}":
            jump pierchat_yes

        "{i}He's clearly taken.{/i}":
            jump pierchat_no

    label pierchat_yes:

        $ pierchat_flag = True

        show f

        m "Hi there, big guy!"

        f "Howdy."

        m "Amazing day, isn't it?"

        f "Sure is. My partner and I always make the most of days like this."

        "{i}Oh. That's not what I wanted to hear, but I guess I can't be surprised.{/i}"

        m "I, uh, just wanted to ask, how did you grow so big?"

        "He laughed confidently with deep, bellowing chuckles."

        f "I eat a lot and lift a lot. Ain't rocket science!"

        "{i}I think I'm blushing.{/i}"

        m "Sounds like a recipe for success. Thanks. You two have a great day!"

        f "Heh, can do."

        hide f

        jump pierchat_done

    label pierchat_no:

        $ pierchat_flag = False

        "{i}Yeah. Still, just getting the heart racing like that has given me some inspiration.{/i}"

        jump pierchat_done

    label pierchat_done:

        "{i}Maybe that's what I need in my life. Bring some bigness to the table!{/i}"

    menu:

        "{i}But where should I go to get started?{/i}"

        "The gym":
            jump gym_start

        "The buffet":
            jump buffet_start

    label gym_start:
        $ gym_start = True

        if pierchat_flag:

            "{i}Well that man mountain did say he lifts a lot.{/i}"

        else:
            
            "{i}Getting a sweat on can be really energising.{/i}"

        scene bg gym
        with Dissolve(.5)

        "{i}The music's doof-doofing and the room smells of assorted deodorants. That aside, I'm pumped to get pumped.{/i}"

        "{i}A light warmup on one of the cardio machines will give me the chance to raise that heart rate.{/i}"

        "And that's not the only thing to get the heart racing. While there are TV screens in front of the treadmill you're on, you casually survey the gym."

        "In particular, there's a really ripped dude in the squat rack, whose shoulders seem to pop out like spiked shoulder pads, even among the rest of his bulging biceps, abs, quads and ... other muscles."

        "There are a few more beefy types and average Joes in and around the machines."

        "You're ready to move on to some real gym activity. The setup around the barbell lifting cage and racks look pretty full-on, but the machines look like a more familiar progression."

        menu:
            "{i}Where should I head to?{/i}"

            "The squat rack":
                jump gym1_rack

            "The machines":
                jump gym1_machines

    label gym1_rack:
        $ gym1_rack = True

        "{i}Well that big guy made it look easy. I'll start light and keep it nice and controlled.{/i}"

        "Starting with an empty barbell, you groove your way into some squats, adding a bit more weight on the ends for your second and third sets."

        "Your legs start to feel the burn, but you're not shaking, just breathing heavier."

        "As you complete your fifth rep, you wobbily rack the weight and suck in some oxygen."

        show f

        "???" "Well done, little buddy. Showing some real mettle there."

        m "Th- thanks man!"

        "???" "Just to let you know, you can set these pegs on the squat cage..."

        "???" "Here, and here."

        "???" "So if you push yourself a bit too hard and you can't stand back up, you can safely bail out and the bar can stay there and not crush you."

        m "High tech! Good to know, thanks, mister."

        f "The name's Ford. Hope I'm not imposing too much. It's just great to see someone taking a shine to the iron."

        m "Not at all! It's great to see a friendly face! I can't remember the last time I was in a gym."

        f "You're doing great, using plenty of heart and muscling your way through it. But if we just tweak your starting position ..."

        "He walks you back underneath the barbell."

        f "If you push your feet out a bit more ..."

        "He places his hands on the inside of your thighs and gently nudges it until your feet point out at 45 degrees."

        f "And get your upper back tight and set to make a nice, firm shelf for the bar to sit on ..."

        "Ford draws a line along the muscles between your shoulder blades with his fingertips."

        f "Really grab the bar tightly, that normally helps activate those muscles."

        f "That's really good. Now you're in a great position of strength. It'll be a bit easier when you get more muscles involved like that. Give it a try."

        "It still wasn't easy, but you do your best and control the movement well."

        m "Hmmm, that just might work. I guess you've done this a lot, huh?"

        f "Sure do, and not just the lifting. I do personal training around these parts, teaching and showing how it's done."

        m "I'd love you to show me a few more things sometime."

        f "I thought you might. We should do a session together."

        m "Totally. Sounds terrific."

        f "I'll let you finish up then. See you around!"

        m "Likewise! Thanks!"

        jump the_end

    label gym1_machines:
        $ gym1_machines = True

        "{i}Awesome! Let's see, there's a pec deck, let's work on that.{/i}"

        "{i}This feels pretty good. I'm not moving as much iron as the big guys, but I'm not too out of place.{/i}"

        pause 1.5

        "After working your way around several of the machines, it's time for leg day. Wouldn't be gym without it."

        "You snake your way into the seat of the leg press."

        "{i}My legs are really bunched up against the plate. Have I gotten taller since I did this exercise last?{/i}"

        "As you fiddle with the seat, a toned, blonde man puts his hand on your shoulder and reaches over to a handle to the side of the seat."

        "???" "It's this one here. It got me too the first time!"

        m "Ah, so subtle! Thanks heaps."

        "???" "No problem, compadre. Gotta give you plenty of room to stretch out and grow, right?"

        m "Ain't got nothing on some of the big guys here."

        "???" "You've been doing pretty well, from what I've noticed. Just getting started?"

        m "I guess it's my first time back in a while."

        "???" "Feels alright?"

        m "Yeah it does actually. My muscles might not agree in a couple of days, but great for now!"

        "He laughs with his body, touching your arm as he chuckles and regathers himself."

        "???" "That's the spirit! Why, I bet you'll be one of the biggest, buffest guys in the gym in no time!"

        m "What makes you say that?"

        "???" "My last boyfriend was a thickly built muscleman. There's something about you, I can just tell."

        menu:
            "{i}Should I ask about his boyfriend?{/i}"

            "Yeah":
                jump j_lastbf_yes
                
            "Nah":
                jump gym1_machines_cont

    label j_lastbf_yes:
        $ j_lastbf = True

        m "What happened to your last boyfriend?"

        "???" "Oh, he left me. I'm away a lot for my job. I think it got to him."

        m "I see. What line of work are you in?"

        "???" "I'm a travel writer, for one of those 'be your own tourguide' books."

        m "Oh cool! It must be fun to see so much of the world."

        "???" "It's got its perks and highlights. But it's a lot less glamourous when you're researching the ins and outs of Bulgarian public transport."

        m "Well you knew the ins and outs of the leg press. Is this gonna be in your next submission?"

        "???" "This may not be the hottest nightspot, but there's a certain charm about the patronage."

        "He smiles at you, looking deep into your eyes."

        jump gym1_machines_cont

    label gym1_machines_cont:
        pause 1.5

        j "My name's Jermaine, by the way."

        # intro yourself

        j "I may not look like it, but I come here a fair bit. If you ever want to grab a protein shake or need rescuing from a machine trying to eat you, just let me know!"

        m "Haha, sure thing! Nice meeting you."

        j "Now smash those legs! Push strong!"

        m "Heh, can do. Thanks again, Jermaine."

        jump the_end

    label buffet_start:
        $ buffet_start = True

        if pierchat_flag:

            "{i}Well that man mountain did say he eats a lot.{/i}"

        else:
            
            "{i}A man's gotta eat.{/i}"

        scene bg buffet
        with Dissolve(.5)

        "{i}There's no shortage of food here. If these aromas are anything to go by, I'm in the right place.{/i}"

        "It's a large open room, with numerous hot pots, a carvery, salad and dessert bars among the many cuisine options available."

        "A long bar with softer lighting complements the buffet. A bartender is mixing a cocktail, showing off with spinning and juggling implements for one of the patrons."

        menu:

            "{i}Where should I start?{/i}"

            "Hit the buffet":
                jump buffet1_eat

            "Visit the bar":
                jump buffet1_bar

    label buffet1_eat:
        $ buffet1_eat = True

        "{i}A full plate is the first step to a full belly. And this plate's loaded!{/i}"

        "You take a seat at a table near some indoor plants. Gentle splashing sounds hint that there's a fountain or some water feature nearby."

        pause 2

        "{i}This curry is off the charts! So good. I can't help but keep shoveling it in my face.{/i}"

        pause 2

        "{i}It's pretty chill here. Not busy, but there are a few people around. No real queues for food, that's a bonus.{/i}"

        menu:

            "{i}Speaking of which, time for seconds?{/i}"

            "{i}Yeah! I wanna try a lot more!{/i}":
                jump buffet1_eat_seconds

            "{i}Let my stomach settle for a minute, there's no rush.{/i}":
                jump buffet1_eat_noseconds

    label buffet1_eat_seconds:
        $ buffet1_eat_seconds = True

        "{i}These meals aren't gonna eat themselves! Let's see... some pasta. Ravioli and lasagna? Why not! Roast beef, roast veggies, this'll do nicely.{/i}"

        "You plump yourself and your loaded plate back at the table and chow down."

        "It's glorious. You can feel your belt poking into your stuffed belly."

        "You pause to exhale deeply, and give your stomach a subtle little rub, urging it to work that pasta down so you can finish the plate."

        jump buffet1_eat_meet

    label buffet1_eat_noseconds:
        "{i}Ahh. This is more relaxing than looking out into the water.{/i}"

        jump buffet1_eat_meet

    label buffet1_eat_meet:

        "A short fellow in a white shirt and apron hovers at your table for a moment, waiting until you look up at him."

        if buffet1_eat_seconds:

            "???" "Hi there! Looks like you might not be ready for dessert yet, but I couldn't help notice how much you've put away tonight and wanted to give you first dibs."

        else:
            
            "???" "Excuse me, sir, would you care for some dessert?"

        "???" "I've just finished baking this warm, moist cake and I've got a hunch that you'll appreciate it more than anyone else here."

        m "Why certainly! I'd love some, thanks!"

        "He cuts you off a piece of the cake so large that it's nearly a quarter of it."

        "As he separates it and exposes more than the outer coating of icing, you notice that it's no ordinary cake."

        "There are two tiers of dark, chocolate coloured cake, sandwiching a middle tier of cinnamon donuts covered in whipped cream."

        m "Oh wow."

        "???" "Wait until you taste it! Go on!"

        "You take a spoon and scoop out a piece. It's so fresh, you can feel its pleasant heat. The icing is rich and decadent, but you can't resist."

        m "You're not kidding. Chef, this is amazing! Full on, but amazing!"

        y "Chef Royce, at your service! On quiet nights like this, I like to experiment. Always helps to get the tick of approval from a sympathetic ear. Or in this case, a sympathetic tummy."

        if buffet1_eat_seconds:

            "He looks down at your midsection, which is stretching your shirt and showing a little bit of skin underneath."

        "He gives your belly two gentle taps and takes a seat opposite you. He gazes at you, distant but smiling. He seems happy, so you keep tucking into more of the cake."

        # AMERICAN ALERT: Jam over jelly

        m "Hey, there's jam in these donuts!"

        y "You better believe it! Nothing but the finest for this venue's finest! It's fun using the injector for it too. I love seeing the donuts really swell and take shape as they fill up."

        m "I hope I'm not keeping you from anything."

        y "Nonsense! If the boss sees me, I'll call it a break. In all honesty, getting feedback is really important to the improvement of my craft. Any thoughts?"

        m "It's really rich, but I'm sure that's the idea. I thought it would be a bit dry with the double layers of cake, but it's beautifully moist, and the whipped cream finishes it well."

        y "Good. Anything negative? Come on, I won't get mad."

        m "If anything, the outside doesn't hint at how unique and tasty a creation it is on the inside."

        y "Surprise! Haha! You're probably right. I could show it off better. That's good stuff, thanks."

        m "Hey, thank you for the personal service."

        y "My pleasure. You know what? I'm just going to leave the rest of it here for you. There's plenty of other desserts for the others."

        m "Uhhh, I don't think I can eat all this."

        y "Come see me later if you need a doggy bag then. I'll send over some tea and coffee to help you through a bit more though."

        "Considering you're basically too full to move right now, it's hard to disagree."

        m "Great!"

        y "Enjoy!"

        "He heads back behind the dessert bar, and you breathe deeply as you lay eyes on the mass of dessert in front of you."

        "A bit more can't hurt. It's a real experience and it feels good to jazz up your day with something out of the ordinary."

        pause 2

        "After an hour, you're nearly falling asleep at the table as your body works to digest the buffet's delights."

        y "It's ok, buddy, you don't need to stay up all night trying to finish it just for me. I appreciate the effort though!"

        "Royce boxes up the remaining cake and helps you up out of your chair."

        y "I've let the front desk staff know you've been extremely helpful today, no charge. Keep me, uhh, keep us in mind next time you'd like to dine!"

        m "I will. I won't be forgetting until at least lunch time at this rate!"

        "You grab your full, firm belly and jokingly knock against it."

        y "Eeee! What a successful night!"

        "Royce smooshes himself against you in a tight hug."

        y "Bye big guy!"

        jump the_end

    label buffet1_bar:
        $ buffet1_bar = True

        "{i}I'll pull up a barstool and see what this bartender is up to.{/i}"

        pause 2

        "Bartender" "Be with you in a tick, sir."

        "As he meets your eyes, he throws his cocktail shaker from behind his back into his left hand, then pours the contents into a wide-brimmed glass via a strainer."

        "He tops off the red drink with a sprig of mint and places it on a small serviette in front of the short squirrel lady who ordered it."

        "By the time he asks you what you'd like to drink, you're a bit mesmerised."

        "Bartender" "Don't fret, I'll throw something together for you!"

        "You nod and smile absentmindedly. The bartender dunks the rim of a glass in what looks like sugar, then pulls out a mini blow torch and fires it up."

        show r trunks

        "???" "Whoa, what did you order?"

        m "I have absolutely no idea."

        "???" "You sure this firebug actually works here?"

        m "At least if it's to scale, he'll only burn down a gingerbread house instead of this whole joint."

        "???" "Whoa, they have a gingerbread house at the dessert bar?"

        m "I haven't seen any, but if there's a pile of charred sugary remains, you know whodunnit."

        "???" "Haha, I'll be sure to do plenty of \"detective work\" and keep us all safe."

        "The man next to you patted his ample belly for emphasis."

        m "Dammit Malone, you've gotta stop eating all the evidence or City Hall will have my ass on toast!"

        "???" "Chief, you know I don't play by the book. I get results!"

        "You both laugh at your impromptu action cop routine. He's got a wide smile splashed across his cute, cherubic face."

        "The bartender returns with your drink, ornately decorated with a curled piece of orange peel."

        "???" "I'll take care of that, plus a pint of pale ale too thanks hotshot."

        m "That's very kind of you, Detective. Have you had dinner yet?"

        "???" "One dinner yes, but I've got more to give. As do these pants."

        "He sticks a thumb into the waistband of his pants and stretches them out, lightly brushing against his soft, fuzzy fat."

        "For a second, you caught a glimpse of the lower part of his gut, hanging down low with a gentle bounce."

        m "Care to join me?"

        "???" "I'd love to. Let's grab some grub."

        hide r trunks

        jump the_end

    label the_end:

        "{i}I've got a really good feeling about this. I think this is the start of a wonderful friendship. Maybe even more...{/i}"

        show bg black
        with fade

    return
