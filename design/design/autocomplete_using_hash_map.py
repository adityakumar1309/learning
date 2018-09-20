words = ["she", "hello", "hell", "sheep", "sleep", "hen", "parrot", "man", "manner", "manual"]

def create_words_hash(words):
    word_to_id_hash = {}
    id_to_word_hash = {}

    prefix_to_word_list = {}

    id_count = 0
    for word in words:
        word_to_id_hash[word] = id_count
        id_to_word_hash[id_count] = word
        id_count = id_count + 1

    for word in words:
        word_id = word_to_id_hash[word]
        char_comb_list = get_all_possible_comb(word)
        for sub_word in char_comb_list:
            if sub_word in prefix_to_word_list:
                prefix_to_word_list[sub_word].append(word_id)
            else:
                prefix_to_word_list[sub_word] = [word_id]

    return prefix_to_word_list, id_to_word_hash

def get_all_possible_comb(word):
    char_comb_list = []
    for i in range(len(word)):
        sub_word = word[0:i]
        char_comb_list.append(sub_word)

    return char_comb_list

prefix_to_word_list, id_to_word_hash = create_words_hash(words)
for input in ['h', 'he', 'm', 's', 'sl', 'sh']:
    print "input: %s"%input
    suggestions_id = prefix_to_word_list[input]
    out = []
    for id in suggestions_id:
        out.append(id_to_word_hash[id])
    print "Autocomplete: %s"%(out)
