if (__name__ == '__main__'):
    __main__();

def __main__():
    return

import requests

class BabelNetAPI:
    def __init__(self, key):
        self.key = key
        
    def getSynsetIds(self, lemma, lang='EN'):
        """
            Retrieve the IDs of the Babel synsets (concepts) denoted by a given word
        """
        response = requests.get(f"https://babelnet.io/v5/getSynsetIds?lemma={lemma}&searchLang={lang}&key={self.key}")
        return response.json()

    def getSynset(self, sysnet_id, lang='EN'):
        """
            Retrieve the information of a given synset
        """
        response = requests.get(f"https://babelnet.io/v5/getSynset?id={sysnet_id}&targetLang={lang}&key={self.key}")
        return response.json()
    
    def getSenses(self, lemma, lang='EN', pos=None):
        """
            Retrieve the senses of a given word
        """
        if (pos):
            response = requests.get(f"https://babelnet.io/v5/getSenses?lemma={lemma}&searchLang={lang}$pos={pos}&key={self.key}")
        else:
            response = requests.get(f"https://babelnet.io/v5/getSenses?lemma={lemma}&searchLang={lang}&key={self.key}")
        return response.json()
    
    def getSynsetIdsFromResourceID(self, lemma, pos=None, source='WIKI', lang='EN'):
        """
            Retrieve a list of BabelNet IDs given a resource identifier
        """
        if (pos):
            response = requests.get(f"https://babelnet.io/v5/getSynsetIdsFromResourceID?id={lemma}&searchLang={lang}&pos={pos}&source={source}&key={self.key}")
        else:
            response = requests.get(f"https://babelnet.io/v5/getSynsetIdsFromResourceID?id={lemma}&searchLang={lang}&source={source}&key={self.key}")
            
        return response.json()
    
    def getOutgoingEdges(self, sysnet_id):
        """
            Retrieve edges of a given BabelNet synset
        """
        response = requests.get(f"https://babelnet.io/v5/getOutgoingEdges?id={sysnet_id}&key={self.key}")
        return response.json()