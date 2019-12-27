import string
import requests
def get_synonym(word_file, dict_file):
    wf2 = word_file.split() #creates a list of the words in the first file.
    #gets the word of the first file and matches it with the key of the dictionary.
    #When the maching key is found, the value of the key is put into the string.
    #replaced_file= ' '.join(str(dict_file.get(word)).replace(' ','\n') for word in wf2) #this one prints with newline.
    replaced_file= ' '.join(str(dict_file.get(word)) for word in wf2) #this one prints without newline.
    return replaced_file #print the synonyms from dictionary.

def get_api(word,dict_file):
    url = "http://words.bighugelabs.com/api/2/2bb34bae0ceb17397297649be2270c82/"#api url.
    wf2 = word.split() #Make all of the words in the file into a list.
    outfile = open("wordsandsyn.txt", "a+") #Open input file.
    dict_file = clean_d
    for word in wf2:
        word = word +"/" #append a "/" at the end of the url.
        url2 = url+word #here is the url.
        r = requests.get(url2)
        strip_extra = r.text.split('\n') #Put the words into a list.
        word = word.replace('/','')
        if word not in dict_file.keys():
            outfile.write(":"+word+":")

            for  w in  strip_extra: #writes the synonyms in cache file. if the word is not in cache.
                if "|syn|" in w:
                    if "adverb|" in w:
                        new = w[11:]
                        outfile.write(new+":")
                    elif "adjective|" in w:
                        new = w[14:]
                        outfile.write(new+":")
                    elif "noun|" or "verb|" in w:
                        new = w[9:]
                        outfile.write(new+":")

            outfile.write('\n')    #writes a newline at the end of the synonym string.
    outfile.close()

f1 = open("words.txt", "r+") #Open input file.
f1string = f1.read().casefold().translate(str.maketrans({key: None for key in string.punctuation})).replace('\n',' ') #converts the input file to a string. Ignores case, punctuation and replaces newline.

d = dict()
with open('wordsandsyn.txt') as file1: #This creates a dictionary of the 2nd file.
  d = dict(line.lstrip(":").strip('\n').split(':', 1) for line in file1) #converts file into a dictionary.

clean_d = {key:item.replace(":"," ") for key, item in d.items()} #Cleans the ":" from dictionary values.
print("\n")
print("Original Words: ")
print(f1string+"\n")

cl_dict_file = dict()
dict_file = dict()
dict_list = list()
final_list = list()
with open('wordsandsyn.txt') as file1: #create a new dictionary.
    dict_file = dict(line.lstrip(":").strip('\n').split(':', 1) for line in file1) #converts file into a dictionary.
    dict_list = list(dict_file.values())
    cl_dict_file = {key: item.replace(":"," ") for key, item in dict_file.items()}
    lst = list()
    for i in range(len(dict_list)):
        final_list = (str(dict_list[i]).split(":"))
        lst.append(final_list[0])
    dict_list2 = list(cl_dict_file)
    new_dict = dict()

    for i in range(len(dict_list2)):    #create a dictionary from the two lists.
        new_dict[dict_list2[i]] = lst[i]

f2 = open("words.txt","w+")
get_api(f1string,new_dict) #get words from api.
with open('wordsandsyn.txt') as file1: #create a new dictionary.
    dict_file = dict(line.lstrip(":").strip('\n').split(':', 1) for line in file1) #converts file into a dictionary.
    dict_list = list(dict_file.values())
    cl_dict_file = {key: item.replace(":"," ") for key, item in dict_file.items()}
    lst = list()
    for i in range(len(dict_list)):
        final_list = (str(dict_list[i]).split(":"))
        lst.append(final_list[0])
    dict_list2 = list(cl_dict_file)
    new_dict = dict()

    for i in range(len(dict_list2)):    #create a dictionary from the two lists.
        new_dict[dict_list2[i]] = lst[i]
get_synonym(f1string,new_dict)
print("Synonyms: ")
print(get_synonym(f1string,new_dict))
print("\n")
f2.write(get_synonym(f1string,new_dict)+"\n")
f2.write("\n")
# #close the files.
f2.close()
f1.close()
file1.close()
