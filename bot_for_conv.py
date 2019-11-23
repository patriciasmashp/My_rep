import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import requests
import random
import check
import time 


token = 'c2106e42075d6e0ff11483a4285fa53633c1deb7a8e4370bbcc23c1d55b499df2edd41f5a4e2106e4ec7a'
# 
session = requests.Session()

group_id = 188695946
vk_session = vk_api.VkApi(token=token)
bot_api = vk_session.get_api()


# def answerf(peer_id, message):
#     vk.method('messages.send', {'peer_id': peer_id, 'message': message, 'random_id': rand()})


def rand():
    r = random.randint(0, 500000000000000)
    print(r)
    return r

def time_rasp(ans):
    if check.check_rep(check.rsoup()):
        vk.method('messages.send', {'peer_id': 2000000002, 'message': check.resoult(), 'random_id': rand()})
    # time.sleep(5)

def ans():
    answer=''
    try:
        for i in check.resoult():
	        answer+=str(i)+'\n'
    except:
	    print('Eror_from_messege')
    return answer





try:
    vk_session.auth(token_only=True)
except vk_api.AuthError as error_msg:
    print(error_msg)


vk = vk_api.VkApi(token=token)
longpoll = VkBotLongPoll(vk, group_id)



for event in longpoll.listen():
    try:
        if event.type == VkBotEventType.MESSAGE_NEW:
            if event.obj.message['text'].lower() == 'замены':
                request = event.obj.message['peer_id']
                print(type(check.resoult()))
                try:
                	vk.method('messages.send', {'peer_id': request, 'message': check.resoult(), 'random_id': rand()})
                except Exception as e:
                	print(e)
            if event.obj.message['text'].lower() == 'тебе за':
                if event.obj.message['from_id'] in [569855371,171791677]:
                    request = event.obj.message['peer_id']
                    vk.method('messages.send', {'peer_id': request, 'message': 'ДоПусКОм!!!!1!!', 'random_id': rand(), 'attachment':'photo-188695946_457239018'})
            if event.obj.message['text'].lower() == 'uvolen':
                break
    except Exception as e:
        raise e

