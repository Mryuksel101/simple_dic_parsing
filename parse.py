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
def addLookedUpWords():
    lookedUpWords.append(wordName)
def addPolysemanticKeyToArray():
    simple_dictionary["words"][-1]["polysemantic"] = []
def increaseTheIndex():
    global index  # global değişkeni kullanacağımızı belirtiyoruz
    index = index + 1
def addEmtyMaptoArray():
    simple_dictionary["words"].append({})
def getWordName(entry):
    global wordName
    wordName =  entry.find(".//{http://www.tei-c.org/ns/1.0}orth").text
    print(wordName)
    simple_dictionary["words"][-1]["word"] = wordName

for entry in entry_elements:
    addEmtyMaptoArray()
    getWordName(entry)
    wordMeaningCount = 0
    
    """
    bazı kelimeler aynı yazıldığı halde birden çok anlama sahip oluyor.
    bütün veriyi kontrol edip aynı isme sahip kaç tane kelime var kontrol et
    """
    if wordName not in lookedUpWords:
        addLookedUpWords()
        for i in entry_elements:
            if(wordName)== i.find(".//{http://www.tei-c.org/ns/1.0}orth").text:
                print("kelime eşleşti")
                wordMeaningCount = wordMeaningCount + 1

            else:
                print("kelime işleşmedi")
   
    print(wordName + "için" + str(wordMeaningCount) + "kelime anlamı var")


'''  increaseTheIndex()
orth_element = root.find(".//{http://www.tei-c.org/ns/1.0}orth")
pos_element = root.find(".//{http://www.tei-c.org/ns/1.0}pos")
simple_dictionary["words"][-1]["type"] = pos_element.text
simple_dictionary["words"][-1]["polysemantic"] = pos_element.text
print(simple_dictionary)
'''
print(lookedUpWords)
