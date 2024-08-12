from classes.Post import Post
from classes.User import User
from classes.ImportantPosts import ImportantPosts
import datetime
import random
import math

def task1main():
    # Example users
    users = [
        User("user1", [], [], 1990, "User One", "M", "12345", [], []),
        User("user2", [], [], 1992, "User Two", "F", "67890", [], []),
        User("user3", [], [], 1985, "User Three", "M", "54321", [], []),
        User("user4", [], [], 1995, "User Four", "F", "98765", [], []),
        User("user5", [], [], 2000, "User Five", "M", "11223", [], []),
    ]

    # Example posts
    posts = [
        Post("user1", [{"quote": "Nice post!", "yapper": "user2"}, {"quote": "Great content!", "yapper": "user3"}], 
             "Post content 1", [{"seen_by": "user2", "datetime": "2023-08-01"}, {"seen_by": "user3", "datetime": "2023-08-01"}], "2023-08-01"),
        Post("user2", [{"quote": "Interesting perspective.", "yapper": "user1"}], 
             "Post content 2", [{"seen_by": "user1", "datetime": "2023-08-02"}, {"seen_by": "user3", "datetime": "2023-08-02"}], "2023-08-02"),
        Post("user3", [{"quote": "Thanks for sharing.", "yapper": "user4"}], 
             "Post content 3", [{"seen_by": "user4", "datetime": "2023-08-03"}, {"seen_by": "user5", "datetime": "2023-08-03"}], "2023-08-03"),
        Post("user4", [{"quote": "Loved it!", "yapper": "user3"}, {"quote": "Very informative.", "yapper": "user2"}], 
             "Post content 4", [{"seen_by": "user1", "datetime": "2023-08-04"}, {"seen_by": "user2", "datetime": "2023-08-04"}, {"seen_by": "user3", "datetime": "2023-08-04"}], "2023-08-04"),
        Post("user5", [{"quote": "Awesome!", "yapper": "user1"}, {"quote": "Helpful post.", "yapper": "user4"}], 
             "Post content 5", [{"seen_by": "user1", "datetime": "2023-08-05"}, {"seen_by": "user2", "datetime": "2023-08-05"}], "2023-08-05"),
    ]

    import_posts = ImportantPosts(users, posts)
    import_posts.create_graph(importance_criteria="comments")
    import_posts.draw_graph()

    # Change importance criteria
    import_posts.update_graph(importance_criteria="views")

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
    engagement = posts.copy()
    for x in posts:
        for y in users:
            for z in users[y].connections:
                if users[y].connections[z].type != "blocked":
                    posts[x].add_view(users[y].username,date.datetime.now())
                    posts[x].add_comment(random.choices(nonsense,k=150),users[y].username)
                    users[y].add_history(posts[x])
        # average views per minute for each post
        engagement[x] = len(posts[x].views)/((datetime.datetime.now()-posts[x].created).total_seconds()/60)   

    cloud = InterestingPostCloud(users)
    cloud.restrictions()
    
def task2main():
    # Sample Data
    users = [
        {"username": "user1", "age": 25, "gender": "female", "posts": 10, "comments": 5, "views": 100, "location": "NY"},
        {"username": "user2", "age": 30, "gender": "male", "posts": 15, "comments": 3, "views": 200, "location": "CA"},
        {"username": "user3", "age": 22, "gender": "female", "posts": 5, "comments": 10, "views": 50, "location": "TX"},
    ]

    posts = [
        {"post_id": "post1", "author": "user1", "views": 100, "content": "Post content 1"},
        {"post_id": "post2", "author": "user2", "views": 200, "content": "Post content 2"},
        {"post_id": "post3", "author": "user1", "views": 50, "content": "Post content 3"},
        {"post_id": "post4", "author": "user3", "views": 30, "content": "Post content 4"},
    ]

    connections = [
        {"from": "user1", "to": "user2", "type": "friends"},
        {"from": "user2", "to": "user3", "type": "follows"},
    ]

    # Create SocialMediaGraph object
    social_media_graph = SocialMediaGraph(users, posts, connections)

    # Define criteria dynamically
    criteria = [
        lambda user: user["posts"] > 5,       # Number of posts (high)
        lambda user: user["gender"] == "female", # Gender
        lambda user: user["views"] > 50,       # Number of views (high)
    ]

    # Highlight interesting users based on criteria
    social_media_graph.highlight_interesting_users(criteria)

    # Visualize the graph
    social_media_graph.visualize_graph()


def main():
    task1main()
    task4main()
    task2main()

main()
