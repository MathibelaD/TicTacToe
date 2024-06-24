document.addEventListener('DOMContentLoaded', () => {
    const cells = document.querySelectorAll('.cell');
    const status = document.querySelector('.status');
    const resetButton = document.getElementById('reset');

    console.log("cell clicked", cells)
    cells.forEach(cell => {
        cell.addEventListener('click', handleClick);
    });

    resetButton.addEventListener('click', resetGame);

    async function handleClick(event) {
        const index = event.target.getAttribute('data-index');
        const response = await fetch('/move', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ index: index })
        });
        const result = await response.json();
        if (result.status === 'invalid') {
            return;
        } else if (result.status === 'win') {
            status.textContent = `${result.winner} wins!`;
            // Trigger confetti animation on win
            confetti({
                particleCount: 200,
                spread: 70,
                origin: { y: 0.6 }
            });
        } else if (result.status === 'continue') {
            updateBoard(result.board);
        }
    }

    async function resetGame() {
        const response = await fetch('/reset', {
            method: 'POST',
        });
        const result = await response.json();
        if (result.status === 'reset') {
            cells.forEach(cell => {
                cell.textContent = '';
            });
            status.textContent = '';
        }
    }

    function updateBoard(board) {
        board.forEach((cell, index) => {
            cells[index].textContent = cell;
        });
    }
});
