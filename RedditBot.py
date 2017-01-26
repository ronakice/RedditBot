import praw
import time
from nltk.sentiment.vader import SentimentIntensityAnalyzer
r = praw.Reddit(user_agent='Comment Extraction And Sentiment Analyser',
                     client_id='Ho4Yr54TEqpV2Q',
                     client_secret="EF-80ngO-IbsULqfc_rjsuperfk",
                     username='rbot42',
                     password='abc123')
sid = SentimentIntensityAnalyzer()
inapp_users=set()
kind_users=set()
with open("wordkind.txt") as f:
    lstk = f.read().split()
with open("wordinapp.txt") as f:
    lstin = f.read().split()
already_seenk=[]
already_seenin=[]
while True:
    inapp_users=set()
    kind_users=set()
    usr_comment_good={}
    usr_comment_bad={}
    msg=""
    ct=0
    for comment in r.subreddit('all').stream.comments():
        body=comment.body.lower()
        ct+=1
        #print(body)
        for wordsk in lstk:
            if body.find(wordsk) != -1:
                if comment.author not in already_seenk:
                    usr_comment_good[comment.author]=body
                    kind_users.add(comment.author)
                break
        for wordsin in lstin:
            if body.find(wordsin) != -1:
                if comment.author not in already_seenin:
                    usr_comment_bad[comment.author]=body
                    inapp_users.add(comment.author)
                break
        if ct==100:
            break
    if len(kind_users)!=0:
        msg = "\nKind users: "
    for user in kind_users:
        #print (user)
        if user not in already_seenk:
            msg+=str(user)+", "
            already_seenk.append(user)
    if len(inapp_users)!=0:
        msg +="\nInappropriate users: "
    for user in inapp_users:
        if user not in already_seenin:
            msg += ", "+ str(user)
            already_seenin.append(user)
        msg +=".\n"
    if len(kind_users)!=0:
        msg += "\nKind user comments: \n"
    for i in usr_comment_good.keys():
        sen=sid.polarity_scores(usr_comment_good[i])
        msg+="%s : %s"%(i, usr_comment_good[i]+ "  Compound Sentiment: " +
        str(sen["compound"]) +"\n")
        msg+="\n"
    if len(inapp_users)!=0:
        msg += "\nInappropriate user comments: \n"
    for i in usr_comment_bad.keys():
        sen=sid.polarity_scores(usr_comment_bad[i])
        msg+="%s : %s"%(i, usr_comment_bad[i] + "  Compound Sentiment: " +
        str(sen["compound"]))
        msg+="\n"
    if len(msg)==0:
        r.redditor('rbot42').message('TEST',
        "Nothing interesting going on right now!")
    else:
        print(msg)
        print(len(msg))
        r.redditor('rbot42').message('TEST',msg)
    time.sleep(15)
