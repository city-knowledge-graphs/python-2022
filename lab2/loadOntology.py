'''
Created on 19 Jan 2021

@author: ejimenez-ruiz
'''
from owlready2 import *


def getClasses(onto):        
    return onto.classes()
    


def loadOntology(urionto):
    
    #Method from owlready
    onto = get_ontology(urionto).load()
    
    print("Classes in Ontology: " + str(len(list(getClasses(onto)))))
    for cls in getClasses(onto):                
        print("\t"+cls.iri)


#Load ontology
urionto="http://protege.stanford.edu/ontologies/pizza/pizza.owl"
loadOntology(urionto)