def edit_bot(n):
    f = open('text.txt', 'r+', encoding='utf8')
    f.write('main' + '|' + str(n))
    f.close()


def edit_main(bot_name, n, words):
    f = open('text.txt', 'r+', encoding='utf8')
    f.write(bot_name + '|' + str(n) + '|' + words)
    f.close()