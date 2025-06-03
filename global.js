// global.js

const STARTING_BALANCE = 100;
const BALANCE_KEY = 'global_balance';

// Initialize balance if not already set
function getBalance() {
    let balance = localStorage.getItem(BALANCE_KEY);
    if (balance === null) {
        localStorage.setItem(BALANCE_KEY, STARTING_BALANCE);
        balance = STARTING_BALANCE;
    }
    return parseInt(balance);
}

function setBalance(amount) {
    localStorage.setItem(BALANCE_KEY, amount);
}

function updateBalanceDisplay() {
    const display = document.getElementById('balance-display');
    if (display) {
        display.textContent = `$${getBalance()}`;
    }
}