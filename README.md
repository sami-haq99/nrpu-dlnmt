# NRPU-Document Level Neural Machine Translation
- **Introduction**:
- This repository contains all the data, scripts and documentation related to document-level nmt experiments
- WMT related data is placed under folder [WMT](/WMT)
- Context Aware Bert for Contextual Information Encoding [bert_ctx](https://github.com/bert-nmt/ctx-bert-nmt)

***Issues***
- SHELL Windows/Ubuntu shell file issue ``` tr -d "\r" <binarize_baseline.sh > a.tmp , mv a.tmp binarize_baseline.sh ```
- unrecognized arguments: --min-lr 1e-09 => --stop-min-lr
- inplace error [ref](https://github.com/pytorch/xla/issues/2369), solution : ```q = q * self. scaling```
- Cannot load model parameters from checkpoint mismatch error: keep the src and tgg dict same as baseline nmt model
- CUDA and Torch issue: tool old NVIDIA drivers [ref](https://pytorch.org/get-started/previous-versions/) ```pip install torch==1.8.1+cu101 torchvision==0.9.1+cu101 torchaudio==0.8.1 -f https://download.pytorch.org/whl/torch_stable.html```
- Pytorch multi-processing issue with multi-gpu environment set ```--num_worker = 0``` in train.py
