# Import the enchant library for spell-checking
import enchant


# Define a function to split merged words into individual words
def split_merged_words(word_to_split):
    # Initialize an empty list to store the resulting individual words
    splitted_words = []

    # Create an instance of the English dictionary
    dictionary = enchant.Dict("en_US")

    # Store the merged word in a variable
    word = word_to_split

    # Calculate the length of the merged word
    length_of_word = len(word)

    # Initialize a variable to keep track of the current index
    i = 0

    # Iterate over the merged word
    while i < length_of_word:
        # Generate substrings of decreasing length, starting from the length of the word
        for j in range(length_of_word, i, -1):
            # Extract a substring to check against the dictionary
            word_to_check = word[i:j]

            # Check if the substring exists in the dictionary
            if dictionary.check(word_to_check):
                # If it is a valid word, append it to the list of splitted words
                splitted_words.append(word_to_check)

                # Update the current index to the end of the valid word
                i = j

                # Break out of the inner for loop
                break

    # Return the list of splitted words
    return splitted_words


# Get user input for the merged words
merged_words = input("Enter the merged words: ")

# Call the function to split the merged words into individual words
words = split_merged_words(merged_words)

# Print the resulting individual words
print("The splitted words:", words)
