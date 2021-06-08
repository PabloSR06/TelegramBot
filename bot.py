# encoding: utf-8
bot_token = "1837182286:AAFSDP59Gwy3RRJg3kfdfj3IueO4sZ3OyMM"

#LIBRERIAS RESPONDER
from telegram.ext import Updater #ENVIAR MENSAJES RESPONDIENDO
import logging #INICIO DE SESION
from telegram.ext import CommandHandler #COMANDOS


#LIBRERIAS DE FECHAS
from datetime import date
from datetime import datetime


#LIBRERIAS RANDOM

import random


#PREDEFINIDO
updater = Updater(token = bot_token, use_context = True)
dispatcher = updater.dispatcher

#INICIO DE SESION
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)

#FUNCIONES DE LOS COMANDOS
def start(update, context):
    print(update.effective_chat.id) #ESCRIBE EL CHAT ID DE LA PERSONA
    
    context.bot.send_message(chat_id=update.effective_chat.id, text="HOLA!") #RESPONDE A EL CHAT EN EL QUE LE HABLAN

def personas(update, context):
    print(update.effective_chat.id) #ESCRIBE EL CHAT ID DE LA PERSONA
    #ALMACENA EL CHAT ID A EL ARCHIVO: personas/personas.txt
    archivo = open('personas/personas.txt', 'a')
    archivo.write(str(update.effective_chat.id)+"\n")
    archivo.close()
    
    context.bot.send_message(chat_id=update.effective_chat.id, text="AHORA ESTÁS EN LA LISTA!!") #RESPONDE A EL CHAT EN EL QUE LE HABLAN

def fecha(update, context):
    selection = random.randint(0, 1)
    now = date.today()
    if(selection == 1):
        id = update.effective_chat.id
        print(str(id) + ' - ' + 'Fecha' ) 
        context.bot.send_message(chat_id=update.effective_chat.id, text=str(now)) 
    else:
        months = ("Enero", "Febrero", "Marzo", "Abri", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")
        day = now.day
        month = months[now.month - 1]
        year = now.year
        fecha = "{} de {} del {}".format(day, month, year)
        context.bot.send_message(chat_id=update.effective_chat.id, text=str(fecha)) 


def instagram(update,context):
    id = update.effective_chat.id
    print(str(id) + ' - ' + 'Instagram' ) 
    instagram = "https://www.instagram.com/pablosr06/"
    context.bot.send_message(chat_id=update.effective_chat.id, text=instagram) 

def frase(update, context):
    
    datos = []
    with open("listas/frases.txt") as fname:
        lineas = fname.readlines()
        for linea in lineas:
            datos.append(linea.strip('\n'))


    selection = random.randint(0, len(datos))
    id = update.effective_chat.id
    print(str(id) + ' - ' + 'frase' + ' - ' + str(selection)) 
    frase = datos[selection]
    context.bot.send_message(chat_id=update.effective_chat.id, text=frase) 



           

start = CommandHandler('start', start) #LLAMA A LA FUNCION start CON EL COMANDO /start
personas = CommandHandler('personas', personas) #LLAMA A LA FUNCION personas CON EL COMANDO /personas
fecha = CommandHandler('fecha', fecha)
instagram = CommandHandler('instagram', instagram)
frase = CommandHandler('frase', frase)

dispatcher.add_handler(start) #ANADE EL COMANDO PARA QUE FUNCIONE
dispatcher.add_handler(personas) #ANADE EL COMANDO PARA QUE FUNCIONE
dispatcher.add_handler(fecha)
dispatcher.add_handler(instagram)
dispatcher.add_handler(frase)

updater.start_polling() #ENCIENDE EL BOT, PARA PARAR updater.stop()

#USAR SIN COMANDOS, NO HACE FALTA EL USO DE LO DE ARRIBA, SALVO el "bot_token" Y LA LISTA DE CHAT-IDs

#LIBRERIAS SIN RESPONDER
from telegram import Bot #ENVIAR MENSAJES SIN RESPONDER

#ENVIAR SIN RESPONDER
def enviarSinResponder():
    
    personasLista = [] #CREA LISTA
    with open('personas/personas.txt', 'r') as archivo: #OBTIENE CHAT IDs OBTENIDOS GRACIAS A /personas
        for personaLinea in archivo:
            persona = personaLinea[:-1]
            personasLista.append(persona)
    for i in personasLista: #MANDA UN MENSAJE A CADA UNO DE LAS PERSONAS QUE HAY EN EL ARCHIVO
        bot = Bot(bot_token) #DEFINE "bot" A NUESTRO TOKEN
        
        bot.send_message(chat_id=i,text="ESTO ES UNA PRUEBA2!") #MANDA MENSAJE

#while True:
   # now = datetime.now()
    #if(now.strftime('%H') == '18' and now.strftime('%M') =='12' and now.strftime('%S') =='31'and now.microsecond =='31'):
     #   enviarSinResponder()
