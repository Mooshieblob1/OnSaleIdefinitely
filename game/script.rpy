Adefine T = Character("Taro", who_color="#0000FF")
define Y = Character ("Yui")
define H = Character("Hikari")
define S = Character("Sawako")
define M = Character("Mitsu")
define C = Character("Chiisato")
define m1 = Character("Customer Relations Officer")
define m2 = Character("Attacker")
define m3 = Character("Large man")
define m4 = Character("Fangirl 1")
define m5 = Character("Fangirl 2")
define who = Character("???")
define YoungT = Character("Young Taro")
define YoungH = Character("Young Hikari")

image t = "Taro/Taro Neutral.png"
image t happy1 = "Taro/Taro Happy.png"
image t happy2 = "Taro/Taro Happy 2.png"
image t laugh = "Taro/Taro Laugh.png"
image t hurt = "Taro/Taro Hurt.png"
image t shocked = "Taro/Taro Shocked.png"
image t uneasy = "Taro/Taro Uneasy.png"
image guard = "Minor/guard.png"
image attacker = "m2.png"
image t grey = "Taro/Taro grey.png"
image t sad = "Taro/Taro sad.png"
image t smile = "Taro/Taro smile.png"
image t angry 1 = "Taro/Taro Angry 1.png"
image t angry 2 = "Taro/Taro Angry 2.png"
image c = "Chiisato/Chiisato.png"
image c grey = "Chiisato/Chiisato grey.png"
image y = "Yui/Yui.png"
image y grey = "Yui/Yui grey.png"
image h = "Hikari/Hikari.png"
image h grey = "Hikari/Hikari grey.png"
image s = "Sawako/Sawako.png"
image s grey = "Sawako/Sawako grey.png"
image m = "Mitsu/Mitsu.png"
image m grey = "Mitsu/Mitsu grey.png"
image m3 = "large man.png"
image m4 = "m4.png"
image m5 = "m5.png"

transform moveleft:
    linear 0.5 xpos 0.2

label start:

    scene bg room
    with fade

    play music ("audio/BLOB 2.wav") loop fadein 1.0

    show guard at left:
        zoom .7

    show t grey at right:
        zoom .7

    m1 "Please state your name, age, and occupation."

    show t sad

    T "Uh… Taro. Tanaka Taro. I'm 27... and I'm a pharmacist."

    "Taro holds his head in his hands."

    "His head is pounding, and his ears are ringing."

    show t grey

    m1 "Please tell me what happened on March 23rd, 20XX."

    hide guard

    show c grey at left:
        zoom .7

    "That girl was smirking at Taro and holding a device that looks like a smartphone attached to a wrist band. Numbers are skyrocketing on a hologram above her arm."

    who "You better explain the story behind your NeuroPhone now."

    show t sad

    T "I… I was..."

    scene bg room1
    with Fade(1.0, 1.0, 1.0, color="#000")

    show t sad at right:
        zoom .7

    # Scene Change STUDIO APARTMENT

    T  "Ugh, my head is pounding. What time is it? What is that noise?"

    "He holds his arm up, his forearm opening up to a touchscreen panel. It displays the time, which is around 5:32."

    "He glances outside towards the window, and a siren is blaring."

    show t angry 1

    T  "Ugh, this again?"

    show t grey

    "Taro's NeuroPhone buzzes lightly."

    "Suddenly, he hears a crash outside his apartment."

    stop music fadeout 1.5

    play music ("audio/BLOB 4.wav") loop fadein 1.5

    "The door is being rattled. Taro immediately jolts up."

    "He grabs the closest makeshift weapon he can find"

    "Taro noticed a ringing noise."

    "Suddenly, an advertisement pop-up displays in Taro's peripheral vision."

    "{b}{i}[Need protection for you and your family? Try our brand new ZT Rifle]{/i}{/b}"

    show t

    T  "Where's that baseball bat I had lying around?"

    show t angry 2

    T  "What the hell is even going on outside?"

    "More crashes come from outside his door."

    show t

    T  "It's probably in the closet."

    "Taro goes to his closet, quickly whipping out a worn-out wooden bat."

    show t grey

    "{b}{i}[Out for a swing with your friends? Try our new Aluminium baseball bats!]{/i}{/b}"

    show t

    T  "This'll be enough to scare them off."

    "He hesitates as he stands in front of the door, taking a deep breath."

    "He readies himself for what's to come."

    "He quickly rushes through the door, suddenly seeing a figure."

    show attacker at left:
        zoom .7

    "All Taro could tell was that this kid was much younger than him."

    "Taro could see that his eyes were frantic."

    "They both stare at each other, eyes locked as they seem to be sizing each other up."

    m2  "P-P-Please! I Need money!"

    "The kid holds a knife in front of Taro, arm trembling heavily."

    show t angry 1

    T "Buzz off kid, I haven't got any money."

    show t grey

    m2 "You don't understand man! I {b}NEED{/b} it!"

    T "You on something kid?"

    m2 "... {w=1}"

    "The kid suddenly stabs him with the knife, then dashes off."
    with hpunch

    hide attacker
    with easeoutleft

    show t hurt

    T  "What the hell?!"

    "Taro clutches the area where he was stabbed, ripping out the knife as fast as he could. His eyes were wide. What just happened?"

    "{b}{i}[If you require a good set of knives then, Japan has got you covered with these sets of high-quality Carbon Steel knives! Perfect for all your kitchen needs]{/i}{/b}"

    "Taro's NeuroPhone buzzes."

    "Throwing down the knife, he tries to bolt towards his attacker, but suddenly collapses in the hallway."

    T  "Crap..."

    show attacker at left:
        zoom .7

    "The attacker slowly moves back toward him. However, all Taro can see is a blur."

    "He has enough energy to grip his head."

    "He's paralysed from whatever was in the knife. He passes out."

    stop music fadeout 1.0

    "...{w=2}     {b}{i}[If you need to capture escaped animals, try our powerful horse tranquilizers today!]{/i}{/b}"

    scene bg room
    with Fade(1, 2.5, 1, color="#000")

    show guard at left:
        zoom .7
    show t at right:
        zoom .7
    with fade

    T "I'm not sure what happened in between where I was stabbed and after I got patched up by the doctor."

    show t grey

    m1 "Please, go on."

    scene bg doctor
    with Fade(1.0, 1.0, 1.0, color="#000")

    play music ("audio/BLOB 3.wav") loop fadein 1.0

    # Scene Change DOCTOR’S OFFICE

    "Taro groans as he slowly comes to. He's sitting in an office, but ... Children were running around on the floor, and various people were sitting on the ground."

    "This clearly wasn't a waiting room, but it sure looked like one."

    show t uneasy at right:
        zoom .7

    T  "How the hell did I get here…?"

    who "Taro?"

    show y at left:
        zoom .7

    "A girl approaches him, She has a gentle smile on her face but still has a concerned look on her face."

    "Taro looks up, eyes brightening when he realises it's a familiar face. Suko Yui, his senior and the woman who ran the sector clinic."

    show y grey

    show t uneasy

    T "If you're here...{w=1.2} that means I'm hurt again, right?"

    show t grey

    show y

    Y "Yeah, You didn't look so good."

    show y grey

    "Taro looks down at his torso."

    "Bandages, all around his stomach area."

    "Taro's NeuroPhone buzzes once more."

    show y

    Y "You better get that thing fixed, don't want it to cause problems later."

    Y "I think I have a toolkit around here somewhere."

    show y grey

    show t

    T  "Since when were you a technician?"

    show t happy1

    "Taro smirks."

    show t grey

    show y

    Y "Very funny, you wise guy."

    show y grey

    "She smiles again."

    show y

    Y "I'm not getting paid to stand around doing nothing."

    Y "Now stay there and don't move, I'm going to find something to fix you up with."

    hide y
    with easeoutleft

    "She exits the room."

    show t uneasy

    "Taro looks around, concerned about the number of people here."

    "It's almost a fire hazard, with how many people are there."

    "A scream could be heard from a few rooms over…"

    T "That sounds awful..."

    "He looks over his shoulder when he hears a few clicks from someone else."

    "The man next to him seems to be breathing heavily. He looked incredibly out of shape, and the stench rolling off him was beyond awful.."

    "There was an irritating buzz emitting from him."

    "Peeking over at the stranger's NeuroPhone, he saw him scrolling on The Company's website, mindlessly browsing the services they offered."

    "However, looking down in the corner Taro noticed a red flashing number that appeared to be getting lower and lower."

    T  "Hey... you're in negative balance there."

    show m3 at left:
        zoom .7

    "The large man slowly turned his head towards Taro and gives him a steely-eyed look."

    show t grey

    m3 "Mind your own business buddy."

    show t

    "Taro's NeuroPhone buzzes again."

    "Taro blinks, and then shakes his head a bit."

    T  "Oh... uh yeah, whatever man."

    show t grey

    "The man goes back to scrolling through his NeuroPhone, giving judgemental glances back at Taro."

    stop music fadeout 1.5

    scene bg room
    with Fade(1.0, 1.0, 1.0, color="#000")

    show guard at left:
        zoom .7
    show t grey at right:
        zoom.7
    with fade

    m1 "What was your relationship with Miss Sawako?"

    show t

    T "Well..."

    scene bg classroom
    with Fade(1.0, 1.0, 1.0, color="#FFF")

    # Scene Change Small Classroom

    play music ("audio/nostalgia.mp3") loop fadein 1.5

    show s grey at left:
        zoom .7

    show t grey at right:
        zoom .7

    who "Hey, Taro! My piece won the last competition!"

    show t grey

    "A girl approaches him, still in uniform despite it being the weekend."

    show t happy1

    "That's great news Sawako!"

    show t grey

    "A bright smile fills her face, a canvas in her arms."

    "The painting was a gorgeous portrait of the Company's President at the time."

    "The soft strokes and detailed eyes were always part of Sawako's style."

    "This one includes deep blues and greens."

    "When Sawako was drawing, she mentioned something about the fluidity and how adaptable the President was."

    show s

    S "They said they loved the way I portrayed the President!"

    show s grey

    show t

    T  "Congrats! I'm happy for you, Sawako. Long live the President Right? haha."

    show t grey

    show s

    "Sawako's cheeks turn bright pink, and she gives Taro a hearty smile."

    S "Yes, long live indeed."

    "They both laugh at each other"

    stop music fadeout 1.0

    scene bg room
    with Fade(1.0, 1.0, 1.0, color="#FFF")

    show guard at left:
        zoom .7

    show t at right:
        zoom .7

    # Scene Change Doctor's Office

    T "After Sawako left for college, a lot changed about her."

    T "She became one of the wealthiest people in the upper sectors, under the President's salary."

    "Taro hesitates as he sits back in his seat."

    scene bg doctor
    with Fade(1.0, 0.5, 1.0, color="#000")

    play music ("audio/BLOB 3.wav") loop fadein 1.5

    show t at right:
        zoom .7

    T "(Has this office always been soo messy?)"

    "Taro's NeuroPhone buzzes again."

    show t grey

    show y at left:
        zoom .7
    with easeinleft

    Y "Taro?"

    "Yui comes back, a toolkit in her hand."

    Y "I can fix you up now."

    show y grey

    show t

    T  "You really have to clean this place up."

    show t grey

    show y

    Y  "{w=1.2}..."

    "Yui simply stares at Taro in the eyes as she starts repairing his NeuroPhone."

    Y "I won't charge you for it this time, but please be more careful."

    show t

    show y grey

    T "Thanks Yui, you're a life-saver. Literally."

    show t grey

    show y

    Y  "...{w=1.2}Stop spurting out nonsense, It's my job."

    show y grey

    "Taro sheepishly rubs the back of his head."

    "{b}{i}[Have someone special in your life? Send them a Digital Gift Card!]{/b}{/i}"

    show t

    T "N-No, It's not what you think!"

    show t grey

    show y

    Y "Sorry?"

    show y grey

    "Taro blinks for a second as his NeuroPhone buzzes."

    show t

    T "Uh... n-nothing."

    show y

    show t grey

    Y "What has gotten into you Taro?"

    show y grey

    show t

    T "I don't know, you're the one that said something about a gift card!."

    show t grey

    show y

    Y "A gift card? What are you talking about Taro?"

    Y "You must be really sick."

    Y "Get some rest then. I can fix you up later."

    show t

    show y grey

    T "Yeah...Okay, I'll do that then."

    hide t
    with easeoutright

    "After Taro leaves the building, Yui holds her own NeuroPhone to her mouth."

    stop music fadeout 1.2

    show y

    Y "...Yes, there is a man who is walking around with a faulty NeuroPhone... Taro Tanaka..."

    scene bg street 1
    with Fade(1.0, 1.0, 1.0, color="#000")

    play music ("audio/BLOB 2.wav") loop fadein 1.0

    # Scene Change Street One

    show t at right:
        zoom .7

    "Taro looks around and realises that he is in Sector 1. Taro lives in Sector 12, very far from here"

    T  "I should stop by Hikari's house instead."

    "After a few minutes of walking, he reaches Hikari's home"

    hide t
    with easeoutright

    "He walks up to the building and enters a house, a sign reading \"Sugita Residence.\""

    # Scene Change Small Computer Den

    scene bg pcden

    show t at right:
        zoom .7

    T  "Hello? Anyone home?"

    "The room is a complete mess. Several laptops were open, files were all over the floor, along with junk food wrappers. A girl sits at the desk, looking mildly disgruntled."

    show h at left:
        zoom .7

    "She swivels her chair towards Taro, running her fingers through her brown bob, her pyjamas wrinkled from sitting for too long."

    "She glares at Taro from her desk."

    show t grey

    H "Oh, it's you."

    show h grey

    show t

    T  "Hey Hikari, mind if I stay in your guest room for the night?"

    show t grey

    show h

    H "If it's one night then fine."

    show t

    show h grey

    T  "Sweet."

    show t grey

    "Taro slumps down on the couch in the room."

    show h

    H "So why are you in this sector?"

    show h grey

    show t

    T "Is it such a shock to you that I might just want to visit?"

    show h

    show t grey

    H "Well yes... You haven't spoken to me in years, let alone visted me."

    show t

    show h grey

    T "Okay well, I got hurt real bad today, so the Doc patched me up."

    show h

    show t grey

    H "And there's the reason for your freeloading."

    "Hikari turns back to her desk and starts typing out on her keyboard."

    show t

    show h grey

    T "It's not freeloading, It's you helping out a friend in need."

    show t grey

    "Hikari is just typing away at her computer, clearly not paying attention to Taro."

    show t

    T "Oh come on Hikari, don't be like that!"

    show t grey

    show h

    H "Maybe you should look at yourself first before you judge others."

    show t

    show h grey

    T "What are you talking about Hikari?"

    show t grey

    show h

    H "Well."

    "Hikari swivels her chair around to face Taro."

    H "You haven't messaged me in years, you never send me birthday wishes and you don't ever visit me."

    H "Then all of a sudden you turn up and ask for a favour when you've done nothing to help me!"

    H "It's like I barely even exist to you anymore!"

    "The sadness on Hikari's face is very obvious to Taro now."

    show h grey

    "Taro's NeuroPhone buzzes again."

    show t

    T "Hikari... I had no idea you felt this way."

    T "Why didn't you say something?"

    show t grey

    show h

    H "Because you're always on that damn NeuroPhone all day, you're too busy with it to notice anything!"

    H "You're just like everyone else, too busy to spend time with others, no matter how much I… they care about them!"

    H "Always going on about profits and stock prices. It pisses me off!"

    H "I should kick you out, but you're lucky I still consider you a friend"

    show h grey

    show t

    T "(Man, I feel really bad for what I did now.)"

    T "Hikari... I didn't mean to barge in like this."

    "Taro's NeuroPhone buzzes loudly as Hikari's fingers stop typing."

    show t grey

    show h

    H "What was that?"

    show t

    show h grey

    T "What was what?"

    show h

    show t grey

    H "That noise, don't tell me you didn't hear it?"

    show h grey

    "Taro's NeuroPhone buzzes again"

    show h

    H "There it is again!"

    "Hikari stares at Taro for a few moments, before getting up from her chair and walking up to him."

    "Taro backs off a little."

    show t

    show h grey

    T "H-h-hey, you're getting really close!"

    show t grey

    "Hikari holds Taro's arm, observing it closely."

    show h

    H "Something's wrong..."

    show h grey

    show t

    "Hikari feels Taro's NeuroPhone buzzing."

    show h

    show t grey

    H "Your NeuroPhone is acting up."

    show h grey

    show t

    T "What are you talking about? Get off me!"

    T "Nothing is wrong with mine, check yours!"

    show h

    show t grey

    H "I already told you I do-"

    show h grey

    "Hikari stops herself from talking and turns away. A flash of panic washes over her face."

    "Taro yanks his arm away from Hikari."

    show t

    T "Honestly, didn't you learn about personal space in elementary school?"

    show t grey

    show h

    "Hikari's face changes from her usual blank expression of dread."

    H "I think you should leave. Now."

    show h grey

    show t

    T "Okay then, I will! Before you try and grope me again!"

    T "Honestly, You'd think it’s your NeuroPhone that wasn't wired properly or something!"

    "Taro storms out of the house, slamming the door behind him."

    hide t
    with easeoutright

    scene bg street 1
    with Fade(1.0, 1.0, 1.0, color="#000")

    show t at right:
        zoom .7
    with easeinright

    # Scene Change Street One

    T "(Jeez, what's up with her?)"

    "Taro decides to go for a stroll around the city."

    scene bg street 2
    with PushMove(1.5, mode="pushleft")

    # Scene Change Street Two

    show t grey at right:
        zoom .7

    "Taro wandered all the way to the east end of the city."

    "Suddenly he bumps into somebody."

    with hpunch

    with Pause(1.0)

    show m at left:
        zoom .7

    M "Hey! Watch where you're go-"

    M "Taro? is that you?"

    show m grey

    show t

    T "Huh? Me?... {w=1.0} Mitsu?"

    show t grey

    show m

    M "It is you! Long time no see!"

    show t

    show m grey

    T "Oh, yeah, how's it going Mitsu?"

    scene bg room
    with Fade(1.0, 1.0, 1.0, color="#000")
    show guard at left:
        zoom .7
    show t at right:
        zoom .7
    with fade

    T "Shima Mitsu was… really something. He used to look pretty formal, his hair neat and wearing more strict clothes, even out of school."

    T "His household was always very traditional and strict. Their lifestyle affected Mitsu in school, but now that he was out..."

    T "He practically looked like a supermodel when I saw him."

    scene bg street 2
    show t at right:
        zoom .7
    show m at left:
        zoom .7
    with Fade(1.0, 1.0, 1.0, color="#000")

    "Taro almost didn't recognise him. The boy who used to wear his school uniform everywhere now was much more mainstream."

    show t grey

    M "Been doing pretty good! And you?"

    show t

    show m grey

    T "Yeah you know, just being stabbed and all. What's up with the hair?"

    show t grey

    show m

    M "Oh this? Yeah I dyed it."

    show t

    show m grey

    T "Why would you do something like that?"

    show m

    show t grey

    M "Cuz it looks cool haha, also the prez is rockin this hairdo as well."

    show m grey

    "Taro's NeuroPhone buzzes."

    show t

    T "I think you look like Yakuza."

    show m

    show t grey

    M "Yakuza?! What are you trying to get at?"

    show m grey

    show t

    "Taro's NeuroPhone buzzes again."

    T "Oh uh.. nothing... sorry I gotta go!"

    "Taro runs down the street."

    hide t
    with easeoutright

    show m

    M "Hey wait! Get your ass over here!"

    show m grey

    m5 "Ahhh! It's him!"

    show m4 at right:
        xalign .5
        zoom .7
    show m5 at right:
        xalign .8
        zoom .7
    with easeinright

    m4 "Shima! I love you!!"

    show m

    M "Hey, get off me! Taro wait!"

    scene bg street 3

    # Scene Change Street Three

    show t at right:
        zoom .7

    T  "I-I think I'm gonna puke."

    "Taro's NeuroPhone is buzzing like crazy now."

    T "God what is up with this thing?"

    "He holds his arm up to see what's going on"

    "Taro notices that his NeuroPhone is sparking and making static noises."

    T "When did it get this badly beaten up?"

    T "I need to take a breather..."

    "Taro heads to the skywalk."

    scene bg skywalk
    with PushMove(1.5, mode="pushleft")

    # Scene Change Skywalk, Looking down

    show t at right:
        zoom .7

    "Taro sits down on the edge of the skywalk, looking down at the city."

    T  "I never realized how loud this place was..."

    scene bg lookup
    with PushMove(1.5, mode="pushdown")

    show t at right:
        zoom .7

    # Scene Change Looking up into the city from the ground

    "Looking up, he could see the streets and paths intertwining with each other. The lights of the city were blinding from this angle."

    T  "I don't remember this place being such an eye-sore."

    "He closes his eyes briefly. All those things Hikari said became clear to him."

    T "I need to go see her."

    # Scene Change Computer Den

    scene bg pcden
    show t at right:
        zoom .7
    with Fade(1.0, 1.0, 1.0, color="#000")

    T "Hikari! I need to talk to you!"

    show h at left:
        zoom .7
    with easeinleft

    H "I told you to leave!"

    show h grey

    show t

    T "This is important! I'm sorry for never visiting you, I'm sorry for never messaging you."

    T "And I'm sorry I never wished you happy birthday...{w=2.0} including today."

    T "Happy birthday Hikari."

    show t grey

    show h

    "Hikari blinks and stares at Taro for a second."

    H "Taro..."

    "Hikari snaps out of it and stands up from her desk."

    H "No, Taro, you need to leave now! They're after you!"

    show h grey

    show t

    T "Who is they?"

    show h

    show t grey

    H "There is no time to explain, you need to hide!"

    show h grey

    show t

    T "But where would I go?"

    show h

    show t grey

    H "Near the west side of the city is my studio, you'll be safe there!"

    H "Head there now, Hurry!"

    show h grey

    show t

    T  "Got it, I'll head there right now!"

    show h

    show t grey

    stop music fadeout 1.0

    H "...Wait. Taro."

    H "Thanks."

    show t smile

    "Taro gives Hikari a cheeky grin before running off."

    hide t
    with easeoutright

    scene bg street 4

    show t at right:
        zoom .7
    with easeinright

    play music ("audio/BLOB 1.wav") loop fadein 1.0

    "As Taro is running through the streets, bumping into loads of people, he stumbles onto the ground."

    # Scene Change Street Four

    "It was only a matter of minutes before Taro heard the sirens go off."

    "He gets up and starts running away, only to hear cars going after him."

    "He only stops when a helicopter suddenly lands much too close, and he's knocked backward, nearly falling over."

    "The helicopter… It had the Company's logo on it."

    "A girl on a microphone sticks her head out."

    show t grey

    show c grey at left:
        zoom .7

    with easeinleft


    who  "Hey! Get in."

    "Taro hesitates, about to scramble backward, but the police sirens are getting louder."

    who  "You're gonna get caught if you don't come in."

    "He reluctantly runs over to the helicopter, the girl pulling him in. She motions to the pilot, who quickly begins to lift off."

    stop music fadeout 1.0

    scene bg helicopter
    show t grey at right:
        zoom .7
    show c grey at left:
        zoom .7
    with pushup

    # Scene Change Helicopte


    "A silence fills the air as the girl beside him settles down, rather elegantly."

    show t

    T  "Who.. are you?"

    show t grey

    show c

    C "You can call me Chiisato."

    show t sad

    "Taro frowns deeply, staring straight at her."

    T  "...Why did you save me?"

    show t grey

    show c

    C "I can't help but be a little curious about someone who managed to go under the radar of our security and somehow disable their NeuroPhone."

    show t hurt

    show c grey

    T "It wasn't me who did it!"

    show t grey

    show c

    C "The signs don't lie."

    "Chiisato points to his NeuroPhone arm, buzzing and sparking."

    show t hurt

    show c grey

    T "I don't know how it got like this, Honest!"

    show t grey

    show c

    C "Likely story."

    show t hurt

    show c grey

    T "It's the truth, I swear!"

    show t grey

    show c

    C "We'll see about that when we land."

    show t sad

    show c grey

    T "Where are you taking me?"

    show t grey

    "Chiisato remains silent. The only sounds Taro hears now are the sounds of the helicopter rotors."

    "After what seemed like hours, the helicopter lands and the guards grab Taro by the arms as Chiisato steps out."

    "The guards follow Chiisato as she walks through a door."

    play music ("audio/BLOB 5.wav") loop fadein 1.0

    # Scene Change Restaurant

    scene bg restaurant
    with pushdown

    show t at right:
        zoom .7

    show c at left:
        zoom .7

    "The guards seat Taro opposite to Chiisato, in what seems like a fancy restaurant."

    show t grey

    C "We'll take two orders of lamb, and two glasses of Bandol rosé."

    show c grey

    show t

    T  "...This place is way too fancy..."

    show c

    show t grey

    C "Now then... care to explain how you got your NeuroPhone damaged?"

    show t

    show c grey

    T  "I already told you, I don't know!"

    show c

    show t grey

    C "You are testing my patience boy."

    C "Don't pretend like I don't know you were conspiring with your little friend Miss Hikari"

    show t

    show c grey

    "Taro's face pales as she brings up her names. How much did she know about him?"

    "Chiisato seems to smirk at his reaction."

    show c

    show t grey

    C "It's pretty easy to track people with NeuroPhones. After all, we take their information for safety reasons."

    C "As for your friend… I can't guarantee that she will be safe anymore."

    C "We, the Company, are here to ensure that everybody is guaranteed safety aand security in their lives. We can't have people like you two compromising that."

    "Chiisato takes a sip of the glass beside her, casually staring out the window."

    C "It's about time for you to go."

    show t

    show c grey

    T  "Go where..?"

    show c grey

    show guard at left:
        zoom .7
        xalign .2

    m1 "I'll take it from here."

    "The agent points a gun at Taro, and before he can react, he blacks out."

    scene bg room
    with Fade(1.0, 1.0, 1.0, color="#000")

    # Scene Change Blackout

    stop music fadeout 1.0

    show t at right:
        zoom .7
    "Taro wakes up in an extremely dark room, everything but the agent is pitch black"

    with Pause(1.0)

    show guard at left:
        zoom .7
    with easeinleft

    show t grey

    m1 "Thank you. We'll take everything from here. Please rest while we fix your NeuroPhone and help you forget."

    show t

    T  "What are you ging to do with me?..."

    show t grey

    m1 "We are simply going to erase your memories and then repair your NeuroPhone so you can go on about your normal daily life."

    m1 "Please do not resist as we are authorized to use lethal force if necessary"

    m1 "But before we proceed with the procedure, I am going to require you to tell me everything that happened to you up until now."

    "Taro's mind blacks out for a moment as he reminisces about the past"

    # Scene Change Nice Looking house

    stop music fadeout 1.0

    scene bg nicehouse
    show t at right:
        zoom .7
    show h grey at left:
        zoom .7
    with Fade(1.0, 1.5, 1.0, color="#FFF")

    play music ("audio/song.mp3") loop fadein 1.0

    YoungT  "Hikari! What did you put down for your future job homework?"

    show t grey

    show h

    YoungH "I want to be a teacher one day! So, I can help people like Mrs Nakamura does. After all, she taught me a lot of what I know today! What about you, Taro?"

    show t

    show h grey

    YoungT  "I think I want to be a police officer! That way, I can beat up bad guys who hurt other people. I want to protect good people!"

    show t grey

    show h

    YoungH "Do you really think we can be a teacher and a cop?"

    show t

    show h grey

    YoungT  "Well, we both want to help good people, and I think we're good people. So, I think we will!"

    scene bg room
    with Fade(1.0, 1.0, 1.0, color="#000")
    stop music fadeout 1.0

    return
