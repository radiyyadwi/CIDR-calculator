# Tugas Kecil CIDR-Calculator

Membuat calculator subnet dan host

## Petunjuk penggunaan program

Program dapat dijalankan dengan menjalankan command "make run" pada folder dimana file "client.py" berada. Program tidak perlu dicompile terlebih dahulu karena menggunakan bahasa python.

## Penjelasan singkat pengerjaan setiap phase 

Pada phase 1, fungsi getValidSubnet(host) mendapatkan subnet yang valid untuk host tertentu. Oleh karena itu saya mengambil 24 bit pada host dengan melakukan split lalu menuliskan kembali dan menambahkan 0 dilanjutkan dengan "/24" sebagai tanda bahwa terdapat 24 bit yang sama

Pada phase 2, fungsi countHosts(subnet) mendapatkan jumlah host yang dapat dipenuhi oleh subnet. Jumlah host yang dapat dipenuhi ialah 2^(32-(bit yang sama)). Untuk mendapatkan nilai bit yang sama saya menggunakan split dari parameter subnet.

Pada phase 3, fungsi isSubnetValid(subnet, host) mengembalikan kondisi apakah subnet valid untuk host yang ada. Untuk melakukan pengecekan, pada awalnya saya melakukan split dari subnet maupun host lalu memperoleh lalu dengan looping membandingkan nilai dari setiap split bila sama maka skore bertambah 8, jika tidak maka akan dilakukan pengecekan setiap bit nya. "T" akan di return bila subnet valid, "F" akan di return bila subnet tidak valid.