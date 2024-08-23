import spacy
import csv

# Download small English model: python -m spacy download en_core_web_sm
# Load.
nlp = spacy.load("en_core_web_sm")

# Retrieved from spacy's source code. Which should I use? One has actual words that BERT might already know?
pos_map_full_txt = {
    "ADJ": "[adjective]",
    "ADP": "[adposition]",
    "ADV": "[adverb]",
    "AUX": "[auxiliary]",
    "CONJ": "[conjunction]",
    "CCONJ": "[coordinating conjunction]",
    "DET": "[determiner]",
    "INTJ": "[interjection]",
    "NOUN": "[noun]",
    "NUM": "[numeral]",
    "PART": "[particle]",
    "PRON": "[pronoun]",
    "PROPN": "[proper noun]",
    "PUNCT": "[punctuation]",
    "SCONJ": "[subordinating conjunction]",
    "SYM": "[symbol]",
    "VERB": "[verb]",
    "X": "[other]",
    "EOL": "[end of line]",
    "SPACE": "[space]",
}

pos_map_abbrev = {
    "ADJ": "[ADJ]",
    "ADP": "[ADP]",
    "ADV": "[ADV]",
    "AUX": "[AUX]",
    "CONJ": "[CONJ]",
    "CCONJ": "[CCONJ]",
    "DET": "[DET]",
    "INTJ": "[INTJ]",
    "NOUN": "[NOUN]",
    "NUM": "[NUM]",
    "PART": "[PART]",
    "PRON": "[PRON]",
    "PROPN": "[PROPN]",
    "PUNCT": "[PUNCT]",
    "SCONJ": "[SCONJ]",
    "SYM": "[SYM]",
    "VERB": "[VERB]",
    "X": "[X]",
    "EOL": "[EOL]",
    "SPACE": "[SPACE]"
}


if __name__ == "__main__":

    tagged_dataset = []

    # Need to parse with correct sentence (statistical modeling does better with actual sentences).
    with open("data/train.masked.tsv", mode='r', newline='') as file:   
        reader = csv.reader(file, delimiter="\t")  # .tsv file

        for row in reader:
            actual = row[0].replace("<mask>", row[1])

            parsed_actual_txt = nlp(actual)
            parsed_masked_txt = nlp(row[0])     # for aligning. To determine where <mask> originally was.
            
            single_instance = ""

            hit_mask = False
            for i, token in enumerate(parsed_actual_txt):
                masked_token = parsed_masked_txt[i].text

                if masked_token == "<":
                    hit_mask = True
                    single_instance += "<mask> "  # should mask be tagged? No? Kinda like cheating otherwise
                    continue
                
                if hit_mask:
                    single_instance += parsed_masked_txt[i+2].text + " " + pos_map_abbrev[parsed_masked_txt[i+2].pos_] + " "
                else:
                    single_instance += token.text + " " + pos_map_abbrev[token.pos_] + " "

            single_instance = single_instance.strip()
            tagged_dataset.append([single_instance, row[1]])

    # Write to .tsv, keeping same format as paper.
    with open("data/tagged.train.masked.tsv", mode ="w", newline='') as file:
        writer = csv.writer(file, delimiter='\t')

        for row in tagged_dataset:
            writer.writerow(row)
