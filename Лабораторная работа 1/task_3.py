# TODO Найдите количество книг, которое можно разместить на дискете
pages_per_book = 100
lines_per_page = 50
chars_per_line = 25
bytes_per_char = 4

volume_of_one_book = pages_per_book * lines_per_page * chars_per_line * bytes_per_char
disk_volume_mb = 1.44
disk_volume_bytes = int(disk_volume_mb * 1024 * 1024)
number_of_books = disk_volume_bytes // volume_of_one_book

print("Количество книг, помещающихся на дискету:", number_of_books)
