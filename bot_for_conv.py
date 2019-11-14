import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import requests
import random
import check


token = ''
# 
session = requests.Session()

group_id = 188695946
vk_session = vk_api.VkApi(token=token)
bot_api = vk_session.get_api()


def answer(peer_id, message):
    vk.method('messages.send', {'peer_id': peer_id, 'message': message, 'random_id': rand()})


def rand():
    r = random.randint(0, 500000000000000)
    print(r)
    return r
# repl = str(check.replasment())
answer=''
try:
    for i in check.resoult():
	    answer+=str(i)+'\n'

except:
	print('Eror_from_messege')

print(answer)

try:
    vk_session.auth(token_only=True)
except vk_api.AuthError as error_msg:
    print(error_msg)
vk = vk_api.VkApi(token=token)
longpoll = VkBotLongPoll(vk, group_id)
for event in longpoll.listen():
    if event.type == VkBotEventType.MESSAGE_NEW:
    	if event.obj.message['text'].lower() == 'замены':
            request = event.obj.message['peer_id']
            vk.method('messages.send', {'peer_id': request, 'message': '%s'%answer, 'random_id': rand()})
