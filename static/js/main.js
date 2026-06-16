function getCSRFToken() {
  const meta = document.querySelector('meta[name="csrf-token"]');
  if (meta) return meta.getAttribute('content');
  const input = document.querySelector('[name=csrfmiddlewaretoken]');
  return input ? input.value : '';
}

function showSpinner() {
  const overlay = document.getElementById('spinner-overlay');
  if (overlay) overlay.classList.add('active');
}

function hideSpinner() {
  const overlay = document.getElementById('spinner-overlay');
  if (overlay) overlay.classList.remove('active');
}

function showToast(message, type) {
  type = type || 'success';
  const container = document.getElementById('toast-container');
  if (!container) return;
  const toast = document.createElement('div');
  toast.className = 'toast toast-' + type;
  toast.textContent = message;
  container.appendChild(toast);
  setTimeout(() => { toast.remove(); }, 3500);
}

function loadProducts() {
  const container = document.getElementById('product-list');
  if (!container) return;
  showSpinner();
  fetch('/api/products/')
    .then(function(r) { return r.json(); })
    .then(function(products) {
      container.innerHTML = '';
      if (!products.length) {
        container.innerHTML = '<div class="empty-state"><div class="icon">🌿</div><h3>Товары не найдены</h3></div>';
        return;
      }
      products.forEach(function(p) {
        var photoHtml = p.photo
          ? '<img src="' + p.photo + '" class="card-img" alt="' + p.title + '">'
          : '<div style="background:linear-gradient(135deg,var(--moss),var(--fern));height:185px;border-radius:8px 8px 0 0;margin:-20px -20px 16px;display:flex;align-items:center;justify-content:center;font-size:48px;">🏕️</div>';
        var stockHtml = p.numberOF > 0
          ? '<p class="stock-ok">✔ В наличии: ' + p.numberOF + ' шт.</p>'
          : '<p class="stock-out">✖ Нет в наличии</p>';
        var card = document.createElement('div');
        card.className = 'card product-card';
        card.innerHTML = photoHtml
          + '<h3>' + p.title + '</h3>'
          + '<p class="price">' + p.price + ' ₽</p>'
          + stockHtml
          + '<a href="/catalog/' + p.id + '/" class="btn btn-primary">Подробнее</a>';
        container.appendChild(card);
      });
    })
    .catch(function(err) {
      container.innerHTML = '<div class="empty-state"><div class="icon">⚠️</div><h3>Ошибка загрузки</h3><p>Не удалось загрузить товары. Попробуйте позже.</p></div>';
      showToast('Ошибка загрузки товаров', 'error');
    })
    .finally(function() { hideSpinner(); });
}

function addToCart(productId) {
  showSpinner();
  fetch('/api/cart-items/', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'X-CSRFToken': getCSRFToken()
    },
    body: JSON.stringify({ product: productId, number: 1 })
  })
    .then(function(r) {
      if (!r.ok) throw new Error('Ошибка сервера');
      return r.json();
    })
    .then(function() {
      showToast('Товар добавлен в корзину!', 'success');
    })
    .catch(function(err) {
      showToast('Не удалось добавить товар: ' + err.message, 'error');
    })
    .finally(function() { hideSpinner(); });
}

document.addEventListener('DOMContentLoaded', function() {
  var addBtns = document.querySelectorAll('.js-add-to-cart');
  addBtns.forEach(function(btn) {
    btn.addEventListener('click', function(e) {
      e.preventDefault();
      addToCart(btn.dataset.productId);
    });
  });
});
