from gensim.models import word2vec

# Set FastText home to the path to the FastText executable
ft_home = '/home/dev/fastText/fasttext'

# Set file names for train and test data
train_file = '/home/dev/wiki/pos.txt'

update_flag = False

model = word2vec.Word2Vec(size=300 , window=5, min_count=1, workers=4)

with open(train_file) as f :
    for line in f.readlines() :
        if (update_flag == False):
            model.build_vocab(line.split(' '), update=False)
            update_flag = True
        else:
            model.build_vocab(line.split(' '), update=True)

with open(train_file) as f:
    for line in f.readlines():
        model.train(line.split(' '))

#FastText.load_word2vec_format('/home/dev/wiki.ko.vec')
#model = FastText.train(ft_home, train_file, min_count=1)

print(model)

result = model.most_similar(positive=['김승우'])
print(result)