from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

game_board = ['' for _ in range(9)]
current_player = 'X'
game_active = True

winning_conditions = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8],
    [0, 3, 6], [1, 4, 7], [2, 5, 8],
    [0, 4, 8], [2, 4, 6]
]

def check_winner():
    for condition in winning_conditions:
        a, b, c = condition
        if game_board[a] and game_board[a] == game_board[b] == game_board[c]:
            return game_board[a]
    if '' not in game_board:
        return 'Draw'
    return None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/move', methods=['POST'])
def move():
    global current_player, game_active
    print("here",request.json)
    data = request.json
    index = int(data['index'])
    if game_board[index] or not game_active:
        print("here", game_board[index], game_active)
        return jsonify({'status': 'invalid'})
    
    game_board[index] = current_player
    print(game_board[index])
    winner = check_winner()
    if winner:
        game_active = False
        return jsonify({'status': 'win', 'winner': winner})
    else:
        current_player = 'O' if current_player == 'X' else 'X'
        print(current_player)
        return jsonify({'status': 'continue', 'board': game_board, 'current_player': current_player})

@app.route('/reset', methods=['POST'])
def reset():
    global game_board, current_player, game_active
    game_board = ['' for _ in range(9)]
    current_player = 'X'
    game_active = True
    return jsonify({'status': 'reset'})

if __name__ == '__main__':
    app.run(debug=True)
