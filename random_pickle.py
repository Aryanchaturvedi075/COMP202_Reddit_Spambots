import pickle
# random word_dict

dictionary = {}
dictionary['PARAGRAPH-OPENER'] = ['In my opinion', 'On the other hand', 'To be honest', 'From my perspective', 'As it appears']
dictionary['MANAGEMENT-SYNONYMS'] = ['management', 'leadership', 'agenda', 'mandate', 'regulation']
dictionary['TROUBLE-SYNONYMS'] = ['shambles', 'debacle', 'wreckage', 'disaster', 'pile of mismanagement']
dictionary['POSITIVE-ADJECTIVE'] = ['bold', 'helpful', 'progressive', 'resilient', 'reliable']
dictionary['BACKHANDED-ADJECTIVE'] = ['detailed', 'useful', 'thoughtful', 'cautious', 'circumstantial']
dictionary['AGENT-SYNONYMS'] = ['right hand', 'stepping stone', 'pillar', 'subordinate', 'assistant']
dictionary['EVOCATIVE-DICTION'] = ['insulting', 'disrespectful', 'belittling', 'humiliating', 'disdainful']
dictionary['SUPPORT-SYNONYMS'] = ['support', 'endorse', 'stand by', 'condone', 'approve']
dictionary['EASY-SYNONYMS'] = ['easy lane', 'lazy river', 'simple route', 'unhurdled path', 'express lane']
dictionary['LIKE-SYNONYMS'] = ['like', 'prefer', 'admire', 'approve', 'side by']
dictionary['PLAN-SYNONYMS'] = ['agenda', 'mandate', 'plan', 'proposition', 'proposal']
dictionary['HATE-SYNONYMS'] = ['hate', 'detest', 'abhor', 'despise', 'loathe']
dictionary['NEGATIVE-ADJECTIVE'] = ['restrictive', 'troublesome', 'incomprehensible', 'time-consuming', 'exhausting', 'hoarding']
dictionary['PRAISE-SYNONYMS'] = ['legend', 'god-sent', 'prophet', 'messiah', 'hidden gem']
dictionary['CANDIDATES'] = ['Boole Ian', 'Elsa IfStatement', 'Dee Bug-Her']
dictionary['ADVERB'] = ['clearly', 'without a doubt', 'hands down', 'ubdoubtedly', 'unquestionably']
dictionary['APPROPRIATE-SYNONYMS'] = ['right', 'vital', 'appropriate', 'essential', 'important']
dictionary['RESTRICTION-SYNONYMS'] = ['planning', 'restrictions', 'procedures', 'contingency', 'course of action']
dictionary['EASY-COMPARATIVE'] = ['half as easy', 'as simple', 'as straightforward', 'as effortless', 'as manageable']
dictionary['BASELESS-SYNONYMS'] = ['baseless', 'groudless', 'on halt', 'discontinued', 'vain']

word_dict = open('word_dict.pkl', 'wb')
pickle.dump(dictionary, word_dict)
word_dict.close()