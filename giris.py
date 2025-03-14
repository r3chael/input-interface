from PyQt5.QtWidgets import *
import sys
import random as rd
import sqlite3



class Pencere(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):

        self.setWindowTitle("Giriş")

        self.kAdi = QLineEdit()
        self.parola = QLineEdit()
        self.parola.setEchoMode(QLineEdit.Password)
        self.giris = QPushButton("Giriş")
        self.kayit = QPushButton("Kayıt Ol")

        h_box1 = QHBoxLayout()

        h_box1.addStretch()
        h_box1.addWidget(self.giris)
        h_box1.addWidget(self.kayit)
        h_box1.addStretch()

        v_box1 = QVBoxLayout()
        
        v_box1.addWidget(QLabel("Kullanıcı Adı:"))
        v_box1.addWidget(self.kAdi)  
        v_box1.addWidget(QLabel("Parola:"))
        v_box1.addWidget(self.parola)
        v_box1.addStretch()
        v_box1.addLayout(h_box1)
        v_box1.addStretch()

        self.kayit.clicked.connect(self.clickkayit)
        self.giris.clicked.connect(self.clickgiris)

        
        self.setLayout(v_box1)
        self.setGeometry(100,100,500,300)

        self.show()

    def clickkayit(self):
        kullanici_adi = self.kAdi.text().strip()
        sifre = self.parola.text().strip()

        if not kullanici_adi or not sifre:
            QMessageBox.warning(self, "Hata", "Kullanıcı adı ve parola boş olamaz!", QMessageBox.Ok)
            return
    
        con = sqlite3.connect("C:/Users/ASUS PC/OneDrive/Masaüstü/python/KullanıcıGirisi/kullanici.db")
        cursor = con.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS kullanicilar(kAd TEXT, password TEXT)")
        con.commit()
        cursor.execute("Insert into kullanicilar Values(?,?)",(kullanici_adi, sifre))
        con.commit()
        con.close()
        print(f"Kayıt Başarılı! Kullanıcı: {kullanici_adi}, Şifre: {sifre}")

        QMessageBox.information(self, "Başarılı", "Kayıt başarılı!", QMessageBox.Ok)
        self.kAdi.clear()
        self.parola.clear()

    def clickgiris(self):
        ad = self.kAdi.text().strip()
        sf = self.parola.text().strip()
        if not ad or not sf:
            QMessageBox.warning(self, "Hata", "Kullanıcı adı ve parola boş olamaz!", QMessageBox.Ok)
            return
    
        con = sqlite3.connect("C:/Users/ASUS PC/OneDrive/Masaüstü/python/KullanıcıGirisi/kullanici.db")
        cursor = con.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS kullanicilar(kAd TEXT, password TEXT)")
        con.commit()
        cursor.execute("SELECT password FROM kullanicilar WHERE kAd = ?", (ad,))
        result = cursor.fetchone()
        con.close()

        if result:
            if result[0] == sf:
                QMessageBox.information(self, "Başarılı", "Giriş başarılı!", QMessageBox.Ok)
                self.kAdi.clear()
                self.parola.clear()
            else:
                QMessageBox.warning(self, "Hata", "Parola yanlış!", QMessageBox.Ok)
                self.parola.clear()
        else:
            QMessageBox.warning(self, "Hata", "Kullanıcı adı bulunamadı!", QMessageBox.Ok)
            self.kAdi.clear()
            self.parola.clear()
        

app = QApplication(sys.argv)
pencere = Pencere()
sys.exit(app.exec_())
