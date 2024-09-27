document.addEventListener("DOMContentLoaded", function() {
  const priceElement = document.querySelector('.price');
  const priceValue = priceElement.textContent.replace('₽', '').trim(); // Убираем знак рубля
  const formattedPrice = Number(priceValue).toLocaleString('ru-RU'); // Форматируем число
  priceElement.textContent = formattedPrice + ' ₽'; // Добавляем пробел перед рублем
});