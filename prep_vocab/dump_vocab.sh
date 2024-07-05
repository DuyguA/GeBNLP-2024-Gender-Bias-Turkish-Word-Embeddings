$SENTENCES_FILE="../prep_data/medical_sentences.txt"
$COUNTS_FILE="medi_counts.txt"
$VOCAB_FILE="medi_vocab.txt"

cat $SENTENCES_FILE | tr " " "\n" | sort | uniq -c | sort -nr > $COUNTS_FILE
awk '{print $2}' $COUNTS_FILE > $VOCAB_FILE
