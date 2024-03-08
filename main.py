def main():
    book_path = "libri/Frankenstein.txt.txt"
    testo = get_book_text(book_path)
    num_par = get_num_words(testo)
    diz_lettere =  get_letter_count(testo)
    diz_lettere_sort = lettere_da_diz_a_list(diz_lettere)
    
    print(f"<<< Begin report of {book_path} >>>")
    
    print(f"<{num_par} words found in the document>")
    for a in diz_lettere_sort:
        if not a["char"].isalpha():
           continue
        print(f"The {a['char']} caracter was found {a['num']} times")
    
    print("<<< End report >>>")
    
def get_num_words(testo):
    parole = testo.split()
    return len(parole)

def sort_on(diz_lettere):
    return diz_lettere["num"]

def lettere_da_diz_a_list(num_diz_lettere):
   lista =[]
   for l in num_diz_lettere:
      lista.append({"char": l, "num": num_diz_lettere[l]})
   lista.sort(reverse = True, key = sort_on)
   return lista

def get_letter_count(testo):
   conteggio = {} 
   for i in testo:
      lowered_string = i.lower()
      conteggio[lowered_string] = conteggio.get(lowered_string, 0) + 1
   return conteggio

def get_book_text(book_path):
    with open(book_path) as f:
     file_content = f.read()
    return file_content

main()
