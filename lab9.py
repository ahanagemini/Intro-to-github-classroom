import numpy as np

def pl_fc_entails(KB, q):
    """
    Determines if a query q is entailed by a Horn Knowledge Base KB.
    Follows the Slide 29 algorithm structure exactly.
    
    KB is a dictionary containing:
        - 'clauses': a list of objects representing Horn clauses.
                     Each clause c has keys 'premise' (list of symbols) and 'head' (symbol).
        - 'symbols_known': a list of symbols initially known to be true.
    q is a string representing the query symbol.
    """
    # local variables initialization
    # count: a table, indexed by clause, initially the number of premises
    count = {}
    for idx, c in enumerate(KB['clauses']):
        count[idx] = len(c['premise'])
        
    # inferred: a table, indexed by symbol, each entry initially false
    inferred = {}
    
    # agenda: a list of symbols, initially the symbols known in KB
    agenda = list(KB['symbols_known'])
    
    # while agenda is not empty do
    while len(agenda) > 0:
        # p <- Pop(agenda)
        p = agenda.pop(0)
        
        # unless inferred[p] do
        if not inferred.get(p, False):
            # inferred[p] <- true
            inferred[p] = True
            
            # for each Horn clause c in whose premise p appears do
            for idx, c in enumerate(KB['clauses']):
                if p in c['premise']:
                    # decrement count[c]
                    ## TODO: Decrement the count for the current clause index
                    pass
                    
                    # if count[c] = 0 then do
                    ## TODO: Check if the clause count is 0
                        # if Head[c] = q then return true
                        ## TODO: If the head of clause c matches q, return True
                        
                        # Push(Head[c], agenda)
                        ## TODO: Append the head of clause c to the agenda
                        pass
                        
    return False
