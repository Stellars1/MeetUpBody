# MeetUp Buddy API Dokümantasyonu

## Kullanıcı İşlemleri

### Kayıt Ol
- **URL**: `/users/register/`
- **Method**: `POST`
- **Body**:
  ```json
  {
    "username": "string",
    "email": "string",
    "password1": "string",
    "password2": "string"
  }
  ```

### Giriş Yap
- **URL**: `/users/login/`
- **Method**: `POST`
- **Body**:
  ```json
  {
    "username": "string",
    "password": "string"
  }
  ```

### Profil Güncelle
- **URL**: `/users/profile/`
- **Method**: `POST`
- **Body**:
  ```json
  {
    "username": "string",
    "email": "string",
    "bio": "string",
    "location": "string",
    "birth_date": "date",
    "interests": [1, 2, 3],
    "profile_picture": "file"
  }
  ```

## Etkinlik İşlemleri

### Etkinlik Listesi
- **URL**: `/events/`
- **Method**: `GET`
- **Query Parameters**:
  - `interest`: İlgi alanı ID'si (opsiyonel)

### Etkinlik Detayı
- **URL**: `/events/<id>/`
- **Method**: `GET`

### Etkinlik Oluştur
- **URL**: `/events/create/`
- **Method**: `POST`
- **Body**:
  ```json
  {
    "title": "string",
    "description": "string",
    "date": "datetime",
    "location": "string",
    "interests": [1, 2, 3],
    "max_participants": "integer"
  }
  ```

### Etkinliğe Katıl
- **URL**: `/events/<id>/join/`
- **Method**: `POST`

### Etkinlikten Ayrıl
- **URL**: `/events/<id>/leave/`
- **Method**: `POST` 