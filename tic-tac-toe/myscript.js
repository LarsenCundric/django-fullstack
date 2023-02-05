let game = [];

const table = document.querySelector('table');
const restart = document.getElementById('restart');
const cells = [...document.querySelectorAll('td')];

const getNewSymbol = (sym) => {
    if (sym === '') return 'X';
    else if (sym === 'X') return 'O';
    return '';
};

table.addEventListener('click', function (e) {
    const i = e.target.dataset.num;
    const newSym = getNewSymbol(game[i]);
    game[i] = newSym;
    e.target.textContent = newSym;
});

const restartFunc = () => {
    game = Array.from({ length: 9 }, () => '');
    cells.forEach((td) => td.textContent = '');
};

restart.addEventListener('click', restartFunc);

restartFunc();
