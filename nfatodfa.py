import pandas as pd

#Kullanıcdan veriyi al

nfa = {}                                 
n = int(input("State sayısı: "))              #State sayısını girin
t = int(input("Geçiş sayısı : "))             #Geçiş sayısını ekleyin
for i in range(n):  
    state = input("State adı: ")              #State adı girilir
    nfa[state] = {}                           #State yolu oluşturulur
    for j in range(t):
        path = input("Geçiş: ")               #Geçişleri ekleyin örneğin (0,1) g,b,
        print("Geçiş yapılacak path ekleyin{} Bu Path'e gidiyor {} : ".format(state,path))
        reaching_state = [x for x in input().split()]  #Bitiş geçişini ekleyin 
        nfa[state][path] = reaching_state     #Dicionary'de bitiş yolları atanır

print("\nNFA :- \n")
print(nfa)                                            #NFA Yazdır
print("\nNFA Tablosu- ")
nfa_table = pd.DataFrame(nfa)
print(nfa_table.transpose())

print("NFA Final aşamasını giriniz: ")
nfa_final_state = [x for x in input().split()]       #NFA final state girilir             
    
new_states_list = []                                 #DFA'da yeni oluşturulacak stateleri belirler
dfa = {}                                             #DFA'nın ihtiyacı olan çıkış tablosu verilir
keys_list = list(list(nfa.keys())[0])                #NFA'daki tüm durumları ekler DFA'daki oluşturulacak olan tüm durumları içerir
path_list = list(nfa[keys_list[0]].keys())           #Yolları listeler ((0-1),(a,b)) gibi

#DFA tablosundaki değişim işlemi
dfa[keys_list[0]] = {}                               #DFA içerisinde yeni bir dictionary oluşturur
for y in range(t):
    var = "".join(nfa[keys_list[0]][path_list[y]])   #Stateteki her bir eleman için uyumlu bir string oluşturur
    dfa[keys_list[0]][path_list[y]] = var            #DFA tablosundaki durumlar atanır
    if var not in keys_list:                         #Listede yeni bir state oluşutulursa
        new_states_list.append(var)                  #new_states_list listesine ekle
        keys_list.append(var)                        #aynı zamanda tüm durumları içeren keys_list listesine ekle

while len(new_states_list) != 0:                     # new_states_list boş değisle durum 1 olur
    dfa[new_states_list[0]] = {}                     #new_states_list'deki ilk elemanı alır
    for _ in range(len(new_states_list[0])):
        for i in range(len(path_list)):
            temp = []                                #Temp listesi oluşiturur
            for j in range(len(new_states_list[0])):
                temp += nfa[new_states_list[0][j]][path_list[i]]  #Stateleri birlikte olanları alır
            s = ""
            s = s.join(temp)                         #Liste öğrelerinden yeni dizi oluşturma
            if s not in keys_list:                   #Listede yeni bir state oluşutulursa
                new_states_list.append(s)            #new_states_list listesine ekle
                keys_list.append(s)                  #aynı zamanda tüm durumları içeren keys_list listesine ekle
            dfa[new_states_list[0]][path_list[i]] = s  #DFA tablosundaki yeni State'e atama
        
    new_states_list.remove(new_states_list[0])       #new_states_list içindeki ilk öğeyi kaldırma

print("\nDFA :- \n")    
print(dfa)                                           #Yapılan DFA'yı yazdır
print("\nDFA Tablosu :- ")
dfa_table = pd.DataFrame(dfa)
print(dfa_table.transpose())

dfa_states_list = list(dfa.keys())
dfa_final_states = []
for x in dfa_states_list:
    for i in x:
        if i in nfa_final_state:
            dfa_final_states.append(x)
            break
        
print("\nDFA Final Aşamaları ",dfa_final_states)       #DFA'nın final aşamasını yazdır