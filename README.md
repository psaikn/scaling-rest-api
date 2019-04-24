# Scaling API


Below are the Designed API's:

Adding Books:
--------------------------------------
curl -X POST \
  http://127.0.0.1:5000/books/create \
  -H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoiMTAwMCIsImp0aSI6ImZmYTg3MWUyLWFiYzAtNDYzOS1iMzYxLTE3NTc4MmIxN2FlYyIsImlhdCI6MTU1NjA3NzEwOSwiZXhwIjoxNTU2MDgwNzA5fQ.3qtUlqI_QtipS7XS6fjM1F40nbX-QO1pZKT-k7I6ITY' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -H 'cache-control: no-cache' \
  -H 'content-type: multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW' \
  -F 'bookname=Algorithms and Data Structures' \
  -F 'author=Narasimha Karamunchi' \
  -F published_date=2018-05-03 \
  -F no_of_books=320 \
  -F rack_no=11
  
  Updating Books:
  ----------------------------------------
  curl -X POST \
  http://127.0.0.1:5000/books/update \
  -H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoiMTAwMCIsImp0aSI6ImZmYTg3MWUyLWFiYzAtNDYzOS1iMzYxLTE3NTc4MmIxN2FlYyIsImlhdCI6MTU1NjA3NzEwOSwiZXhwIjoxNTU2MDgwNzA5fQ.3qtUlqI_QtipS7XS6fjM1F40nbX-QO1pZKT-k7I6ITY' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -H 'cache-control: no-cache' \
  -H 'content-type: multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW' \
  -F 'bookname=Algorithms and Data Structures' \
  -F 'author=Narasimha Karamunchi D' \
  -F published_date=2018-05-03 \
  -F no_of_books=320 \
  -F rack_no=11 \
  -F bookid=300
  
  Get All Books:
  ---------------------------------------------
  curl -X GET \
  http://127.0.0.1:5000/books/all \
  -H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoiMTAwMCIsImp0aSI6ImZmYTg3MWUyLWFiYzAtNDYzOS1iMzYxLTE3NTc4MmIxN2FlYyIsImlhdCI6MTU1NjA3NzEwOSwiZXhwIjoxNTU2MDgwNzA5fQ.3qtUlqI_QtipS7XS6fjM1F40nbX-QO1pZKT-k7I6ITY' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -H 'cache-control: no-cache' \
  -H 'content-type: multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW' \
  -F 'bookname=Algorithms and Data Structures' \
  -F 'author=Narasimha Karamunchi D' \
  -F published_date=2018-05-03 \
  -F no_of_books=320 \
  -F rack_no=11 \
  -F bookid=300
  
  Get Single Book:
  -----------------------------------------------------
  curl -X POST \
  http://127.0.0.1:5000/books/getbook \
  -H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoiMTAwMCIsImp0aSI6ImE5YjNkMDA3LThjNGEtNGM4Ni1iZjA4LWM2MmRiMGIxYWI4NCIsImlhdCI6MTU1NjA4MTA5NiwiZXhwIjoxNTU2MDg0Njk2fQ.hKzEdbHMkV9xZWUiYJdRgDSFOVaIpWjgOfXZZHxRxts' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -H 'Postman-Token: 10a626aa-f22b-4134-aed6-781ec68b7b9f' \
  -H 'cache-control: no-cache' \
  -H 'content-type: multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW' \
  -F bookid=3
