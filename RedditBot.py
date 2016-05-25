import praw
import time

r=praw.Reddit('Simple comment parser')
r.login()
inapp_users=set()
kind_users=set()
lstk=["thank","please"]
lstin=["shit","stupid","retarded"]
already_seenk=[]
already_seenin=[]
while True:
    comments=r.get_comments('uwaterloo')
    for comment in comments:
        body=comment.body.lower()
        for wordsk in lstk:
            if body.find(wordsk) != -1:
                kind_users.add(comment.author)
                break
        for wordsin in lstin:
            if body.find(wordsin) != -1:
                inapp_users.add(comment.author)
                break
    msg = "Kind users: "
    for user in kind_users:
        #print (user)
        if user not in already_seenk:
            msg+=str(user)+", "
            already_seenk.append(user)
    msg +=". "+"Inappropriate users: "
    for user in inapp_users:
        # print (user)
        if user not in already_seenin:
            msg += ", "+ str(user)
            already_seenin.append(user)
        msg +="."
    r.user.send_message('rbotq42', msg)
    time.sleep(15)


