#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings('ignore')
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


cd C:\Users\HP\Downloads


# In[3]:


df=pd.read_csv('AJIO campaign performance analysis.csv')
df.head()


# In[4]:


df.shape


# In[5]:


df.describe()


# In[6]:


df.info()


# In[ ]:





# In[7]:


#change tthe data types of variables
var=['Likes','Comments','Shares','Saves']
df[var] = df[var].fillna(0).astype(int)

df.info()


# In[8]:


df.head()


# In[9]:


pd.set_option('display.float_format', '{:.2f}'.format)
df.describe(percentiles=[.25,.5,.75,.90,.95,.99])


# In[10]:


#calculate engagement rate
df['Engagement_rate'] = df.apply(lambda row: 100*(row['Engagement'] / row['Impressions']) if row['Platform'] == 'Twitter' and row['Impressions'] != 0 else 100*(row['Engagement'] / row['Reach']) if row['Reach'] != 0 else 0, axis=1)


# In[11]:


df.head()


# In[12]:


df.Engagement_rate.describe()


# In[ ]:





# ## Divide the dataframe into w/o collab and over all performance

# #### As we've worked solely with creators on Instagram Reels, we'll analyze the overall performance, taking into account the impact of these collaborations, and compare it to other platforms.

# In[13]:


df_without_collab=df[pd.isna(df['Creator'])]
df_without_collab.head()


# In[ ]:





# In[ ]:





# In[ ]:





# ## 1. Platformwise peformance

# ### 1.1 Overall Performance (with collaboration)

# In[14]:


platform=pd.DataFrame()


# In[15]:


platform['avg_reach']= round(df.groupby('Platform')['Reach'].mean())
platform['avg_views']= round(df.groupby('Platform')['Views'].mean())
platform['avg_engagement']= round(df.groupby('Platform')['Engagement'].mean())
platform['avg_impression']= round(df.groupby('Platform')['Impressions'].mean())
platform.head()


# In[16]:


platform=platform.reset_index()
platform.head()


# In[17]:


platform['Engagement_rate']=platform.apply(lambda row: 100 * (row['avg_engagement'] / row['avg_impression'])
                                             if row['Platform'] == 'Twitter'
                                             else 100 * (row['avg_engagement'] / row['avg_reach']), axis=1)


# In[18]:


#overall platform performance
platform.head()


# In[ ]:





# In[ ]:





# ### 1.2 Platform performance without collaboration

# In[19]:


platform_without_collab=pd.DataFrame()
platform_without_collab['avg_reach']= round(df_without_collab.groupby('Platform')['Reach'].mean())
platform_without_collab['avg_views']= round(df_without_collab.groupby('Platform')['Views'].mean())
platform_without_collab['avg_engagement']= round(df_without_collab.groupby('Platform')['Engagement'].mean())
platform_without_collab['avg_impression']= round(df_without_collab.groupby('Platform')['Impressions'].mean())
platform_without_collab.head()


# In[20]:


platform_without_collab=platform_without_collab.reset_index()
platform_without_collab.head()


# In[21]:


platform_without_collab['Engagement_rate']=platform_without_collab.apply(lambda row: 100 * (row['avg_engagement'] / row['avg_impression'])
                                             if row['Platform'] == 'Twitter'
                                             else 100 * (row['avg_engagement'] / row['avg_reach']), axis=1)


# 

# In[22]:


#Without collaboration platform performance
platform_without_collab.head()


# In[23]:


#sorting values
platform=platform.sort_values(by='avg_reach', ascending=False)
platform.head()


# In[24]:


platform_without_collab=platform_without_collab.sort_values(by='avg_reach', ascending=False)
platform_without_collab.head()


# In[25]:


#plotting subplots
plt.figure(figsize=(20,10))
plt.subplot(2, 4, 1)
plt.bar(platform['Platform'], platform['avg_reach'])
plt.subplot(2, 4, 2)
plt.bar(platform['Platform'], platform['avg_views'])
plt.subplot(2, 4, 3)
plt.bar(platform['Platform'], platform['avg_engagement'])
plt.subplot(2, 4, 4)
plt.plot(platform['Platform'], platform['Engagement_rate'])
plt.subplot(2, 4, 5)
plt.bar(platform_without_collab['Platform'], platform_without_collab['avg_reach'])
plt.subplot(2, 4, 6)
plt.bar(platform_without_collab['Platform'], platform_without_collab['avg_views'])
plt.subplot(2, 4, 7)
plt.bar(platform_without_collab['Platform'], platform_without_collab['avg_engagement'])
plt.subplot(2, 4, 8)
plt.plot(platform_without_collab['Platform'], platform_without_collab['Engagement_rate'])
plt.show()


# In[ ]:





# ## 2. Format-wise Performance

# ### 2.1 Overall Performance (with collaboration)

# In[26]:


Format=pd.DataFrame()


# In[27]:


Format['avg_reach']= round(df.groupby('Format')['Reach'].mean())
Format['avg_views']= round(df.groupby('Format')['Views'].mean())
Format['avg_engagement']= round(df.groupby('Format')['Engagement'].mean())
Format['avg_impression']= round(df.groupby('Format')['Impressions'].mean())
Format.head()


# In[28]:


Format=Format.reset_index()
Format.head()


# In[29]:


Format['Engagement_rate']=Format.apply(lambda row: 100 * (row['avg_engagement'] / row['avg_impression'])
                                             if row['Format'] == 'Tweets'
                                             else 100 * (row['avg_engagement'] / row['avg_reach']), axis=1)
Format.head()


# In[ ]:





# ### 2.2 Format performance without collaboration

# In[30]:


Format_without_collab=pd.DataFrame()


# In[31]:


Format_without_collab['avg_reach']= round(df_without_collab.groupby('Format')['Reach'].mean())
Format_without_collab['avg_views']= round(df_without_collab.groupby('Format')['Views'].mean())
Format_without_collab['avg_engagement']= round(df_without_collab.groupby('Format')['Engagement'].mean())
Format_without_collab['avg_impression']= round(df_without_collab.groupby('Format')['Impressions'].mean())
Format_without_collab.head()


# In[32]:


Format_without_collab=Format_without_collab.reset_index()
Format_without_collab.head()


# In[33]:


Format_without_collab['Engagement_rate']=Format_without_collab.apply(lambda row: 100 * (row['avg_engagement'] / row['avg_impression'])
                                             if row['Format'] == 'Tweets'
                                             else 100 * (row['avg_engagement'] / row['avg_reach']), axis=1)
Format_without_collab.head()


# In[34]:


#sorting values
Format=Format.sort_values(by='avg_reach', ascending=False)
Format.head()


# In[35]:


Format_without_collab=Format_without_collab.sort_values(by='avg_reach', ascending=False)
Format_without_collab.head()


# In[36]:


#plotting subplots
plt.figure(figsize=(20,10))
plt.subplot(2, 4, 1)
plt.bar(Format['Format'], Format['avg_reach'])
plt.xticks(rotation=90)
plt.subplot(2, 4, 2)
plt.bar(Format['Format'], Format['avg_views'])
plt.xticks(rotation=90)
plt.subplot(2, 4, 3)
plt.bar(Format['Format'], Format['avg_engagement'])
plt.xticks(rotation=90)
plt.subplot(2, 4, 4)
plt.plot(Format['Format'], Format['Engagement_rate'])
plt.xticks(rotation=90)
plt.subplot(2, 4, 5)
plt.bar(Format_without_collab['Format'], Format_without_collab['avg_reach'])
plt.xticks(rotation=90)
plt.subplot(2, 4, 6)
plt.bar(Format_without_collab['Format'], Format_without_collab['avg_views'])
plt.xticks(rotation=90)
plt.subplot(2, 4, 7)
plt.bar(Format_without_collab['Format'], Format_without_collab['avg_engagement'])
plt.xticks(rotation=90)
plt.subplot(2, 4, 8)
plt.plot(Format_without_collab['Format'], Format_without_collab['Engagement_rate'])
plt.xticks(rotation=90)
plt.show()


# ## 3.Content Type-Wise Performance
# 

# ### 3.1 Overall Performance (with collaboration)

# In[37]:


Type=pd.DataFrame()


# In[38]:


Type['avg_reach']= round(df.groupby('Content Type')['Reach'].mean())
Type['avg_views']= round(df.groupby('Content Type')['Views'].mean())
Type['avg_engagement']= round(df.groupby('Content Type')['Engagement'].mean())
Type['avg_impression']= round(df.groupby('Content Type')['Impressions'].mean())
Type.head()


# In[39]:


Type=Type.reset_index()
Type.head()


# In[40]:


Type['Engagement_rate']=Type.apply(lambda row: 100 * (row['avg_engagement'] / row['avg_reach']), axis=1)
Type.head()


# ### 3.2 Content Type performance without collaboration

# In[41]:


Type_without_collab=pd.DataFrame()


# In[42]:


Type_without_collab['avg_reach']= round(df_without_collab.groupby('Content Type')['Reach'].mean())
Type_without_collab['avg_views']= round(df_without_collab.groupby('Content Type')['Views'].mean())
Type_without_collab['avg_engagement']= round(df_without_collab.groupby('Content Type')['Engagement'].mean())
Type_without_collab['avg_impression']= round(df_without_collab.groupby('Content Type')['Impressions'].mean())
Type_without_collab.head()


# In[43]:


Type_without_collab=Type_without_collab.reset_index()
Type_without_collab.head()


# In[44]:


Type_without_collab['Engagement_rate']=Type_without_collab.apply(lambda row: 100 * (row['avg_engagement'] / row['avg_reach']), axis=1)
Type_without_collab.head()


# In[45]:


#sorting values
Type=Type.sort_values(by='avg_reach', ascending=False)
Type.head()


# In[46]:


Type_without_collab=Type_without_collab.sort_values(by='avg_reach', ascending=False)
Type_without_collab.head()


# In[47]:


#plotting subplots
plt.figure(figsize=(20,15))
plt.subplot(2, 4, 1)
plt.bar(Type['Content Type'], Type['avg_reach'])
plt.xticks(rotation=45)
plt.subplot(2, 4, 2)
plt.bar(Type['Content Type'], Type['avg_views'])
plt.xticks(rotation=45)
plt.subplot(2, 4, 3)
plt.bar(Type['Content Type'], Type['avg_engagement'])
plt.xticks(rotation=45)
plt.subplot(2, 4, 4)
plt.plot(Type['Content Type'], Type['Engagement_rate'])
plt.xticks(rotation=45)
plt.subplot(2, 4, 5)
plt.bar(Type_without_collab['Content Type'], Type_without_collab['avg_reach'])
plt.xticks(rotation=45)
plt.subplot(2, 4, 6)
plt.bar(Type_without_collab['Content Type'], Type_without_collab['avg_views'])
plt.xticks(rotation=45)
plt.subplot(2, 4, 7)
plt.bar(Type_without_collab['Content Type'], Type_without_collab['avg_engagement'])
plt.xticks(rotation=45)
plt.subplot(2, 4, 8)
plt.plot(Type_without_collab['Content Type'], Type_without_collab['Engagement_rate'])
plt.xticks(rotation=45)
plt.show()


# ## 4. Content bucket wise Performance

# ### 4.1 Overall Performance (with collaboration)

# In[48]:


Bucket=pd.DataFrame()


# In[49]:


Bucket['avg_reach']= round(df.groupby('Content Buckets')['Reach'].mean())
Bucket['avg_views']= round(df.groupby('Content Buckets')['Views'].mean())
Bucket['avg_engagement']= round(df.groupby('Content Buckets')['Engagement'].mean())
Bucket['avg_impression']= round(df.groupby('Content Buckets')['Impressions'].mean())
Bucket.head()


# In[50]:


Bucket=Bucket.reset_index()
Bucket.head()


# In[51]:


Bucket['Engagement_rate']=Bucket.apply(lambda row: 100 * (row['avg_engagement'] / row['avg_reach']), axis=1)
Bucket.head()


# ### 4.2 Content Buckets performance without collaboration

# In[52]:


Bucket_without_collab=pd.DataFrame()


# In[53]:


Bucket_without_collab['avg_reach']= round(df_without_collab.groupby('Content Buckets')['Reach'].mean())
Bucket_without_collab['avg_views']= round(df_without_collab.groupby('Content Buckets')['Views'].mean())
Bucket_without_collab['avg_engagement']= round(df_without_collab.groupby('Content Buckets')['Engagement'].mean())
Bucket_without_collab['avg_impression']= round(df_without_collab.groupby('Content Buckets')['Impressions'].mean())
Bucket_without_collab.head()


# In[54]:


Bucket_without_collab=Bucket_without_collab.reset_index()
Bucket_without_collab.head()


# In[55]:


Bucket_without_collab['Engagement_rate']=Bucket_without_collab.apply(lambda row: 100 * (row['avg_engagement'] / row['avg_reach']), axis=1)
Bucket_without_collab.head()


# In[56]:


#sorting values
Bucket=Bucket.sort_values(by='avg_reach', ascending=False)
Bucket.head()


# In[57]:


Bucket_without_collab=Bucket_without_collab.sort_values(by='avg_reach', ascending=False)
Bucket_without_collab.head()


# In[58]:


#plotting subplots
plt.figure(figsize=(20,15))
plt.subplot(2, 4, 1)
plt.bar(Bucket['Content Buckets'], Bucket['avg_reach'])
plt.xticks(rotation=45)
plt.subplot(2, 4, 2)
plt.bar(Bucket['Content Buckets'], Bucket['avg_views'])
plt.xticks(rotation=45)
plt.subplot(2, 4, 3)
plt.bar(Bucket['Content Buckets'], Bucket['avg_engagement'])
plt.xticks(rotation=45)
plt.subplot(2, 4, 4)
plt.plot(Bucket['Content Buckets'], Bucket['Engagement_rate'])
plt.xticks(rotation=45)
plt.subplot(2, 4, 5)
plt.bar(Bucket_without_collab['Content Buckets'], Bucket_without_collab['avg_reach'])
plt.xticks(rotation=45)
plt.subplot(2, 4, 6)
plt.bar(Bucket_without_collab['Content Buckets'], Bucket_without_collab['avg_views'])
plt.xticks(rotation=45)
plt.subplot(2, 4, 7)
plt.bar(Bucket_without_collab['Content Buckets'], Bucket_without_collab['avg_engagement'])
plt.xticks(rotation=45)
plt.subplot(2, 4, 8)
plt.plot(Bucket_without_collab['Content Buckets'], Bucket_without_collab['Engagement_rate'])
plt.xticks(rotation=45)
plt.show()


# ## 5. Month wise Performance

# ### 5.1 Overall Performance (with collaboration)

# In[59]:


Month=pd.DataFrame()


# In[60]:


Month['avg_reach']= round(df.groupby('Month')['Reach'].mean())
Month['avg_views']= round(df.groupby('Month')['Views'].mean())
Month['avg_engagement']= round(df.groupby('Month')['Engagement'].mean())
Month['avg_impression']= round(df.groupby('Month')['Impressions'].mean())
Month.head(6)


# In[61]:


Month=Month.reset_index()
Month.head()


# In[62]:


Month['Engagement_rate']=Month.apply(lambda row: 100 * (row['avg_engagement'] / row['avg_reach']), axis=1)
Month.head()


# ### 5.2 Month performance without collaboration

# In[63]:


Month_without_collab=pd.DataFrame()


# In[64]:


Month_without_collab['avg_reach']= round(df_without_collab.groupby('Month')['Reach'].mean())
Month_without_collab['avg_views']= round(df_without_collab.groupby('Month')['Views'].mean())
Month_without_collab['avg_engagement']= round(df_without_collab.groupby('Month')['Engagement'].mean())
Month_without_collab['avg_impression']= round(df_without_collab.groupby('Month')['Impressions'].mean())
Month_without_collab.head()


# In[65]:


Month_without_collab=Month_without_collab.reset_index()
Month_without_collab.head()


# In[66]:


Month_without_collab['Engagement_rate']=Month_without_collab.apply(lambda row: 100 * (row['avg_engagement'] / row['avg_reach']), axis=1)
Month_without_collab.head()


# In[67]:


#sorting values
Month=Month.sort_values(by='avg_reach', ascending=False)
Month.head()


# In[68]:


Month_without_collab=Month_without_collab.sort_values(by='avg_reach', ascending=False)
Month_without_collab.head()


# In[69]:


#plotting subplots
plt.figure(figsize=(20,15))
plt.subplot(2, 4, 1)
plt.bar(Month['Month'], Month['avg_reach'])
plt.xticks(rotation=45)
plt.subplot(2, 4, 2)
plt.bar(Month['Month'], Month['avg_views'])
plt.xticks(rotation=45)
plt.subplot(2, 4, 3)
plt.bar(Month['Month'], Month['avg_engagement'])
plt.xticks(rotation=45)
plt.subplot(2, 4, 4)
plt.plot(Month['Month'], Month['Engagement_rate'])
plt.xticks(rotation=45)
plt.subplot(2, 4, 5)
plt.bar(Month_without_collab['Month'], Month_without_collab['avg_reach'])
plt.xticks(rotation=45)
plt.subplot(2, 4, 6)
plt.bar(Month_without_collab['Month'], Month_without_collab['avg_views'])
plt.xticks(rotation=45)
plt.subplot(2, 4, 7)
plt.bar(Month_without_collab['Month'], Month_without_collab['avg_engagement'])
plt.xticks(rotation=45)
plt.subplot(2, 4, 8)
plt.plot(Month_without_collab['Month'], Month_without_collab['Engagement_rate'])
plt.xticks(rotation=45)
plt.show()


# ## 6. Date wise Performance

# In[70]:


Date=pd.DataFrame()


# In[71]:


Date['Reach']= round(df.groupby('Date of release')['Reach'].sum())
Date['Views']= round(df.groupby('Date of release')['Views'].sum())
Date['Engagement']= round(df.groupby('Date of release')['Engagement'].sum())
Date['Impression']= round(df.groupby('Date of release')['Impressions'].sum())
Date.head()


# In[72]:


Date=Date.reset_index()
Date.head()


# In[73]:


plt.figure(figsize=(25,15))
plt.subplot(4, 1, 1)
plt.plot(Date['Date of release'], Date['Reach'])
plt.subplot(4, 1, 2)
plt.plot(Date['Date of release'], Date['Views'])
plt.subplot(4, 1, 3)
plt.plot(Date['Date of release'], Date['Engagement'])
plt.subplot(4, 1, 4)
plt.plot(Date['Date of release'], Date['Impression'])
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:




