import xml.etree.ElementTree as ET
with open("C:/Users/Mustafa Yüksel/Desktop/simple_dic_parsing/deneme.xml", "r", encoding="utf-8") as file:
    xml_text = file.read()
root = ET.fromstring(xml_text)
simple_dictionary = {}
simple_dictionary["words"] = []
entry_elements = root.findall(".//{http://www.tei-c.org/ns/1.0}entry")
index = 0
lookedUpWords = []
wordName = "empty"
def addQuoteOrQuotesForMultipleMeaning(quoteList : list):
    if 1 == len(quoteList):
        simple_dictionary["words"][-1]["definitions"][-1]["transition"] = quoteList[0].text
    else:
        simple_dictionary["words"][-1]["definitions"][-1]["transitions"] = [] 
        for b in quoteList:
            simple_dictionary["words"][-1]["definitions"][-1]["transitions"].append(b.text)
def addQuoteOrQuotes( quoteList : list):
    if 1 == len(quoteList):
        simple_dictionary["words"][-1]["transition"] = quoteList[0].text
    else:
        simple_dictionary["words"][-1]["transitions"] = []
        for b in quoteList:
            simple_dictionary["words"][-1]["transitions"].append(b.text)

def addValueToDefinitions(value:str):
    simple_dictionary["words"][-1]["definitions"][-1]["definition"] = value
def addMapToDefinitions():
    simple_dictionary["words"][-1]["definitions"].append({})
def addDefinitions():
    simple_dictionary["words"][-1]["definitions"] = []
def addWordDefinition():
    definition = sameWordsBox[0].find(".//{http://www.tei-c.org/ns/1.0}def").text
    simple_dictionary["words"][-1]["definition"] = definition
def getWordTypeForOneMeaninWords():
    simple_dictionary["words"][-1]["type"] = sameWordsBox[0].find(".//{http://www.tei-c.org/ns/1.0}pos").text

def addWordNameToMap():
    simple_dictionary["words"][-1]["word"] = wordName
def addLookedUpWords():
    lookedUpWords.append(wordName)
def addPolysemanticKeyToArray():
    if wordMeaningCount==1:
       print
    else:
        simple_dictionary["words"][-1]["polysemantic"] = []
def increaseTheIndex():
    global index  # global değişkeni kullanacağımızı belirtiyoruz
    index = index + 1
def addEmtyMaptoArray():
    simple_dictionary["words"].append({})
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
        addEmtyMaptoArray()
        addLookedUpWords()
        sameWordsBox = []
        for i in entry_elements:
            if(wordName)== i.find(".//{http://www.tei-c.org/ns/1.0}orth").text: # kelimemeiz x diyelim. bütün datada kaç tane x var ona bakıyoruz
                print("kelime eşleşti")
                wordMeaningCount = wordMeaningCount + 1
                sameWordsBox.append(i)
            else:
                print("kelime işleşmedi")
        addWordNameToMap()
        if(wordMeaningCount==1): # kelimenin sadece bir anlamı varsa
            getWordTypeForOneMeaninWords()
            cits = sameWordsBox[0].findall(".//{http://www.tei-c.org/ns/1.0}cit")
            if 1 == len(cits):
                addWordDefinition()
                # cits birden fazla ise birden fazla anlam vardır
                # bazen kelimenin sadece bir anlamı olsa da birden fazla fiil veya birden fazla sıfat anlamı olabilir.

                #kelimenin kaç tane çevirisi var
                quoteBox = cits[0].findall(".//{http://www.tei-c.org/ns/1.0}quote")
                addQuoteOrQuotes(quoteBox)

            else:
                senseler = sameWordsBox[0].findall(".//{http://www.tei-c.org/ns/1.0}sense")
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


           
        else:
            print



   


'''
.findall(".//{http://www.tei-c.org/ns/1.0}sense")[0].text
orth_element = root.find(".//{http://www.tei-c.org/ns/1.0}orth")
pos_element = root.find(".//{http://www.tei-c.org/ns/1.0}pos")
simple_dictionary["words"][-1]["type"] = pos_element.text
simple_dictionary["words"][-1]["polysemantic"] = pos_element.text
print(simple_dictionary)
'''
print(simple_dictionary)
