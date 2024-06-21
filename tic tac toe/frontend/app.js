const usernameInput = document.getElementById('username');
const boardDiv = document.getElementById('board');

let board = ['', '', '', '', '', '', '', '', '']; // Inicjalizacja pustej planszy

// Funkcja renderująca planszę
function renderBoard() {
    boardDiv.innerHTML = '';
    board.forEach((mark, index) => {
        const cell = document.createElement('div');
        cell.textContent = mark;
        cell.classList.add('cell');
        cell.addEventListener('click', () => makeMove(index));
        boardDiv.appendChild(cell);
    });
}

// Funkcja wykonująca ruch
async function makeMove(position) {
	console.log("ASDASDSAD");
    if (board[position] === '') {
        board[position] = 'X';
        renderBoard();
        const response = await fetch('/play', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ board })
        });
        const data = await response.json();
        board[data.position] = 'O'; // Odpowiedź od backendu - ruch przeciwnika
        renderBoard();
    }
}

renderBoard();
