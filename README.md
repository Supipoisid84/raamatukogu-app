3. Raamatukogu andmebaas

Kirjeldus: andmebaas haldab raamatukogu lugejate andmeid, raamatute laenutusi ja autorite informatsiooni. See on mõeldud raamatukogudele, et jälgida raamatute liikumist ja lugejate tegevust

Tabelid

    users: sisaldab lugejate infot (eesnimi, perenimi, email, tel, profiilipilt)
    books: raamatud (raamatu id, pealkiri, autor, žanr)
    loans: laenutused (lugeja id, raamatu id, laenutamise kuupäev, tagastamise tähtaeg)
    authors: autorite info (autori nimi, sünniaeg, rahvus)

JOIN ideed

    Ühenda users ja loans, et näha, millised lugejad on milliseid raamatuid laenutanud
    Ühenda books ja authors, et kuvada raamatud koos nende autoritega
    Ühenda users, loans ja books, et kuvada kõik laenutused koos lugejate ja raamatute detailidega

<img width="827" height="399" alt="Kuvatõmmis 2026-05-12 135757" src="https://github.com/user-attachments/assets/e7988bd6-5216-4967-a2a5-6badc07eb9d6" />
    
<img width="1053" height="477" alt="Kuvatõmmis 2026-05-12 135545" src="https://github.com/user-attachments/assets/e77e7aa0-d247-42d4-84de-5c7e98ba7e96" />
    
<img width="548" height="327" alt="Kuvatõmmis 2026-05-19 092345" src="https://github.com/user-attachments/assets/10995c53-d933-4df8-87f2-58feb06b812d" />
    
<img width="652" height="570" alt="Kuvatõmmis 2026-05-19 091841" src="https://github.com/user-attachments/assets/94a89438-0c37-4c27-9950-a80e631a63a0" />
    
<img width="1097" height="441" alt="Kuvatõmmis 2026-05-19 091745" src="https://github.com/user-attachments/assets/5d759292-d303-4bcf-9e70-09c4b49f3d6d" />
    
<img width="672" height="408" alt="Kuvatõmmis 2026-05-19 090942" src="https://github.com/user-attachments/assets/58ca7397-bac0-4fb3-b712-853c9deb6682" />
    
<img width="1084" height="553" alt="Kuvatõmmis 2026-05-12 140142" src="https://github.com/user-attachments/assets/128553c2-b012-47b9-a627-6b54aa8fc475" />

3. Raamatukogu andmebaas

    Kui vastuseid on liiga palju, siis LIMIT 10 näiteks.
    Leia kõige laenutatum raamat ja selle autor.
   
<img width="370" height="265" alt="Kuvatõmmis 2026-05-19 094346" src="https://github.com/user-attachments/assets/1bb351c8-52eb-4c40-ab92-1473c2716ba3" />

    Loe kokku laenutused iga raamatu kohta, kasutades COUNT() funktsiooni.

 <img width="372" height="287" alt="Kuvatõmmis 2026-05-19 094356" src="https://github.com/user-attachments/assets/52c8a57c-26a4-4254-80e7-2c878746f7c4" />

    Kasuta GROUP BY raamatu ID järgi, et grupeerida tulemused raamatute kaupa.
    Kasuta alampäringut, et leida kõige populaarsem raamat.

<img width="354" height="306" alt="Kuvatõmmis 2026-05-19 094407" src="https://github.com/user-attachments/assets/87958570-b036-4994-b630-8cec9bab08a9" />

Ülesanne 18

    Lae alla ja paigalda SQLiteStudio
    Ava oma eelnevalt loodud andmebaas
    Teosta vähemalt üks Ülesanne 17 loodud päringutest
    Tee programmiaknast ekraanitõmmis. Näha peab olema andmebaas, tabelid, päring ja tulemus
    
<img width="494" height="376" alt="Kuvatõmmis 2026-05-19 105116" src="https://github.com/user-attachments/assets/e150085b-232d-4b96-b466-b41ed1f11a2d" />

