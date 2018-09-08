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
    print('From '+writing_type+' pool\n')
    writingitem = random_article(writing_type)
    print('Question:')
    print(writingitem['first'])
    if 'second' in writingitem.keys():
        print('\n'+writingitem['second'])
    print('\nInstruction:')
    print(writingitem['instru'])