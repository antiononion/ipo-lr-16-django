1. Статические файлы в Django
CSS, JS, изображения — всё что не меняется динамически. Используются для оформления сайта.

2. Настройка STATIC в settings.py
```python
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
```

3. Тег подключения статических файлов
```html
{% load static %}
<link rel="stylesheet" href="{% static 'css/style.css' %}">
```

4. Наследование шаблонов
```html
<!-- base.html -->
{% block content %}{% endblock %}

<!-- child.html -->
{% extends "base.html" %}
{% block content %}текст{% endblock %}
```

5. Подключение Bootstrap 5
```html
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
```

6. Bootstrap Grid — 12 колонок
```html
<div class="row">
  <div class="col-6">половина</div>
  <div class="col-6">половина</div>
</div>
```
Сумма колонок в строке = 12.

7. Адаптивные карточки товаров
```html
<div class="row row-cols-1 row-cols-md-3 g-4">
  <div class="col">
    <div class="card h-100">...</div>
  </div>
</div>
```

8. Fetch API vs XMLHttpRequest
Fetch — современный, основан на Promise, код чище. XMLHttpRequest — старый, колбэки, многословный.

9. GET-запрос через Fetch
```javascript
fetch('/api/products/')
  .then(res => res.json())
  .then(data => console.log(data))
```

10. CSRF-токен в POST-запросе
```javascript
fetch('/api/order/', {
  method: 'POST',
  headers: {
    'X-CSRFToken': document.cookie.match(/csrftoken=([^;]+)/)[1],
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({data: 'value'})
})
```

11. Динамическое создание HTML из API
```javascript
fetch('/api/products/')
  .then(res => res.json())
  .then(data => {
    data.forEach(p => {
      document.getElementById('list').innerHTML += `<div>${p.title}</div>`
    })
  })
```

12. Адаптивная вёрстка и медиа-запросы Bootstrap
- `col-sm-` — от 576px
- `col-md-` — от 768px
- `col-lg-` — от 992px
- `col-xl-` — от 1200px

13. Пагинация через Paginator
```python
from django.core.paginator import Paginator
paginator = Paginator(products, 10)  # 10 на страницу
page = paginator.get_page(request.GET.get('page'))
```

14. Спиннер загрузки
```javascript
document.getElementById('spinner').style.display = 'block'
fetch('/api/products/')
  .then(res => res.json())
  .then(data => {
    document.getElementById('spinner').style.display = 'none'
  })
```

15. Обработка ошибок Fetch
```javascript
fetch('/api/products/')
  .then(res => {
    if (!res.ok) throw new Error('Ошибка ' + res.status)
    return res.json()
  })
  .catch(err => console.error(err))
```