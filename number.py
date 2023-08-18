dictionary = {}
for i in range(30000):
    dictionary[str(i)] = i
file_path = r"C:/Users/Mustafa Yüksel/Desktop/numara.txt"
with open(file_path, "w", encoding="utf-8") as file:
    
    # Metni dosyaya yaz
    file.write("{}".format(dictionary))

print("bitti")