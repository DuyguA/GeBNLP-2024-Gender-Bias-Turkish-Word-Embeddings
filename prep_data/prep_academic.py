from datasets import load_dataset
import datasets, json
from torch.utils.data import DataLoader
from sentence_splitter import split_into_sentences
import string






def prep_dump(loader):
  lines_written = 0
  global chunk_counter
  ofile_name128 = "academic_sentences.txt"
  with open(ofile_name128, "a+") as ofile128:
    for batch in loader:
      docs = batch["text"]
      for doc in docs:
          sentences = split_into_sentences(doc)
          for sentence in sentences:
            sentence = sentence.translate(str.maketrans('', '', string.punctuation))
            ofile128.write(sentence+ "\n")
          


acrawl1 = load_dataset("turkish-nlp-suite/Bilkent-writings", split="train")
aload1 = DataLoader(acrawl1, batch_size=1000)

acrawl2 = load_dataset("turkish-nlp-suite/Akademik-Ozetler", split="train")
aload2 = DataLoader(acrawl2, batch_size=1000)

acrawl3 = load_dataset("turkish-nlp-suite/Makaleler", split="train")
aload3 = DataLoader(acrawl3, batch_size=1000)

academic_crawls = [aload1, aload2, aload3]




for loader in academic_crawls:
    prep_dump(loader)

