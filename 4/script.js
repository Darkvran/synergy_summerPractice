const num1Input = document.getElementById('num1');
const num2Input = document.getElementById('num2');
const resultBox = document.getElementById('result');
const buttons = document.querySelectorAll('.calc-btn');

// Математические функции
const add = (a, b) => a + b;
const sub = (a, b) => a - b;
const mul = (a, b) => a * b;
const div = (a, b) => {
    if (b === 0) throw new Error("Деление на ноль");
    return a / b;
};

// Обработчик кликов по кнопкам операций
buttons.forEach(button => {
    button.addEventListener('click', () => {
        const val1 = num1Input.value.trim();
        const val2 = num2Input.value.trim();

        // Проверка на пустые поля или нечисловые значения
        if (val1 === '' || val2 === '' || isNaN(val1) || isNaN(val2)) {
            resultBox.textContent = "Ошибка: введите числа!";
            resultBox.classList.add('error');
            return;
        }

        const a = parseFloat(val1);
        const b = parseFloat(val2);
        const op = button.getAttribute('data-op');
        let res;

        resultBox.classList.remove('error');

        try {
            switch (op) {
                case 'add': res = add(a, b); break;
                case 'sub': res = sub(a, b); break;
                case 'mul': res = mul(a, b); break;
                case 'div': res = div(a, b); break;
            }
            // Округляем до 4 знаков во избежание плавающей точки вроде 0.1 + 0.2 = 0.30000000000000004
            resultBox.textContent = Number.isInteger(res) ? res : res.toFixed(4);
        } catch (err) {
            resultBox.textContent = `Ошибка: ${err.message}`;
            resultBox.classList.add('error');
        }
    });
});