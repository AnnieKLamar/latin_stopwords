import pandas as pd


'''
This is the list of stopwords computed by mean frequency (how often the words appear in Latin literature). 
These are the words with the *highest* mean frequency. 
'''
cltk_mean = ["et", "in", "est", "non", "ad", "ut", "cum", "quod", "qui", "sed", "si", "de", "quae", "quam", "per", "ex",
             "nec", "sunt", "esse", "se", "hoc", "enim", "ab", "aut", "autem", "etiam", "quid", "te", "atque", "uel",
             "eius", "me", "quo", "sit", "iam", "quia", "ne", "haec", "mihi", "tamen", "ac", "tibi", "nam", "sic",
             "ita", "id", "pro", "eo", "nunc", "uero", "neque", "inter", "quem", "erat", "ille", "ergo", "ipse", "eum",
             "quibus", "quoque", "sibi", "ego", "quidem", "nisi", "qua", "omnia", "hic", "post", "fuit", "tu", "nihil",
             "ea", "illa", "his", "omnes", "nos", "esset", "modo", "dum", "sine", "quis", "ubi", "sicut", "ante", "sub",
             "tam", "secundum", "deus", "potest", "dei", "nobis", "quos", "igitur", "ei", "omnibus", "res", "cui",
             "sua", "apud", "eorum"]

'''
This is the list of stopwords computed from variance probability. 
Mathematically, variance is the average of the squared deviation from the mean. Practically, variance is a measure of 
how "spread out" or "distributed" a word is throughout Latin literature. For example, a word that appears 100 times in
100 texts has greater variance than a word that appears 200 times in a single text.
These are the words with the *highest* variance.
'''
cltk_variance = ["et", "in", "est", "non", "quod", "ad", "ut", "cum", "qui", "de", "si", "sed", "quae", "per", "ex",
                 "quam", "esse", "nec", "te", "sunt", "autem", "me", "enim", "se", "dig", "hoc", "aut", "ab", "bibit",
                 "quid", "uel", "atque", "mihi", "eius", "quaestio", "pro", "etiam", "tibi", "quia", "sit", "iam",
                 "secundum", "quo", "ac", "ne", "ergo", "od", "nihil", "tu", "haec", "sic", "id", "nam", "ego", "neque",
                 "tamen", "eum", "deus", "nunc", "dei", "ita", "eo", "uero", "sicut", "uos", "hic", "erat", "nouus",
                 "fuit", "nos", "ille", "inter", "dum", "quem", "quoque", "quidem", "esset", "bellum", "ipse", "sibi",
                 "nummus", "anno", "quibus", "post", "his", "omnia", "ea", "super", "qua", "sub", "illa", "dominus",
                 "deo", "rex", "nisi", "totus", "dixit", "dicitur", "ed", "ante"]

'''
This is the list of stopwords computed from entropy probability.
Mathematically, entropy is a measure of randomness in a probability distribution. In the context of corpus linguistics,
we measure the corpus cross entropy (aka log probability) for pairs of texts. Here, it is likely that the CLTK is 
measuring word entropy (aka unigram entropy). University entropy is the average information content of words.
These are the words with the *lowest* entropy. 
'''
cltk_entropy = ["et", "in", "est", "non", "ad", "ut", "cum", "quod", "qui", "sed", "si", "de", "quae", "quam", "per",
                "ex", "nec", "sunt", "esse", "se", "hoc", "ab", "enim", "aut", "autem", "etiam", "quid", "quo", "atque",
                "eius", "te", "uel", "sit", "me", "iam", "ne", "haec", "quia", "tamen", "nam", "ac", "mihi", "ita",
                "sic", "tibi", "id", "pro", "eo", "inter", "nunc", "quem", "ipse", "uero", "neque", "quibus", "ille",
                "erat", "eum", "sibi", "qua", "nisi", "quoque", "ergo", "quidem", "omnia", "post", "hic", "fuit", "ego",
                "ea", "nihil", "omnes", "his", "illa", "modo", "tu", "esset", "sine", "nos", "dum", "ubi", "ante",
                "quis", "tam", "sub", "sicut", "quos", "omnibus", "potest", "nobis", "sua", "cui", "igitur", "res",
                "ei", "tantum", "cuius", "apud", "contra", "magis"]

'''
This is the list of words computed from Borda count (aka Borda sort). 
The Borda method of counting assigns each word one point per word that is less frequent. In a corpus of ten words, the 
most common word gets a score of 9 and the least common gets a score of 0. 
These are the words with the *highest* points in Borda count.
'''
cltk_borda = ["et", "in", "est", "non", "ad", "ut", "quod", "cum", "qui", "si", "sed", "de", "quae", "quam", "per",
              "ex", "nec", "esse", "sunt", "se", "hoc", "enim", "autem", "ab", "aut", "te", "quid", "uel", "etiam",
              "atque", "me", "eius", "quo", "sit", "quia", "iam", "ne", "ac", "mihi", "haec", "tamen", "tibi", "pro",
              "nam", "id", "ita", "sic", "eo", "neque", "uero", "eum", "nunc", "inter", "ergo", "erat", "quem", "ipse",
              "ego", "quibus", "nihil", "ille", "quoque", "quidem", "sibi", "dig", "nisi", "qua", "post", "ea", "tu",
              "hic", "fuit", "omnia", "his", "esset", "nos", "sicut", "illa", "omnes", "sine", "secundum", "bibit",
              "modo", "dum", "quis", "quaestio", "ubi", "deus", "od", "ante", "dei", "potest", "tam", "sub", "ei",
              "uos", "nouus", "quos", "nobis", "bellum"]

'''
This is the list of stopwords provided by the International Organization for Standardization (ISO). They are likely
based on frequency, although it is possible to submit requests for additions and deletions. 
'''
ISO = ["a", "ab", "ac", "ad", "at", "atque", "aut", "autem", "cum", "de", "dum", "e", "erant", "erat", "est", "et",
       "etiam", "ex", "haec", "hic", "hoc", "in", "ita", "me", "nec", "neque", "non", "per", "qua", "quae", "quam",
       "qui", "quibus", "quidem", "quo", "quod", "re", "rebus", "rem", "res", "sed", "si", "sic", "sunt", "tamen",
       "tandem", "te", "ut", "vel"]

'''
This is the list of stopwords from the Perseus Digital Library (PDL) hosted at Tuft's University.
'''
PDL = ["ab", "ac", "ad", "adhic", "aliqui", "aliquis", "an", "ante", "apud", "at", "atque", "aut", "autem", "cum",
       "cur", "de", "deinde", "dum", "ego", "enim", "ergo", "es", "est", "et", "etiam", "etsi", "ex", "fio", "haud",
       "hic", "iam", "idem", "igitur", "ille", "in", "infra", "inter", "interim", "ipse", "is", "ita", "magis", "modo",
       "mox", "nam", "ne", "nec", "necque", "neque", "nisi", "non", "nos", "o", "ob", "per", "possum", "post", "pro",
       "quae", "quam", "quare", "qui", "quia", "quicumque", "quidem", "quilibet", "quis", "quisnam", "quisquam",
       "quisque", "quisquis", "quo", "quoniam", "sed", "si", "sic", "sive", "sub", "sui", "sum", "super", "suus", "tam",
       "tamen", "trans", "tu", "tum", "ubi", "uel", "uero", "unus", "ut"]

'''
This is the list of stopwords provided by the Digital Classicist available at 
http://wiki.digitalclassicist.org/Stopwords_for_Greek_and_Latin.
This list was originally based on the PDL list, but has since removed 'unus' and 'ut,' and added 'an'. Due to its
similarity with the PDL list and unstable provenence, it is not included in the JOHD data paper for this dataset. 
We have included it here for reference and archival purposes.
'''
DC = ["a", "ab", "ac", "ad", "adhic", "aliqui", "aliquis", "an", "ante", "apud", "at", "atque", "aut", "autem", "cum",
      "cur", "de", "deinde", "dum", "ego", "enim", "ergo", "es", "est", "et", "etiam", "etsi", "ex", "fio", "haud",
      "hic", "iam", "jam", "idem", "igitur", "ille", "in", "infra", "inter", "interim", "ipse", "is", "ita", "magis",
      "modo", "mox", "nam", "ne", "nec", "necque", "neque", "nisi", "non", "nos", "o", "ob", "per", "possum", "post",
      "pro", "quae", "quam", "quare", "qui", "quia", "quicumque", "quidem", "quilibet", "quis", "quisnam", "quisquam",
      "quisque", "quisquis", "quo", "quoniam", "sed", "si", "sic", "sive", "siue", "sub", "sui", "sum", "super", "suus",
      "tam", "tamen", "trans", "tu", "tum", "ubi", "uel", "vel", "uero", "vero"]

all_stop_lists = [cltk_mean, cltk_variance, cltk_entropy, cltk_borda, ISO, PDL, DC]


def create_word_set():
    all_words = set()
    for stop_list in all_stop_lists:
        for word in stop_list:
            all_words.add(word)
    return all_words


def fill_dataframe():
    all_words = create_word_set()
    all_rows = []
    for word in all_words:
        current_row = [word]
        for stop_list in all_stop_lists:
            if word in stop_list:
                current_row.append('Y')
            else:
                current_row.append('N')
        all_rows.append(current_row)
    column_names = ['word', 'CLTKM', 'CLTKV', 'CLTKE', 'CLTKB', 'ISO', 'PDL', 'DC']
    df = pd.DataFrame(all_rows, columns=column_names)
    return df
