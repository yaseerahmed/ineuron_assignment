def replace(f_name,rem_text,rep_text):
    with open(f_name,'r') as f:
        content = f.read()
        content = content.replace(rem_text,rep_text)
    
    with open(f_name,'w') as f:
        f.write(content)

file_name = "example.txt"
remove_text = input()  #will take input string from console which has to be removed
replace_text = input() #read the replacing text

replace(file_name,remove_text,replace_text)



#Note: In vscode the run file on terminal