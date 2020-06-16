'''
def bot_witch(*kwargs):
    elems = kwargs
    print(elems[0][0][0], elems[0][0][1])


bot_witch(
    [['text on btn', 'answer'], ['text on btn 1', 'answer 1'], ['text on btn', 'answer'], ['text on btn', 'answer'],
     ['text on btn', 'answer']])


def main():
    if True:
        bot_witch([['паша лох', 'да, конечно!'],
                   ['нет ты лох', 'а в бубен?'],
                   ['', ''],
                   ['', ''],
                   ['', ''],
                   ['', ''],
                   ['', '']
                   ])
    else:
        bot_witch()
'''