import os
import time
import hashlib as h

print('Welcome to your Folder Sync Script!')

source_input = input('Please insert the path of the Source folder: ')
while not os.path.isdir(source_input):
    source_input = input('Please insert a valid folder path: ')

replica_input = input('Please insert the path of the Replica folder: ')
while not os.path.isdir(replica_input):
    replica_input = input('Please insert a valid folder path: ')

sync_frequency_input = input('How frequently should the folders be synchronized?\nExample: "2m" for 2 minutes, "40s" for 40 seconds: ')
while sync_frequency_input[-1] not in ['m', 's']:
    sync_frequency_input = input('Please insert a valid input: ')

if sync_frequency_input[-1] == 'm':
    sleep_amount = int(sync_frequency_input[:-1]) * 60
else:
    sleep_amount = int(sync_frequency_input[:-1])

log_filepath_input = input('Please insert the path you wish for the log file to be created at: ')

LOG = 'folder_sync_log.txt'

log_filepath = os.path.join(log_filepath_input, LOG)
if not os.path.exists(log_filepath_input):
    os.makedirs(log_filepath_input)

# functions

def log(message):
    with open(log_filepath, 'a') as f:
        now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        f.write('[' + now + ']' + ' ' + message + '\n')

def compareFiles(file_name_1, file_name_2):
    with open(file_name_1, 'rb') as file_object_1:
        with open(file_name_2, 'rb') as file_object_2:
            if h.md5(file_object_1.read()).hexdigest() == h.md5(file_object_2.read()).hexdigest():
                return True
            else:
                return False

def printLogMessage():
    with open(log_filepath, 'r') as f:
        last_line = f.readlines()[-1]  
    print(last_line)

# main loop

while True:
    log('Synchronizing folders...')
    printLogMessage()

    source_content = os.listdir(source_input)
    replica_content = os.listdir(replica_input)
    for file in replica_content:
        if file in source_content:
            if compareFiles(source_input + '\\' + file, replica_input + '\\' + file):
                log(f'{file} is up to date.')
                printLogMessage()
            else:
                os.remove(replica_input + '\\' + file)
                os.system('copy ' + source_input + '\\' + file + ' ' + replica_input)
                log(f'{file} updated.')
                printLogMessage()
        else:
            os.remove(replica_input + '\\' + file)
            log(f'{file} removed from {replica_input}.')
            printLogMessage()


    for file in source_content:
        if file not in replica_content:
            os.system('copy ' + source_input + '\\' + file + ' ' + replica_input)
            log(f'{file} copied to {replica_input}.')
            printLogMessage()

    print('All done.')
    print(f'Sleeping for {sleep_amount} seconds...')
    
    time.sleep(float(sleep_amount))
