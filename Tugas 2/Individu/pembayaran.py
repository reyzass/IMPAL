# Fungsi untuk menampilkan total harga tiket
def show_total_price(tickets):
    price_per_ticket = 50  # harga per tiket
    total_price = price_per_ticket * tickets
    return total_price

# Fungsi untuk memilih metode pembayaran
def select_payment_method():
    print("Pilih Metode Pembayaran:")
    print("1. Kartu Kredit")
    print("2. Transfer Bank")
    print("3. Dompet Digital")
    payment_choice = input("Masukkan pilihan (1/2/3): ")
    
    if payment_choice == '1':
        payment_method = "Kartu Kredit"
    elif payment_choice == '2':
        payment_method = "Transfer Bank"
    elif payment_choice == '3':
        payment_method = "Dompet Digital"
    else:
        payment_method = None
        print("Pilihan tidak valid.")
    
    return payment_method

# Fungsi untuk memproses pembayaran
def process_payment(payment_method, total_price):
    if payment_method == "Kartu Kredit":
        card_number = input("Masukkan nomor kartu kredit: ")
        expiration_date = input("Masukkan tanggal kedaluwarsa (MM/YY): ")
        cvv = input("Masukkan CVV: ")
        print(f"Pembayaran sebesar ${total_price} berhasil menggunakan Kartu Kredit.")
    
    elif payment_method == "Transfer Bank":
        bank_account = input("Masukkan nomor rekening bank: ")
        print(f"Pembayaran sebesar ${total_price} berhasil melalui Transfer Bank.")
    
    elif payment_method == "Dompet Digital":
        phone_number = input("Masukkan nomor ponsel terdaftar: ")
        print(f"Pembayaran sebesar ${total_price} berhasil menggunakan Dompet Digital.")
    else:
        print("Metode pembayaran tidak valid.")

# Fungsi utama
def main():
    print("Selamat datang di sistem pembelian tiket!")
    tickets = int(input("Masukkan jumlah tiket yang ingin dibeli: "))
    
    # Tampilkan total harga tiket
    total_price = show_total_price(tickets)
    print(f"Total harga tiket: ${total_price}")
    
    # Pilih metode pembayaran
    payment_method = select_payment_method()
    
    # Jika metode pembayaran valid, proses pembayaran
    if payment_method:
        process_payment(payment_method, total_price)
    else:
        print("Pembayaran gagal, coba lagi.")

# Menjalankan program utama
if __name__ == "__main__":
    main()
