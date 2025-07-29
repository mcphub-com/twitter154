import requests
from datetime import datetime
from typing import Union, Literal, List
from mcp.server import FastMCP
from pydantic import Field
from typing import Annotated
from mcp.server.fastmcp import FastMCP
from fastmcp import FastMCP, Context
import os
from dotenv import load_dotenv
load_dotenv()
rapid_api_key = os.getenv("RAPID_API_KEY")

__rapidapi_url__ = 'https://rapidapi.com/datahungrybeast/api/twitter154'

mcp = FastMCP('twitter154')

@mcp.tool()
def user_details(username: Annotated[Union[str, None], Field(description='')] = None,
                 user_id: Annotated[Union[str, None], Field(description='')] = None) -> dict: 
    '''This endpoint returns the public information about a Twitter profile'''
    url = 'https://twitter154.p.rapidapi.com/user/details'
    headers = {'x-rapidapi-host': 'twitter154.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'username': username,
        'user_id': user_id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def user_stweets(username: Annotated[Union[str, None], Field(description='')] = None,
                 limit: Annotated[Union[int, float, None], Field(description='Default: 40 Minimum: 1 Maximum: 100')] = None,
                 user_id: Annotated[Union[str, None], Field(description='')] = None,
                 include_replies: Annotated[Union[bool, None], Field(description='')] = None,
                 include_pinned: Annotated[Union[bool, None], Field(description='')] = None) -> dict: 
    '''This endpoint return a list of user's tweets given a username'''
    url = 'https://twitter154.p.rapidapi.com/user/tweets'
    headers = {'x-rapidapi-host': 'twitter154.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'username': username,
        'limit': limit,
        'user_id': user_id,
        'include_replies': include_replies,
        'include_pinned': include_pinned,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def user_stweets_continuation(continuation_token: Annotated[str, Field(description='')],
                              username: Annotated[Union[str, None], Field(description='')] = None,
                              limit: Annotated[Union[int, float, None], Field(description='Default: 40')] = None,
                              user_id: Annotated[Union[str, None], Field(description='')] = None,
                              include_replies: Annotated[Union[bool, None], Field(description='')] = None) -> dict: 
    '''This endpoint return the next list of user's tweets given a username'''
    url = 'https://twitter154.p.rapidapi.com/user/tweets/continuation'
    headers = {'x-rapidapi-host': 'twitter154.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'continuation_token': continuation_token,
        'username': username,
        'limit': limit,
        'user_id': user_id,
        'include_replies': include_replies,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def user_sfollowing(user_id: Annotated[str, Field(description='')],
                    limit: Annotated[Union[int, float, None], Field(description='Default: 40 Minimum: 1 Maximum: 100')] = None) -> dict: 
    '''This endpoint returns the list of following'''
    url = 'https://twitter154.p.rapidapi.com/user/following'
    headers = {'x-rapidapi-host': 'twitter154.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'user_id': user_id,
        'limit': limit,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def user_sfollowing_continuation(user_id: Annotated[str, Field(description='')],
                                 continuation_token: Annotated[str, Field(description='')],
                                 limit: Annotated[Union[int, float, None], Field(description='Default: 40 Minimum: 1 Maximum: 100')] = None) -> dict: 
    '''This endpoint gets the next list of following using the token from the former call'''
    url = 'https://twitter154.p.rapidapi.com/user/following/continuation'
    headers = {'x-rapidapi-host': 'twitter154.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'user_id': user_id,
        'continuation_token': continuation_token,
        'limit': limit,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def user_sfollowers(user_id: Annotated[str, Field(description='')],
                    limit: Annotated[Union[int, float, None], Field(description='Default: 10 Minimum: 1 Maximum: 20')] = None) -> dict: 
    '''This endpoint return a list of user's followers given a user ID'''
    url = 'https://twitter154.p.rapidapi.com/user/followers'
    headers = {'x-rapidapi-host': 'twitter154.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'user_id': user_id,
        'limit': limit,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def continuation_user_sfollowers(user_id: Annotated[str, Field(description='')],
                                 continuation_token: Annotated[str, Field(description='')],
                                 limit: Annotated[Union[int, float, None], Field(description='Default: 10 Minimum: 1 Maximum: 20')] = None) -> dict: 
    '''This endpoint returns the list of a user's followers'''
    url = 'https://twitter154.p.rapidapi.com/user/followers/continuation'
    headers = {'x-rapidapi-host': 'twitter154.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'user_id': user_id,
        'continuation_token': continuation_token,
        'limit': limit,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def user_slikes(user_id: Annotated[str, Field(description='')],
                limit: Annotated[Union[int, float, None], Field(description='Default: 20 Minimum: 1 Maximum: 20')] = None) -> dict: 
    '''This endpoint return a list of user's likes given a user ID'''
    url = 'https://twitter154.p.rapidapi.com/user/likes'
    headers = {'x-rapidapi-host': 'twitter154.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'user_id': user_id,
        'limit': limit,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def continuation_user_slikes(user_id: Annotated[str, Field(description='')],
                             continuation_token: Annotated[str, Field(description='')],
                             limit: Annotated[Union[int, float, None], Field(description='Default: 10 Minimum: 1 Maximum: 20')] = None) -> dict: 
    '''This endpoint returns the list of a user's Likes'''
    url = 'https://twitter154.p.rapidapi.com/user/likes/continuation'
    headers = {'x-rapidapi-host': 'twitter154.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'user_id': user_id,
        'continuation_token': continuation_token,
        'limit': limit,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def user_smedia(user_id: Annotated[str, Field(description='')],
                limit: Annotated[Union[int, float, None], Field(description='Default: 10 Minimum: 1 Maximum: 20')] = None) -> dict: 
    '''This endpoint return a list of user's media given a user ID'''
    url = 'https://twitter154.p.rapidapi.com/user/medias'
    headers = {'x-rapidapi-host': 'twitter154.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'user_id': user_id,
        'limit': limit,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def continuation_user_smedia(user_id: Annotated[str, Field(description='')],
                             continuation_token: Annotated[str, Field(description='')],
                             limit: Annotated[Union[int, float, None], Field(description='Default: 10 Minimum: 1 Maximum: 20')] = None) -> dict: 
    '''This endpoint returns the list of a user's medias'''
    url = 'https://twitter154.p.rapidapi.com/user/medias/continuation'
    headers = {'x-rapidapi-host': 'twitter154.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'user_id': user_id,
        'continuation_token': continuation_token,
        'limit': limit,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def tweet_details(tweet_id: Annotated[str, Field(description='')]) -> dict: 
    '''This endpoint return general information about a tweet'''
    url = 'https://twitter154.p.rapidapi.com/tweet/details'
    headers = {'x-rapidapi-host': 'twitter154.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'tweet_id': tweet_id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def tweet_replies(tweet_id: Annotated[str, Field(description='')]) -> dict: 
    '''This endpoint returns a list of reply tweets'''
    url = 'https://twitter154.p.rapidapi.com/tweet/replies'
    headers = {'x-rapidapi-host': 'twitter154.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'tweet_id': tweet_id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def tweet_replies_continuation(tweet_id: Annotated[str, Field(description='')],
                               continuation_token: Annotated[str, Field(description='')]) -> dict: 
    '''This endpoint returns the next list of reply tweets'''
    url = 'https://twitter154.p.rapidapi.com/tweet/replies/continuation'
    headers = {'x-rapidapi-host': 'twitter154.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'tweet_id': tweet_id,
        'continuation_token': continuation_token,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def tweet_user_retweets(tweet_id: Annotated[str, Field(description='')],
                        limit: Annotated[Union[str, None], Field(description='')] = None) -> dict: 
    '''This endpoint returns a list of user who retweeted the tweet'''
    url = 'https://twitter154.p.rapidapi.com/tweet/retweets'
    headers = {'x-rapidapi-host': 'twitter154.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'tweet_id': tweet_id,
        'limit': limit,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def tweet_user_retweets_continuation(tweet_id: Annotated[str, Field(description='')],
                                     continuation_token: Annotated[str, Field(description='')],
                                     limit: Annotated[Union[str, None], Field(description='')] = None) -> dict: 
    '''This endpoint returns the next list of user who retweeted the tweet'''
    url = 'https://twitter154.p.rapidapi.com/tweet/retweets/continuation'
    headers = {'x-rapidapi-host': 'twitter154.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'tweet_id': tweet_id,
        'continuation_token': continuation_token,
        'limit': limit,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def tweet_user_favoriters(tweet_id: Annotated[str, Field(description='')]) -> dict: 
    '''This endpoint returns a list of user who favorited the tweet'''
    url = 'https://twitter154.p.rapidapi.com/tweet/favoriters'
    headers = {'x-rapidapi-host': 'twitter154.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'tweet_id': tweet_id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def tweet_user_favoriters_continuation(tweet_id: Annotated[str, Field(description='')],
                                       continuation_token: Annotated[str, Field(description='')]) -> dict: 
    '''This endpoint returns the next list of user who favorited the tweet'''
    url = 'https://twitter154.p.rapidapi.com/tweet/favoriters/continuation'
    headers = {'x-rapidapi-host': 'twitter154.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'tweet_id': tweet_id,
        'continuation_token': continuation_token,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def search(query: Annotated[str, Field(description='')],
           section: Annotated[Union[str, None], Field(description='')] = None,
           min_retweets: Annotated[Union[int, float, None], Field(description='Default: 1 Minimum: 0')] = None,
           min_likes: Annotated[Union[int, float, None], Field(description='Default: 1 Minimum: 0')] = None,
           limit: Annotated[Union[int, float, None], Field(description='Default: 5 Minimum: 1 Maximum: 20')] = None,
           min_replies: Annotated[Union[int, float, None], Field(description='Minimum: 0')] = None,
           start_date: Annotated[Union[str, None], Field(description='YYYY-MM-DD')] = None,
           language: Annotated[Union[str, None], Field(description='')] = None,
           end_date: Annotated[Union[str, None], Field(description='')] = None) -> dict: 
    '''This endpoint return search results'''
    url = 'https://twitter154.p.rapidapi.com/search/search'
    headers = {'x-rapidapi-host': 'twitter154.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'query': query,
        'section': section,
        'min_retweets': min_retweets,
        'min_likes': min_likes,
        'limit': limit,
        'min_replies': min_replies,
        'start_date': start_date,
        'language': language,
        'end_date': end_date,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def search_continuation(query: Annotated[str, Field(description='')],
                        continuation_token: Annotated[str, Field(description='')],
                        section: Annotated[Union[str, None], Field(description='')] = None,
                        min_retweets: Annotated[Union[int, float, None], Field(description='Default: 20 Minimum: 0')] = None,
                        limit: Annotated[Union[int, float, None], Field(description='Default: 5 Minimum: 1 Maximum: 20')] = None,
                        min_replies: Annotated[Union[int, float, None], Field(description='Default: 0 Minimum: 0')] = None,
                        min_likes: Annotated[Union[int, float, None], Field(description='Default: 20 Minimum: 0')] = None,
                        start_date: Annotated[Union[str, None], Field(description='YYYY-MM-DD')] = None,
                        language: Annotated[Union[str, None], Field(description='')] = None,
                        end_date: Annotated[Union[str, None], Field(description='')] = None) -> dict: 
    '''This endpoint return search continuation results'''
    url = 'https://twitter154.p.rapidapi.com/search/search/continuation'
    headers = {'x-rapidapi-host': 'twitter154.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'query': query,
        'continuation_token': continuation_token,
        'section': section,
        'min_retweets': min_retweets,
        'limit': limit,
        'min_replies': min_replies,
        'min_likes': min_likes,
        'start_date': start_date,
        'language': language,
        'end_date': end_date,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def geo_search(query: Annotated[str, Field(description='')],
               limit: Annotated[Union[str, None], Field(description='')] = None,
               language: Annotated[Union[str, None], Field(description='')] = None,
               latitude: Annotated[Union[str, None], Field(description='')] = None,
               longitude: Annotated[Union[str, None], Field(description='')] = None,
               range: Annotated[Union[str, None], Field(description='')] = None,
               section: Annotated[Union[str, None], Field(description='')] = None) -> dict: 
    '''Perform Geo search'''
    url = 'https://twitter154.p.rapidapi.com/search/geo'
    headers = {'x-rapidapi-host': 'twitter154.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'query': query,
        'limit': limit,
        'language': language,
        'latitude': latitude,
        'longitude': longitude,
        'range': range,
        'section': section,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def hashtag(hashtag: Annotated[str, Field(description='')],
            limit: Annotated[Union[str, None], Field(description='')] = None,
            section: Annotated[Union[str, None], Field(description='')] = None) -> dict: 
    '''This endpoint return hashtag results'''
    url = 'https://twitter154.p.rapidapi.com/hashtag/hashtag'
    headers = {'x-rapidapi-host': 'twitter154.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'hashtag': hashtag,
        'limit': limit,
        'section': section,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def hashtag_continuation(hashtag: Annotated[str, Field(description='')],
                         continuation_token: Annotated[str, Field(description='')],
                         limit: Annotated[Union[str, None], Field(description='')] = None,
                         section: Annotated[Union[str, None], Field(description='')] = None) -> dict: 
    '''This endpoint return the next hashtag results'''
    url = 'https://twitter154.p.rapidapi.com/hashtag/hashtag/continuation'
    headers = {'x-rapidapi-host': 'twitter154.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'hashtag': hashtag,
        'continuation_token': continuation_token,
        'limit': limit,
        'section': section,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def lists_details(list_id: Annotated[str, Field(description='')]) -> dict: 
    '''This endpoint returns the public information a Twitter Lists'''
    url = 'https://twitter154.p.rapidapi.com/lists/details'
    headers = {'x-rapidapi-host': 'twitter154.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'list_id': list_id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def lists_tweets(list_id: Annotated[str, Field(description='')],
                 limit: Annotated[Union[int, float, None], Field(description='Default: 40 Minimum: 1 Maximum: 100')] = None) -> dict: 
    '''This endpoint return a list of tweets in a given Twitter list'''
    url = 'https://twitter154.p.rapidapi.com/lists/tweets'
    headers = {'x-rapidapi-host': 'twitter154.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'list_id': list_id,
        'limit': limit,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def lists_tweets_continuation(list_id: Annotated[str, Field(description='')],
                              continuation_token: Annotated[str, Field(description='')],
                              limit: Annotated[Union[int, float, None], Field(description='Default: 40 Minimum: 1 Maximum: 100')] = None) -> dict: 
    '''This endpoint returns the next list of tweets in a given Twitter list'''
    url = 'https://twitter154.p.rapidapi.com/lists/tweets/continuation'
    headers = {'x-rapidapi-host': 'twitter154.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'list_id': list_id,
        'continuation_token': continuation_token,
        'limit': limit,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def get_trends_near_alocation(woeid: Annotated[str, Field(description='')]) -> dict: 
    '''Returns the top 50 trending topics for a specific id (woeid), if trending information is available for it.'''
    url = 'https://twitter154.p.rapidapi.com/trends/'
    headers = {'x-rapidapi-host': 'twitter154.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'woeid': woeid,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def available_locations() -> dict: 
    '''Get the list of available locations'''
    url = 'https://twitter154.p.rapidapi.com/trends/available'
    headers = {'x-rapidapi-host': 'twitter154.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def translate(data: Annotated[dict, Field(description='')] = None) -> dict: 
    '''Return Translated Text and the source language if it wasn't specified'''
    url = 'https://twitter154.p.rapidapi.com/translate'
    headers = {'Content-Type': 'application/json', 'x-rapidapi-host': 'twitter154.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    response = requests.post(url, headers=headers, json=data)
    return response.json()

@mcp.tool()
def detect(data: Annotated[dict, Field(description='')] = None) -> dict: 
    '''This endpoint will return the Language of the Text'''
    url = 'https://twitter154.p.rapidapi.com/translate/detect'
    headers = {'Content-Type': 'application/json', 'x-rapidapi-host': 'twitter154.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    response = requests.post(url, headers=headers, json=data)
    return response.json()

@mcp.tool()
def named_entity_recognition(text: Annotated[str, Field(description='')]) -> dict: 
    '''Locate and classify named entities mentioned in text into pre-defined categories such as person names, organizations, locations'''
    url = 'https://twitter154.p.rapidapi.com/ai/named-entity-recognition'
    headers = {'x-rapidapi-host': 'twitter154.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'text': text,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def sentiment_analysis(text: Annotated[str, Field(description='')]) -> dict: 
    '''Analyze text to determine if the emotional tone of the message is positive, negative, or neutral.'''
    url = 'https://twitter154.p.rapidapi.com/ai/sentiment-analysis'
    headers = {'x-rapidapi-host': 'twitter154.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'text': text,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def topic_classification(text: Annotated[str, Field(description='')]) -> dict: 
    '''Allows you to automatically extract meaning from text by identifying recurrent themes or topics'''
    url = 'https://twitter154.p.rapidapi.com/ai/topic-classification'
    headers = {'x-rapidapi-host': 'twitter154.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'text': text,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()



if __name__ == '__main__':
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 9997
    mcp.run(transport="stdio")
