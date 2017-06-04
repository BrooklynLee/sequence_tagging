from kor_model.data_crawler import crawler
from kor_model.data_embed_model import build_data
from kor_model.config import config

# (1) get some korean texts for embedding models by using WebCrawler
crawler.spider(3, 'https://ko.wikipedia.org/wiki/', reg_exp='[가-히\s]{1,}')

# (2) build data (Mecab, Embedding, Char Embedding)
build_data.build_data(config)

# (3) train NER Model (1.bilstm-crf, 2.attention)


# (4) eval


# (5) predict