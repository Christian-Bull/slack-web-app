# contains api calls to the slack api
from app import models
from slack import WebClient
import os
from datetime import datetime

# setup slack api
token = os.environ.get('SLACK_TOKEN')

# est is minus 5 utc
time_delta = -5

def get_pins(channel_id, user_id, user):
    slackclient = WebClient(token)

    results = slackclient.pins_list(
        token=token,
        channel=channel_id
    )
    data = []

    for item in results['items']:

        # TODO Add method that deals with empty user arg
        # this only works for pins that are messages
        try:
            if item['message']['user'] == user_id:
                # convert to est timestamp
                ts = int(item['created'])
                ts_str = datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M')

                # get headers and convert user_ids to usernames
                pinned_by = models.get_user_name(item['created_by'])
                headers = ['date', 'user', 'text', 'pinned by']

                # add this row
                row = {
                    "date": ts_str,
                    "user": user,
                    "text": item['message']['text'],
                    "pinned_by": pinned_by
                }
                data.append(row)
        except:
            pass

    return headers, data
