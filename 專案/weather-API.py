import requests
from time import sleep

#city ='HongKong'
print('你可以在這裏查詢地方的温度')
sleep(1)

city =input('請輸入地方 ')
api_key = 'b85f1d04ed29cb2e9f8acc9c041658b0'
address = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

try:
    data = requests.get(address)
    x=(round(data.json()['main']['temp']-273.15,2))
    # print(f'現在{city}是攝氏'+str(round(data.json()['main']['temp']-273.15,2))+'。')
    print(f'現在{city}是攝氏°{x}。')
except:
    print('地方輸入錯誤，請重新確認是否有錯字!')
    

#data = requests.get(address)

# print(f'現在{city}是攝氏'+str(round(data.json()['main']['temp']-273.15,2))+'。')

# x=(round(data.json()['main']['temp']-273.15,2))

if x <= 18:
    print('今天很汵。')
elif x >= 18 and x <= 22:
    print('今天很涼。')
else:
    print('今天很熱。')