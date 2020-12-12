shakespear = """King. Sweet Gertrude leaue vs too, For we haue closely sent for Hamlet hither, That he, as 'twere by accident, may thereAffront Ophelia. Her Father, and my selfe (lawful espials) Will so bestow our selues, that seeing vnseeneWe may of their encounter frankely iudge, And gather by him, as he is behaued,If't be th' affliction of his loue, or no. That thus he suffers for Qu. I shall obey you, And for your part Ophelia, I do wish That your good Beauties be the happy cause Of Hamlets wildenesse: so shall I hope your Vertues Will bring him to his wonted way againe, To both your Honors"""
ralph_waldo_emerson = """These are the voices which we hear in solitude, but they grow faint and inaudible as we enter into the world. Society everywhere is in conspiracy against the manhood of every one of its members. Society is a joint-stock company, in which the members agree, for the better securing of his bread to each shareholder, to surrender the liberty and culture of the eater. The virtue in most request is conformity. Self-reliance is its aversion. It loves not realities and creators, but names and customs."""
words_shakespear = []
for i in map(str.lower,shakespear.split(' ')):
    i = i.strip('.,\n')
    words_shakespear.append(i)
words_shakespear = set(words_shakespear)
#words_shakespear = set(shakespear.split(' '))
#words_emerson = set(ralph_waldo_emerson.split(' '))
words_emerson = []
for i in map(str.lower,ralph_waldo_emerson.split(' ')):
    i = i.strip('.,')
    words_emerson.append(i)
words_emerson = set(words_emerson)
print('Повторяющиеся слова: ')
print(words_shakespear & words_emerson)
print('Уникальные слова')
print(words_shakespear ^ words_emerson)
