import gensim, os
from gensim.models.wrappers.fasttext import FastText
from gensim.models import word2vec
from kor_model.config import config

def load_pretrained_fasttext() :
    # Set FastText home to the path to the FastText executable
    ft_home = '/home/dev/fastText/fasttext'

    # Set file names for train and test data
    train_file = config.pos_path

    # Use FaceBook Corpus
    #model = FastText.load_word2vec_format('/home/dev/wiki.ko.vec')
    model = FastText.train(ft_home, train_file, min_count=1)

    print(model)

    result = model.most_similar(positive=['김승우'])
    print(result)

    return model

load_pretrained_fasttext()