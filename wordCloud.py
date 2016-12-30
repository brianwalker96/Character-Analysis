from PIL import Image
import numpy as np
from wordcloud import WordCloud

#from os import path
#import matplotlib.pyplot as plt
#from wordcloud import ImageColorGenerator

class WordCloudHelper:
	def __init__ (self):
		print "WordCloudHelper - initializing"
		self.riceMask = np.array(Image.open("logo.jpg"))

	def graphWords(self, words):
		print "WordCloudHelper - generating WordCloud"
		wc = WordCloud(background_color="white", max_words=2000, mask=self.riceMask)
		wc.generate(words)
		wc.to_file("word_cloud.png")

#def grey_color_func(word, font_size, position, orientation, random_state=None, **kwargs):
#    return "hsl(0, 0%%, %d%%)" % random.randint(60, 100)

#text = "hey there soul sister what is going on shut up it doesn't matter bye Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of de Finibus Bonorum et Malorum (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of Lorem Ipsum, Lorem ipsum dolor sit amet.., comes from a line in section 1.10.32. he standard chunk of Lorem Ipsum used since the 1500s is reproduced below for those interested. Sections 1.10.32 and 1.10.33 from de Finibus Bonorum et Malorum by Cicero are also reproduced in their exact original form, accompanied by English versions from the 1914 translation by H. Rackham. Hey, I'm once again: back. I don't suppose you fell for that little thing about the refresh button. After all, you're a responsible, intelligent person who apparently has a lot of time on your hands. Well, you can't possibly have more time than I do. I mean, after all, I made this site. You're only browsing it. And most people don't even come here. Not even my friends...*sniffle* The just ignore this poor, pathetic little page. All they do is fill out the TAB form and leave. I think. Maybe they're here right now! HI! HOW ARE YOU DOING? I'M FINE! THANKS FOR COMING! YES, I'M YELLING! Who am I kidding. This page won't get a single hit, unless I bribe people...now that has possibilities. Okay, fill out the TAB form, so I have proof that you bothered to come here and...uh...I'll...uh...send you a sandwich? Please allow 6-8 weeks for delivery. I'm bored. I'm gonna go hug a moose. MOOSE! I love-d you moose! Hey, I'm back again! Yea...*waits for applause* okay! Now I want all you loyal fans...*cricket chirps* to go to the link to see what I'm like. I took a whole bunch of personality quizzes and posted them there. I'm an evil villain, kitty and a freakazoid so far. And I only took the quiz once, too. Spooky how accurate they are...anyway, I command you to go! I'm going. I'm back. I'm gonna start counting how many times I say back. Let's see: 1...2...3...4...5! Wow. I must really be desperate for something to do. I now officially have proof that someone has been here! It was one of my friends. Apparently this page really is getting long, because my friend said something to that effect. Maybe. Anyway, moving on! I'm just basically typing nothing. Just like all those reports people have to do. You know? With a specific number of words. They start out with half that number, and then just fill in words until they have the right amount. I salute those people. You're great tradition is being carried out here, on the second most pointless site ever! Well. Maybe eventually some weird, bored person will wander onto my site on accident and be mildly entertained be my site until they wander onto a live video feed of a coffee maker. Or maybe not. I only know that I'm entertaining me, which was my original goal. So. I've done what I've set out to accomplish. Yea, me! I'm so special. You see, most people, they don't like reading or writing. So if you're not most people, you've made it down this far without skipping, skimming or getting the spark notes version. (Which I think does not exist) My point is, if you've bothered to read this, then, (like me) you probley have also read the ketchup bottle so many times that you have it down verbatim. Look verbatim up. It's a word. But, you should know that, since you like reading. Or maybe you're just skimming. Anyway, there's nothing wrong with reading food labels. You might be asked a question about them on a quiz show. And now, for the million-dollar question: How many calories are there in a single serving of Mustard? I can just see it now...It could be called Know-Your-Food. Or You are What you Eat. It'd probley be as popular as those game shows that no one's ever heard of. Speaking of food, what's up with pie? There's strawberry pie, apple, pumpkin and so many others, but there is no grape pie! I know. I'm just as upset about this unfortunate lack of development in the pie division. Think about it. Grapes are used to make jelly, jam, juice and raisins. What makes them undesirable for pie? Would they dry into raisins? Couldn't you just stick some jelly in a piecrust and bake it? It just doesn't make any sense. Another thing that bothers me is organ grinders. You know, the foreign guys with the bellhop hats and the little music thingy and the cute little monkey with the bellhop hat who collects the money? Okay. They're basically begging on the street. How did they ever afford an organ-thingy? Wouldn't it make more sense to get a kazoo, if you're broke? And if they're so poor, what possessed them to buy a monkey? I mean, I don't think I could afford a monkey, and I'm not exactly on the streets. Obviously I at least have a computer...so, back to the organ grinders. I would have sold the monkey and the organ and been able to eat for at least a year. Or, if I was weirder than I am, I could at least kill the monkey with the organ and eat it. Why on earth did they keep the monkey? It must have cost a fortune to feed...not to mention the mess. That's just one of those many facts of life that are better left mysteries. Especially since no one but me would ask the question. I better go. I think I hear a monkey...Okay...now I'm back. That's the sixth time I've said back! I realize that this longest text ever must be very boring and not worth anyone's time. But I'd like to take this time to thank the 2 and 1/2 people in the entire universe who have bothered to read this entire thing. I'm not exactly sure who they are, but: thanks! Right now, my spacebar is malfunctioning...that's not good...I have to press it two or three times just to insert a freaking space. Mayb"
# read the mask image
# taken from
# http://www.stencilry.org/stencils/movies/alice%20in%20wonderland/255fk.jpg
#alice_mask = np.array(Image.open("logo.jpg"))


#wc = WordCloud(background_color="white", max_words=2000, mask=alice_mask)
# generate word cloud
#wc.generate(text)


# store to file
#wc.to_file("alice.png")

# # show
# plt.imshow(wc)
# plt.axis("off")
# plt.figure()
# plt.imshow(wc.recolor(color_func = grey_color_func))
# #plt.imshow(alice_mask, cmap=plt.cm.gray)
# plt.axis("off")
# plt.show()

# def graphWordBag(text):
# 	wordcloud = WordCloud().generate(text)
# 	plt.imshow(wordcloud)
# 	plt.axis("off")
# 	wordcloud = WordCloud(max_font_size=40, relative_scaling=.5).generate(text)
# 	plt.figure()
# 	plt.imshow(wordcloud)
# 	plt.axis("off")
# 	plt.savefig("wordcloud.png")