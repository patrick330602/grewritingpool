import random
import json

import grewritingpool.fetch


def random_article(writing_type):
    json_list = grewritingpool.fetch.fetch_type(writing_type)
    datalist = json.loads(json_list)
    secure_random = random.SystemRandom()
    writingitem = secure_random.choice(datalist)
    return writingitem

def print_random_article(writing_type):
    writingitem = ""
    if writing_type == 'default':
        writing_type = 'all'
        print("Writing type not set, default to 'all'...\n")
    if writing_type == 'all':
        secure_random = random.SystemRandom()
        writing_type = secure_random.choice(['argument','issue'])
        writingitem = random_article(writing_type)
    elif writing_type in ('argument','argument'):
        writingitem = random_article(writing_type)
    print('From '+writing_type+' pool\n')
    print('Question:')
    print(writingitem['first'])
    if 'second' in writingitem.keys():
        print('\n'+writingitem['second'])
    print('\nInstruction:')
    print(writingitem['instru'])