# 🎯 GitClone - Mudahnya Clone Repository GitHub!

GitClone adalah tools Python interaktif yang memungkinkan Anda mencari, melihat, dan mengkloning repository GitHub dengan tampilan terminal yang menarik dan pengalaman yang lebih menyenangkan! 🚀

---

## ✨ Fitur Unggulan
✅ Tampilan banner ASCII art "GitClone" yang keren!  
✅ Dapatkan informasi pengguna GitHub, termasuk jumlah followers, following, dan total repository.  
✅ Lihat daftar repository pengguna dalam tampilan yang rapi.  
✅ Clone repository favorit Anda dengan satu perintah!  
✅ Nikmati musik latar belakang yang bisa Anda ganti sesuai selera. 🎶  

---

## ⚙️ Instalasi
Pastikan Python dan Git sudah terinstal di perangkat Anda. Selanjutnya, pasang dependensi dengan menjalankan perintah berikut:

```sh
pip install requests termcolor pyfiglet pygame
```

Jika Git belum terinstal, Anda bisa mengunduhnya di [git-scm.com](https://git-scm.com/).

---

## 🚀 Cara Menggunakan
1️⃣ Jalankan skrip dengan perintah berikut:
   ```sh
   python GitClone.py
   ```
2️⃣ Masukkan username GitHub yang ingin Anda lihat.  
3️⃣ Pilih repository yang ingin dikloning dengan mengetikkan nama dari daftar yang tersedia.  
4️⃣ Repository akan dikloning ke folder lokal Anda secara otomatis. 🎉  

---

## 🎵 Kustomisasi Musik
GitClone hadir dengan musik latar yang bisa Anda ubah sesuai selera! 🎼

Untuk mengganti musik:
1️⃣ Pastikan file musik dalam format `.mp3`.  
2️⃣ Pindahkan file musik pilihan Anda ke dalam direktori yang sama dengan `gitclone.py`.  
3️⃣ Edit baris berikut dalam kode:
   ```python
   pygame.mixer.music.load("whoa.mp3")
   ```
   Ganti `whoa.mp3` dengan nama file musik pilihan Anda, misalnya:
   ```python
   pygame.mixer.music.load("lagu_kesukaan.mp3")
   ```
4️⃣ Jalankan kembali script `gitclone.py`, dan musik latar baru akan dimainkan otomatis.  

---

## 📌 Catatan Penting
🔹 Tools ini hanya digunakan untuk mengkloning repository publik.  
🔹 Anda bebas melakukan forking atau modifikasi ulang kode ini sesuai kebutuhan.  
🔹 Gunakan dengan bijak dan jangan melanggar kebijakan GitHub! 😉  

---

## 💡 Kontribusi
Kami membuka kesempatan bagi siapa pun untuk berkontribusi! Jika Anda punya ide atau ingin menambahkan fitur baru, silakan buat pull request atau diskusi di repository.  

---

## 📜 Lisensi
GitClone adalah proyek open-source dan bebas untuk digunakan serta dimodifikasi sesuai kebutuhan Anda.  

**👨‍💻 Developer:**  [Dekurity](https://github.com/Dekurity) 
🎉 Terima kasih telah menggunakan GitClone! Jangan lupa berbagi jika bermanfaat! 😃

