🔹 Bước 0: Kiểm tra đã cài Git chưa

Mở Terminal / Command Prompt và chạy:

git --version


Nếu hiện phiên bản (vd: git version 2.43.0) → OK

Nếu báo lỗi → cần cài Git trước: https://git-scm.com

### Chạy demo

## Window: Mở Terminal / Command Prompt và chạy: ##
git clone https://github.com/nardouhn/pet_hopital.git

cd pet_hopital

git branch -a

git checkout frontend

git pull

🎯 Sau khi clone xong 

npm install

npm run dev

### MacOS
git --version

cd ~
mkdir Projects

cd Projects

git clone https://github.com/nardouhn/pet_hopital.git

cd pet_hopital

git branch -a

git checkout frontend

git pull origin frontend

cd frontend

npm install

npm run dev
