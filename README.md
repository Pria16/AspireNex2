# AspireNex2
This is the 2nd task
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tic-Tac-Toe AI README</title>
</head>
<body>
    <h1>Tic-Tac-Toe AI</h1>
    <p>This project implements an unbeatable AI agent that plays the classic game of Tic-Tac-Toe against a human player. The AI uses the Minimax algorithm with Alpha-Beta Pruning to always make the optimal move.</p>
    
    <h2>Project Structure</h2>
    <ul>
        <li><strong>create_board</strong>: Initializes a 3x3 Tic-Tac-Toe board.</li>
        <li><strong>print_board</strong>: Prints the current state of the board in a 3x3 grid format.</li>
        <li><strong>is_winner</strong>: Checks if the current board is a win for the given player.</li>
        <li><strong>is_draw</strong>: Checks if the board is full and the game is a draw.</li>
        <li><strong>get_available_moves</strong>: Returns the indices of the empty spots on the board.</li>
        <li><strong>minimax</strong>: Implements the Minimax algorithm with Alpha-Beta Pruning to evaluate board states.</li>
        <li><strong>get_best_move</strong>: Finds the best move for the AI by simulating all possible moves.</li>
        <li><strong>play_game</strong>: Main game loop where the human and AI take turns until there is a win or a draw.</li>
    </ul>
    
    <h2>How to Play</h2>
    <ol>
        <li>Run the <code>play_game</code> function to start the game.</li>
        <li>The human player will be prompted to enter a move (0-8), which corresponds to the position on the board as follows:</li>
        <pre>
        0 | 1 | 2
        ---------
        3 | 4 | 5
        ---------
        6 | 7 | 8
        </pre>
        <li>The AI will make its move automatically using the Minimax algorithm.</li>
        <li>The game continues until either the human player or the AI wins, or the game is a draw.</li>
    </ol>
    
    <h2>Example</h2>
    <pre>
    Enter your move (0-8): 0
    | X |   |   |
    |   |   |   |
    |   |   |   |
    
    AI is thinking...
    AI has made its move:
    | X |   |   |
    |   | O |   |
    |   |   |   |
    
    Next move:
    </pre>
    
    <h2>Dependencies</h2>
    <p>This project only requires Python 3 and standard libraries. No additional dependencies are needed.</p>
    
    <h2>License</h2>
    <p>This project is licensed under the MIT License.</p>
</body>
</html>

