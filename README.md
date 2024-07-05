## Gender Bias in Turkish Word Embeddings: A Comprehensive Study of Syntax, Semantics and Morphology Across Domains

This repository contains code for the GEBNLP 2024 paper, Gender Bias in Turkish Word Embeddings: A Comprehensive Study of Syntax, Semantics and Morphology Across Domains.

## Overview

The code consists of 3 phases:

* Prepare training data, dump vocabulary files and train Floret vectors
* [Optional] Train sPacy models to measure Floret vector success
* Sort the vocab words by POS tags and calculate the gender score w_word * w_woman - w_word * w_men

All phases are explained below.

### Prepare the training data

In this phase, we download data from HUggingface repos and dump the data as sentence per line. We implemented a simple sentence splitter to avoid overhead. For each data genre web, academical and medical crawl there's an associated script `prep_{corpus}.py` , pick the one you want and run. This will dump the data into a text file called `sentences_{corpus}.txt`. Be careful with mC4, data size is about 160GB. Other corpora are sized much less, academical crawl is about 4.3 GB and medical crawl is much less. 

### Dump the vocab


### Train Floret vectors


### [Optional] Train spaCy models



### Pick up the gender results by POS category
