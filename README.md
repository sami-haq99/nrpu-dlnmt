# NRPU-Document Level Neural Machine Translation
- **Introduction**:
- This repository contains all the data, scripts and documentation related to document-level nmt experiments
- WMT related data is placed under folder [WMT](/WMT)
- Context Aware Bert for Contextual Information Encoding [bert_ctx](https://github.com/bert-nmt/ctx-bert-nmt)
- Transformers [Explained](http://jalammar.github.io/illustrated-transformer/)
- Tensor2Tensor network for [learning](http://jalammar.github.io/illustrated-transformer/)

***Issues***
- SHELL Windows/Ubuntu shell file issue ``` tr -d "\r" <binarize_baseline.sh > a.tmp , mv a.tmp binarize_baseline.sh ```
- unrecognized arguments: --min-lr 1e-09 => --stop-min-lr
- inplace error [ref](https://github.com/pytorch/xla/issues/2369), solution : ```q = q * self. scaling```
- Cannot load model parameters from checkpoint mismatch error: keep the src and tgg dict same as baseline nmt model
- CUDA and Torch issue: tool old NVIDIA drivers [ref](https://pytorch.org/get-started/previous-versions/) ```pip install torch==1.8.1+cu101 torchvision==0.9.1+cu101 torchaudio==0.8.1 -f https://download.pytorch.org/whl/torch_stable.html```
- Pytorch multi-processing issue with multi-gpu environment set ```--num_worker = 0``` in train.py
- RuntimeError: Subtraction, the `-` operator, with a bool tensor is not supported [ref](https://github.com/OpenNMT/OpenNMT-py/issues/1524) ```fairseq/models/transformer.py", line 359, in get_bert_embeddings
    attention_mask=1. - bert_encoder_padding_mask)``` 
- Can't import libble: copy libbleu.cpython-36m-x86_64-linux-gnu.so into ctx-bert-nmt folder scoring
- Fairseq score.py error: [ref](https://github.com/pytorch/fairseq/issues/2460)
- UTF conversions https://www.tecmint.com/convert-files-to-utf-8-encoding-in-linux/
