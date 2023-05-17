# Merged-Word-Splitter
Merged Word Splitter: Splitting Words using Dictionary Lookup.

This code defines a function called split_merged_words that takes a single parameter word_to_split. It aims to split a merged word into individual words based on a dictionary lookup.

The function begins by initializing an empty list called splitted_words to store the resulting individual words. It then creates an instance of the enchant library's English dictionary using enchant.Dict("en_US").

Next, it stores the merged word provided as the input in a variable called word. The code calculates the length of the merged word and stores it in the variable length_of_word.

To split the merged word, the code uses two nested loops. The outer while loop iterates over the merged word until the current index i reaches the end of the word.

Inside the while loop, the inner for loop generates substrings of decreasing length, starting from the length of the word and going down to the current index i. These substrings are extracted from the merged word and stored in the variable word_to_check.

The code then checks if the word_to_check substring exists in the dictionary using the dictionary.check(word_to_check) method. If the substring is found in the dictionary, it is considered a valid word and is appended to the splitted_words list. The current index i is updated to the end of the valid word, and the inner loop is broken to proceed to the next iteration of the while loop.

Once the while loop completes, the function returns the splitted_words list.

Outside the function, the code prompts the user to enter the merged words and stores the input in the merged_words variable. It then calls the split_merged_words function, passing the merged_words as an argument, and stores the result in the words variable.

Finally, it prints the resulting individual words by displaying the contents of the words list.
