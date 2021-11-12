import preprocess_arkerpay as pa

print("beginning test")

yorick = 'Alas poor Yorick!  I knew him, Horatio.'
print(yorick)
print('avg word length: ' + str(round(pa.get_avg_wordlength(yorick), 2)))
print('character counts: ' + str(pa.get_charcounts(yorick)))
print('word counts: ' + str(pa.get_wordcounts(yorick)))
print('uppercase counts: ' + str(pa.get_uppercase_counts(yorick)))


very_web = "I think <b>I</b> sent 11,000 emails to president@whitehouse.gov and rt @joebiden and @kamalaharris.  Don't they read https://rcp.com ?"
print(very_web)
print('digit counts: ' + str((pa.get_digit_counts(very_web))))
print('emails: ' + str(pa.get_emails(very_web)))
print('hashtag counts: ' + str(pa.get_hashtag_counts(very_web)))
print('mention counts: ' + str(pa.get_mention_counts(very_web)))
print('urls: ' + str(pa.get_urls(very_web)))
print('removed emails: ' + pa.remove_emails(very_web))
print('removed html: ' + pa.remove_html_tags(very_web))
print('removed rts: ' + pa.remove_rt(very_web))
print('removed urls: ' + pa.remove_urls(very_web))


nothing = "Where, why, and how.  I don't know.  I can't know.  Whudd'ya think?  Sheeet.  Nuthin'"
print(nothing)
print('stopword counts: ' + str(pa.get_stopwords_counts(nothing)))
print('contraction exp: ' + pa.get_cont_exp(nothing))
print('remove stopwords: ' + pa.remove_stopwords(nothing))
print('remove special characters: ' + pa.remove_special_chars(nothing))
print('spelling correction: ' + str(pa.spelling_correction(nothing)))



long_poem = str('I have wished a bird would fly away, And not sing by my house all day; Have clapped my hands at him from the door When it seemed as if I could bear no more. ' +
    'The fault must partly have been in me. The bird was not to blame for his key. And of course there must be something wrong In wanting to silence any song. ')

print('removed rare words: ' + pa.remove_rare_words(long_poem))
print('removed common words: ' + pa.remove_common_words(long_poem))
print('made to base: ' + pa.make_to_base(long_poem))

# going to let this one go
pa.remove_accented_chars


