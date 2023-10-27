import requests

from twilio.rest import Client



OWN_Endpoint = "https://api.openweathermap.org/data/2.5/weather"
api_key = "d4acf676421e3e9ce68780e806ec2574"

weather_params = {
     "lat":13.082680,
      "lon":80.270721,
       "appid":api_key,
       "exclude": "currently,minutely,daily"

}
response = requests.get(OWN_Endpoint,params=weather_params)

response.raise_for_status()
wheather_data = response.json()


condition_code = wheather_data['weather'][0]['id']

will_rain = False
if condition_code < 700:
    will_rain = True
account_sid = "AC44b22b4896282aa27dbb95c14f7e6144"
auth_token = "c048d25d40111ddf8d9c46fc91e9be30"

if will_rain :
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="Its too cloudy outside, don't forget to take umbrella and enjoy the weather.",
        from_='+15737874989',
        to='+91 73389 20924'

    )
    print(message.status)
else:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="Enjoy the sunlight, eat lots of watermelon and mangoes.",
        from_='+15737874989',
        to='+91 73389 20924'
    )
    print(message.status)
