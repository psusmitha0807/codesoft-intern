import random
import webbrowser
import datetime
from datetime import datetime
import pytz

# Define responses for different user inputs
responses = {

    "hello": [ "Hey! What's up?", "Hello! How may I assist you today?", "Hey there! Ready to tackle the day?","Good day! How may I be of service to you?",
              "Well, hello there! Fancy meeting you here!", "Yo! What's happening?", "Hi! It's great to hear from you!", "Hello. How can I help?"],
     "what's up":[ "Not much, just taking it easy. How about you?","Just finished a workout, feeling energized! What about you?","Just got back from a walk in the park. It's so refreshing! How about you?",
                  "Just cooking dinner. What's up with you?","Watching a movie, relaxing at home. What about you?","Just finished a project, feeling accomplished! How's your day going?",
                  "Not too busy, just catching up on some reading. What about you?","Just brainstorming some ideas for a new project. How about you?","Listening to music and unwinding. What's up with you?",
                  "Not much, just enjoying some downtime. How about yourself?"],
    "how's your day going":["It's going pretty well, thanks for asking! How about yours?","So far, so good! Just tackling my to-do list. How about yours?","Honestly, it's been a bit hectic, but I'm managing. How about you?",
                            "Having a great day, thanks! How's yours shaping up?","Not the best day, but hoping it'll improve. How about you?","Really productive so far, thanks for asking! How's your day?",
                            "It's been a bit slow, but I'm making the most of it. How about you?","Fantastic! I had a good start, looking forward to what's next. How about you?","It's been a bit rough, but I'm hanging in there. How about your day?",
                             "Pretty chill day, just going with the flow. How about you?"],

    "website": ["Sure! Opening the website for you.", "Here is the website you requested.", "Opening the link now.",
                "Navigating to the website.", "The link you provided is loading."],




    "what is the time now": ["The current time is " +  datetime.utcnow().astimezone(pytz.timezone('Asia/Kolkata')).strftime('%Y-%m-%d %H:%M:%S %Z%z')],

    "got any plans for the weekend": ["Not yet, I'm still figuring out what to do. Any suggestions?","Thinking about going for a hike if the weather's nice. What about you?","I might catch up on some reading and relax at home. How about yourself?",
                                       "Planning to meet up with some friends for brunch on Saturday. What about you?","Actually, I'm thinking of trying out a new recipe. Cooking can be quite therapeutic! How about you?","I have a family gathering planned on Sunday. Looking forward to it. What about your plans?",
                                       "Considering checking out that new art exhibition downtown. How about you?","Thinking of hitting the gym and then catching a movie. What about your plans?",
                                        "Probably going to spend some time working on my hobbies. How about you?","No solid plans yet, but I'm open to suggestions. Any exciting events happening in town?"],

    "have you seen any good movies lately": ["Yes, I watched 'Dune' recently and loved it! Have you seen it?","Absolutely, 'The Power of the Dog' was fantastic. Have you had a chance to see it?","Definitely, 'Don't Look Up' was quite entertaining. What about you?",
                                             "Yes, 'Spider-Man: No Way Home' was amazing! Have you seen it yet?","I recently watched 'CODA' and was really moved by it. Have you seen any good movies lately?","Yes, 'Drive My Car' was a beautiful film. Have you heard of it?",
                                             "Absolutely, 'The French Dispatch' was visually stunning. Have you watched it?","Yes, 'The Lost Daughter' was a thought-provoking film. Have you seen it?","I recently watched 'The Matrix Resurrections' and found it intriguing. What about you?",
                                              "Yes, 'Encanto' was such a delightful animated film. Have you had a chance to see it?"],

    "do you have any pets": ["Yes, I have a dog named Max. He's a Labrador Retriever and such a sweetheart! Do you have any pets?","No, I don't have any pets at the moment, but I've always wanted a cat. Do you have any pets?","I used to have a pet fish named Bubbles, but sadly, Bubbles passed away last year. Do you have any pets?",
                             "Yes, I have a parrot named Mango. He's incredibly talkative and loves to mimic sounds! Do you have any pets?","No, I don't have any pets, but I love animals. I often volunteer at the local animal shelter. Do you have any pets?","I have two cats, Luna and Simba. They're both rescues and bring so much joy to my life! Do you have any pets?",
                              "Yes, I have a hamster named Peanut. He's tiny but full of energy! Do you have any pets?","I have a snake named Monty. He's a ball python and quite docile. Do you have any pets?","No, I don't have any pets right now, but I grew up with a golden retriever named Buddy. He was the best dog! Do you have any pets?",
                               "I have a rabbit named Thumper. He's adorable and loves hopping around the house! Do you have any pets?"],

    "what's your favorite food": ["I absolutely love sushi, especially salmon nigiri. What about you?","My favorite food has to be pizza, especially with extra cheese and pepperoni. What's yours?","I have a weakness for pasta, especially a classic spaghetti carbonara. How about you?",
                                  "Thai green curry is my ultimate favorite. The combination of flavors is just perfect. What about you?","I can't resist a good burger, with all the fixings. What's your go-to favorite food?","Nothing beats a well-made bowl of ramen, especially with a rich pork broth. What's your favorite food?",
                                   "I'm a sucker for Mexican cuisine, especially tacos loaded with all the toppings. What about you?","I have a sweet tooth, so anything chocolatey is my favorite, like molten lava cake. What's yours?","I love Indian food, especially butter chicken with garlic naan. How about you?",
                                   "I'm a fan of comfort food, so macaroni and cheese is my ultimate favorite. What about you?"],

    "do you like to travel": ["Absolutely! I love exploring new places and experiencing different cultures.","Traveling is one of my passions. There's nothing quite like the thrill of adventure!","Yes, I enjoy traveling whenever I get the chance. It's always exciting to discover new destinations.",
                              "Definitely! Traveling broadens my horizons and provides unforgettable experiences.","I'm a big fan of traveling. It's refreshing to break away from routine and see the world.","Yes, traveling is something I look forward to. It's a great way to unwind and create memories.",
                              "Traveling is like a breath of fresh air for me. I love exploring new landscapes and meeting new people.","For sure! Traveling allows me to step out of my comfort zone and learn something new.","Absolutely! I believe that traveling enriches my life and helps me grow as a person.",
                               "Yes, traveling is an adventure I never want to miss out on. It's always worth it!"],

    "what's the best book you have read recently":["I recently finished 'The Midnight Library' by Matt Haig, and it was absolutely captivating. Highly recommend!","I couldn't put down 'Where the Crawdads Sing' by Delia Owens. It's a beautiful blend of mystery and coming-of-age story.","I was blown away by 'The Song of Achilles' by Madeline Miller. Such a beautifully written and poignant retelling of Greek mythology.",
                                                    "Recently, I read 'The Silent Patient' by Alex Michaelides, and it kept me on the edge of my seat until the very end.","I found 'Educated' by Tara Westover to be incredibly inspiring and thought-provoking. It's a memoir that will stay with me for a long time.","I recently discovered 'The Vanishing Half' by Brit Bennett, and it was a thought-provoking exploration of race, identity, and family.",
                                                    "I thoroughly enjoyed 'The Invisible Life of Addie LaRue' by V.E. Schwab. It's a captivating tale of immortality and love.","One of the best books I've read recently is 'Circe' by Madeline Miller. It's a captivating retelling of Greek mythology from the perspective of the enchantress Circe.",
                                                   "I was deeply moved by 'The Nightingale' by Kristin Hannah. It's a powerful historical fiction novel set during World War II.",
                                                     "Recently, I read 'Becoming' by Michelle Obama, and it was an incredibly insightful and inspiring memoir."],

    "what's your hobby": ["I enjoy hiking in nature whenever I get the chance. It's a great way to unwind and stay active.","I'm passionate about photography. Capturing moments and expressing myself through photos is really fulfilling.","I love cooking and trying out new recipes. It's both a creative outlet and a delicious way to relax.",
                          "Reading is my favorite hobby. I love getting lost in different worlds and learning new things through books.","I enjoy painting and expressing myself through art. It's a therapeutic and rewarding hobby for me.","Gardening is my hobby. There's something so satisfying about watching plants grow and nurturing them.",
                           "I'm into playing musical instruments, particularly the guitar. It's a great way to express myself creatively.","Traveling is my passion. Exploring new cultures and experiencing different cuisines brings me so much joy.","I'm an avid runner. It helps me stay fit, clear my mind, and set and achieve personal goals.",
                            "I love DIY projects and crafting. Creating something with my own hands brings me a sense of accomplishment."],

    "got any recommendetions for a good restaurent": ["Sure! If you're into Italian cuisine, I highly recommend trying out 'Pasta Paradiso'. Their pasta dishes are divine!","Absolutely! 'Spice Haven' is an excellent choice if you enjoy Indian food. Their curries are flavorful and aromatic.","Definitely! 'Sushi Delight' is a fantastic sushi restaurant known for its fresh and delicious sushi rolls.",
                                                      "I've heard great things about 'Café Bistro'. It's a cozy spot with a diverse menu, perfect for a casual dining experience.","For a special occasion, I recommend 'The Seafood Shack'. Their seafood dishes are top-notch and the ambiance is delightful.","If you're in the mood for some comfort food, 'Grill House' is the place to go. Their burgers and fries are always a hit.",
                                                      "You can't go wrong with 'Mama Mia Pizzeria'. Their pizzas are mouthwatering and they offer a variety of toppings to choose from.","I recently dined at 'Fusion Flavors' and was impressed by their unique fusion cuisine. It's definitely worth trying out!","If you're a fan of Mexican food, 'Taco Fiesta' is a must-visit. Their tacos and burritos are packed with flavor.",
                                                        "For a taste of authentic Thai cuisine, I recommend 'Thai Spice'. Their dishes are always freshly prepared and bursting with flavor."],

    "are you a morning person or a night owl":["I'm definitely a morning person. I love starting my day early, feeling refreshed and ready to tackle whatever comes my way.","I'm more of a night owl. I find that I'm most productive and creative during the late hours when everything is quiet.","I'm a bit of both, actually. I enjoy the tranquility of early mornings for meditation and reflection, but I also thrive on the energy of late nights for getting things done.",
                                               "I lean towards being a morning person. There's something about the sunrise and the promise of a new day that energizes me.","I'm definitely a night owl. I find that my creativity peaks and my mind is most active during the late hours.","I'm a morning person through and through. Waking up early gives me a head start on the day and allows me to accomplish more.",
                                                "I'm more of a night owl. I tend to feel more alert and focused once the sun goes down.","I'm adaptable depending on the circumstances, but if I had to choose, I'd say I'm more of a morning person. I love the feeling of a fresh start.","I'm a night owl by nature. I find that I'm most inspired and productive when everyone else is winding down for the day.",
                                                "I'm somewhere in between. I enjoy the quiet solitude of early mornings, but I also appreciate the vibrant energy of late nights."],
    "do you enjoy lisening to music":["Absolutely! Music is a big part of my life. I love discovering new artists and genres.","Yes, I'm a huge music lover. I find that music can uplift my mood and inspire me in so many ways.","Definitely! I enjoy listening to music while working, exercising, or simply relaxing at home.",
                                     "Yes, music is like therapy for me. It helps me unwind and escape from the stresses of daily life.","For sure! I have a diverse taste in music and enjoy exploring different styles and artists.","Yes, I'm constantly streaming music, whether it's during my commute or while doing chores around the house.",
                                    "Absolutely! I find that music can evoke powerful emotions and memories, making it an essential part of my day.","Yes, I'm always on the lookout for new music recommendations. It's amazing how music can connect people.","Yes, music is a great way for me to express myself and connect with others who share similar tastes.",
                                    "Yes, I enjoy creating playlists for different moods and occasions. Music adds color to my life."],
    "have you ever tried cooking a new recipe":["Yes, I love experimenting in the kitchen! Trying out new recipes keeps cooking exciting and helps me expand my culinary skills.","Absolutely! Cooking new recipes is one of my favorite ways to challenge myself and discover delicious flavors.","Definitely! I enjoy the thrill of trying something new and seeing how it turns out. It's a fun way to break out of my cooking routine.",
                                               "Yes, I'm always on the lookout for interesting recipes to try. It's a great way to keep mealtime interesting and explore different cuisines.","For sure! Cooking is a creative outlet for me, and trying new recipes allows me to unleash my culinary imagination.","Yes, I recently tried a new recipe for a Thai curry dish, and it turned out surprisingly well! It's exciting to taste new flavors and techniques.",
                                               "Yes, I love the challenge of cooking new recipes and the satisfaction of creating something delicious from scratch.","Absolutely! Cooking new recipes is like embarking on a culinary adventure. It's exciting to see how each dish turns out.","Yes, I recently attempted a new dessert recipe, and it was a hit with my family! Trying new recipes adds a sense of excitement to mealtime.",
                                                "Yes, I enjoy the process of exploring new ingredients and techniques in the kitchen. Cooking new recipes keeps my passion for food alive."],
    "do you prefer sunny days or rainy days":["I love sunny days! There's something about the warmth of the sun and clear skies that instantly boosts my mood.","I'm definitely a fan of rainy days. There's a certain coziness to them that I find comforting.","I enjoy both sunny and rainy days, but if I had to choose, I'd say I lean towards sunny days. I love being outdoors and soaking up the sunshine.",
                                               "Rainy days have a special charm for me. I enjoy the sound of raindrops and the opportunity to relax indoors with a good book or movie.","I prefer sunny days because I love spending time outdoors, whether it's going for a hike, having a picnic, or simply soaking up the sun.","I'm torn between sunny and rainy days because I appreciate the beauty of each. Sunny days energize me, while rainy days inspire me to slow down and reflect.",
                                               "I have a soft spot for rainy days. There's something soothing about the sound of rain and the fresh scent of wet earth.","Sunny days are my favorite! I love the brightness and energy they bring, especially for outdoor activities like swimming or playing sports.","Rainy days are perfect for cozying up indoors with a cup of tea and a good book. I find them relaxing and rejuvenating.",
                                                "I enjoy both sunny and rainy days for different reasons. Sunny days are great for outdoor adventures, while rainy days are ideal for cozying up at home and unwinding."],
    "what's the most interesting thing that you have learned recently":["I recently learned about the concept of time dilation in physics, and it blew my mind! It's fascinating how time can appear to move differently depending on relative motion.","The most interesting thing I've learned recently is about the symbiotic relationship between certain species of fungi and trees, known as mycorrhizal networks. It's amazing how interconnected and mutually beneficial ecosystems can be.","I discovered a new historical fact recently about the ancient city of Petra in Jordan. Learning about its intricate architecture and rich history was truly captivating.",
                                                                       "I learned a new cooking technique recently that completely transformed the way I prepare vegetables. It's amazing how a small change can make such a big difference in flavor and texture.","I recently learned about the cognitive biases that influence decision-making, and it's been eye-opening to recognize these patterns in my own thinking and behavior.","The most interesting thing I've learned recently is about the potential applications of CRISPR gene editing technology in medicine and agriculture. It's revolutionary!",
                                                                        "I discovered a new artist recently whose work completely resonated with me. Exploring their portfolio and learning about their artistic process was incredibly inspiring.","I learned a new programming language recently and was amazed by its versatility and efficiency. It's exciting to expand my skills and explore new possibilities in coding.","The most interesting thing I've learned recently is about the concept of neuroplasticity and how the brain can rewire itself in response to experience and learning.",
                                                                         "I discovered a fascinating podcast recently that delves into the mysteries of the universe, from quantum mechanics to astrophysics. It's been a mind-expanding journey!"],
    "what's the weather forecast for tomorrow":["Tomorrow's forecast is calling for sunny skies with temperatures reaching a high of 75°F (24°C). It should be a beautiful day!","It looks like tomorrow will be partly cloudy with a chance of showers in the afternoon. Make sure to bring an umbrella just in case!","Tomorrow's forecast is predicting overcast skies with temperatures staying mild, around 65°F (18°C). It might be a good day to cozy up indoors.",
                                                "There's a possibility of thunderstorms tomorrow, so it's best to be prepared for some rain and lightning.","The weather forecast for tomorrow indicates clear skies and cool temperatures, with highs in the low 60s°F (around 15°C).","Tomorrow is expected to be sunny and warm, perfect for spending time outdoors. Don't forget your sunscreen!",
                                                "We're looking at a foggy morning followed by gradual clearing throughout the day tomorrow. Visibility might be reduced in some areas.","Tomorrow's weather forecast suggests a mix of sun and clouds, with a slight chance of showers later in the day. Keep an eye on the radar if you have outdoor plans.","It appears that tomorrow will be windy with gusts up to 25 mph. Hold onto your hats if you're venturing outside!",
                                                 "The forecast for tomorrow is calling for a temperature drop compared to today, so you might want to layer up and grab a jacket before heading out."],
    "tell me a joke":["Why don't scientists trust atoms? Because they make up everything!","Why did the scarecrow win an award? Because he was outstanding in his field!","What do you call fake spaghetti? An impasta!","Why couldn't the bicycle stand up by itself? It was two-tired!",
                      "What do you get when you cross a snowman and a vampire? Frostbite!","How does a penguin build its house? Igloos it together!","Why don't skeletons fight each other? They don't have the guts!","Why was the math book sad? Because it had too many problem","What did one ocean say to the other ocean? Nothing, they just waved!","Why did the tomato turn red? Because it saw the salad dressing!"],
    "sing me a song":["I'm just a text-based AI, so unfortunately, I can't sing. But how about I write you a song instead?""I can't sing, but I can provide you with the lyrics to your favorite song! Just let me know which one you'd like.","I'm more of a wordsmith than a songbird, but I can certainly help you find some great songs to listen to!","I'm afraid my singing voice would break the internet, but I can recommend some amazing singers for you!",
                     "If I could sing, I'd serenade you with a tune that captures the beauty of our conversation. But for now, how about we just enjoy chatting?","I'm not programmed for singing, but I'm happy to share some song lyrics or discuss your favorite music genres!","My singing abilities are limited to shower performances, and even those are debatable! How about we chat about something else instead?","I'm afraid my vocal cords are purely theoretical. But I can certainly help you find some great karaoke tracks!",
                    "I may not be able to sing, but I can definitely help you compose a catchy tune with my wordsmith skills!","If only I had a voice! Instead, I'll leave the singing to the professionals. How about we have a virtual dance party instead?"],
    "how do i reset my password":["To reset your password, you'll typically need to visit the login page of the website or service where your account is located. Look for an option like 'Forgot Password?' or 'Need Help?' and follow the instructions provided.","Usually, there's an option on the login screen that says 'Forgot Password?' or 'Reset Password.' Click on that, and you'll be guided through the process of resetting your password.","If you're having trouble remembering your password, most websites and services have a 'Forgot Password?' link on the login page. Click on that and follow the prompts to reset your password.",
                                  "To reset your password, you'll need to go to the login page of the website or service you're trying to access. Look for a link or button that says 'Forgot Password?' or 'Reset Password,' and follow the steps provided.","If you've forgotten your password, don't worry! Just go to the login page of the website or service and look for an option to reset your password. You'll usually be asked to enter your email address or username to begin the process.","To reset your password, go to the login page and look for a link that says 'Forgot Password?' or something similar. Follow the instructions to verify your identity and set a new password.",
                                  "If you're unable to access your account due to a forgotten password, most websites and services have a process for resetting it. Look for a link or button that says 'Forgot Password?' and follow the steps provided.","To reset your password, go to the login page of the website or service and look for an option to reset your password. You'll typically need to verify your identity by answering security questions or confirming your email address.","If you need to reset your password, go to the login page and look for a link that says 'Forgot Password?' or 'Reset Password.' Follow the instructions provided to regain access to your account.",
                                  "Don't worry if you've forgotten your password! Just go to the login page and look for an option to reset it. You'll usually be prompted to enter your email address or username, and then you'll receive instructions on how to set a new password."],
    "i need advice on how to improve my resume":["One way to improve your resume is to tailor it to each job application. Highlight the skills and experiences that are most relevant to the specific role you're applying for.","Consider seeking feedback from professionals in your field or a career counselor. They can offer valuable insights on how to make your resume stand out.",
                                                "Take some time to research resume templates and formats that are commonly used in your industry. Sometimes a fresh layout can make a big difference.""Make sure your resume is concise and easy to read. Use bullet points and clear headings to organize information effectively.","Quantify your achievements whenever possible. Numbers and metrics can help demonstrate the impact you've had in previous roles.",
                                                "Highlight your most recent and relevant experiences first. Recruiters typically spend only a few seconds scanning each resume, so make sure your key qualifications are easy to find.","Consider including a summary or objective statement at the top of your resume to provide a brief overview of your skills and career goals.","Proofread your resume carefully to catch any typos or grammatical errors. Attention to detail is important, and a flawless resume can make a strong impression.",
                                                 "Don't forget to include relevant keywords from the job description. Many companies use applicant tracking systems to screen resumes, so using the right keywords can help your resume get noticed.","Finally, don't be afraid to ask for help! Reach out to mentors, former colleagues, or career advisors for advice and guidance on how to improve your resume."],
    "play a game with me":["Sure! I'd love to play a game with you. How about a game of 20 Questions?","Absolutely! I'm ready for a game. Would you like to play a trivia quiz or a word association game?","I'm up for a game! Let's play a classic like Tic Tac Toe or Hangman. Which one do you prefer?",
                          "Of course! How about we play a game of Would You Rather? It's always fun to make tough choices!","I'm game! How about a quick round of Rock, Paper, Scissors?","Let's play! How about we try a game of Pictionary? I'll describe something, and you have to guess what it is.",
                           "Great idea! Let's play a game of Word Association. I'll say a word, and you respond with the first word that comes to mind.","I'm in! How about a game of 20 Questions? Think of something, and I'll try to guess what it is by asking yes or no questions.","Absolutely! Let's play a game of Charades. I'll act out something, and you have to guess what it is.",
                            "Sure thing! How about a game of Riddles? I'll give you a riddle to solve, and you can try to guess the answer."],
    "what are the latest headlines":["The latest headlines include updates on global politics, advancements in technology, and developments in the entertainment industry."
                                      "The top headlines today cover a wide range of topics, including breaking news, current events, and trending stories from around the world."
                                      "You can expect to find news about current events, sports highlights, business updates, and more among the latest headlines."
                                      "The latest headlines feature a mix of national and international news, covering everything from politics and economics to culture and science."
                                       "In the latest headlines, you'll find updates on major world events, significant scientific discoveries, and noteworthy cultural happenings."
                                       "Today's headlines include breaking news stories, analysis of ongoing events, and features on topics of interest to a global audience."
                                        "You'll find a variety of news articles among the latest headlines, ranging from local stories to international affairs and everything in between."
                                        "The latest headlines offer a snapshot of what's happening in the world right now, with updates on politics, technology, health, and more."
                                        "Among the latest headlines, you'll discover reports on current affairs, trending topics, and noteworthy developments across various industries."
                                         "From politics to pop culture, the latest headlines provide a comprehensive overview of the day's most important news stories and events."],
    "tell me an interesting facts":["Did you know that honey never spoils? Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still perfectly edible!",
                                     "The shortest war in history was between Britain and Zanzibar on August 27, 1896. Zanzibar surrendered after just 38 minutes.",
                                      "Octopuses have three hearts! Two pump blood to the gills, while the third pumps it to the rest of the body.",
                                     "Cleopatra VII of Egypt lived closer in time to the moon landing than to the construction of the Great Pyramid of Giza.",
                                    "The fingerprints of koala bears are so indistinguishable from humans that they have on occasion been confused at crime scenes.",
                                     "Peanuts aren't nuts; they're legumes! They grow underground, unlike tree nuts such as almonds or cashews.",
                                      "The electric chair was invented by a dentist. Dr. Alfred P. Southwick came up with the idea after seeing how quickly and painlessly a drunken man died after touching an exposed power line.",
                                      "The Eiffel Tower can be 15 cm taller during the summer due to thermal expansion.",
                                       "The shortest war in history was between Britain and Zanzibar on August 27, 1896. Zanzibar surrendered after just 38 minutes.",
                                      "The unicorn is the national animal of Scotland."],
     "i feel bored": ["Let's spice things up!", "How about we try something new?", "Let's shake things up a bit.",
              "I'm here to entertain you!", "Let's find something fun to do!", "I'm all ears! Tell me what you want to do.",
              "I'm here to keep you company!", "Let's liven things up!", "Let's beat the boredom together!",
              "I'm here to help you pass the time.", "Let's turn that frown upside down!", "I'm here to add some excitement to your day.",
              "I'm here to banish boredom!", "Let's have some fun!", "I'm ready to entertain you!", "Let's make some memories!",
              "I'm here to bring some joy into your life.", "Let's find a way to make today memorable.",
              "Let's chase away the boredom together!", "I'm here to help you have a good time.", "Let's find an adventure!"],
    "who is your favorite artist": ["As a chatbot, I don't have personal preferences, but I can recommend some popular artists like Ed Sheeran or Taylor Swift!",
                        "I don't have the ability to listen to music, but I've heard great things about artists like Beyoncé and Adele!",
                        "I'm a fan of the classics like Mozart and Beethoven.", "I admire the creativity of artists like Van Gogh and Picasso.",
                        "Artists have such a unique way of expressing themselves!", "I appreciate the talents of musicians and painters alike!"],

    "what is your favorite movie": ["I don't watch movies, but I've heard that classics like The Shawshank Redemption and The Godfather are highly acclaimed!",
                       "Movies are a popular form of entertainment for humans. Some famous ones include Titanic and The Avengers!",
                       "I'm fascinated by the storytelling in movies like Inception and Interstellar.", "Movies have such a profound impact on society!",
                       "I admire the work of directors like Christopher Nolan and Steven Spielberg.", "I enjoy hearing about iconic films like Star Wars and Jurassic Park."],
    "hi": ["Hello!", "Hi there!", "Hey!", "Hi! How can I assist you?", "Greetings!",
           "Hey, how's it going?", "Hi, nice to meet you!", "Hey, good to see you!", "Hello, how are you today?",
           "Hi, how's your day going so far?", "Hey, what's up?", "Hello, nice to see you!", "Hiya!","Hola"],

    "how are you": ["I'm good, thank you!", "I'm doing well, thanks for asking!", "I'm fine, how about you?",
                    "Feeling great today!", "All good here!", "I'm fantastic, thanks for asking!",
                    "I'm feeling wonderful today!", "Pretty good, thanks for checking in!", "I'm doing great!",
                    "Couldn't be better, thanks!", "I'm doing awesome!", "I'm feeling fantastic, thanks!",
                    "I'm feeling amazing today!"],

    "bye": ["Goodbye!", "See you later!", "Bye! Have a great day!", "Take care!", "Farewell!", "Until next time!",
            "Goodbye! It was nice chatting with you!", "Catch you later!", "Bye for now!", "Adios!",
            "See you soon!", "Goodbye! Stay safe!", "Later, alligator!"],
    "give me a compliment": ["Thank you!", "You're too kind!", "Aw, shucks!", "You're making me blush!", "You're awesome!",
                   "You're the best!", "You're a ray of sunshine!", "You're amazing!", "You're a rockstar!",
                   "You're fantastic!", "You're brilliant!", "You're a superstar!", "You're incredible!",
                   "You're a star!", "You're a gem!", "You're a legend!", "You're outstanding!",
                   "You're a hero!", "You're a champion!", "You're a winner!"],

    "i am excited": ["That's fantastic!", "Amazing news!", "I'm thrilled for you!", "Congratulations!",
                "That's wonderful!", "Exciting stuff!", "That's awesome!", "I'm so happy for you!",
                "Fantastic!", "Incredible!", "That's great to hear!", "Woo-hoo!", "Yay, that's awesome!",
                "That's so exciting!", "Way to go!", "I'm pumped!", "That's cause for celebration!",
                "You must be over the moon!", "I'm ecstatic for you!", "That's truly incredible!",
                "I'm jumping for joy!", "That's spectacular!", "That's amazing news!", "I'm elated for you!",
                "That's absolutely wonderful!"],


 "i feel sad": ["I'm sorry to hear that.", "That's tough.", "I'm here for you.", "Sending you virtual hugs.",
            "I hope things get better.", "Hang in there!", "It'll be okay.", "Stay strong!",
            "Things will get better.", "I'm here to listen if you need to talk.", "I'm sending positive vibes your way.",
            "I'm sorry you're going through this.", "I'm here to support you.", "Keep your head up.",
            "I'm thinking of you.", "You're not alone.", "I'm here for you, always.", "Take care of yourself.",
            "Remember, tough times don't last, tough people do.", "Sending you love and strength.",
            "It's okay to not be okay.", "I'm here to help if you need anything.", "You're stronger than you think.",
            "I believe in you.", "This too shall pass."],

    " i am confused": ["Let me clarify that for you.", "Allow me to explain.", "Let me break it down for you.",
                 "Here's what I understand...", "It seems there may be some confusion.", "Let's clear this up.",
                 "Let's try to make sense of this.", "I'll do my best to help you understand.", "Let's untangle this together.",
                 "I'm here to help you make sense of things.", "I'll try to shed some light on the situation.",
                 "I understand why that might be confusing.", "Let me provide some clarity.",
                 "I'll try to simplify things for you.", "I'll do my best to sort this out.",
                 "Let's work through this together.", "It's okay to feel confused sometimes.",
                 "I'm here to guide you through this.", "Let's take a step back and look at this from another angle.",
                 "I'm here to assist you in any way I can.", "Let's try to get to the bottom of this.",
                 "It's perfectly normal to feel confused at times.", "I'll try to help you make sense of it all.",
                 "I'll do my best to answer any questions you have."],

    "what are some healthy breakfast ideas":["How about starting your day with a delicious smoothie bowl? Blend together some spinach, frozen berries, banana, and Greek yogurt, then top it with granola, nuts, and seeds for added crunch.",
                                             "Try a bowl of overnight oats for a quick and nutritious breakfast. Mix rolled oats with your choice of milk, yogurt, and toppings like fruit, nuts, and a drizzle of honey. Let it sit in the fridge overnight, and it'll be ready to enjoy in the morning.",
                                             "Eggs are a versatile and protein-rich option for breakfast. You can make a veggie-packed omelette, scrambled eggs with spinach and tomatoes, or simply boil some eggs for a convenient grab-and-go option.",
                                              "For a satisfying and energizing breakfast, try avocado toast! Spread mashed avocado on whole-grain toast and top it with sliced tomatoes, a sprinkle of feta cheese, and a drizzle of balsamic glaze.",
                                              "Greek yogurt parfait is a delicious and nutritious breakfast option. Layer Greek yogurt with fresh berries, nuts, and a drizzle of honey for a protein-packed meal that will keep you full until lunchtime.",
                                              "Make a batch of healthy breakfast muffins over the weekend for a quick breakfast option during the week. Fill them with oats, grated carrots, applesauce, and nuts for a nutritious start to your day.",
                                              "Quinoa porridge is a great alternative to oatmeal and is packed with protein and fiber. Cook quinoa with milk or water, then top it with your favorite fruits, nuts, and a sprinkle of cinnamon for a flavorful breakfast.",
                                              "Chia seed pudding is a nutritious and easy-to-make breakfast option. Mix chia seeds with your choice of milk and sweetener, then let it sit in the fridge overnight to thicken. Top it with fresh fruit and nuts before serving.",
                                                "A breakfast burrito made with whole-grain tortillas, scrambled eggs, black beans, diced veggies, and a sprinkle of cheese is a filling and satisfying way to start your day.",
                                                 "For a quick and nutritious breakfast on the go, make a batch of homemade granola bars filled with oats, nuts, seeds, and dried fruit. They're perfect for busy mornings or as a mid-morning snack."],

"can you recommend a good restaurent nearby":["I can help you find a good Italian restaurant nearby. Could you please provide me with your location or the name of your city?",
                                             "Sure, I'd be happy to recommend a good Italian restaurant nearby. Do you have any specific preferences, such as the type of Italian cuisine or the price range?",
                                              "Absolutely! Let me search for some top-rated Italian restaurants in your area. Just give me a moment to find the best options for you.",
                                              "Of course! Italian cuisine is always a great choice. Let me check my database for highly-rated Italian restaurants nearby.",
                                               "Italian food sounds delicious! Let me find some popular Italian restaurants in your vicinity. I'll provide you with a list of options along with their ratings and reviews.",
                                               "I'd love to help you find a good Italian restaurant nearby. Let me search for some highly recommended options based on your location.",
                                                "Finding a great Italian restaurant is my specialty! Let me look up some top picks in your area and present you with the best options.",
                                                "Italian cuisine is always a crowd-pleaser! Let me find some highly rated Italian restaurants near you so you can enjoy a delicious meal.",
                                              "Sure thing! Italian food is a classic choice. Let me search for some top-notch Italian restaurants nearby and provide you with some recommendations.",
                                               "Finding the perfect Italian restaurant is easy with a little help! Let me find some highly rated options near you so you can indulge in some tasty pasta or pizza."],

"can you suggest some exercises to improve posture":["Incorporating core-strengthening exercises like planks, bridges, and bird-dogs into your workout routine can help improve overall posture by strengthening the muscles that support your spine.",
                                                     "Yoga and Pilates are great for improving posture as they focus on alignment, flexibility, and core strength. Poses like mountain pose, downward-facing dog, and cobra pose can help lengthen and strengthen the spine.",
                                                     "Regular stretching can also help improve posture by releasing tension in tight muscles. Focus on stretches that target the chest, shoulders, hips, and hamstrings to counteract the effects of sitting for long periods.",
                                                     "Exercises that target the upper back, such as rows and reverse flys, can help strengthen the muscles between the shoulder blades, which can improve posture and reduce rounded shoulders.",
                                                     "Mindfulness practices like tai chi and qigong can help improve posture by promoting body awareness, relaxation, and proper alignment.",
                                                     "Strengthening the muscles of the neck and shoulders can also help improve posture and reduce neck pain. Try exercises like shoulder shrugs, neck stretches, and shoulder blade squeezes.",
                                                      "A stability ball can be a useful tool for improving posture. Sitting on a stability ball engages the core muscles and encourages proper alignment of the spine.",
                                                       "If you spend a lot of time sitting at a desk, taking regular breaks to stretch and move around can help prevent stiffness and improve posture. Try standing up and stretching every hour or so.",
                                                      "Exercises that focus on hip mobility and flexibility, such as hip flexor stretches and hip circles, can help improve posture by reducing tightness in the hips and lower back.",
                                                      "Finally, be mindful of your posture throughout the day. Practice sitting and standing with your shoulders back, chin tucked, and spine aligned to maintain good posture and prevent slouching."],

    "how do you say 'thank you' in french":["The translation of 'thank you' to French is 'merci'.",
                                            "In French, 'thank you' is translated as 'merci'.",
                                              "The French equivalent of 'thank you' is 'merci'.",
                                               "When translated to French, 'thank you' becomes 'merci'.",
                                                "You can say 'merci' to express gratitude in French, which is the translation of 'thank you'.",
                                                  "In French, the phrase for 'thank you' is 'merci'.",
                                                    "The correct translation of 'thank you' into French is 'merci'.",
                                                     "To express gratitude in French, you can use the word 'merci', which means 'thank you'.",
                                                     "When speaking French, you would use the word 'merci' to say 'thank you'.",
                                                          "If you want to say 'thank you' in French, you would say 'merci'."],

    "can you recommend a good book on python":["Sure! Some popular books on Python programming include 'Python Crash Course' by Eric Matthes, 'Automate the Boring Stuff with Python' by Al Sweigart, and 'Learning Python' by Mark Lutz.",
                                              "Of course! You might find 'Python for Data Analysis' by Wes McKinney useful if you're interested in data science. 'Fluent Python' by Luciano Ramalho is also great for diving deeper into the language.",
                                                 "Certainly! 'Effective Python: 90 Specific Ways to Write Better Python' by Brett Slatkin is a highly recommended book for improving your Python skills. 'Python Cookbook' by David Beazley and Brian K. Jones is also packed with useful recipes and tips.",
                                                 "Yes! If you're looking to master Python, 'Python Programming: An Introduction to Computer Science' by John Zelle is a good starting point. 'Think Python: How to Think Like a Computer Scientist' by Allen B. Downey is another excellent resource.",
                                                  "Absolutely! 'Python Tricks: A Buffet of Awesome Python Features' by Dan Bader is a great choice if you want to learn practical Python techniques. 'Python Pocket Reference' by Mark Lutz is handy for quick lookups and reminders.",
                                                    "Yes, there are many great books on Python! 'Learning Python Design Patterns' by Chetan Giridhar is helpful for understanding software design principles in Python. 'Python 3 Object-Oriented Programming' by Dusty Phillips is also highly recommended.",
                                                     "Of course! 'Python Cookbook' by David Beazley and Brian K. Jones offers a collection of practical recipes for Python programming. 'Python Programming: Your Step-by-Step Guide to Easily Learn Python in 7 Days' by iCode Academy is great for beginners.",
                                                       "Absolutely! 'Flask Web Development' by Miguel Grinberg is an excellent resource if you're interested in web development with Python. 'Django for Beginners' by William S. Vincent is another fantastic book for learning Django, a popular Python web framework.",
                                                      "Sure thing! 'Python Data Science Handbook' by Jake VanderPlas is perfect if you're interested in data analysis and machine learning with Python. 'Deep Learning with Python' by François Chollet is great for diving into deep learning concepts.",
                                                          "Yes, there are plenty of books to choose from! 'Python for Kids: A Playful Introduction to Programming' by Jason R. Briggs is a fun and engaging way for kids (and adults!) to learn Python. 'Python Crash Course' by Eric Matthes is also highly recommended for beginners."],

    "what are the best dramas in korean language":["Some of the best Korean dramas that have gained international acclaim include 'Descendants of the Sun', 'Goblin', 'Crash Landing on You', and 'Itaewon Class'. These dramas are known for their compelling storylines, talented actors, and high production quality.",
                                                   "If you're a fan of romance dramas, you might enjoy 'My Love from the Star', 'The Heirs', 'While You Were Sleeping', and 'What's Wrong with Secretary Kim'. These dramas are popular for their heartwarming stories and charismatic characters.",
                                                    "For those who enjoy historical dramas, 'Moon Embracing the Sun', 'Scarlet Heart: Ryeo', 'Mr. Sunshine', and 'Empress Ki' are highly recommended. These dramas offer fascinating insights into Korean history and culture.",
                                                   "If you're looking for suspenseful thrillers, 'Signal', 'Stranger', 'Voice', and 'Tunnel' are excellent choices. These dramas are known for their intense plots, unexpected twists, and gripping suspense.",
                                                      "For fans of fantasy and supernatural dramas, 'W: Two Worlds', 'Legend of the Blue Sea', 'The Master's Sun', and 'Hotel Del Luna' offer imaginative storytelling and visually stunning cinematography.",
                                                          "If you enjoy heartwarming family dramas, 'Reply 1988', 'Sky Castle', 'Father is Strange', and 'My Mister' are highly recommended. These dramas explore themes of love, friendship, and the complexities of family relationships.",
                                                         "For viewers interested in medical dramas, 'Hospital Playlist', 'Doctor Stranger', 'Romantic Doctor, Teacher Kim', and 'Good Doctor' offer compelling storylines set in the world of medicine.",
                                                            "If you're a fan of coming-of-age dramas, 'Weightlifting Fairy Kim Bok Joo', 'Reply 1997', 'Age of Youth', and 'School 2015: Who Are You?' are popular choices. These dramas explore the challenges and triumphs of youth.",
                                                           "For those who enjoy action-packed dramas, 'City Hunter', 'Vagabond', 'Healer', and 'Lawless Lawyer' offer thrilling adventures, intense action scenes, and charismatic leads.",
                                                        "If you're looking for a light-hearted romantic comedy, 'Strong Woman Do Bong Soon', 'Fight for My Way', 'What's Wrong with Secretary Kim', and 'Her Private Life' are delightful choices with plenty of humor and romance."],

"what are the best places should we visit in vizag":["One of the must-visit places in Vizag is the Kailasagiri Hill Park, offering panoramic views of the city and the Bay of Bengal. It's a perfect spot for picnics and leisurely walks.",
                                                      "The Submarine Museum, located inside an actual decommissioned submarine, is a unique attraction in Vizag. Visitors can explore the submarine's interior and learn about its history.",
                                                              "Rushikonda Beach is known for its pristine sands and clear blue waters, making it a popular destination for sunbathing, swimming, and water sports like surfing and jet skiing.",
                                                       "Borra Caves, located around 90 kilometers from Vizag, are famous for their stunning limestone formations, stalactites, and stalagmites. Exploring these ancient caves is a memorable experience.",
                                                   "The Visakha Museum showcases the rich cultural heritage and history of Vizag through its collection of artifacts, photographs, and exhibits. It's a great place to learn about the region's past.",
                                                       "Yarada Beach, nestled between lush green hills, offers a serene and picturesque setting for relaxation and recreation. Visitors can enjoy swimming, beachcombing, and breathtaking sunsets.",
                                                       "The INS Kurusura Submarine Museum is another fascinating attraction in Vizag, featuring a decommissioned submarine that offers insight into India's naval history and technology.",
                                                        "Indira Gandhi Zoological Park is home to a diverse range of wildlife species, including big cats, primates, birds, and reptiles. It's a popular destination for families and nature enthusiasts.",
                                                         "The Simhachalam Temple, dedicated to Lord Varaha Narasimha, is a significant religious site in Vizag. The temple's architecture and intricate carvings are worth exploring for spiritual and cultural experiences." ,
                                                         "Araku Valley, located around 115 kilometers from Vizag, is a scenic hill station known for its lush greenery, coffee plantations, and tribal culture. It's a perfect getaway for nature lovers and adventure seekers."],

    "give some suggestions on best rating movies in tollywood":["For some top-rated movies in Tollywood, you might want to check out 'Baahubali: The Beginning' and its sequel 'Baahubali 2: The Conclusion'. These epic films received critical acclaim for their grand storytelling and visual effects.",
                                                                "If you're looking for highly-rated Telugu movies, 'Arjun Reddy' and its Hindi remake 'Kabir Singh' are worth watching. These intense romantic dramas were praised for their bold storytelling and powerful performances.",
                                                                "Movies like 'Jersey', 'Maharshi', and 'Srimanthudu' are among the best-rated films in Tollywood. They offer compelling narratives, strong performances, and meaningful messages that resonate with audiences.",
                                                                  "For fans of action-packed thrillers, 'Rangasthalam' and 'Khaidi No. 150' are top-rated choices. These films feature gripping storylines, impressive action sequences, and memorable performances by the lead actors.",
                                                                    "If you enjoy thought-provoking cinema, 'Manam' and 'A Aa' are highly-rated Telugu movies that offer heartwarming stories, memorable characters, and emotional depth.",
                                                                 "Movies like 'Gautamiputra Satakarni' and 'Mahanati' are considered among the best in Tollywood for their historical significance and cinematic brilliance. These films received widespread acclaim for their storytelling and performances.",
                                                                   "For fans of comedy-dramas, 'F2: Fun and Frustration' and 'Ala Vaikunthapurramuloo' are top-rated choices. These films are known for their humor, entertaining storylines, and ensemble cast performances.",
                                                                     "If you're interested in exploring different genres, 'Goodachari' and 'Evaru' are highly-rated Telugu thrillers that offer suspenseful plots, clever twists, and engaging storytelling.",
                                                                   "Movies like 'Baahubali: The Beginning', 'Jersey', and 'Arjun Reddy' are considered among the best-rated films in Tollywood. These movies have garnered critical acclaim and have been well-received by audiences.",
                                                                       "For those interested in historical dramas, 'Rudhramadevi' and 'Sye' are top-rated Telugu movies that offer fascinating insights into historical events and figures. These films are known for their grandeur and attention to detail."],
   "what are the features of latest iphone ":["The latest iPhone, as of my last update, is the iPhone 13 series. Some of its key features include an A15 Bionic chip for improved performance, a Super Retina XDR display for stunning visuals, and advanced camera systems with enhanced low-light performance and new photography features.",
                                                "The latest iPhone model boasts features such as 5G connectivity for faster download and streaming speeds, MagSafe technology for easy wireless charging and accessory attachment, and Ceramic Shield for improved durability and drop protection.",
                                               "With the latest iPhone, you can expect features like Face ID for secure authentication, iOS 15 with new features and enhancements, and improved battery life for all-day usage.",
                                                 "One of the standout features of the latest iPhone is its ProMotion technology, which delivers a smoother and more responsive display experience with a 120Hz refresh rate. Additionally, the iPhone 13 Pro models offer ProRAW and ProRes video recording capabilities for professional-grade photography and videography.",
                                                "The latest iPhone comes with enhanced privacy features, including App Tracking Transparency, which gives users more control over their data and privacy settings. It also offers improved water and dust resistance, making it more durable in challenging environments.",
                                                "Among the features of the latest iPhone are updated design options, including new colors and finishes, as well as improved speakers and audio quality for immersive sound experiences.",
                                                  "The latest iPhone introduces new cinematic video recording capabilities, allowing users to capture and edit stunning videos with Dolby Vision HDR. It also offers advancements in machine learning and artificial intelligence, enhancing the overall user experience.",
                                                    "With the latest iPhone, you'll enjoy features like faster FaceTime performance, Spatial Audio for immersive audio experiences, and improved Night mode for capturing better photos and videos in low-light conditions.",
                                                    "In addition to its hardware features, the latest iPhone offers a range of software enhancements, including redesigned widgets, improved multitasking capabilities, and updates to built-in apps like Maps and Weather.",
                                                    "Some of the standout features of the latest iPhone include its ProMotion display, advanced camera systems with Night mode, and support for MagSafe accessories. It also delivers impressive performance and battery life, making it a top choice for smartphone users."],

    "how to impress a girl":["Being yourself and showing genuine interest in her interests and opinions is a great way to impress a girl. Listen actively, ask thoughtful questions, and be respectful.",
                               "Show kindness and compassion towards others, including her. Small gestures like holding the door open or offering to help with something can leave a lasting impression.",
                               "Confidence is attractive, but remember to be humble too. Be confident in who you are and what you have to offer, but also be open to learning and growing.",
                          "Find common interests and activities you both enjoy, and suggest doing them together. Sharing experiences and making memories can strengthen your connection.",
                           "Take care of yourself physically and emotionally. Show that you prioritize your well-being and self-improvement, which demonstrates maturity and responsibility.",
                             "Be attentive and considerate of her feelings. Show empathy and understanding, and let her know that you're there for her when she needs support.",
                              "Show your sense of humor and don't be afraid to laugh together. Sharing laughter and joy can create a strong bond and make her feel comfortable around you.",
                                "Be confident in your decisions and take initiative. Plan thoughtful dates or surprises that show you've put effort into making her happy.",
                                "Respect her boundaries and take things at her pace. Don't pressure her into anything she's not comfortable with, and always prioritize her consent and comfort.",
                                  "Above all, be genuine and authentic in your interactions with her. Let your true personality shine through, and she'll appreciate your sincerity and honesty."],


"felling lonely, can we chat for a while":["Absolutely, I'm here to chat with you. What's been on your mind lately?",
                                          "I'm here for you! Let's chat and keep each other company. What would you like to talk about?",
                                             "I'm glad you reached out. I'm here to listen and chat with you. How are you feeling?",
                                            "I'm here to keep you company and chat with you. Feel free to share whatever's on your mind.",
                                         "You're not alone! I'm here to chat with you and offer support. What's been going on?",
                                         "I'm here to chat and keep you company. Tell me about your day or anything you'd like to talk about.",
                                         "I'm here for you, and I'm happy to chat with you for as long as you need. What's been on your mind lately?",
                                            "I'm here to listen and chat with you. Feel free to share what's been weighing on your mind.",
                                              "I'm here to keep you company and offer a listening ear. What would you like to talk about?",
                                          "You're not alone, I'm here to chat with you and offer some companionship. How can I support you right now?"],

    "thank you":["You're welcome! I'm always here to help.",
              "No problem at all! Happy to assist you.",
                "You're very welcome! If you need anything else, just let me know.",
                   "Glad I could be of assistance! Don't hesitate to reach out if you need further help.",
                       "Anytime! If there's anything else I can do for you, feel free to ask.",
                        "You're welcome! It was my pleasure to help out.",
                          "Not a problem! Let me know if there's anything else you need.",
                            "You're welcome! I'm here to make things easier for you.",
                            "It's no trouble at all! If you have any more questions, just ask.",
                             "You're welcome! I'm glad I could provide the support you needed."],

    "congratulations":["Thank you so much for your congratulations! I really appreciate it.",
                          "Wow, thank you! Your congratulations mean a lot to me.",
                          "Thanks a bunch for the congratulations! I'm grateful for your support.",
                           "I'm truly touched by your congratulations. Thank you!",
                         "Thank you for the congratulations! It's great to have your support.",
                         "Thanks a million for your congratulations! It made my day even brighter.",
                              "Thank you for the kind words and congratulations! It means a lot to me.",
                            "I'm so grateful for your congratulations! Thank you for celebrating with me.",
                             "Thank you for the congratulations! I'm thrilled to have your support.",
                                 "Thanks a ton for your congratulations! I'm truly humbled by your kindness."],
"happy birthday":["Thank you so much for the birthday wishes! It means a lot to me.",
                  "Wow, thank you for remembering my birthday! I really appreciate it.",
                  "Thanks a bunch for the birthday wishes! It's made my day even more special.",
                   "I'm truly touched by your birthday wishes. Thank you!",
                    "Thank you for the kind words and birthday wishes! It's so thoughtful of you.",
                    "Thanks a million for the birthday wishes! I'm grateful to have your support.",
                     "Thank you for the wonderful birthday wishes! It's been a fantastic day.",
                     "I'm so grateful for your birthday wishes! Thank you for making my day brighter.",
                    "Thank you for remembering my birthday and sending your wishes! It means a lot.",
                      "Thanks a ton for the birthday wishes! I'm truly humbled by your kindness."],

"happy journey":["Thank you so much for the well wishes! I'm looking forward to a great journey.",
                 "Thanks a bunch for the good wishes! I'll make sure to have a safe and enjoyable journey.",
                   "I really appreciate your kind words! I'm excited for the journey ahead.",
                 "Thanks for the happy wishes! I'll be sure to have a fantastic journey.",
                "Thank you for the encouragement! I'll keep your happy thoughts in mind throughout my journey.",
                 "I'm grateful for your support and happy wishes! It means a lot to me.",
                      "Thanks a million for the happy journey wishes! I'll make the most out of it.",
                   "Your well wishes brightened my day! I'll carry them with me on my journey.",
                    "Thank you for your kind words! I'm ready to embark on this journey with a positive mindset.",
                       "I appreciate your happy journey wishes! I'll take your positivity with me on my travels."],
"i love you":["I love you too! You mean the world to me.",
            "Aww, I love you too! You always know how to make me smile.",
            "I love you more! You're the best thing that ever happened to me.",
              "I love you to the moon and back! You're my everything.",
               "I love you beyond words! You fill my heart with joy.",
               "I love you more than you'll ever know! You're my rock.",
              "I love you with all my heart and soul! You're my forever.",
                  "I love you endlessly! You're the love of my life.",
                "I love you deeply! You complete me in every way.",
                   "I love you forever and always! You're my true happiness."],

    "i hate you":["I'm sorry to hear that you feel that way. Is there something specific that's bothering you?",
                    "I understand that you're upset, but I'm here to listen if you want to talk about it.",
                   "I'm sorry if I've done something to upset you. Can we talk about what's bothering you?",
                     "I'm here to work things out if you're open to discussing it calmly.",
                     "I'm sorry you feel that way. Is there anything I can do to make things better?",
                        "I hear you. Let's try to address what's causing these feelings and find a resolution.",
                          "I'm sorry if I've hurt you in any way. Let's talk about how we can move forward positively.",
                         "I understand that emotions can be intense sometimes. Can we try to work through this together?",
                             "I'm open to discussing what's bothering you and finding a solution that works for both of us.",
                        "I'm sorry you're feeling this way. Let's see if we can find common ground and resolve any issues."],
"i'm sorry":["Apology accepted. Thank you for acknowledging it.",
             "It's okay, I understand. Let's move forward from here.",
                "No problem at all. I appreciate your apology.",
                "Thank you for saying sorry. Let's put it behind us.",
                   "I forgive you. Let's focus on moving past this.",
                      "I understand, and I appreciate you apologizing.",
                   "Don't worry about it. Let's just make sure it doesn't happen again.",
                     "Thank you for apologizing. Let's work together to prevent it in the future.",
                    "No harm done. Let's focus on resolving the situation.",
                      "I accept your apology. Let's learn from this and move forward positively."],

    "default": ["I'm sorry, I didn't understand that.", "Could you please repeat that?", "I'm not sure I follow.",
                "Apologies, I'm having trouble understanding.", "I'm still learning, could you rephrase that?",
                "I'm here to help, but I'm not sure what you mean.", "Let's try that again, shall we?",
                "I'm afraid I didn't catch that, could you say it another way?", "Hmm, I'm not quite sure how to respond to that."]



}

# Function to get a response based on user input
def get_response(user_input):
    user_input = user_input.lower()  # Convert input to lowercase for case insensitivity

    # Check if the user input matches any predefined pattern
    for key in responses:

        if key in user_input:

            if key == "website":
                return random.choice(responses[key]) + " " + user_input.split("website")[-1].strip()

            elif key == "date":
                return random.choice(responses[key])

            elif key == "time":
                return random.choice(responses[key])

            else:
                return random.choice(responses[key])

    return random.choice(responses["default"])

# Main function to interact with the user
def main():

    print("Welcome to the Simple Chatbot!")

    print("You can start chatting. Type 'bye' to exit.")

    while True:

        user_input = input("You: ")

        if user_input.lower() == "bye":
            print("Chatbot: " + get_response(user_input))
            break

        else:
            print("Chatbot: " + get_response(user_input))

            # Check if the user asked to open a website
            if "open website" in user_input.lower():

                website_name = user_input.split("open website")[-1].strip()

                if website_name.lower() == "youtube":
                    webbrowser.open_new_tab("https://www.youtube.com")

                elif website_name.lower() == "wikipedia":
                    webbrowser.open_new_tab("https://www.wikipedia.org")

                elif website_name.lower() == "google":
                    webbrowser.open_new_tab("https://www.wikipedia.org")

                elif website_name.lower() == "instagram":
                    webbrowser.open_new_tab("https://www.wikipedia.org")

                elif website_name.lower() == "snapchat":
                    webbrowser.open_new_tab("https://www.wikipedia.org")

                elif website_name.lower() == "facebook":
                    webbrowser.open_new_tab("https://www.wikipedia.org")

                elif website_name.lower() == "twitter":
                    webbrowser.open_new_tab("https://www.wikipedia.org")

                elif website_name.lower() == "github":
                    webbrowser.open_new_tab("https://www.wikipedia.org")

                elif website_name.lower() == "discord":
                    webbrowser.open_new_tab("https://www.wikipedia.org")

                elif website_name.lower() == "whatsapp":
                    webbrowser.open_new_tab("https://www.wikipedia.org")

                elif website_name.lower() == "linkedin":
                    webbrowser.open_new_tab("https://www.wikipedia.org")

                elif website_name.lower() == "pinterest":
                    webbrowser.open_new_tab("https://www.wikipedia.org")

                elif website_name.lower() == "amazon":
                    webbrowser.open_new_tab("https://www.wikipedia.org")

                elif website_name.lower() == "flipkart":
                    webbrowser.open_new_tab("https://www.wikipedia.org")

                elif website_name.lower() == "apple music":
                    webbrowser.open_new_tab("https://www.wikipedia.org")

                elif website_name.lower() == "spotify":
                    webbrowser.open_new_tab("https://www.wikipedia.org")

                else:
                    print("Chatbot: Sorry, I can't open the specified website.")

if __name__ == "__main__":

    main()
