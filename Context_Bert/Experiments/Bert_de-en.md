# Context Aware Bert
**IWST'14 Experiments**:
- IWST'14 test train and dev data used [link](http://dl.fbaipublicfiles.com/fairseq/data/iwslt14/de-en.tgz)  1.5M sentences
- Doc-Level Data preparation with exisitng scripts [link](https://github.com/bert-nmt/ctx-bert-nmt)
- Joint BPE 10000
- Try When and Why is Document-level Context Useful in Neural Machine Translation? [link](https://aclanthology.org/D19-6503/)

**Results**

| Model | Context | De-En | Paper(de-en) | En-De|Paper(en-de)|
|-------|--------|---------|---------| -|-|
| Transformer | - | 34.98 | 35.08| 28.71|28.51|
| Bert_sent_transformer | - |36.07 | 36.11| 30.10|30.45|
| Bert_ctx_transformer | cur-prev-next | 35.51 | 36.11|-| -|
| Bert_ctx_transformer | cur-next |  35.49 | 36.57|29.80 |30.66|
| Bert_ctx_transformer | prev-cur | - | -| -|-|
| Bert_ctx_transformer | 3-prev | 34.38 | 36.51| -| -|
| Bert_ctx_transformer | 1-prev | - |-| 29.63| 30.69|

Score difference|Us  | Them |
|-|----|-------|
|-|0.53  | 1.03|



**Next**
- Specilized context information ``` '[CLS] {} [SEP] {} [SEP]'.format(' '.join(prevs), line)```
- Train from pre-trained model
- Stop word removel from context 
- En-De jobs
