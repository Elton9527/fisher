# 判断 q 是关键字还是isbn
def is_isbn_or_key(word):
    # isbn13个 0 到 9 的数字组成
    # isbn10 10个0到9的数字组成，含有一些'-'
    isbn_or_key = 'key'
    if len(word) == 13 and word.isdigit():
        isbn_or_key = 'isbn'
    short_word = word.replace('-', '')
    if '-' in word and len(short_word) == 10 and short_word.isgit():
        isbn_or_key = 'isbn'
    pass