document.addEventListener("DOMContentLoaded", function() {
  const priceElements = document.querySelectorAll('.price'); // обработка всех элементов с классом price
  priceElements.forEach(priceElement => {
    let priceValue = priceElement.textContent.replace('₽', '').trim();

    if (!isNaN(priceValue) && priceValue !== "") { // провека на число
      const formattedPrice = Number(priceValue).toLocaleString('ru-RU'); // форматирование
      priceElement.textContent = formattedPrice + ' ₽';
    } else {
      console.warn("Некорректное значение цены:", priceValue); // вывод предупреждения в консоль для отладки
    }
  });
});
