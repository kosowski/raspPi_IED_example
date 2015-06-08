#importamos la libreria tweepy para acceder de forma sencilla
#a la API de Twitter
import tweepy
import socket   #for sockets
 
#Aqui van nuestras claves de acceso a Twitter, obtenidas en http://dev.twitter.com
CONSUMER_KEY = '****************' 
CONSUMER_SECRET = '*******************************'
ACCESS_KEY = '*******-**********************************'
ACCESS_SECRET = '**************************************'
 
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

 
# Creamos datagrama UDP
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
except socket.error:
    print('Failed to create socket')

# para enviarlo a nosotrosmismos (localhost) en el puerto 8888 
host = 'localhost';
port = 8888;

# enviamos el numero de positivos, un gion separador, y el numero de negativos
msg = str(countPos)+'-'+str(countNeg)

# aqui lo enviamos
try :
    #Set the whole string
    s.sendto(msg, (host, port))
    
except socket.error as msg:
    print('Error Code : ' + str(msg[0]) + ' Message ' + msg[1])

