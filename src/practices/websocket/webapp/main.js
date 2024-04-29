import { createBoard, playMove } from "./connect4.js";


window.addEventListener("DOMContentLoaded", () => {
  // Initialize the UI.
  const board = document.querySelector(".board");
  createBoard(board);

  const websocket = new WebSocket("ws://localhost:8001/")
  initGame(websocket)
  receiveMoves(board, websocket);
  sendMoves(board, websocket);
});

function showMessage(message) {
  window.setTimeout(() => window.alert(message), 50);
}

function initGame(websocket) {
    websocket.addEventListener("open", () => {
        const event = {type: "init"};
        websocket.send(JSON.stringify(event));
    });
}

function receiveMoves(board, websocket) {
  websocket.addEventListener("message", ({data}) => {
    console.log(data);
    const event = JSON.parse(data);
    switch (event.type) {
        case "play":
            playMove(board, event.player, event.column, event.row);
            break;
        case "win":
            showMessage(`Player ${event.player} wins!`)
            websocket.close(1000);
            break;
        case "error":
            showMessage(event.message);
            break;
        default:
            throw new Error(`Unsupported event type: ${event.type}.`);
    }
  });
}

function sendMoves(board, websocket) {
    board.addEventListener("click", ({target}) => {
        const column = target.dataset.column;

        if(column === undefined) {
            return;
        }

        const event = {type: "play", column: parseInt(column, 10)};

        websocket.send(JSON.stringify(event));
    });
}