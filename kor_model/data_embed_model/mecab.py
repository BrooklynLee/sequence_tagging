from konlpy.tag import Mecab

mecab = Mecab('/usr/local/lib/mecab/dic/mecab-ko-dic')
with open('/home/dev/wiki/test.txt', 'r') as in_file :
    with open('/home/dev/wiki/pos.txt', 'w+') as out_file:
        for line in in_file.readlines() :
            for word, tag in mecab.pos(line):
                out_file.write('{0} '.format(word))