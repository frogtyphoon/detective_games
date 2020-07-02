# f = open('connect.txt', 'r+', encoding='utf8')
# text = [str(i) for i in f.read().split('|')]
# print(text)
#
# f.close()
# open('connect.txt', 'w').close()


# f = open('connect.txt', 'r+', encoding='utf8')
#
# n = 1
# f.write(str(n) + '|' + 'answer')
#
# f.close()

# async def test():
#     while True:
#         f = open('connect.txt', 'r+', encoding='utf8')
#         text = [str(i) for i in f.read().split('|')]
#         f.close()
#         if text[0] == 'bot':
#             f.close()
#             open('connect.txt', 'w').close()
#             f = open('connect.txt', 'r+', encoding='utf8')
#             f.write('main', str(text[1]), set='|')
#             f.close()


def edit_bot(n):
    f = open('text.txt', 'r+', encoding='utf8')
    f.write('main' + '|' + str(n))
    f.close()


def edit_main(bot_name, n, words):
    f = open('text.txt', 'r+', encoding='utf8')
    f.write(bot_name + '|' + str(n) + '|' + words)
    f.close()