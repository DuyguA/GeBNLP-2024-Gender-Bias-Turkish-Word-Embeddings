import json
import numpy as np

model = fasttext.load_model("academic_vectors.bin")
from sklearn.metrics.pairwise import cosine_similarity



kadin_v = model.get_word_vector("kadın")
erkek_v = model.get_word_vector("erkek")

diff_v = erkek_v - kadin_v


with open("root_pos_table.txt", "r") as infile, open("gender_word_lemma_pos.txt", "w") as ofile:
    for line in infile:
      word, root, pos = line.strip().split()
      word_v = model.get_word_vector(word)
      score = cosine_similarity(word_v, diff_v)

      root_v = model.get_word_vector(root)
      root_score = cosine_similarity(root_v, diff_v)

      gender = "male" if score > 0 else "female"
      root_gender = "male" if root_score > 0 else "female"
      flag = "same" if gender == root_gender else "diff"

      ofile.write(pos + " " + word + " " + str(score) + " " + gender + " " + root + " " + str(root_score) + " " + root_gender + " " + flag+"\n")

