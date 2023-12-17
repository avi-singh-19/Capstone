function draw_box(container, row, col, letter = '') {
  const box = document.createElement('div');
  box.className = 'box';
  box.textContent = letter;
  box.id = `box${row}${col}`;

  container.appendChild(box);
  return box;
}

function draw_grid(container) {
  const grid = document.createElement('div');
  grid.className = 'grid';

  for (let row = 0; row < 6; row++) {
    for (let col = 0; col < 5; col++) {
      draw_box(grid, row, col);
    }
  }
  container.appendChild(grid);
}

function start(){
    const game = document.getElementById('game');
    draw_grid(game);
}

start();