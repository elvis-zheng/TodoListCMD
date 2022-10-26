# Variable
listKegiatan = []

# Function
def tampilkanKegiatan():
    print()
    if(listKegiatan): # Cek apakah listKegiatan memiliki isi
        print("List Kegiatan")
        print("-------------")
        for i in range(len(listKegiatan)):
            print(i + 1, end=". ") # Untuk print nomor, misalnya: 1. 2. 3.
            print(listKegiatan[i])
    else:
        print("================================")
        print("| Anda tidak memiliki kegiatan |")
        print("================================")

def tambahKegiatan(namaKegiatan):
    listKegiatan.append(namaKegiatan)

def hapusKegiatan(nomorKegiatan):
    if(nomorKegiatan <= len(listKegiatan)): # Cek apakah nomor yang diinput user ada di listKegiatan
        del listKegiatan[nomorKegiatan - 1] # -1 supaya kegiatan yang hapus sesuai dengan nomor kegiatan yang di input
    else:
        # Print Error
        print("================================================")
        print("| Nomor kegiatan yang anda berikan tidak valid |")
        print("================================================")

while True:
    tampilkanKegiatan() # Print Isi List dari "listKegiatan"
    print("\nOpsi pilihan program TodoList :","\n1. Tambahkan kegiatan", "\n2. Hapus kegiatan") # Print Opsi yang dapat user pilih
    opsiTerpilih =  input("\nSilahkan masukkan pilihan anda : ")
    
    if opsiTerpilih == "1":
        namaKegiatan = input("Masukkan kegiatan anda : ")
        tambahKegiatan(namaKegiatan)

    elif opsiTerpilih == "2":
        nomorKegiatan = int(input("Masukkan nomor kegiatan yang akan dihapus : "))
        hapusKegiatan(nomorKegiatan)

    else:
        # Print Error
        print("============================")
        print("| Pilihan anda tidak valid |")
        print("============================")
    
