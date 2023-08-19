import xml.etree.ElementTree as ET
with open("C:/Users/Mustafa Yüksel/Desktop/simple_dic_parsing/deneme.xml", "r", encoding="utf-8") as file:
    xml_text = file.read()
root = ET.fromstring(xml_text)
simple_dictionary = {}
entry_elements = root.findall(".//{http://www.tei-c.org/ns/1.0}entry")
index = 0
lookedUpWords = []
wordName = "empty"
def addInflection(element):
    #  simple_dictionary[wordName]["polysemy"]
    orthElements = element.findall(".//{http://www.tei-c.org/ns/1.0}orth")
    if len(orthElements)>1:
        if duoWords:
            simple_dictionary[wordName]["polysemy"][-1]["inflection"] = []
            for orth in orthElements:
                simple_dictionary[wordName]["polysemy"][-1]["inflection"].append(orth.text)
        else:
            simple_dictionary[wordName]["inflection"] = []
            for orth in orthElements:
                simple_dictionary[wordName]["inflection"].append(orth.text)
def getCitsElements(element):
    getCitsElements = element.findall(".//{http://www.tei-c.org/ns/1.0}cit")
    return getCitsElements

def addItemsToMap(entryElement,):
    citsElements = getCitsElements(entryElement)
    if 1 == len(citsElements):
                addWordDefinition(entryElement)
                # cits birden fazla ise birden fazla anlam vardır.
                # typelar ortak def[{ definition transitions ayrı mapte tutulur}]
                #  
                #kelimenin kaç tane çevirisi var
                quoteBox = citsElements[0].findall(".//{http://www.tei-c.org/ns/1.0}quote")
                addQuoteOrQuotes(quoteBox)

    else:
        senseler = entryElement.findall(".//{http://www.tei-c.org/ns/1.0}sense")
        # senseler kelime anlamı(def) için ve çeviri (quote) için lazım
        # 0,2 gibi çift sayılarda quote'ya, 1,3 gibi tek sayılarda def'e odaklanacağız
        # çünkü yok var yok var şeklinde gidiyor
        addDefinitions()
        sayi = 0
        for b in senseler:
            if sayi % 2 == 1:
                definition = b.find(".//{http://www.tei-c.org/ns/1.0}def").text
                addValueToDefinitions(definition)
            else:
                addMapToDefinitions()
                quoteBox = senseler[sayi].findall(".//{http://www.tei-c.org/ns/1.0}quote")
                addQuoteOrQuotesForMultipleMeaning(quoteBox)

                print("deneme")
            sayi = sayi + 1
def addQuoteOrQuotesForMultipleMeaning(quoteList : list):
    if 1 == len(quoteList):
        if duoWords:
            simple_dictionary[wordName]["polysemy"][-1]["transition"] = quoteList[0].text
        else:
            simple_dictionary[wordName]["definitions"][-1]["transition"] = quoteList[0].text
    else:
        if duoWords:
            simple_dictionary[wordName]["polysemy"][-1]["definitions"][-1]["transitions"] = []
            for b in quoteList:
                simple_dictionary[wordName]["polysemy"][-1]["definitions"][-1]["transitions"].append(b.text)
        else:
            simple_dictionary[wordName]["definitions"][-1]["transitions"] = [] 
            for b in quoteList:
                simple_dictionary[wordName]["definitions"][-1]["transitions"].append(b.text)
def addQuoteOrQuotes( quoteList : list,):
    if 1 == len(quoteList):
        if duoWords:
            simple_dictionary[wordName]["polysemy"][-1]["transition"] = quoteList[0].text
        else:
            simple_dictionary[wordName]["transition"] = quoteList[0].text
    else:
        if duoWords:
            simple_dictionary[wordName]["polysemy"][-1]["transitions"] = []
            for b in quoteList:
                simple_dictionary[wordName]["polysemy"][-1]["transitions"].append(b.text)

        else:
            simple_dictionary[wordName]["transitions"] = []
            for b in quoteList:
                simple_dictionary[wordName]["transitions"].append(b.text)

def addValueToDefinitions(value:str):
    if duoWords:
        simple_dictionary[wordName]["polysemy"][-1]["definitions"][-1]["definition"] = value
    else:
        simple_dictionary[wordName]["definitions"][-1]["definition"] = value
def addMapToDefinitions():
    if duoWords:
        simple_dictionary[wordName]["polysemy"][-1]["definitions"].append({})
    else:
        simple_dictionary[wordName]["definitions"].append({})
def addDefinitions():
    if duoWords:
        simple_dictionary[wordName]["polysemy"][-1]["definitions"]=[]
    else:
        simple_dictionary[wordName]["definitions"] = []
def addWordDefinition(element,):
    global wordName
    definition = element.find(".//{http://www.tei-c.org/ns/1.0}def").text
    if duoWords:
        simple_dictionary[wordName]["polysemy"][-1]["definition"] = definition
    else:
        simple_dictionary[wordName]["definition"] = definition
def getWordType(element):
    simple_dictionary[wordName]["type"] = element.find(".//{http://www.tei-c.org/ns/1.0}pos").text

def addWordNameToMap():
    simple_dictionary[wordName]["word"] = wordName
def addLookedUpWords():
    lookedUpWords.append(wordName)
def increaseTheIndex():
    global index  # global değişkeni kullanacağımızı belirtiyoruz
    index = index + 1
def addEmtyMaptoMap():
    global simple_dictionary 
    simple_dictionary = {wordName: {}}
    #simple_dictionary[wordName] = dict(),
def getWordName(entry):
    global wordName
    wordName =  entry.find(".//{http://www.tei-c.org/ns/1.0}orth").text

for entry in entry_elements:
    getWordName(entry)
    wordMeaningCount = 0
    
    """
    bazı kelimeler aynı yazıldığı halde birden çok anlama sahip oluyor.
    bütün veriyi kontrol edip aynı isme sahip kaç tane kelime var kontrol et
    """
    if wordName not in lookedUpWords:
        duoWords = False
        #addEmtyMaptoMap()
        addLookedUpWords()
        sameWordsBox = []
        for i in entry_elements:
            simple_dictionary[wordName] = {}
            if(wordName)== i.find(".//{http://www.tei-c.org/ns/1.0}orth").text: # kelimemeiz x diyelim. bütün datada kaç tane x var ona bakıyoruz
                print("kelime eşleşti")
                wordMeaningCount = wordMeaningCount + 1
                sameWordsBox.append(i)
            else:
                print("kelime işleşmedi")
        #addWordNameToMap()
        if(wordMeaningCount==1): # kelimenin sadece bir anlamı varsa
            addInflection(entry)
            getWordType(sameWordsBox[0])
            addItemsToMap(sameWordsBox[0])
        else:
            duoWords = True
            simple_dictionary[wordName]["polysemy"] = []
            for sameWord in sameWordsBox:
                simple_dictionary[wordName]["polysemy"].append({})
                simple_dictionary[wordName]["polysemy"][-1]["type"] = sameWord.find(".//{http://www.tei-c.org/ns/1.0}pos").text
                addItemsToMap(sameWord)
                addInflection(sameWord)

                
            



   


'''
.findall(".//{http://www.tei-c.org/ns/1.0}sense")[0].text
orth_element = root.find(".//{http://www.tei-c.org/ns/1.0}orth")
pos_element = root.find(".//{http://www.tei-c.org/ns/1.0}pos")
simple_dictionary["words"][-1]["type"] = pos_element.text
simple_dictionary["words"][-1]["polysemantic"] = pos_element.text
print(simple_dictionary)
'''
print(simple_dictionary)
