from datasets import load_dataset
import datasets, json
from torch.utils.data import DataLoader
from sentence_splitter import split_into_sentences
import string






def prep_dump(loader):
  lines_written = 0
  global chunk_counter
  ofile_name128 = "mc4_sentences.txt"
  with open(ofile_name128, "a+") as ofile128:
    for batch in loader:
      docs = batch["text"]
      for doc in docs:
          sentences = split_into_sentences(doc)
          for sentence in sentences:
            sentence = sentence.translate(str.maketrans('', '', string.punctuation))
            ofile128.write(sentence+ "\n")
          


mcrawl1 = load_dataset("turkish-nlp-suite/temiz-mC4", split="train")
mload1 = DataLoader(mcrawl1, batch_size=1000)


mc_crawls = [mload1]




for loader in mc_crawls:
    prep_dump(loader)

