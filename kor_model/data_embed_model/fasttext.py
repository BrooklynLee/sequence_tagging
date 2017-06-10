import gensim, os
from gensim.models.wrappers.fasttext import FastText
import fasttext
from gensim.models import word2vec
from kor_model.config import config

def load_pretrained_fasttext() :
    # Set FastText home to the path to the FastText executable
    ft_home = '/home/dev/fastText/fasttext'

    # Set file names for train and test data
    train_file = config.pos_path

    # Use FaceBook Corpus
    model = fasttext.cbow(ft_home, '/home/dev/wiki/test.txt')
    # model = FastText.load_word2vec_format('/home/dev/wiki.ko.vec')

    result = model.most_similar(positive=['김승우'])
    return model

load_pretrained_fasttext()