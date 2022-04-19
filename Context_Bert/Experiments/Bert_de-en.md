# Context Aware Bert
**IWST'14 Experiments**:
- IWST'14 test train and dev data used [link](http://dl.fbaipublicfiles.com/fairseq/data/iwslt14/de-en.tgz)  1.5M sentences
- Doc-Level Data preparation with exisitng scripts [link](https://github.com/bert-nmt/ctx-bert-nmt)
- Joint BPE 10000
- Try When and Why is Document-level Context Useful in Neural Machine Translation? [link](https://aclanthology.org/D19-6503/)
- 2-4-22: Sadaf: I am noticing, the lesser the context, better the results. Our results are taking us towards a study of BERT vs context.
- 7-4-22: Sami: Yes, you were right, I have used Keyword extraction library to use only significat keywords as context, with this the size of context is reduced upto 60-70 % [Keyword Extractor] (https://github.com/LIAAD/yake). 
- 8-4-22: We should not have trained from Test Best, train from Valid Best gives improvements.
- Kindly get the results for 1-prev and 1-next along with summary as context and only content words as context. 
- 19-4-22: Text Summarization uses (NLTK) nlp constructs that does not support German, need to incorporate [Spacy](https://spacy.io/models/de) for Lemmatization and Stemming 

**Results**

| Model | Context | De-En | Paper(de-en) | En-De|Paper(en-de)|
|-------|--------|---------|---------| -|-|
| Transformer | - | 34.98 | 35.08| 28.71|28.51|
| Bert_sent_transformer | - |36.07 | 36.11| 30.10|30.45|
| Bert_ctx_transformer | prev-cur-next | 35.51 | 36.84|29.53| 30.75|
| Bert_ctx_transformer | cur-next |  35.49 | 36.57|29.80 |30.66|
| Bert_ctx_transformer | 3-prev | 34.72 | 36.51| 29.16| 30.75|
| Bert_ctx_transformer | 1-prev | 35.41 |36.50| 29.63| 30.69|
| Bert_ctx_transformer | 1-prev (keywords) | 36.03* |NA| 30.10| NA|
| Bert_ctx_transformer | 1-prev (summarization) | - |NA| 29.76 |NA|
| Bert_ctx_transformer | prev-cur-next (keywords) | 35.83 |NA| 30.31| NA|

*train from bert_sent instead of baseline_sent
Score difference|Us  | Them |
|-|----|-------|
|-|0.53  | 1.03|



**Next**
- Specilized context information ``` '[CLS] {} [SEP] {} [SEP]'.format(' '.join(prevs), line)```
- Train from pre-trained model
- Stop word removel from context 
- En-De jobs
- Joined Dictionary and Src Dst dictionary
- Text Summarization (spacy)[https://betterprogramming.pub/extractive-text-summarization-using-spacy-in-python-88ab96d1fd97]
- Text Summarization using (spacy)[https://medium.com/analytics-vidhya/text-summarization-using-spacy-ca4867c6b744]
