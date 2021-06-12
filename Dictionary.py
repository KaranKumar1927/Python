acronyms = {'TBH' : 'To be honest',
            'IDK' : 'I dont know'}

Sentence = 'TBH ' + ',' + 'IDK' + 'what happened'

convert = acronyms.get('TBH') +  ',' + acronyms.get('IDK') + ' what happened'

print(convert)