import praw

reddit = praw.Reddit(client_id='LPq2XYvvdQ0Lrw',
                     client_secret='qujKPHoZMZQ6pzQR2-cO0lhTNWM',
                     user_agent='XxTyboxX')

def displayFormat():
    print("\n")
    for i in range(50):
        print("-", end = "")
    print("\nThese are the top posts in the \"" + var + "\" subreddit")
    for i in range(50):
        print("-", end = "")

postCount = 1;
var = input("Please enter the name of a subreddit: ")
displayFormat()

try:
    for submission in reddit.subreddit(var).hot(limit=10):
        print("\n%d: " % (postCount) + submission.title)
        postCount += 1
except Exception as e:
    print("Error! You didn't enter a valid subreddit")

