from nltk import word_tokenize, pos_tag


def create_tags(sentence):
    tokens = word_tokenize(sentence)
    poss_tagged_list = pos_tag(tokens)

    print(sentence)
    print(tokens)
    print(poss_tagged_list)
    return poss_tagged_list