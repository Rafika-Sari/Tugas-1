# SOAL
# Buatlah sebuah program untuk menentukan apakah seorang siswa lulus ujian atau tidak.
# Siswa dinyatakan lulus apabila nilai ujian teori dan ujian praktek minimal 70
# Program menerima input berupa nilai ujian teori dan nilai ujian praktek
# Nilai ujian dapat berupa bilangan desimal
# Jika nilai ujian teori dan praktek minimal 70, maka akan menampilkan tulisan "Selamat, anda lulus!"
# Jika nilai ujian teori minimal 70 dan praktek kurang dari 70, maka akan menampilkan tulisan "Anda harus mengulang ujian praktek!"
# Jika nilai ujian teori kurang dari 70 dan praktek minimal  70, maka akan menampilkan tulisan "Anda harus mengulang ujian teori!"
# Jika nilai ujian teori dan praktek kurang dari  70, maka akan menampilkan tulisan "Anda harus mengulang ujian teori dan praktek!"

nilai_teori = float(input("Masukkan nilai ujian teori: "))
nilai_praktek = float(input("Masukkan nilai ujian praktek: "))
if nilai_teori < 70:
    print("Anda harus mengulang ujian teori")
elif nilai_praktek < 70:
    print("Anda harus mengulang ujian praktek")  
elif nilai_teori <= 70 and nilai_praktek <= 70:
    print("Anda harus mengulang ujian teori dan praktek")
else: 
    #nilai_teori >= 70 and nilai_praktek >= 70:
    print("Selamat, anda lulus !")
    
# Catatan :
# Belum berhasil untuk membuat program menampilkan bila nilai teori & praktek kurang dari 70
