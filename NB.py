pos = {
    'I': 0.09,
    'always': 0.07,
    'like': 0.29,
    'foreign': 0.04,
    'films': 0.08
}

neg = {
    'I': 0.16,
    'always': 0.06,
    'like': 0.06,
    'foreign': 0.15,
    'films': 0.11
}

prior_pos = 0.4
prior_neg = 0.6

sentence = 'I always like foreign films'

pos_pro = prior_pos
neg_pro = prior_neg

for word in sentence.split():
    pos_pro *= pos[word]
    neg_pro *= neg[word]

if pos_pro > neg_pro:
    print('This is a positive comment.')
else:
    print('This is a negative comment.')
