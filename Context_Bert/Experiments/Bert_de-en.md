# Context Aware Bert
**IWST'14 Experiments**:
- IWST'14 test train and dev data used [link](http://dl.fbaipublicfiles.com/fairseq/data/iwslt14/de-en.tgz)  1.5M sentences
- Doc-Level Data preparation with exisitng scripts [link](https://github.com/bert-nmt/ctx-bert-nmt)
- Joint BPE 10000
- Try When and Why is Document-level Context Useful in Neural Machine Translation? [link](https://aclanthology.org/D19-6503/)

**Results**

| Model | Context | Direction | BLEU | Paper|Checkpint|
|-------|--------|---------|---------| -|-|
| Transformer | - | De-En | 34.98| 35.08|-|
| Bert_ctx_transformer | cur-prev-next | De-En | 35.51|36.11| -|
| Bert_ctx_transformer | cur-next | De-En | 35.49| 36.57|-|
| Bert_ctx_transformer | prev-cur | De-En | -| -|-|
| Bert_ctx_transformer | 3-prev | De-En | 34.38| 36.51| -|
| Bert_ctx_transformer | curr-next from 3-prev | De-En | -| -|

Score difference|Us  | Them |
|-|----|-------|
|-|0.53  | 1.03|



**Next**
- Specilized context information ``` '[CLS] {} [SEP] {} [SEP]'.format(' '.join(prevs), line)```
- Train from pre-trained model
- Stop word removel from context 
- En-De jobs
