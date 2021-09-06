bot_token = "1837182286:AAFSDP59Gwy3RRJg3kfdfj3IueO4sZ3OyMM"

from telegram.ext import CallbackQueryHandler, CommandHandler, ConversationHandler, Filters, MessageHandler, Updater, commandhandler #ENVIAR MENSAJES RESPONDIENDO
import logging #INICIO DE SESION
from datetime import date, datetime
import random
from telegram import Bot, ChatAction, InlineKeyboardMarkup, InlineKeyboardButton
import os
import qrcode
import pyshorteners


#FUNCIONES DE LOS COMANDOS
def start(update, context):
    id = update.effective_chat.id 
    entrada = (str(id) + ' - ' + 'Start')
    print(entrada)
    historial(entrada) #Envia a la funcion historial, la entrada
    
    context.bot.send_message(chat_id=id, text="BOT INICIADO!") #RESPONDE EL CHAT

#Comando help que no hace nada  
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
    id = update.effective_chat.id

    print(id) #ESCRIBE EL CHAT ID DE LA PERSONA
    #ALMACENA EL CHAT ID A EL ARCHIVO: personas/personas.txt
    archivo = open('personas/personas.txt', 'a')
    archivo.write(str(id)+"\n")
    archivo.close()

    try:
        os.mkdir('listas/' + str(id))
    except:
        print('directorio ya creado')
        


    dir = 'listas/' + str(id) + '/historial' + '.txt'
    file = open(dir, "a")
    file.close()

    dir = 'listas/' + str(id) + '/notas' + '.txt'
    file = open(dir, "a")
    file.close()
    
    context.bot.send_message(chat_id=update.effective_chat.id, text="AHORA ESTÁS EN LA LISTA!!") #RESPONDE A EL CHAT EN EL QUE LE HABLAN


#Imprime la fecha de hoy de 2 formas distintas
def fecha(update, context):
    selection = random.randint(0, 1)
    now = date.today()

    id = update.effective_chat.id
    infocom(id, "Fecha", str(selection))


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
    infocom(id, "Instagram")

    instagram = "https://www.instagram.com/pablosr06/"
    context.bot.send_message(chat_id=id, text=instagram) 

#Info sobre el autor
def autor(update, context):
    update.message.reply_text(
        text='El autor es Pablo Suárez',
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton(text='Otros enlaces', url='https://linktr.ee/pablosr')],
        ])
    )


#Envia una frase aleatoria
def frase(update, context):
    datos = []
    with open("listas/frases.txt") as fname:
        lineas = fname.readlines()
        for linea in lineas:
            datos.append(linea.strip('\n'))


    selection = random.randint(0, len(datos))

    id = update.effective_chat.id
    infocom(id, 'Frase', str(selection))

    frase = datos[selection]
    context.bot.send_message(chat_id=id, text=frase) 
    
#Funcion echo sin terminar
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

    infocom(id, "Moneda", str(selection))

    if(selection == 0):
        msg = 'Cara'
    else:
        msg = 'Cruz'
        
    context.bot.send_message(chat_id=id, text=msg) 


# Funcion para controlar la escritura en el historial y en la consola 

def infocom(id, nombre, selection=0 ):
    now = date.today()  

    if(selection == 0):
        entrada = (str(now) + ' - ' + nombre)
    else:  
        entrada = (str(now) + ' - ' + nombre + ' - ' + selection)
    
    print(entrada) 
    historial(entrada, id)
    

#ADD TO historial.txt ALL the history that is printed in the console
''''
def historial(historia):    
    Historial = [] 
    with open('listas/historial.txt', 'r+') as archivo: 
        contenido= archivo.read()
        archivo.write(historia + "\n") '''

#ADD the history to his own id.txt
def historial(historia, id):    
    Historial = [] 
    dir = 'listas/' + str(id) + '/historial' + '.txt'
    with open(dir, 'r+') as archivo: 
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
        
#Funcion para acortar URL

INPUT_URL = 0

def url(update, context):
    
    update.message.reply_text(
        text = 'Tienes un enlace para acortar?',
        reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text = 'Acortar URL', callback_data = 'url')]
        ])
    )

def url_callback_handler(update, context):

    query = update.callback_query
    query.answer()

    #Cambia el primer mensaje por otro
    query.edit_message_text(
        text='Envíame un enlace para acortarlo.'
    )

    return INPUT_URL

def input_url(update, context):

    id = update.effective_chat.id

    #Guarda el mensaje con el link
    url = update.message.text
    #Informacion sobre el chat
    chat = update.message.chat

    
    infocom(id, 'URL', str(url))

    #A la funcion de pyshorteners le das la url
    s = pyshorteners.Shortener()
    short = s.chilpit.short(url)

    #Envia la nueva url 
    chat.send_message(
        text=short
    )

    #Termina 
    return ConversationHandler.END

INPUT_NOTASNEW = 0
INPUT_NOTASSEE = 0
INPUT_NOTAS_VERTODAS = 0
INPUT_NOTAS_ULTNOTA = 0
INPUT_NOTAS_NUMNOTA = 0

def notas(update, context):

    update.message.reply_text(
        text = 'Que quieres hacer?',
        reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text = 'Nueva nota', callback_data='newnotas')],
            [InlineKeyboardButton(text = 'Ver notas', callback_data='seenotas')]
        ])
    )

def newnotas_callback_handler(update, context):

    query = update.callback_query
    query.answer()

    #Cambia el primer mensaje por otro
    query.edit_message_text(
        text='Que nota quieres añadir'
    )

    return INPUT_NOTASNEW

def newinput_notas(update, context):
    id = update.effective_chat.id

    #Guarda la nota
    nota = update.message.text
    #Informacion sobre el chat
    chat = update.message.chat
  
    infocom(id, 'Notas', nota)

    dir = 'listas/' + str(id) + '/notas' + '.txt'
    with open(dir, 'r+') as archivo: 
        contenido= archivo.read()
        archivo.write(nota + "\n") 

    #Envia la nota que se ha guardado
    chat.send_message(
        text = 'Guardado, ' + nota
    )

    #Termina 
    return ConversationHandler.END

def seenotas_callback_handler(update, context):
    id = update.effective_chat.id

    query = update.callback_query
    query.answer()
    
    '''
    dir = 'listas/' + str(id) + '/notas' + '.txt'
    with open(dir, 'r') as archivo: 
        numnotas = len(archivo.readlines())
    '''

    #Cambia el primer mensaje por otro
    query.edit_message_text(
        text = 'Que quieres hacer?',
        reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text = 'Ver todas ', callback_data='vertodas')],
            [InlineKeyboardButton(text = 'Ver ultima nota', callback_data='ultnota')],
            [InlineKeyboardButton(text = 'Ver nota numero....', callback_data='numnota')],
        ])
    )

    return INPUT_NOTASSEE

def seeinput_notas(update, context):
    id = update.effective_chat.id

    #Guarda la nota
    nota = update.message.text
    #Informacion sobre el chat
    chat = update.message.chat
  
    infocom(id, 'Ver Notas', nota)

    dir = 'listas/' + str(id) + '/notas' + '.txt'
    with open(dir, 'r+') as archivo: 
        contenido= archivo.read()
        archivo.write(nota + "\n") 

    #Envia la nota que se ha guardado
    chat.send_message(
        text = 'Guardado, ' + nota
    )

    #Termina 
    return ConversationHandler.END

def notas_vertodas_callback_handler(update, context):
    id = update.effective_chat.id

    query = update.callback_query
    query.answer()
    

    #Cambia el primer mensaje por otro
    query.edit_message_text(
        text = '1',
    )

    return ConversationHandler.END


if __name__ == '__main__':

    updater = Updater(token = bot_token, use_context = True)

    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)

    dispatcher = updater.dispatcher
    
    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('personas', personas))
    dispatcher.add_handler(CommandHandler('help', help))
    #dispatcher.add_handler(MessageHandler(Filters.text, text))
    dispatcher.add_handler(CommandHandler('fecha', fecha))
    dispatcher.add_handler(CommandHandler('instagram', instagram))
    dispatcher.add_handler(CommandHandler('frase', frase))
    dispatcher.add_handler(CommandHandler('Moneda', moneda))
    dispatcher.add_handler(CommandHandler('echo', echo))
    dispatcher.add_handler(CommandHandler('autor', autor))

    dispatcher.add_handler(CommandHandler('url', url))

    dispatcher.add_handler(ConversationHandler(
        entry_points=[
            CallbackQueryHandler(pattern='url', callback=url_callback_handler)
        ],
        states={
            INPUT_URL: [MessageHandler(Filters.text, input_url)]
        },
        fallbacks=[]
    ))

    dispatcher.add_handler(CommandHandler('notas', notas))
    '''
    dispatcher.add_handler(ConversationHandler(
        entry_points=[
            CallbackQueryHandler(pattern='newnotas', callback=newnotas_callback_handler)
        ],
        states={
            INPUT_NOTAS: [MessageHandler(Filters.text, newinput_notas)]
        },
        fallbacks=[]
    ))

    dispatcher.add_handler(ConversationHandler(
        entry_points=[
            CallbackQueryHandler(pattern='seenotas', callback=seenotas_callback_handler)
        ],
        states={
            INPUT_NOTAS: [MessageHandler(Filters.text, seeinput_notas)]
        },
        fallbacks=[]
    ))
    '''

    dispatcher.add_handler(ConversationHandler(
        entry_points=[
            CallbackQueryHandler(pattern='newnotas', callback=newnotas_callback_handler),
            CallbackQueryHandler(pattern='seenotas', callback=seenotas_callback_handler),
            CallbackQueryHandler(pattern='vertodas', callback=notas_vertodas_callback_handler),
            CallbackQueryHandler(pattern='ultnota', callback=seenotas_callback_handler),
            CallbackQueryHandler(pattern='numnota', callback=seenotas_callback_handler)
        ],
        states={
            INPUT_NOTASNEW: [MessageHandler(Filters.text, newinput_notas)],
            INPUT_NOTASSEE: [MessageHandler(Filters.text, seeinput_notas)],
            #INPUT_NOTAS_VERTODAS: [MessageHandler(Filters.text, input_notas_vertodas)],
            #INPUT_NOTAS_ULTNOTA: [MessageHandler(Filters.text, input_notas_ultnota)],
            #INPUT_NOTAS_NUMNOTA: [MessageHandler(Filters.text, input_notas_numnota)]
        },
        fallbacks=[]
    ))

    
    


    
    #dispatcher.add_error_handler(error)
    
    updater.start_polling()
    updater.idle()