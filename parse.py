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
            addWordDefinition()
            cits = sameWordsBox[0].findall(".//{http://www.tei-c.org/ns/1.0}cit")
            if 1 == len(cits):
                # cits birden fazla ise birden fazla anlam vardır
                # bazen kelimenin sadece bir anlamı olsa da birden fazla fiil veya birden fazla sıfat anlamı olabilir.

                #kelimenin kaç tane çevirisi var
                quoteBox = cits[0].findall(".//{http://www.tei-c.org/ns/1.0}quote")
                if 1 == len(quoteBox):
                    simple_dictionary["words"][-1]["transition"] = quoteBox[0].text
                else:
                    simple_dictionary["words"][-1]["transitions"] = []
                    for b in quoteBox:
                        simple_dictionary["words"][-1]["transitions"].append(b.text)

            else:
                senseler = sameWordsBox[0].findall(".//{http://www.tei-c.org/ns/1.0}sense")
                # senseler kelime anlamı için lazım
                # senseler dizinde işimize yarayacak olan dizideki indekler tek basamaklı sayılardır
                # çünkü yok var yok var şeklinde gidiyor
                sayi = 1
                for b in senseler:
                    b.find(".//{http://www.tei-c.org/ns/1.0}def").text
                    sayi = sayi+2
            


           
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
