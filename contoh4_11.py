........ random

# user-defined function bernama bilangan_batu() untuk simulasi menimbang batu
def ...............(x):
    hasil= random.randint(0, .....) # built-in function: randint()
    return ............

# Membuat panggilan function
# Hantar nilai bilangan batu yang digunakan ke dalam bilangan_batu()
def main():
    terus = "Y"
    while terus == "Y":
        hasil_timbang = .............(4)
        print(f"Hasil timbangan anda ialah {...............} batu.")

        # Menangkap batu. Membuat panggilan fungsi
        # Hantar hasil timbangan ke dalam bilangan_batu()
        if hasil_timbang > 0:
            tangkap = bilangan_batu(.................)
            print(f"Hasil tangkapan anda ialah {..............} batu.")
        terus = input("\nTeruskan [Y] atau berhenti [T]? Tekan [Y|T] ")
        print("")

###########################
# Jangan ubah kod di bawah!
###########################
if __name__ == "__main__":
    main()        
