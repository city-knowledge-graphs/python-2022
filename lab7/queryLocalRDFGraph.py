'''
Created on 18 Mar 2022

@author: ejimenez-ruiz
'''
from rdflib import Graph

import owlrl


def queryLocalGraph(local_rdf, format_data, query_file):

    g = Graph()
    g.parse(local_rdf, format=format_data)
    
        
    print("Loaded '" + str(len(g)) + "' triples.")
    
    #for s, p, o in g:
    #    print((s.n3(), p.n3(), o.n3()))
    
    #Do reasoning!
    owlrl.DeductiveClosure(owlrl.OWLRL_Semantics, axiomatic_triples=True, datatype_axioms=False).expand(g)
    print("After reasoning '" + str(len(g)) + "' triples.")
    
    #Load query
    query = open(query_file, 'r').read()    
    
    qres = g.query(query)

    print("\nQuery: ")
    print(query)
    
    print("Results: ")

    for row in qres:        
        #Row is a list of matched RDF terms: URIs, literals or blank nodes
        row_str =""
        for element in row:
            row_str += str(element) + ", "
        
        print("'%s'" % (str(row_str))) 


#Init files
format="ttl"
dataset="../files/playground.ttl"

query="query_playground.txt"
#query="solution/query7.1.txt"
#query="solution/query7.2.txt"
#query="solution/query7.3.txt"

queryLocalGraph(dataset, format, query)

