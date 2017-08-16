#!/usr/bin/env python

def stemWord(w):
    """Renders a word in to its generic form.
    
    This function is used preprocess words for NLP.
    It removes all trailing punctuation marks "';-?.,!:".
    It also removes the possessive "'s" from words.
    And it converts it to all lower case
    
    Args:
        w (str): A string containing the input word
    
    Returns:
        str a simpler version of the word
    """
    w=w.split("'")[0]#Separates and eliminates all after the "'"
    w=[letter for letter in w if not (letter in ';-?.,!:')] #Eliminates the simbols on w
    return ''.join(w).lower() #Joins and puts in lowercase 


class LanguageModel:
    """Class that contains the data needed for the analysis of text
    """
    @staticmethod
    def getWordFreq(txt):
        """Returns a dictionary where the keys are stemmed words and values
        are the number they occured in txt.
        
        As na example if txt == "The dog likes the cat!" the resulting 
        frequency dictionary should be {"the":2,"dog":1,"likes":1,"cat":1}
        
        Hints: 
            -Use split to break the text in to a list of words
            stem all words in the list
            -Make sure a dictionary element exists before operating on it.
        
        Args:
            txt (str): a string containing free text
            
        Returns:
            dict: A dictionary whith stemmed words (str) for keys and int 
            values containing the occurence count of these words.
        """
        
        list1 = txt.split()
        newlist = []
        dic = {}
        for word in list1:
           newlist.append(stemWord(word))
    
        for word in newlist:
            if dic.has_key(word) == True:
                dic[word] = dic[word] +1
            else:
                dic[word] = 1
        return dic
        
    @staticmethod
    def mergeWordFreqDict(frDict1,frDict2):
        """Takes two dictionaries containing word frequencies and returns a 
        single dictionary containing their sum.
        
        In essence this fuction takes the frequencies produced from two
        different strings with text and returns a dictionary with the 
        word frequencies of the concatenation of these two strings.
        
        Hints:
            -Dictionary .keys() returns a list so you might need to cast it 
            to a set, if you want to get the union.
            -It is better if you create a dictionary with 0 for all words in
            both dictionaries and then update the values
            -If frDict1=={"hello":1,"world":1} and frDict2=={"goodbye":1,"world":1},
            the result must be {"hello":1,"world":2,"goodbye":1}
            -The simplest solution involves 3 non nested for loops.
        
        Args:
            frDict1 (dict): a dictionary with stemmed words as keys and 
            positive integers as values.
            frDict2 (dict): a dictionary with stemmed words as keys and 
            positive integers as values.
        
        Returns:
            dict: a dictionary with stemmed words as keys and positive 
            integers as values.
        """
        
        new_dict = frDict1         
        
        for i in frDict2:
            if i in new_dict:
                new_dict[i] += frDict2[i]
            else:
                new_dict[i] = frDict2[i]
            
        return new_dict

    def __init__(self,txtList=[]):
        """LangueModel constructor
        
        Initialises the class members to valid values.
        __texts is a list with one or more strings with texts.
        __wordFreq is a dictionary with stemmed words for keys and the 
        count of the occurences of each word (int) as values.
        
        Args:
            txtList (list): A list of strings where each string will 
            contains some text.
        """
        self.__wordFreq={}#Dictionary with the word's frequencies.
        self.__texts=[]#A list with a text string
        if txtList.__class__ != [].__class__:
            raise Exception('txtList must be a list of strings')
        for txt in txtList:
            self.addText(txt)#add text to the list

    def addText(self,txt):
        """Adds a string containing text to the model
        
        This method just uses getWordFreq and mergeWordFreqDict static 
        methods on a specific instance of the class
        
        Args:
            txt (str): the string containing text to be added
        """
        self.__texts.append(txt)  
        newFreq=LanguageModel.getWordFreq(txt)   #newFreq is a dictionary with the word's frequencies of the added text
        self.__wordFreq=LanguageModel.mergeWordFreqDict(self.__wordFreq,newFreq)  #Sum of the two dictionaries

    def addTextFile(self,fileName):
        """Ads text contained in a text-file
        
        Args:
            fileName (str): the absolute or relative path to a file 
            containing text.
        """
        self.addText(open(fileName).read())#Adds text in a file

    def wordCount(self):
        """Returns the total number of words found in self.__texts
        
        Hints:
        -The answer can be writen in a single line
        -The method values() of dict is the key to solving this question
        -The distionary __wordFreq contains how many times each word was 
        found in the texts

        Returns:
            int: the count of all the words
        """
        
        return sum(self.__wordFreq.values())
        
        
    def uniqueWordCount(self):
        """Returns the number of unique words found in self.__texts

        Unique word means that a word occuring twice or more times, counts 
        as one.

        Hints:
        -The answer can be writen in a single line
        -The method keys() of dict is the key to solving this question

        Returns:
            int: the count of unique words
        
        """
        
        return len(self.__wordFreq.keys())
        

    def getWordProbabillity(self,word):
        """Returns the probabillity of a word occuring according to the 
        model
        
        The probabillity of a word occuring is the number of times it has 
        occured divided by the count of all word occurences in __texts
        
        Args:
            word (str): an string with a word which is not necessarilly 
            stemmed.

        Returns:
            float: a float between 0 and 1 that contains the probabillity
        """
        stemmedWord=stemWord(word)#Converts 'word' in a simple string in lowercase
        if stemmedWord in self.__wordFreq.keys():#if the word is in the list
            return self.__wordFreq[stemmedWord]/float(self.wordCount())#Divide between all the words to know the probabillity  
        else:
            return 0#If not found return 0

    def __str__(self):
        """Generate a string description of the Language Model
        
        Hints:
        -The result must be constructed with string concatenation
        -Cast an integer to a string before concatening it.
        -Use the already availabe methods to obtain information
        -lm=LanguageModel(['hello world','Goodbye World!'])
        lm.__str__() will return
        "LanguageModel\n\t#texts:2\n\t#words:4\n\t#unique words:3\n"
        -self.__texts, is a list containing all texts the LanguageModel has 
        seen.

        Returns:
            string: A description of the language model spanning 4 lines.
        """
        uwords = self.uniqueWordCount(self)
        nwords = self.wordCount(self)
        texts = len(self.__texts(self))
        
        lm = "The lenguage model has:\n\t" + "texts:" + str(texts) + "\n\t"+ "words:" + str(nwords) + "\n\t" + "unique words:" + str(uwords) + "\n"
        
        return lm

    def __repr__(self):
        """Generate a string description of the Language Model that allows 
        to reconstruct it
        
        Returns:
            string: A python expression that invockes the constructor of the
            class so that if executed a deep copy of the LangueageModel is 
            obtained.
        """
        res=str(self.__class__)+'('+self.__texts.__repr__()+')'
        return res

    def getWordsByProbabillity(self):
        """Produces a list containing all stemmed words from the language 
        model sorted from the most probable to the least probable
        
        Hints:
        -function reversed returns a list with reverse order of the input 
        list
        -function sorted returns a list with the elements of the input sorted
        in ascending order.
        -A list of tuples is sorted by the first element of each tuple

        Returns:
            list: a list of strings (not tuples!)
        """
        finalist = {}
        newdict = self.__wordFreq.keys()
        for i in newdict:
            finalist[i] = self.getWordProbabillity(i)
            
        sorted_keys = sorted(finalist, key=finalist.__getitem__)
        
        l = list(reversed(sorted_keys))
        
        return l
             
    def isPalindrome(sentence):
        """Tells us whether a string is a palindrome.
        
        Pallindromes are sentences whos characters read in both directions are 
        the same. Testing for pallindromes ignores spaces and puntuation marks
        as if they did not exist.
        
        Hits:
        -A list can be indexed form the end with negative values. 
        -The first character in a string is at position 0
        If a=[1,"b",3,4] Then a[-1] is 4, a[-2] is 3, etc.
        -The expression a[len(a)-1]==a[-1] is always True if a is not empty
        -You will need to use .split() and .join methods of the str type
        
        Args:
            sentence (str): A string with one or more words assumed to have no 
            possessive (stemWord can help).
        
        Returns:
            bool: The return value. True if the sentence was a palindrome, False
            otherwise.
        """
        
        answer = True 
              
        newstring = stemWord(sentence)
       
        s_no_space = newstring.replace(" ","")#remplaza el espacio
    
        if  s_no_space ==  s_no_space[::-1]:#compara las dos listas
             answer = True#si son iguales es que son cap i cua
        else:
             answer = False
                
        return answer


    if __name__ == '__main__':
        #Everything here is ignored by joc-de-proves
        #You can debug your program by testing your functions and classes here
        pass
