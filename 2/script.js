const resultEl = document.getElementById('result');
const btnMinus = document.getElementById('btn-minus');
const btnPlus = document.getElementById('btn-plus');
const warningEl = document.getElementById('warning');

let count = 0;

function updateUI() {
    resultEl.textContent = count;

    if (count > 0) {
        resultEl.style.backgroundColor = 'yellow';
    } else if (count < 0) {
        resultEl.style.backgroundColor = 'green';
    } else {
        resultEl.style.backgroundColor = 'red';
    }

    btnPlus.disabled = (count >= 10);
    btnMinus.disabled = (count <= -10);

    if (count === 10 || count === -10) {
        warningEl.textContent = 'вы достигли экстремального значения';
    } else {
        warningEl.textContent = '';
    }
}

btnPlus.addEventListener('click', () => {
    if (count < 10) {
        count++;
        updateUI();
    }
});

btnMinus.addEventListener('click', () => {
    if (count > -10) {
        count--;
        updateUI();
    }
});