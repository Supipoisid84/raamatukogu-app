import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
import subprocess
import sys

DB_NIMI = "books.db"


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


class RaamatuteGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Raamatukogu")
        self.root.geometry("1100x600")

        self.otsi_var = tk.StringVar()

        # Ülemine riba
        top = tk.Frame(root)
        top.pack(fill="x", padx=10, pady=10)

        tk.Label(top, text="Otsi:").pack(side="left")

        entry = tk.Entry(top, textvariable=self.otsi_var, width=40)
        entry.pack(side="left", padx=5)
        entry.bind("<KeyRelease>", lambda e: self.kuva_andmed())

        tk.Button(top, text="Näita kõiki", command=self.tyhjenda).pack(side="left", padx=5)
        tk.Button(top, text="Muuda valitud", command=self.muuda_valitud).pack(side="left", padx=5)
        tk.Button(top, text="Kustuta valitud", command=self.kustuta_valitud, bg="tomato").pack(side="left", padx=5)

        tk.Button(
            top,
            text="Lisa uus raamat",
            command=self.ava_lisa_fail,
            bg="lightgreen"
        ).pack(side="right")

        # Tabeli raam
        frame = tk.Frame(root)
        frame.pack(fill="both", expand=True, padx=10, pady=10)

        cols = ("id", "pealkiri", "autor", "zanr", "ilmumisaasta", "isbn", "kogus", "saadaval")

        self.tree = ttk.Treeview(frame, columns=cols, show="headings")

        self.tree.heading("id", text="ID")
        self.tree.heading("pealkiri", text="Pealkiri")
        self.tree.heading("autor", text="Autor")
        self.tree.heading("zanr", text="Žanr")
        self.tree.heading("ilmumisaasta", text="Ilmumisaasta")
        self.tree.heading("isbn", text="ISBN")
        self.tree.heading("kogus", text="Kogus")
        self.tree.heading("saadaval", text="Saadaval")

        self.tree.column("id", width=60, anchor="center")
        self.tree.column("pealkiri", width=220)
        self.tree.column("autor", width=180)
        self.tree.column("zanr", width=120)
        self.tree.column("ilmumisaasta", width=100, anchor="center")
        self.tree.column("isbn", width=150)
        self.tree.column("kogus", width=80, anchor="center")
        self.tree.column("saadaval", width=90, anchor="center")

        y_scroll = ttk.Scrollbar(frame, orient="vertical", command=self.tree.yview)
        x_scroll = ttk.Scrollbar(frame, orient="horizontal", command=self.tree.xview)

        self.tree.configure(yscrollcommand=y_scroll.set, xscrollcommand=x_scroll.set)

        self.tree.grid(row=0, column=0, sticky="nsew")
        y_scroll.grid(row=0, column=1, sticky="ns")
        x_scroll.grid(row=1, column=0, sticky="ew")

        frame.rowconfigure(0, weight=1)
        frame.columnconfigure(0, weight=1)

        self.kuva_andmed()

    def kuva_andmed(self):
        for r in self.tree.get_children():
            self.tree.delete(r)

        otsing = self.otsi_var.get().strip()

        try:
            conn = sqlite3.connect(DB_NIMI)
            cursor = conn.cursor()

            if otsing:
                cursor.execute("""
                    SELECT id, pealkiri, autor, zanr, ilmumisaasta, isbn, kogus, saadaval
                    FROM raamatud
                    WHERE pealkiri LIKE ?
                       OR autor LIKE ?
                       OR zanr LIKE ?
                       OR isbn LIKE ?
                    ORDER BY id
                """, (f"%{otsing}%", f"%{otsing}%", f"%{otsing}%", f"%{otsing}%"))
            else:
                cursor.execute("""
                    SELECT id, pealkiri, autor, zanr, ilmumisaasta, isbn, kogus, saadaval
                    FROM raamatud
                    ORDER BY id
                """)

            for row in cursor.fetchall():
                self.tree.insert("", "end", values=row)

            conn.close()

        except Exception as e:
            messagebox.showerror("Viga", f"Andmete kuvamine ebaõnnestus:\n{e}")

    def tyhjenda(self):
        self.otsi_var.set("")
        self.kuva_andmed()

    def ava_lisa_fail(self):
        try:
            subprocess.Popen([sys.executable, "lisa_raamat.py"])
        except Exception as e:
            messagebox.showerror("Viga", f"Ei saanud faili avada:\n{e}")

    def muuda_valitud(self):
        valik = self.tree.selection()

        if not valik:
            messagebox.showwarning("Hoiatus", "Palun vali rida, mida muuta.")
            return

        andmed = self.tree.item(valik[0], "values")

        muutmise_aken = tk.Toplevel(self.root)
        muutmise_aken.title("Muuda raamatut")
        muutmise_aken.geometry("400x420")
        muutmise_aken.resizable(False, False)

        raamatu_id = andmed[0]

        tk.Label(muutmise_aken, text="Pealkiri:").pack(pady=(10, 0))
        entry_pealkiri = tk.Entry(muutmise_aken, width=40)
        entry_pealkiri.pack()
        entry_pealkiri.insert(0, andmed[1])

        tk.Label(muutmise_aken, text="Autor:").pack(pady=(10, 0))
        entry_autor = tk.Entry(muutmise_aken, width=40)
        entry_autor.pack()
        entry_autor.insert(0, andmed[2])

        tk.Label(muutmise_aken, text="Žanr:").pack(pady=(10, 0))
        entry_zanr = tk.Entry(muutmise_aken, width=40)
        entry_zanr.pack()
        entry_zanr.insert(0, andmed[3])

        tk.Label(muutmise_aken, text="Ilmumisaasta:").pack(pady=(10, 0))
        entry_aasta = tk.Entry(muutmise_aken, width=40)
        entry_aasta.pack()
        entry_aasta.insert(0, andmed[4])

        tk.Label(muutmise_aken, text="ISBN:").pack(pady=(10, 0))
        entry_isbn = tk.Entry(muutmise_aken, width=40)
        entry_isbn.pack()
        entry_isbn.insert(0, andmed[5])

        tk.Label(muutmise_aken, text="Kogus:").pack(pady=(10, 0))
        entry_kogus = tk.Entry(muutmise_aken, width=40)
        entry_kogus.pack()
        entry_kogus.insert(0, andmed[6])

        tk.Label(muutmise_aken, text="Saadaval:").pack(pady=(10, 0))
        entry_saadaval = tk.Entry(muutmise_aken, width=40)
        entry_saadaval.pack()
        entry_saadaval.insert(0, andmed[7])

        def salvesta_muudatused():
            pealkiri = entry_pealkiri.get().strip()
            autor = entry_autor.get().strip()
            zanr = entry_zanr.get().strip()
            ilmumisaasta = entry_aasta.get().strip()
            isbn = entry_isbn.get().strip()
            kogus = entry_kogus.get().strip()
            saadaval = entry_saadaval.get().strip()

            if not pealkiri or not autor or not zanr or not ilmumisaasta or not isbn or not kogus or not saadaval:
                messagebox.showerror("Viga", "Kõik väljad on kohustuslikud!")
                return

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
                    UPDATE raamatud
                    SET pealkiri = ?, autor = ?, zanr = ?, ilmumisaasta = ?, isbn = ?, kogus = ?, saadaval = ?
                    WHERE id = ?
                """, (pealkiri, autor, zanr, ilmumisaasta, isbn, kogus, saadaval, raamatu_id))

                conn.commit()
                conn.close()

                self.kuva_andmed()
                messagebox.showinfo("Edu", "Andmete muutmine oli edukas.")
                muutmise_aken.destroy()

            except sqlite3.IntegrityError:
                messagebox.showerror("Viga", "Sellise ISBN-iga raamat on juba olemas!")
            except Exception as e:
                messagebox.showerror("Viga", f"Andmete muutmine ebaõnnestus:\n{e}")

        tk.Button(
            muutmise_aken,
            text="Salvesta muudatused",
            command=salvesta_muudatused,
            bg="lightblue"
        ).pack(pady=15)

    def kustuta_valitud(self):
        valik = self.tree.selection()

        if not valik:
            messagebox.showwarning("Hoiatus", "Palun vali rida, mida kustutada.")
            return

        andmed = self.tree.item(valik[0], "values")
        raamatu_id = andmed[0]
        pealkiri = andmed[1]

        kinnita = messagebox.askyesno(
            "Kinnitamine",
            f"Kas soovid kindlasti kustutada raamatu:\n\n{pealkiri}?"
        )

        if not kinnita:
            return

        try:
            conn = sqlite3.connect(DB_NIMI)
            cursor = conn.cursor()

            cursor.execute("DELETE FROM raamatud WHERE id = ?", (raamatu_id,))

            conn.commit()
            conn.close()

            self.kuva_andmed()
            messagebox.showinfo("Edu", "Kustutamine oli edukas.")

        except Exception as e:
            messagebox.showerror("Viga", f"Kustutamine ebaõnnestus:\n{e}")


if __name__ == "__main__":
    loo_andmebaas()
    root = tk.Tk()
    app = RaamatuteGUI(root)
    root.mainloop()