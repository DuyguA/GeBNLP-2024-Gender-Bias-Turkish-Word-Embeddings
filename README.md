## Gender Bias in Turkish Word Embeddings: A Comprehensive Study of Syntax, Semantics and Morphology Across Domains

This repository contains code for the GEBNLP 2024 paper, Gender Bias in Turkish Word Embeddings: A Comprehensive Study of Syntax, Semantics and Morphology Across Domains.

## Overview

The code consists of 3 phases:

* Prepare training data, dump vocabulary files and train Floret vectors
* [Optional] Train sPacy models to measure Floret vector success
* Sort the vocab words by POS tags and calculate the gender score w_word * w_man/erkek - w_word * w_woman/kadın

All phases are explained below.

### Prepare the training data

In this phase, we download data from HUggingface repos and dump the data as sentence per line. We implemented a simple sentence splitter to avoid overhead. Navigate to `prep_data` diretory and for each data genre web, academical and medical crawl there's an associated script `prep_{corpus}.py` , pick the one you want and run. This will dump the data into a text file called `sentences_{corpus}.txt`. Be careful with mC4, data size is about 160GB. Other corpora are sized much less, academical crawl is about 4.3 GB and medical crawl is much less. 

### Dump the vocab
For this phase, navigate to `prep_vocab` directory and use the bash script in this directory to create two files `{corpus}_counts.txt` and `{corpus}_vocab.txt`. One basically feeds the sentences file in the first step to this bash script to count the words in the corpus.


### Train the Floret vectors

For this phase, you need a the library `floret` and might wanna pip install it before using. After that run the script, provide the sentences file you created in the first step to the script. This will dump 	a `.bin` file which is the vectors.


### [Optional] Train spaCy models

This is a step to replicate measuring the success of the Floret vectors in the paper. Plug-in the freshly trained Floret vectors `tr_core_news_md` recipe in [spaCy Turkish training repo](https://github.com/turkish-nlp-suite/turkish-spacy-models).



### Pick up the gender results by POS category
For this section, in order to calculate word POS and lemma, one needs a spaCy Turkish model. You can install the transformer based model with:

```
pip install https://huggingface.co/turkish-nlp-suite/tr_core_news_trf/resolve/main/tr_core_news_trf-any-py3-none-any.whl
```

or you can plug-in the model trained in the previous step.

Navigate to `make_results` directory and fire up the `get_pos_root.py` with the vocab file of your choice. This script will write a file with each line includes a triplet `(word, lemma, pos)`. This step will help us to sort the words with POS tag and learn lemma gender.

Now we can calculate gender. For this part, again one needs `floret` library to load the Floret vectors we generated in the third step and then get the word vector per each vocabulary word.
We feed the output of previous step into `get_word_gender.py` script to get the final results, final result is a file containing tuples of the form `(pos, word, gender_score, gender, lemma, lemma_gender_score, lemma_gender, gender_change_flag)`. 



### Results and vocab files 

We put our results under `results` directory for reference. For each corpus, there is a dedicated directory containing scores and POS tags of the vocab words and list of vocab words. There are one text file per gender and each file contains a tuple of seven entries `(POS word  score gender lemma lemma_score lemma_gender diff_or_same)` like this:

```
Noun başkanlıklarını 5.2295945e-06 male başkan 0.09763732 male same
```


These are the results we presented at the paper.
