# Context Aware Bert
- **IWST'14**:
- IWST'14 test train and dev data used [link](http://dl.fbaipublicfiles.com/fairseq/data/iwslt14/de-en.tgz)
- Doc-Level Data preparation with exisitng scripts [link](https://github.com/bert-nmt/ctx-bert-nmt)
- Joint BPE 10000
- 
-**Results**
| Model | Context | Direction | BLEU | Checkpint|
|-------|--------|---------|---------| -|
| Transformer | - | En-De | 34.98| -|
| Bert_ctx | cur-prev-next | En-De | 35.51| -|
| Transformer | cur-next | En-De | 35.49| -|
| Transformer | 3-prev | En-De | 34.38| -|
| Transformer | curr-next from 3-prev | En-De | -| -|



**Next**
- Specilized context information ``` '[CLS] {} [SEP] {} [SEP]'.format(' '.join(prevs), line)```
- Train from pre-trained model
- Separate BPE learn
