import json
import spacy

smodel = spacy.load("tr_core_news_trf")


def get_lemma_pos(word):
  doc = smodel(word)
  lemma = doc[0].lemma
  pos = doc[0].pos_
  return lemma, pos



with open("vocab.txt", "r") as allw, open("root_pos_table.txt", "w") as ofile:
  for word in allw:
    word = word.strip()
    lemma, pos = get_lemma_pos(word)
    if lemma != "Unk":
        ofile.write(word + " " + lemma + " "  + pos + "\n")

