'''
Created on 19 Jan 2021

@author: ejimenez-ruiz
'''
from owlready2 import *


def getClasses(onto):        
    return onto.classes()
    
def getDataProperties(onto):        
    return onto.data_properties()
    
def getObjectProperties(onto):        
    return onto.object_properties()
    
def getIndividuals(onto):        
    return onto.individuals()


#RDFS label can be accessed this was with OWLready
def getRDFSLabelsForEntity(entity):
    #One can also check if the attribute exists for non standard annotations
    #if hasattr(entity, "label"):    
    return entity.label

def loadOntology(urionto):
    
    #Method from owlready
    onto = get_ontology(urionto).load()
    
    print("Classes in Ontology: " + str(len(list(getClasses(onto)))))
    for cls in getClasses(onto):                
        print(cls.iri)
        print("\t"+cls.name)  
        #Labels from RDFS label
        print("\t"+str(getRDFSLabelsForEntity(cls)))
        
    print("Object properties in Ontology: " + str(len(list(getObjectProperties(onto)))))
    for oprop in getObjectProperties(onto):                
        print(oprop.iri)
        print("\t"+oprop.name)  
        #Labels from RDFS label
        print("\t"+str(getRDFSLabelsForEntity(oprop)))
    
    
    print("Data properties in Ontology: " + str(len(list(getDataProperties(onto)))))
    for dprop in getObjectProperties(onto):                
        print(dprop.iri)
        print("\t"+dprop.name)  
        #Labels from RDFS label
        print("\t"+str(getRDFSLabelsForEntity(dprop)))
        
    
    print("Individuals in Ontology: " + str(len(list(getIndividuals(onto)))))
    for indiv in getIndividuals(onto):                
        print(indiv.iri)
        print("\t"+indiv.name)  
        #Labels from RDFS label
        print("\t"+str(getRDFSLabelsForEntity(indiv)))

#Load ontology
urionto="http://protege.stanford.edu/ontologies/pizza/pizza.owl"
loadOntology(urionto)