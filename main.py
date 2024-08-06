from classes.Post import Post
from classes.User import User
import datetime


def task4main():
# word cloud of interesting posts   

    person1 = User(username="bob12",birth_year=1988,zipcode=55378)
    person2 = User(username="its_meg",birth_year=1996,real_name="megan ashby",gender="she/her",zipcode=90039)
    person3 = User(username="payuspaytas",birth_year=1988,gender="f",zipcode=61032)
    users = [person1,person2,person3]
    person4 = User(username="muskrat",birth_year=1971,real_name="elon musn't",zipcode=17739)
    users.append(person4)

    postA = Post(owner="payuspaytas",content="like do dogs have brains??? serious question",created=datetime.datetime(2013,7,3,16,19,0,0,None,0))
    postB =
    postC = 
    postD = 
    posts = [postA, postB, postC, postD]

def main():
    task4main()

main()
