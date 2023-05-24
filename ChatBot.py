from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Token de acceso al bot de Telegram
TOKEN = 'TU_TOKEN_DE_TELEGRAM'

# Función para manejar el comando /start
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('¡Hola! Bienvenido al chat de atención al cliente de la tienda de repuestos de electrónica. ¿En qué puedo ayudarte?')

# Función para manejar los mensajes de texto
def handle_text(update: Update, context: CallbackContext) -> None:
    message = update.message.text.lower()
    
    if 'repuesto' in message:
        update.message.reply_text('Tenemos una amplia variedad de repuestos de electrónica. ¿Para qué dispositivo necesitas el repuesto?')
    elif 'consulta' in message or 'pregunta' in message:
        update.message.reply_text('Claro, adelante. Estoy aquí para responder tus preguntas.')
    elif 'horario' in message:
        update.message.reply_text('Nuestro horario de atención es de lunes a viernes de 9:00 am a 6:00 pm.')
    else:
        update.message.reply_text('Lo siento, no comprendo tu consulta. Por favor, intenta preguntar de otra manera o especifica más detalles.')

# Crea el objeto Updater y el Dispatcher
updater = Updater(TOKEN, use_context=True)
dispatcher = updater.dispatcher

# Agrega los manejadores de comandos y mensajes de texto
dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_text))

# Inicia el bot
updater.start_polling()
