# 한글 NER 테스트 (BI-LSTM CRF , Attention Seq2Seq)
- glove vector lib download needed. 
- (locate txt file under data/glove.6B/)
- Data file [link](http://nlp.stanford.edu/data/glove.6B.zip) 
```
wget http://nlp.stanford.edu/data/glove.6B.zip
```
- step1 : make it work on python3.5 and tf1.1 (done) 
- step2 : test korean with mecab tockenizer (done)
- step3 : develop whole process on hoyai project with rest webservice 

# Blog explaining Theory 
Check original projects [blog post](https://guillaumegenthial.github.io/sequence-tagging-with-tensorflow.html)

# Functions implemented for Korean NER 
 - Simple WebCrawler : gather data from korean wiki pedia for w2v train 
 - w2v, fasttext embedding model : provide custom train for model 
 - korean char divide func : divide Korean char into smaller pieces for train 
 - BI-LSTM CRF for NER : implement it with tensorflow 
 - Attention seq2seq for NER : working on it (~ing) 

# Korean NER Test Result 
Train Data : [link](https://github.com/shinu89/KoNER/blob/master/data/gazette).
Use only word list for train model, I think train sentences with Tag will imporove the 
performace, for now accuracy with train data is 66%, but if w2v lag of dict problem solved
we can expect performace improvement 

 - Word Level Test
```
['한화증권']['OG']
['김승우']['PS'] 
['김수상']['PS']
['6시30분']['DT']
```
 - Sentence Level Test 
```
[['6시30분']['한화건설']['김승우']['약속']]
[['DT']['OG']['PS']['OO']]
```


