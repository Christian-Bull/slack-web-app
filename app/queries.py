# contains api calls to the slack api
from slack import WebClient
import os
from datetime import datetime

# setup slack api
token = os.environ.get('SLACK_TOKEN')


def get_pins(channel_id, user_id, user):
    slackclient = WebClient(token)

    results = slackclient.pins_list(
        token=token,
        channel=channel_id
    )
    data = []

    for item in results['items']:
        # this only works for pins that are
        try:
            if item['message']['user'] == user_id:
                # convert to est timestamp
                ts = int(item['created'])
                ts_utc = datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M')
                row = {
                    "date": ts_utc,
                    "user": user,
                    "text": item['message']['text']
                }
                data.append(row)
        except:
            pass
    return data
