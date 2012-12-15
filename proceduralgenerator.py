#.testingtext.txt is at https://gist.github.com/4286227
#output is at https://gist.github.com/4286238 with above input
#output for the letter/word a says the letter is imediatly followed by a (twice) and b(once) when in fact it is followed by b twice and never by a.
#similar outputs are produced for various inputs. 
from collections import Counter
import pickle as p
from random import random, choice
import math
import sys
def makehist(filename):
    textin = open(filename, 'U').read()
    words = textin.replace('\n'," ").split(' ')
    histogram = {}
    for baseword in list(set(words)):
        followingfreqs = {}#a dict of [wount, score] lists for each word(key)
        for pos in [i for i, x in enumerate(words) if x == baseword]:
            try:
                followingword = words[pos+1]
                try:
                    followingfreqs[followingword] = [followingfreqs[followingword][0] + 1,followingfreqs[followingword][1]]
                except KeyError:
                    followingfreqs[followingword] = [1,0]
            except:
                pass
        histogram[baseword] = followingfreqs
    p.dump(histogram,open("histogramout.pickle","w"))
def calcwords(length):
    histogram = p.load(open("histogramout.pickle","r"))
    word = choice(histogram.keys())
    sentance = word
    while len(sentance) <length-10:
        wordscores = [[key,histogram[word][key][0]] for key in histogram[word]]
        wordscores.sort(key=lambda x: x[1])
        word = wordscores[(int(math.floor((random()**2)*len(wordscores))))][0]
        sentance = sentance + " " + word
    print sentance
helptext = """
Options:
-m=<filename> Produces a histogram for the generation of text from filename.
-p=<charecters> Prints <charecters> of text generated from the above histogram
-h Print this help text.
"""
for argument in sys.argv[1:]:
    if argument[:2] == "-m":
        if argument[3:] != "":
            makehist(argument[3:])
        else:
            print "Make histogram error - no source file specified"
            print helptext
    elif argument[:2] == "-p":
        try:
            calcwords(int(argument[3:]))
        except:
            print "you need to specify a charecter limit"
            print helptext
    elif argument[:2] == "-h":
        print helptext
    else:
        print "error unrecognized argument:" + argument
        print helptext
    
