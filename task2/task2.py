file=str(input("enter  your file name with extension:"))
r=(file.partition("."))
filename, separator,extension= file.partition(".")
print("the extension of the file is:",extension)