import sqlite3
import tkinter as tk
from tkinter import messagebox


DB_NIMI = "books.db"


# Andmebaasi loomine
def loo_andmebaas():
    conn = sqlite3.connect(DB_NIMI)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS raamatud (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        pealkiri TEXT NOT NULL,
        autor TEXT NOT NULL,
        zanr TEXT NOT NULL,
        ilmumisaasta INTEGER NOT NULL,
        isbn TEXT NOT NULL UNIQUE,
        kogus INTEGER NOT NULL,
        saadaval INTEGER NOT NULL
    )
    """)

    conn.commit()
    conn.close()


# Andmete lisamine
def lisa_raamat():
    pealkiri = entry_pealkiri.get().strip()
    autor = entry_autor.get().strip()
    zanr = entry_zanr.get().strip()
    ilmumisaasta = entry_aasta.get().strip()
    isbn = entry_isbn.get().strip()
    kogus = entry_kogus.get().strip()
    saadaval = entry_saadaval.get().strip()

    # Kohustuslike väljade kontroll
    if not pealkiri or not autor or not zanr or not ilmumisaasta or not isbn or not kogus or not saadaval:
        messagebox.showerror("Viga", "Kõik väljad on kohustuslikud!")
        return

    # Arvuliste väljade kontroll
    try:
        ilmumisaasta = int(ilmumisaasta)
        kogus = int(kogus)
        saadaval = int(saadaval)
    except ValueError:
        messagebox.showerror("Viga", "Ilmumisaasta, kogus ja saadaval peavad olema arvud!")
        return

    try:
        conn = sqlite3.connect(DB_NIMI)
        cursor = conn.cursor()

        cursor.execute("""
        INSERT INTO raamatud (pealkiri, autor, zanr, ilmumisaasta, isbn, kogus, saadaval)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (pealkiri, autor, zanr, ilmumisaasta, isbn, kogus, saadaval))

        conn.commit()
        conn.close()

        messagebox.showinfo("Edu", "Raamat lisati edukalt!")

        # Tühjenda väljad
        entry_pealkiri.delete(0, tk.END)
        entry_autor.delete(0, tk.END)
        entry_zanr.delete(0, tk.END)
        entry_aasta.delete(0, tk.END)
        entry_isbn.delete(0, tk.END)
        entry_kogus.delete(0, tk.END)
        entry_saadaval.delete(0, tk.END)

    except sqlite3.IntegrityError:
        messagebox.showerror("Viga", "Sellise ISBN-iga raamat on juba olemas!")
    except Exception as e:
        messagebox.showerror("Viga", f"Andmete lisamine ebaõnnestus!\n{e}")


# Käivita DB loomine
loo_andmebaas()


# GUI
aken = tk.Tk()
aken.title("Raamatukogu haldus")
aken.geometry("400x400")


tk.Label(aken, text="Pealkiri:").pack()
entry_pealkiri = tk.Entry(aken, width=40)
entry_pealkiri.pack()

tk.Label(aken, text="Autor:").pack()
entry_autor = tk.Entry(aken, width=40)
entry_autor.pack()

tk.Label(aken, text="Žanr:").pack()
entry_zanr = tk.Entry(aken, width=40)
entry_zanr.pack()

tk.Label(aken, text="Ilmumisaasta:").pack()
entry_aasta = tk.Entry(aken, width=40)
entry_aasta.pack()

tk.Label(aken, text="ISBN:").pack()
entry_isbn = tk.Entry(aken, width=40)
entry_isbn.pack()

tk.Label(aken, text="Kogus:").pack()
entry_kogus = tk.Entry(aken, width=40)
entry_kogus.pack()

tk.Label(aken, text="Saadaval:").pack()
entry_saadaval = tk.Entry(aken, width=40)
entry_saadaval.pack(pady=5)

tk.Button(aken, text="Lisa raamat", command=lisa_raamat, bg="lightgreen").pack(pady=10)

aken.mainloop()