#!/usr/bin/python

# using the haxor hackernews python api wrapper
# don't resubmit a query with frequency greater than every 30 seconds

from hackernews import HackerNews
hn = HackerNews()
from datetime import datetime
import matplotlib
from matplotlib import pyplot as plt

story_tup_list = []
comment_tup = ()
get_comments = False
now = datetime.now()

top_story_ids = hn.top_stories(limit=30)

for story_id in top_story_ids:
    story = hn.get_item(story_id)
    story_tup = (story.title, story.score, story.submission_time)
    story_tup_list.append(story_tup)

    if(get_comments == True):
        for comment_id in story.kids:
            comment = hn.get_item(comment_id)
            comment_tup = (comment.submission_time, comment.text)


story_tup_list.sort(key=lambda tup: tup[1], reverse=True)
for story in story_tup_list[:5]:
    print story[0], story[1]
    string_list = story[0].split(" ")
    print string_list, now - story[2]

plt.plot()

# mystring_list = comment.split(" ")
# if(mystring_list == "Japan"):
#     print mystring_list
