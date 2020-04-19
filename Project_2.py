#!/usr/bin/env python
# coding: utf-8

# # Project 2 - Hacker News
# Hacker News is a site started by the startup incubator Y Combinator, where user-submitted stories (known as "posts") are voted and commented upon, similar to reddit. Hacker News is extremely popular in technology and startup circles, and posts that make it to the top of Hacker News' listings can get hundreds of thousands of visitors as a result.
# 
# Database column details:
# 
# - id: The unique identifier from Hacker News for the post
# - title: The title of the post
# - url: The URL that the posts links to, if it the post has a URL
# - num_points: The number of points the post acquired, calculated as the total -number of upvotes minus the total number of downvotes
# - num_comments: The number of comments that were made on the post
# - author: The username of the person who submitted the post
# - created_at: The date and time at which the post was submitted
# 
# We're specifically interested in posts whose titles begin with either Ask HN or Show HN. Users submit Ask HN posts to ask the Hacker News community a specific question
# 
# 

# In[5]:



from csv import reader
opened_file=open('hacker_news.csv')
read_file=reader(opened_file)
hn=list(read_file)


# In[9]:


print(hn[0:5])


# In[10]:


headers=hn[0]


# In[11]:


hn=hn[1:]


# In[12]:


print(headers)
print(hn[0:4])


# In[13]:


ask_posts=[]
show_posts=[]
other_posts=[]
for each_row in hn:
    title=each_row[1]
    title=title.lower()
    if title.startswith('ask hn'):
        ask_posts.append(each_row)
    elif title.startswith('show hn'):
        show_posts.append(each_row)
    else:
        other_posts.append(each_row)
        
print(len(ask_posts))
print(len(show_posts))
print(len(other_posts))


# In[16]:


print(ask_posts[0:5])
print(show_posts[0:5])


# In[18]:


#Obtaining the average number of comments for the ask posts
total_ask_comments=0
for each_row in ask_posts:
    num_comments=each_row[4]
    num_comments=int(num_comments)
    total_ask_comments+=num_comments
    
avg_ask_comments=total_ask_comments/len(ask_posts)
print(avg_ask_comments)


# In[19]:


#Obtaining the average number of comments for the show posts
total_show_comments=0
for each_row in show_posts:
    num_comments=each_row[4]
    num_comments=int(num_comments)
    total_show_comments+=num_comments
    
avg_show_comments=total_show_comments/len(show_posts)
print(avg_show_comments)


# On average the Asks posts have a higher average (~14 comments) against 10 comments from the Show posts.

# In[36]:


import datetime as dt
result_list=[]
for each_row in ask_posts:
    created=each_row[6]
    num_comments=each_row[4]
    num_comments=int(num_comments)
    alist=[created,num_comments]
    result_list.append(alist)


# In[54]:


counts_by_hour={}
comments_by_hour={}
date_format='%m/%d/%Y %H:%M'
for each_row in result_list:
    a_date=each_row[0]
    num_comments=each_row[1]
    dt_object=dt.datetime.strptime(a_date,date_format)
    hour=dt_object.strftime(%H)
    if hour in counts_by_hour:
        counts_by_hour[hour]+=1
        comments_by_hour[hour]+=num_comments
    if hour not in counts_by_hour:
        counts_by_hour[hour]=1
        comments_by_hour[hour]=num_comments
    


# In[86]:


print(comments_by_hour)


# In[55]:


avg_by_hour=[]
for each_val in counts_by_hour:
    avg_val=comments_by_hour[each_val]/counts_by_hour[each_val]
    val_list=[each_val,avg_val]
    avg_by_hour.append(val_list)


# In[68]:


swap_avg_by_hour=[]
for each_row in avg_by_hour:
    hour=each_row[0]
    comments=each_row[1]
    a_list=[comments,hour]
    swap_avg_by_hour.append(a_list)
    
sorted_swap=sorted(swap_avg_by_hour,reverse=True)
print(sorted_swap[0:5])


# In[83]:


print("Top 5 Hours for Ask Posts Comments")
print_string="{hour}: {average:.2f} average comments per post."
for each_row in sorted_swap[0:5]:
    hour=each_row[1]
    avg_val=each_row[0]
    ft_hour=dt.datetime.strptime(hour,'%H')
    ft_hour=ft_hour.strftime('%H:%M')
    output=print_string.format(hour=ft_hour,average=avg_val)
    print (output)


# The hour that received most average comments per hour is 15:00 with 38,59 comments

# In[ ]:




