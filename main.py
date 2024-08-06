from classes.Post import Post
from classes.User import User
import datetime
import random


def task4main():
# word cloud of interesting posts   

# create users and add their connections    
    person1 = User(username="bob12",birth_year=1988,zipcode=55378)
    person2 = User(username="its_meg",birth_year=1996,real_name="megan ashby",gender="she/her",zipcode=90039)
    person3 = User(username="payuspaytas",birth_year=1988,gender="f",zipcode=61032)
    users = [person1,person2,person3]
    person4 = User(username="muskrat",birth_year=1971,real_name="elon musn't",zipcode=17739)
    users.append(person4)
    person4.add_connection("payuspaytas","blocked")
    person1.add_connection("muskrat","follows")
    person2.add_connection("bob12","friends")
    person2.add_connection("payuspaytas","read posts by")
    
# create posts and populate authors' post lists    
    postA = Post(owner="payuspaytas",content="like do dogs have brains??? serious question",created=datetime.datetime(2013,7,3,16,19,0,0,None,0))
    person3.add_post(postA)
    postB = Post(owner="muskrat",content="Always think about this with my little fluffy dog. My big dog does look like a wolf.",created=datetime.datetime(2024,5,4,9,7,0,0,None,0))
    person4.add_post(postB)    
    postC = Post(owner="bob12",content="Hi Reddit, what breed of dog should I get my 4 year old niece? I was thinking a golden retriever, alaskan malamute, or a poodle. Not looking for an older or half-grown dog, I want a puppy to be able to grow with her.",created=datetime.datetime(2023,9,30,1,49,0,0,None,0))
    person2.add_post(postC)   
    postD = Post(owner="its_meg",content="hey guys look at my new pup! i think i'll name it michelle obama <3",created=datetime.datetime.now())
    person1.add_post(postD)
    postE = Post(owner="bob12",content="Kathy, if you see this message me. Your cat escaped the yard and destroyed my plants again.",created=datetime.datetime.now())
    person1.add_post(postE)    
    posts = [postA, postB, postC, postD, postE]

# populate users' posts with comments and views
    nonsense = "When using AI to write content as a helping functionality, the ethical dimension involved tends to be utilitarian lens because the writer’s quality of life may increase since using AI can save time that could be used for activities that positively impact one’s life."
    for x in posts:
        for y in users:
            for z in users[y].connections:
                if users[y].connections[z].type != "blocked":
                    posts[x].add_view(users[y].username,date.datetime.now())
                    posts[x].add_comment(random.choices(nonsense,k=150),users[y].username)
                    users[y].add_history(posts[x])
                    

def main():
    task4main()

main()
