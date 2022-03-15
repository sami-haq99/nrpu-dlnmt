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
| Bert_ctx | cur-prev-next | En-De | 35.51|36.11| -|
| Transformer | cur-next | En-De | 35.49| 36.57|-|
| Transformer | 3-prev | En-De | 34.38| 36.51| -|
| Transformer | curr-next from 3-prev | En-De | -| -|

|Us  | Them |
|----|-------|
|0.53  | 1.03|



**Next**
- Specilized context information ``` '[CLS] {} [SEP] {} [SEP]'.format(' '.join(prevs), line)```
- Train from pre-trained model
- Separate BPE learn
