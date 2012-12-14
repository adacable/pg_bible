#.testingtext.txt is at https://gist.github.com/4286227
#output is at https://gist.github.com/4286238 with above input
#output for the letter/word a says the letter is imediatly followed by a (twice) and b(once) when in fact it is followed by b twice and never by a.
#similar outputs are produced for various inputs. 
from collections import Counter
import pickle as p
from random import random, choice
import math
def makehist():
    textin = open('bibleraw.t', 'U').read()
    words = textin.replace('\n'," ").split(' ')
    histogram = {}
    for baseword in list(set(words)):
        followingfreqs = {}#a dict of (wount, score) turples for each word(key)
        for pos in [i for i, x in enumerate(words) if x == baseword]:
            try:
                followingword = words[pos+1]
                try:
                    followingfreqs[followingword] = [followingfreqs[followingword][0] + 1,followingfreqs[followingword][1]]
                except KeyError:
                    followingfreqs[followingword] = [1,0]#set (count,score) turple to 1 count, no score
            except:
                pass
        histogram[baseword] = followingfreqs
    p.dump(histogram,open("histogramout.pickle","w"))
def calcwords():
    histogram = p.load(open("histogramout.pickle","r"))
    word = choice(histogram.keys())
    sentance = word
    while len(sentance) <130:
        wordscores = [[key,histogram[word][key][0]] for key in histogram[word]]
        wordscores.sort(key=lambda x: x[1])
        word = wordscores[int(math.floor((random()**8)*len(wordscores)))][0]
        sentance = sentance + " " + word
    print sentance
calcwords()
