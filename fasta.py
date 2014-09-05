import sys

class FASTAReader(object): #defining function of object called "fastareader" making a new type of thing. A fastareader does not exist in python
    def __init__( self, file ):  #initializes the state of the object. self refers to the object
        self.file = file
        self.last_sid = None 
    def next( self ):
        if self.last_sid is None:    
            line = sys.stdin.readline() # read first line of file
            assert line.startswith(">") #confirms it is the correct file type
            sid = line[1:].rstrip("\r\n") # take first character off string. 
        else:
            sid = self.last_sid
            
        sequences = []  #accumulate data into list
        while True:
            line = sys.stdin.readline()
            if line == "" and not sequences:
                raise StopIteration 
            if line.startswith(">") or line == "": #break code if line starts with >
                self.last_sid = line[1:].rstrip("\r\n")
                break
            else: 
                sequences.append (line.strip() ) #gets rid of all white space
        
        sequence = "".join( sequences )  
        return sid, sequence #returns values from a funtion or method
        
    def __iter__(self):
        return self