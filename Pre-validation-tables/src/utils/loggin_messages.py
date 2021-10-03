import logging

default = 'Error message not founded'

def error_messages(message_code):
    messages = {
        1: 'Source not founded'
    }

    message = messages.get(message_code)
    if message:
        logging.error(message)
    else:
        raise logging.error(default)

def info_messages(message_code=0, auto=True, message=None):
    messages = {
        0: 'Info message empty'
    }
    if auto == False and message != None:
        logging.info(message)
    else:
        message = messages.get(message_code)
        if message:
            logging.error(message)
        else:
            raise logging.error(default)

