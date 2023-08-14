import xml.etree.ElementTree as ET
with open("C:/Users/Mustafa Yüksel/Desktop/simple_dic_parsing/deneme.xml", "r", encoding="utf-8") as file:
    xml_text = file.read()
root = ET.fromstring(xml_text)
simple_dictionary = {}
simple_dictionary["words"] = []
entry_elements = root.findall(".//{http://www.tei-c.org/ns/1.0}entry")
index = 0
wordName = "deneme"
def addPolysemanticKeyToArray():
    simple_dictionary["words"][-1]["polysemantic"] = []
def increaseTheIndex():
    global index  # global değişkeni kullanacağımızı belirtiyoruz
    index = index + 1
def getNextIndex():
    nextIndex = index + 1
    return nextIndex
def addEmtyMaptoArray():
    simple_dictionary["words"].append({})
def getWordName(entry):
    wordName =  entry.find(".//{http://www.tei-c.org/ns/1.0}orth").text
    print(wordName)
    simple_dictionary["words"][-1]["word"] = wordName
def getNextWordName():
    nextEntry = entry_elements[getNextIndex()]
    nextwordName =  nextEntry.find(".//{http://www.tei-c.org/ns/1.0}orth").text
    return nextwordName

for entry in entry_elements:
    addEmtyMaptoArray()
    getWordName(entry)
    """
    bazı kelimeler aynı yazıldığı halde birden çok anlama sahip oluyor.
    bundan bir sonraki index'teki elementin ismi bu index'teki elementin ismiyle uyuşuyor mu kontrol et.
    Eğer uyuşuyor ise kelimenin birden fazla anlamı var demektir
    """
    if wordName == getNextWordName() : 
        print("kelimenin birden fazla anlamı var")
        addPolysemanticKeyToArray()
    else:
        print("kelimenin birden fazla anlamı yok")    
    
    increaseTheIndex()
orth_element = root.find(".//{http://www.tei-c.org/ns/1.0}orth")
pos_element = root.find(".//{http://www.tei-c.org/ns/1.0}pos")
simple_dictionary["words"][-1]["type"] = pos_element.text
simple_dictionary["words"][-1]["polysemantic"] = pos_element.text
print(simple_dictionary)