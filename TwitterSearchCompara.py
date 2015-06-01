#importamos la libreria tweepy para acceder de forma sencilla
#a la API de Twitter
import tweepy
 
#Aqui van nuestras claves de acceso a Twitter, obtenidas en http://dev.twitter.com
CONSUMER_KEY = 'HcQ3clbNtGOUomFkOCcTfQ' 
CONSUMER_SECRET = '6TPOeBC3qRo5iQbZpEZq1Ums8yvhTSgjmK0NrLvKZE'
ACCESS_KEY = '465700537-HCNXTvVootESey32GByYN52NqvTDdOmMkmRw44ZF'
ACCESS_SECRET = 'kdC5WuLKhwZPGV7DwKsyzMVCy8ELA11XNSIOqiMAtDzey'
 
#Primero nos identificamos ante Twitter con nuestras claves
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

#guardamos en la variable "twitter" el objeto que nos da acceso a Twitter
twitter = tweepy.API(auth)

#Buscamos todos los tweets (limitado por twitter a los ultimos dias) con el hashtag raspberrypi y el emoticono :)
#  y recorremos los resultados aumentando un contador por cada tweet
countPos = 0
for tweets in tweepy.Cursor(twitter.search, q='#raspberrypi :)').items():
    countPos+=1

#Buscamos todos los tweets (limitado por twitter a los ultimos dias)  con el hashtag raspberrypi y el emoticono :( 
# y recorremos los resultados aumentando un contador por cada tweet
countNeg = 0
for tweets in tweepy.Cursor(twitter.search, q='#raspberrypi :(').items():
    countNeg+=1
    
print('Tweets positivos ' + str(countPos))
print('Tweets negativos ' + str(countNeg))
