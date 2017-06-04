# pip install hanja
from hanja import hangul
import numpy as np
import re
from eng_model.config import config

# result = get_onehot_vector("가- -2")
# print(result)
# result = get_onehot_word(result)
# print(result)

UNK = "$UNK$"
NUM = "$NUM$"
NONE = "O"

class CoNLLDataset(object):
    """
    Class that iterates over CoNLL Dataset
    """
    def __init__(self, filename, processing_word=None, processing_tag=None,
                 max_iter=None):
        """
        Args:
            filename: path to the file
            processing_words: (optional) function that takes a word as input
            processing_tags: (optional) function that takes a tag as input
            max_iter: (optional) max number of sentences to yield
        """
        self.filename = filename
        self.processing_word = processing_word
        self.processing_tag = processing_tag
        self.max_iter = max_iter
        self.length = None


    def __iter__(self):
        try :
            niter = 0
            with open(self.filename) as f:
                words, tags = [], []
                for line in f:
                    words += [line[0:len(line)-1]]
                    tags += [line[len(line)-1:len(line)]]
        except Exception as e :
            raise Exception (e)

    def __len__(self):
        """
        Iterates once over the corpus to set and store length
        """
        if self.length is None:
            self.length = 0
            for _ in self:
                self.length += 1

        return self.length


def get_onehot_vector(sent) :
    """
    convert sentecne to vector
    :return: list
    """
    return_vector = []
    embeddings = np.zeros([30])
    idx = ['0','1','2','3','4','5','6','7','8','9','-', ' ']
    num_reg = re.compile("[0-9- ]")

    if(type(sent) != type('str')) :
        raise Exception ("input must be str")

    for char in sent :
        vector_a = np.copy(embeddings)
        vector_b = np.copy(embeddings)
        vector_c = np.copy(embeddings)
        vector_d = np.copy(embeddings)

        if (num_reg.match(char) == None):
            anl = hangul.separate(char)
            vector_a[anl[0] if anl[0] > 0 else 0 ] = 1
            vector_b[anl[1] if anl[1] > 0 else 0 ] = 1
            vector_c[anl[2] if anl[2] > 0 else 0 ] = 1
        elif (num_reg.match(char)) :
            vector_d[idx.index(char)] = 1
        return_vector.append(np.append(vector_a ,[vector_b ,vector_c, vector_d]))
    return return_vector

def get_onehot_word(vec_list) :
    """
    convert sentecne to vector
    :return: list
    """
    idx = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '-', ' ']
    return_vector = []
    if(len(vec_list) == 0 or len(vec_list[0]) != 120) :
        raise Exception ("input size error")

    for vec in vec_list :
        anl = np.array(vec).reshape(4,30)

        if (np.argmax(anl[3]) > 0):
            return_vector.append(idx[np.argmax(anl) - 90])
        else :
            return_vector.append(hangul.build(np.argmax(anl[0]),
                                              np.argmax(anl[1]),
                                              np.argmax(anl[2])))
    return return_vector