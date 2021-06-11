bot_token = "1837182286:AAFSDP59Gwy3RRJg3kfdfj3IueO4sZ3OyMM"

from telegram.ext import Updater #ENVIAR MENSAJES RESPONDIENDO
import logging #INICIO DE SESION
from telegram.ext import CommandHandler, Filters, MessageHandler #COMANDOS
from datetime import date
from datetime import datetime
import random
from telegram import Bot
import os


#FUNCIONES DE LOS COMANDOS
def start(update, context):
    id = update.effective_chat.id 
    entrada = (str(id) + ' - ' + 'Start')
    print(entrada)
    historial(entrada) #Envia a la funcion historial, la entrada
    
    context.bot.send_message(chat_id=id, text="BOT INICIADO!") #RESPONDE EL CHAT
    
def help(update, context):
    update.message.reply_text('help command received')

# function to handle errors occured in the dispatcher 
def error(update, context):
    update.message.reply_text('an error occured')

# function to handle normal text 
def text(update, context):
    text_received = update.message.text
    update.message.reply_text(f'Escibiste "{text_received}" ? \n\n Prueba a escribir un comando con /')
    
    
def personas(update, context):
    print(update.effective_chat.id) #ESCRIBE EL CHAT ID DE LA PERSONA
    #ALMACENA EL CHAT ID A EL ARCHIVO: personas/personas.txt
    archivo = open('personas/personas.txt', 'a')
    archivo.write(str(update.effective_chat.id)+"\n")
    archivo.close()
    
    context.bot.send_message(chat_id=update.effective_chat.id, text="AHORA ESTÁS EN LA LISTA!!") #RESPONDE A EL CHAT EN EL QUE LE HABLAN


#Imprime la fecha de hoy de 2 formas distintas
def fecha(update, context):
    selection = random.randint(0, 1)
    now = date.today()

    id = update.effective_chat.id
    entrada = (str(id) + ' - ' + 'Fecha' + ' - ' +str(selection))
    print(entrada) 
    historial(entrada)

    if(selection == 1):
        context.bot.send_message(chat_id=id, text=str(now)) 
    else:
        months = ("Enero", "Febrero", "Marzo", "Abri", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")
        day = now.day
        month = months[now.month - 1]
        year = now.year
        fecha = "{} de {} del {}".format(day, month, year)
        context.bot.send_message(chat_id=id, text=str(fecha)) 

#Envia el enlace a instagram
def instagram(update,context):
    id = update.effective_chat.id
    entrada = (str(id) + ' - ' + 'Instagram')
    print(entrada) 
    historial(entrada)

    instagram = "https://www.instagram.com/pablosr06/"
    context.bot.send_message(chat_id=id, text=instagram) 

#Envia una frase aleatoria
def frase(update, context):
    datos = []
    with open("listas/frases.txt") as fname:
        lineas = fname.readlines()
        for linea in lineas:
            datos.append(linea.strip('\n'))


    selection = random.randint(0, len(datos))
    id = update.effective_chat.id
    entrada = str(id) + ' - ' + 'Frase' + ' - ' + str(selection) 
    print(entrada) 
    historial(entrada)

    frase = datos[selection]
    context.bot.send_message(chat_id=id, text=frase) 
    

def echo(update, context):
    if(len(update.args) > 0):
        user_says = " ".join(context.args)
        update.message.reply_text(user_says)
    else:
        update.message.reply_text("Tienes que escribir un argumento")


#Envia cara o cruz
def moneda(update, context):
    selection = random.randint(0, 1)
    id = update.effective_chat.id
    entrada = str(id) + ' - ' + 'Moneda' + ' - ' + str(selection)
    print(entrada) 
    historial(entrada)

    if(selection == 0):
        msg = 'Cara'
    else:
        msg = 'Cruz'
        
    context.bot.send_message(chat_id=id, text=msg) 

#ADD TO historial.txt ALL the history that is printed in the console
def historial(historia):    
    Historial = [] 
    with open('listas/historial.txt', 'r+') as archivo: 
        contenido= archivo.read()
        archivo.write(historia + "\n")


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


if __name__ == '__main__':

    updater = Updater(token = bot_token, use_context = True)
    dispatcher = updater.dispatcher

    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)

    dispatcher = updater.dispatcher
    
    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('personas', personas))
    dispatcher.add_handler(CommandHandler('help', help))
    dispatcher.add_handler(MessageHandler(Filters.text, text))

    dispatcher.add_handler(CommandHandler('fecha', fecha))
    dispatcher.add_handler(CommandHandler('instagram', instagram))
    dispatcher.add_handler(CommandHandler('frase', frase))
    dispatcher.add_handler(CommandHandler('Moneda', moneda))
    dispatcher.add_handler(CommandHandler('echo', echo))
    
    dispatcher.add_error_handler(error)
    
    updater.start_polling()
    updater.idle()