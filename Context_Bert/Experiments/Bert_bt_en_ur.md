
# Context Aware Bert En Ur
**IWST'14 Backtranslated Experiments**:
- IWST'14 test train and dev data back-translated
- UTF-8 Conversion issues 
- Source side contextual encoding using Bert *bert-base-uncased* and *bert-base-multilingual-uncased* for english and urdu respectively
- Tokenization issues: Indic tokenizer for urdu
- Bert Sent-level integration to be done

**Results**

|Name| Model | Context | Own(de-en) | Own(ur-en) | Own(en-de)| Own(en-ur)|
|-|-------|--------|---------|---------| -|-|
|M1| Transformer | - | 34.98 | 50.03| 28.71|57.95|
|M2| Bert_sent_transformer | - |36.07 | -| 30.10|-|
|M3| Bert_ctx_transformer | prev-cur-next | 35.51 | -|29.53| -|
|M4| Bert_ctx_transformer | cur-next |  35.49 | 47.35|29.80 |54.23|
|M5| Bert_ctx_transformer | 3-prev | 34.72 | -| 29.16| -|
|M6| Bert_ctx_transformer | 1-prev | 35.41 |-| 29.63| -|

