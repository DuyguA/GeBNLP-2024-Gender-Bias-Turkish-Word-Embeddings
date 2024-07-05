import floret

sentences_file = "../prep_vocab/academic_sentences.txt"


# train vectors
model = floret.train_unsupervised(
    sentences_file,
    model="cbow",
    mode="floret",
    hashCount=2,
    bucket=200000,
    minn=3,
    maxn=6,
    dim=100,
)


# export floret vector table
model.save_floret_vectors("academic_vectors.floret")

