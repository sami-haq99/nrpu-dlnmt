# WMT Data
- **WMT test and dev data**:
  - WMT test and dev dataset for back translation, en part of en-de set will be translated.
  - WMT data may include .sgm or xml files that may need to be converted into plaintext format.
  - Following command may be used to convert .sgm files into plaintext [ref](https://www.kaggle.com/nltkdata/wmt15-eval):
  - Example:
     ```sed -e 's/<[^>]*>//g; /^\s*$/d' newstest-2015.enru.src.en.sgm | head -n100 > newstest-2015-100sents.en-ru.src.en```
