import os
import socket
from collections import Counter

# a. List name of all the text files at location: /home/data
file_names = os.listdir('/home/app')

# b. Read the two text files and count total number of words in each text files
total_word_count = 0
if_file_path = '/home/app/IF.txt'
limerick_file_path = '/home/app/Limerick-1.txt'

with open(if_file_path, 'r') as if_file, open(limerick_file_path, 'r') as limerick_file:
    if_words = if_file.read().split()
    limerick_words = limerick_file.read().split()

    # c. Add all the number of words to find the grand total
    total_word_count = len(if_words) + len(limerick_words)

    # d. List the top 3 words with maximum number of counts in IF.txt
    top_words_count = Counter(if_words).most_common(3)

# e. Find the IP address of the machine
host_ip = socket.gethostbyname(socket.gethostname())

# f. Write all the output to a text file at location: /home/output/result.txt
output_file_path = '/home/output/result.txt'
with open(output_file_path, 'w') as result_file:
    result_file.write(f"Files in /home/app: {file_names}\n\n")
    result_file.write(f"Total words in IF.txt: {len(if_words)}\n")
    result_file.write(f"Total words in Limerick-1.txt: {len(limerick_words)}\n")
    result_file.write(f"Grand Total words: {total_word_count}\n\n")
    result_file.write("Top 3 words in IF.txt:\n")
    for word, count in top_words_count:
        result_file.write(f"{word}: {count} occurrences\n")
    result_file.write(f"\nMachine IP address: {host_ip}\n")

# g. Print the information on the console
with open(output_file_path, 'r') as result_file:
    result_content = result_file.read()
    print(result_content)


# h. Write the results to results.txt after creating the file
with open('/home/app/results.txt', 'w') as results_txt:
    results_txt.write(result_content)