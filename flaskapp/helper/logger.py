import logging

def info(info):
    print("\n\n")
    print("Info\n",info,flush=True) #This need to be logged 
    logging.info(info)

def error(info):
    print("\n\n")
    print("Error\n",info,flush=True) #This need to be logged
    logging.error(info) 