import tkinter as tk
from tkinter import messagebox

class UserCredentials:
    def __init__(self):
        self.username = ""

def authenticate(username, password):
    # Kullanıcı adı ve şifreyi kontrol et (örneğin, basit bir hardcoded kontrol)
    if username == "abc" and password == "123":
        return True
    else:
        return False

def on_login_button_click(credentials_obj):
    entered_username = username_entry.get()
    entered_password = password_entry.get()

    if authenticate(entered_username, entered_password):
        credentials_obj.username = entered_username
        messagebox.showinfo("Başarılı", "Giriş başarılı!")
        root.destroy()  # Ana pencereyi kapat
    else:
        messagebox.showerror("Hata", "Geçersiz kullanıcı adı veya şifre!")

# Ana pencere oluştur
root = tk.Tk()
root.title("Kullanıcı Girişi")

# Kullanıcı adı etiketi ve giriş kutusu
tk.Label(root, text="Kullanıcı Adı:").grid(row=0, column=0)
user_credentials = UserCredentials()  # Kullanıcı adını saklamak için bir nesne oluştur
username_entry = tk.Entry(root)
username_entry.grid(row=0, column=1)

# Şifre etiketi ve giriş kutusu
tk.Label(root, text="Şifre:").grid(row=1, column=0)
password_entry = tk.Entry(root, show="*")
password_entry.grid(row=1, column=1)

# Giriş butonu
login_button = tk.Button(root, text="Giriş", command=lambda: on_login_button_click(user_credentials))
login_button.grid(row=2, column=0, columnspan=2)

# Pencereyi başlat
root.mainloop()

# Root döngüsü bittikten sonra kullanıcı adını kullanabilirsiniz
print("Kullanıcı Adı:", user_credentials.username)
