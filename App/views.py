from django.shortcuts import render
from datetime import datetime

import cryptocompare
import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate('cryptotracker-53997-firebase-adminsdk-egcsg-ec07b4dce9.json')
myApp = firebase_admin.initialize_app(cred)
import time


# Create your views here.






def base(request):
    return render(request,'App/base.html')

def index(request):
    if request.method == "POST":


        eth_server_start = request.POST.get('start_eth_server','')
        global eth_server_start
        eth_server_stop = request.POST.get('stop_eth_server','')
        global eth_server_stop




    return render(request,'App/index.html')


def startEthServer():
    while (eth_server_start and not eth_server_stop):
        now = int(datetime.now().strftime("%H%M")) / 100
        db = firestore.client()
        save_data = db.collection('ETH').document(f'{time.localtime().tm_year}').collection(
            f'{time.localtime().tm_mon}').document(f'{time.localtime().tm_mday}').collection('Data')
        save_data.add({
            'time': now,
            'price': cryptocompare.get_price('ETH', currency='USD')
        }
        )
        print('data_saved')
        time.sleep(60)



class StartServer:
    def __init__(self,coin_name,):
        self.coin_name = coin_name

        while (eth_server_start and not eth_server_stop):
            now = int(datetime.now().strftime("%H%M")) / 100
            db = firestore.client()
            save_data = db.collection(f'{coin_name}').document(f'{time.localtime().tm_year}').collection(
                f'{time.localtime().tm_mon}').document(f'{time.localtime().tm_mday}').collection('Data')
            save_data.add({
                'time': now,
                'price': cryptocompare.get_price(f'{coin_name}', currency='USD')
            }
            )
            print('data_saved')
            time.sleep(60)

if(eth_server_start == 'start' and not eth_server_stop):
    while(eth_server_stop!="stop"):
        eth_server = StartServer('ETH')