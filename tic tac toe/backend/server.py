from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

players = {}  # Dictionary to store player information
board = ['', '', '', '', '', '', '', '', '']  # Initialize the board
current_player = 'X'  # Player X starts

def check_winner():
    # Define winning combinations
    win_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]  # Diagonals
    ]
    
    # Check if any player has won
    for combo in win_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] != '':
            return board[combo[0]]  # Return the winning player
    return None  # No winner yet

@app.route('/join', methods=['POST'])
def join_game():
    global players
    global board
    board = ['', '', '', '', '', '', '', '', '']
    player_id = request.json.get('username')
    can_play = len(players) < 2
    if player_id not in players and len(players) < 2:
        players[player_id] = 'X' if len(players) % 2 == 0 else 'O'
    print(players, can_play, flush=True)
    return jsonify({'player_can_play': can_play, 'players_in_queue': len(players), 'player_mark': players[player_id] if can_play else ""})

@app.route('/play', methods=['POST'])
def play():
    global current_player
    data = (request.json)['data_to_send']
    print("\n",data,"\n")
    username = data['username']  # Get player's username
    position = data['pos']  # Get position from input data
    if username in players and players[username] == current_player:
        if position is not None and board[position] == '':
            board[position] = current_player
            current_player = 'O' if current_player == 'X' else 'X'
    winner = check_winner()
    print(f"It's {current_player}'s turn, board is: {board}, winner: {winner}")
    return jsonify({'board': board, 'winner': winner})


@app.route('/board', methods=['GET'])
def get_board():
    global board
    winner = check_winner()
    if winner:
        players.clear()
    return jsonify({'board': board, 'winner': winner})
    

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
