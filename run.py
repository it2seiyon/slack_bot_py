import time
import asyncio
from slackclient import SlackClient

#slack token
token = ''
sc = SlackClient(token)


async def run_bot():
    if sc.rtm_connect():  # connect to a Slack RTM websocket
        while True:
            msg = sc.rtm_read()
            if len(msg) > 0:
                analytics_msg(msg[0])
            time.sleep(1)
    else:
        print('Connection Failed, invalid token?')


def analytics_msg(msg):
    print(msg)  #
    if 'user' in msg:
        print(msg)
        if msg['type'] == 'member_joined_channel':
            if 'inviter' in msg and msg['inviter'] == 'U5GUVDV0W':
                sc.api_call(
                    "chat.postMessage",
                    channel=msg['channel'],
                    text="초대해 주셔서 감사합니다. :grin:")
            else:
                name = ''
                if 'user_profile' in msg and 'name' in msg['user_profile']:
                    name = msg['user_profile']['name'] + "님 "
                sc.api_call(
                    "chat.postMessage",
                    channel=msg['channel'],
                    text=name + "반갑습니다. 아직은 지능이 낮아서 많은 도움은 못드립니다. 앞으로 많은 발전 하겠습니다. :grin:")


loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)
asyncio.get_event_loop().run_until_complete(run_bot())
asyncio.get_event_loop().run_forever()
