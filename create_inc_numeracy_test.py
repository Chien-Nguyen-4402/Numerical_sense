# Adversarial Probe: increasing numeracy in given text.

# Original Test: I have <mask> dogs.
# Ours: I have 4 cars. I have <mask> dogs.

def concatenate_files(file1, file2, output_file):
    with open(file1, 'r') as f1, open(file2, 'r') as f2, open(output_file, 'w') as out_file:
        for line1, line2 in zip(f1, f2):
            concatenated_line = line1.strip() + " " + line2.strip() + '\n'
            out_file.write(concatenated_line)

file1_path = "./data/numersense.gkb_best_filtered.txt"
file2_path = "./data/numersense.test.core.masked.txt"
output_file_path = "masked.inc.numeracy.txt"

concatenate_files(file1_path, file2_path, output_file_path)