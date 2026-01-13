file = open("sample.txt", "r")
content = file.read()
file.close()
print(f"File Content: 'sample.txt' - {content}")