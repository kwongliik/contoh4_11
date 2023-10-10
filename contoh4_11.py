import random

# user-defined function untuk simulasi menimbang batu
def bilangan_batu(x):
    hasil= random.randint(0, x) # built-in function: randint()
    return hasil

# Membuat panggilan function
# Hantar nilai bilangan batu yang digunakan ke dalam bilangan_batu()
def main():
    terus = "Y"
    while terus == "Y":
        hasil_timbang = bilangan_batu(5)
        print(f"Hasil timbangan anda ialah {hasil_timbang} batu.")

        # Menangkap batu. Membuat panggilan fungsi
        # Hantar hasil timbangan ke dalam bilangan_batu()
        if hasil_timbang > 0:
            tangkap = bilangan_batu(hasil_timbang)
            print(f"Hasil tangkapan anda ialah {tangkap} batu.")
        terus = input("\nTeruskan [Y] atau berhenti [T]? Tekan [Y|T] ")
        print("")

if __name__ == "__main__":
    main()        
