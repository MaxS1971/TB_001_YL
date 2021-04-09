import wikipedia

wikipedia.set_lang('ru')

def search_wiki(word):
    print(word)
    w = wikipedia.search(word)
    if w:
        #w1 = wikipedia.page(w[0]).content
        w1 = wikipedia.summary(word)
        return w1
    return None


