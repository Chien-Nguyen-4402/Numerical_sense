# # Open the original file in read mode and a new file in write mode
# with open('./data/Part_of_Speech_Tagging/Obsolete/train.pos.tsv', 'r') as original, open('train.pos.txt', 'w') as modified:
#     for line in original:
#         # Split the line into the main part and the last word based on the last tab character
#         parts = line.rsplit('\t', 1)
#         if len(parts) == 2:
#             main_part, last_word = parts
#             # Replace '<mask>' with the last word (trim newline characters from last_word)
#             modified_line = main_part.replace('<mask>', last_word.strip()) + '\n'
#             modified.write(modified_line)
#         else:
#             # Handle lines that do not conform to expected format
#             modified.write(line)  # Optionally modify this line to handle unexpected formats


# Open the original file in read mode and a new file in write mode
# with open('./data/Part_of_Speech_Tagging/Obsolete/masked.train.pos.tsv', 'r') as original, open('modified_file.txt', 'w') as modified:
#     for line in original:
#         # Split the line into columns based on the tab delimiter
#         columns = line.strip().split('\t')
#         if len(columns) > 0:
#             # Replace '<mask>' with '<mask>[NUM]' in the first column
#             columns[0] = columns[0].replace('<mask>', '<mask> [NUM]')
        
#         # Join the columns back into a single line with space separation
#         modified_line = ' '.join(columns) + '\n'
#         modified.write(modified_line)


# Open the original text file in read mode and a new text file in write mode
with open('./data/Part_of_Speech_Tagging/masked.train.pos.txt', 'r') as original, open('modified_file.txt', 'w') as modified:
    for line in original:
        # Strip the line to remove trailing newlines and split it into columns based on spaces (if it's space-separated)
        columns = line.strip().split()
        if len(columns) > 1:
            # Take the last word (assumed to be the last element in columns)
            last_word = columns[-1]
            # Reassemble the line without the last word
            main_part = ' '.join(columns[:-1])
            # Replace '<mask>' with the last word
            modified_line = main_part.replace('<mask>', last_word)
            # Write the modified line to the new file
            modified.write(modified_line + '\n')
        else:
            # Write the line as is if there's no space to split or modification needed
            modified.write(line)

