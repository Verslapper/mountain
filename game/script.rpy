define m = Character("Me")
define n = Character("Me", color="#DDDDDD")
define f = Character(_("Ford"), color="#3BB9FF") #Deep Sky Blue
define r = Character(_("Richter"), color="#996515") #Golden Brown

image bg pier = "pier.jpg"
image bg gym = "gym.jpg"
image bg buffet = "buffet.jpg"
image bg black = "black.jpg"
image r trunks = "richter_trunks.png"
image r naked = "richter_naked.png"
image f = "ford_fluff.png"
image f naked = "ford_naked.png"

default pierchat_flag = False
default gym_start = False
default gym1_rack = False
default gym1_machines = False
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

        "Oh. That's not what I wanted to hear, but I guess I can't be surprised."

        m "I, uh, just wanted to ask, how did you grow so big?"

        "He laughed confidently with deep, bellowing chuckles."

        f "I eat a lot and lift a lot. Ain't rocket science!"

        "I think I'm blushing."

        m "Sounds like a recipe for success. Thanks. You two have a great day!"

        f "Heh, can do."

        hide f

        jump pierchat_done

    label pierchat_no:

        $ pierchat_flag = False

        "Yeah. Still, just getting the heart racing like that has given me some inspiration."

        jump pierchat_done

    label pierchat_done:

        "Maybe that's what I need in my life. Bring some bigness to the table!"

    menu:

        "But where should I go to get started?"

        "The gym":
            jump gym_start

        "The buffet":
            jump buffet_start

    label gym_start:
        $ gym_start = True

        if pierchat_flag:

            "Well that man mountain did say he lifts a lot."

        else:
            
            "Getting a sweat on can be really energising."

        scene bg gym
        with Dissolve(.5)

        "The music's doof-doofing and the room smells of assorted deodorants. That aside, I'm pumped to get pumped."

        "A light warmup on one of the cardio machines will give me the chance to raise that heart rate."

        "And that's not the only thing to get the heart racing. While there are TV screens in front of the treadmill you're on, you casually survey the gym."

        "In particular, there's a really ripped dude in the squat rack, whose shoulders seem to pop out like spiked shoulder pads, even among the rest of his bulging biceps, abs, quads and ... other muscles."

        "There are a few more beefy types and average Joes in and around the machines."

        "You're ready to move on to some real gym activity. The setup around the barbell lifting cage and racks look pretty full-on, but the machines look like a fairly familiar to progress to."

        menu:
            "Where should I head to?"

            "The squat rack":
                jump gym1_rack

            "The machines":
                jump gym1_machines

    label gym1_rack:
        $ gym1_rack = True

        "Well that big guy made it look easy. I'll start light and keep it nice and controlled."

        # Have Ford come over and set the safety pegs

        # Then he watches you and gives a pointer

        # Then he says that he's a PT

        # Then you set up a session for next time

        jump the_end

    label gym1_machines:
        $ gym1_machines = True

        "Awesome! Let's see, there's a pec deck, let's work on that."

        "This feels pretty good. I'm not moving as much iron as the big guys, but I'm not too out of place."

        pause 1.5

        "After working your way around several of the machines, it's time for leg day. Wouldn't be gym without it."

        "You snake your way into the seat of the leg press."

        "My legs are really bunched up against the plate. Have I gotten taller since I did this exercise last?"

        "As you fiddle with the seat, a toned "

        # Your helper comes in and shows you how to adjust the leg press

        # You talk about relative size

        # He mentions he got his last boyfriend big

        # Choose to elaborate, and thus reveal his "travel writer" job

        # He says he's here every second day, so you can come back
        # Or go for a protein shake and do some relationship building?

        jump the_end

    label buffet_start:
        $ buffet_start = True

        if pierchat_flag:

            "Well that man mountain did say he eats a lot."

        else:
            
            "A man's gotta eat."

        scene bg buffet
        with Dissolve(.5)

        "There's no shortage of food here. If these aromas are anything to go by, I'm in the right place."

        "It's a large open room, with numerous hot pots, a carvery, salad and dessert bars among the many cuisine options available."

        "A long bar with softer lighting complements the buffet. A bartender is mixing a cocktail, showing off with spinning and juggling implements for one of the patrons."

        menu:

            "Where should I start?"

            "Let's dig in!":
                jump buffet1_eat

            "Visit the bar":
                jump buffet1_bar

    label buffet1_eat:
        $ buffet1_eat = True

        "A full plate is the first step to a full belly. And this plate's loaded!"

        "I'll take a seat at the table next to those indoor plants."

        pause 2

        "This curry is off the charts! So good. I can't help but keep shoveling it in my face."

        pause 2

        "It's pretty chill here. Not busy, but there are a few people around. No real queues for food, that's a bonus."

        menu:

            "Speaking of which, time for seconds?"

            "Yeah! I wanna try a lot more!":
                jump buffet1_eat_seconds

            "Let my stomach settle for a minute, there's no rush.":
                jump buffet1_eat_noseconds

    label buffet1_eat_seconds:
        $ buffet1_eat_seconds = True

        "These meals aren't gonna eat themselves! Let's see... some pasta. Ravioli and lasagna? Why not! Roast beef, roast veggies, this'll do nicely."

        # Ready to meet

        jump the_end

    label buffet1_eat_noseconds:
        "Ahh. This is more relaxing than looking out into the water."

        # Ready to meet

        jump the_end

    label buffet1_bar:
        $ buffet1_bar = True

        "I'll pull up a barstool and see what this bartender is up to."

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

        "I've got a really good feeling about this. I think this is the start of a wonderful friendship. Maybe even more..."

        show bg black
        with fade

    return
