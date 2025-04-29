# MeetUp Buddy – Ortak Etkinlik Planlayıcı

Bu proje, insanların ilgi alanlarına göre ortak etkinlikler oluşturup buluşmalar düzenleyebilecekleri bir platform geliştirmek amacıyla hazırlanmıştır.

## Özellikler

- Kullanıcı kaydı ve girişi
- Profil yönetimi
- İlgi alanları seçimi
- Etkinlik oluşturma ve katılım
- Etkinlik filtreleme
- Responsive tasarım

## Teknolojiler

- Frontend: HTML/CSS, JavaScript, Bootstrap 5
- Backend: Django
- Veritabanı: PostgreSQL
- Deployment: Docker
- Versiyon Kontrol: Git + GitHub

## Kurulum

1. Projeyi klonlayın:
```bash
git clone https://github.com/yourusername/meetup-buddy.git
cd meetup-buddy
```

2. Virtual environment oluşturun ve aktif edin:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate  # Windows
```

3. Bağımlılıkları yükleyin:
```bash
pip install -r requirements.txt
```

4. Environment değişkenlerini ayarlayın:
```bash
cp config/.env.example config/.env
# .env dosyasını düzenleyin
```

5. Veritabanı migrasyonlarını uygulayın:
```bash
python manage.py migrate
```

6. Süper kullanıcı oluşturun:
```bash
python manage.py createsuperuser
```

7. Geliştirme sunucusunu başlatın:
```bash
python manage.py runserver
```

## Docker ile Kurulum

1. Docker ve Docker Compose'u yükleyin

2. Projeyi başlatın:
```bash
docker-compose up -d
```

3. Migrasyonları uygulayın:
```bash
docker-compose exec web python manage.py migrate
```

4. Süper kullanıcı oluşturun:
```bash
docker-compose exec web python manage.py createsuperuser
```

## Test

Testleri çalıştırmak için:
```bash
python manage.py test
```

## Katkıda Bulunma

1. Fork'layın
2. Feature branch oluşturun (`git checkout -b feature/amazing-feature`)
3. Değişikliklerinizi commit edin (`git commit -m 'Add some amazing feature'`)
4. Branch'inizi push edin (`git push origin feature/amazing-feature`)
5. Pull Request oluşturun

## Lisans

Bu proje MIT lisansı altında lisanslanmıştır. Detaylar için [LICENSE](LICENSE) dosyasına bakın.

## İletişim

Proje Sahibi - [@yourusername](https://github.com/yourusername)

Proje Linki: [https://github.com/yourusername/meetup-buddy](https://github.com/yourusername/meetup-buddy)
