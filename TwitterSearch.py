#importamos la libreria tweepy para acceder de forma sencilla
#a la API de Twitter
import tweepy
 
#Aqui van nuestras claves de acceso a Twitter, obtenidas en http://dev.twitter.com
CONSUMER_KEY = '****************' 
CONSUMER_SECRET = '****************'
ACCESS_KEY = '****************-****************'
ACCESS_SECRET = '****************'
 
#Primero nos identificamos ante Twitter con nuestras claves
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

#guardamos en la variable "twitter" el objeto que nos da acceso a Twitter
twitter = tweepy.API(auth)

#Buscamos tweets con el hashtag raspberrypi y el emoticono :) hasta un maximo de 10
#ordenador por mas reciente y recorremos los resultados
for tweets in twitter.search(q='#raspberrypi :)',count=10, result_type='recent'):
    #para cada tweet sacamos por pantalla la fecha de creacion
    print(tweets.created_at)
    #el nombre de usuario
    print(tweets.user.screen_name)
    # y el texto
    print(tweets.text)
    # despues ponemos 40 asteriscos como separador con el proximo tweet
    print(' *'*40)
