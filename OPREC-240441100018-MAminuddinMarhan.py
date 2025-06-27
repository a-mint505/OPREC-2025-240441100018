produk = {"Laptop": 5500000, "Smartphone": 3000000, "Tablet": 2000000, "Smartwatch": 1500000, "Headphone": 500000}
def cek_penawaran(barang, jumlah):
    harga_total = barang * jumlah
    jumlah_penawaran = int(input("Masukkan harga penawaran anda: "))
    if jumlah_penawaran < harga_total * 0.8:
        print("Penawaran ditolak. Harga asli digunakan.")
        return barang
    else:
        return jumlah_penawaran


def hitung_diskon(barang, jumlah):
    harga_total = barang * jumlah
    if harga_total > 10000000:
        return harga_total * 0.9
    elif harga_total > 5000000:
        return harga_total * 0.95
    else:
        return harga_total
    
def diskon(barang, jumlah):
    harga_total = barang * jumlah
    if harga_total > 10000000:
        return "10%"
    elif harga_total > 5000000:
        return "5%"
    else:
        return harga_total

def transaksi():
    while True:
        try:
            nama = str(input("Masukkan nama pembeli: "))
            umur = int(input("Masukkan umur pembeli: "))
            member = str(input("Apakah pelanggan member (ya/tidak): "))
            print("\n===PILIH GADGET YANG INGIN DIBELI===")
            print("1. Laptop (Rp. 5500000)")
            print("2. Smartphone (Rp.3000000)")
            print("3. Tablet (Rp. 2000000)")
            print("4. Smartwatch (Rp. 1500000)")
            print("5. Headphone (Rp. 500000)")
            gadget = str(input("Gadget yang ingin dibeli: \n"))
            def cek_produk(gadget):
                if gadget == "1":
                    return produk["Laptop"]
                elif gadget == "2":
                    return produk["Smartphone"]
                elif gadget == "3":
                    return produk["Tablet"]
                elif gadget == "4":
                    return produk["Smartwatch"]
                elif gadget == "5":
                    return produk["Headphone"]
                else:
                    print("Input tidak valid")
                    return False
            cek_produk(gadget)
            jumlah = int(input("Jumlah unit gadget yang dibeli: "))
            if umur < 17 and hitung_diskon(cek_produk, jumlah) > 3000000:
                print("Maaf, anda belum cukup umur untuk membeli produk ini.")
                break
            penawaran = str(input("Apakah ingin melakukan penawaran? (ya/tidak): "))
            if member == "ya" and penawaran != "ya":
                total_pembelian = cek_penawaran(cek_produk(gadget), jumlah)
                print("\n=== STRUK PEMBELIAN ===")
                print(f"Nama Pembeli: {nama}")
                print(f"Produk Dibeli: {cek_produk(gadget)}")
                print(f"Jumlah Unit: {jumlah}")
                print(f"Harga/Unit: Rp. {cek_produk(gadget)}")
                print(f"Subtotal: Rp. {total_pembelian}")
                print(f"Diskon: Rp. {diskon(cek_produk(gadget), jumlah)}")
                print(f"Total Akhir: Rp. {hitung_diskon(cek_produk(gadget), jumlah)}")
            elif member == "ya" and penawaran == "ya":
                print("\n=== STRUK PEMBELIAN ===")
                print(f"Nama Pembeli: {nama}")
                print(f"Produk Dibeli: {cek_produk(gadget)}")
                print(f"Jumlah Unit: {jumlah}")
                print(f"Harga/Unit: Rp. {cek_produk(gadget)}")
                print(f"Subtotal: Rp. {total_pembelian}")
                print(f"Diskon: Rp. {diskon(cek_produk(gadget), jumlah)}")
                print(f"Total Akhir: Rp. {hitung_diskon(cek_produk(gadget), jumlah) * cek_penawaran(gadget, jumlah) / 2}")
            else:
                total_pembelian = cek_produk(gadget) * jumlah
                print(f"Total Akhir: Rp. {total_pembelian}")
            input = input("apakah ingin melakukan pembelian lagi: ")
            if input != "ya":
                break
            
        except ValueError:
            print("Input tidak valid.")

if __name__ == "__main__":
    transaksi()