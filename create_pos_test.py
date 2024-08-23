import spacy

# Testing our probe. Will POS tagging and using our FT on POS help with predictions?

# Load the English tokenizer, tagger, parser, NER and word vectors
nlp = spacy.load("en_core_web_sm")

def tag_sentences_from_file(file_path, output_file):

    # Open the file
    all_texts = ""

    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            # Process the line (each line is assumed to be a sentence)

            # Replace <mask> with an arbitrary number "two" so spacy tagging done correctly.
            processed_line = line.strip().replace("<mask>", "two")

            properly_pos_line = nlp(processed_line)
            pos_line = nlp(line)

            correct_test_line = ""
            # reached_mask = False

            for i, tok in enumerate(properly_pos_line):
                if pos_line[i].text != "<":
                    correct_test_line += tok.text + " " + "[" + tok.pos_ + "]" + " "
                elif pos_line[i].text == "<":   # reached beginning of mask
                    # reached_mask = True
                    correct_test_line += "<mask> [NUM] "
                # elif reached_mask == True:   # already reached mask, need t
                #     correct_test_line += 

            all_texts += correct_test_line.strip() + "\n"

    with open(output_file, 'w', encoding = 'utf-8') as file:
        file.write(all_texts)


tag_sentences_from_file("./data/numersense.test.core.masked.txt", "test.txt")


# test = "I have two friends"

# test1 = nlp(test)

# for i, tok in enumerate(test1):
#     print(i, tok.text, "[" + tok.pos_ + "]")