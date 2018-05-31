#include <iostream>
#include <stdlib.h>


/*
 * Bogdan Bernovici - Battleship project - ATCN
 */

using namespace std;

void initializeBoard(char (&m)[10][10]) {

    for (int i = 0; i < 10; i++) {
        for (int j = 0; j < 10; j++) {
            m[i][j] = '0';
        }
    }
}

bool isPossibleToPlace(int i, int j, char (&m)[10][10], int size, int direction, int orientation) {
    bool isPossible = true;
    if (orientation == 0) {
        if (j + (size * direction) >= 0 && j + (size * direction) <= 9) {
            while (size > 0) {
                if (m[i][j + (size * direction)] != '0') {
                    isPossible = false;
                }
                size--;
            }
        } else {
            isPossible = false;
        }
    } else {
        if (i + (size * direction) >= 0 && i + (size * direction) <= 9) {

            while (size > 0) {
                if (m[i + (size * direction)][j] != '0') {
                    isPossible = false;
                }
                size--;
            }
        } else {
            isPossible = false;
        }
    }
    return isPossible;
}

void placeBattleship(int i, int j, char (&m)[10][10], int size, int direction, int orientation) {
    cout << endl << "Direction " << direction << " Orientation " << orientation << endl;
    if (orientation == 0) {
        while (size >= 1) {
            m[i][j + (size * direction)] = '#';
            size--;
        }
    } else {
        while (size >= 1) {
            m[i + (size * direction)][j] = '#';
            size--;
        }
    }
}

int createBattleship(char (&m)[10][10], int size) {
    int randomI = rand() % 10;
    int randomJ = rand() % 10;
    int randomOrientation = rand() % 2; // 0 for vertical, 1 for horizontal
    int randomDirection = rand() % 2; // -1 or 1
    cout << randomI << " " << randomJ << " " << randomOrientation << " " << randomDirection << endl;
    if (randomDirection == 0) {
        randomDirection = -1;
    }

    if (isPossibleToPlace(randomI, randomJ, m, size, randomDirection, randomOrientation)) {
        placeBattleship(randomI, randomJ, m, size, randomDirection, randomOrientation);
    } else {
        createBattleship(m, size);
    }
}

void populateBoardWithBattleships(char (&m)[10][10]) {

    // Place 4 blocks ship first (the largest)
    createBattleship(m, 4);

    //Place 2 of 3 blocks ships
    createBattleship(m, 3);
    createBattleship(m, 3);

    //Place 3 of 2 blocks ships
    createBattleship(m, 2);
    createBattleship(m, 2);
    createBattleship(m, 2);

    //Place 4 of 1 block ships
    createBattleship(m, 1);
    createBattleship(m, 1);
    createBattleship(m, 1);
    createBattleship(m, 1);
}

void showPlayerBoard(char (&m)[10][10]) {
    cout << endl << "[Player 1]" << endl;
    for (int i = 0; i < 10; i++) {
        for (int j = 0; j < 10; j++) {
            cout << m[i][j] << " ";
        }
        cout << endl;
    }
}

void showEnemyBoard(char (&m)[10][10]) {
    cout << endl << "[Enemy AI]" << endl;
    for (int i = 0; i < 10; i++) {
        for (int j = 0; j < 10; j++) {
            if (m[i][j] != '#') {
                cout << m[i][j] << " ";
            } else {
                cout << '0' << " ";
            }
        }
        cout << endl;
    }
}

void doPlayerTurn(char (&m)[10][10]) {
    int x, y;
    cout << endl << "Choose [X,Y] where to attack the enemy." << endl;
    cout << "X = ";
    cin >> x;
    cout << "Y = ";
    cin >> y;
    if (m[x][y] == '#') {
        m[x][y] = 'X';
        showEnemyBoard(m);
        cout << "You hit a ship! You have one more turn.";
        doPlayerTurn(m);
    } else {
        m[x][y] = '1';
    }
}

void doEnemyTurn(char (&m)[10][10]) {
    int x = rand() % 10;
    int y = rand() % 10;

    if (m[x][y] == '#') {
        m[x][y] = 'X';
        doEnemyTurn(m);
    } else {
        m[x][y] = '1';
    }
}

bool winnerExists(char (&player)[10][10], char (&enemy)[10][10]) {

    bool winner = true;
    //check if player won
    for (int i = 0; i < 10; i++) {
        for (int j = 0; j < 10; j++) {
            if (player[i][j] == '#') {
                winner = false;
            }
        }
    }
    if (winner) {
        cout << endl << "[[[[ ENEMY AI HAS WON!!! ]]]]" << endl;
        cout << "[[[[ TRY AGAIN! ]]]]" << endl;
        return true;
    } else {
        winner = true;
    }

    //check if enemy won
    for (int i = 0; i < 10; i++) {
        for (int j = 0; j < 10; j++) {
            if (enemy[i][j] == '#') {
                winner = false;
            }
        }
    }
    if (winner) {
        cout << endl << "[[[[ YOU HAVE WON!!! ]]]]" << endl;
        cout << "[[[[ CONGRATULATIONS! ]]]]" << endl;
        return true;
    } else {
        return false;
    }
}

int main() {

    srand(time(0)); // for the random function

    int playing = 1;
    int finished;
    char player[10][10], enemy[10][10];
    int round;

    while (playing == 1) {

        // Initialize player and enemy matrices
        cout << endl << "[PLACING BATTLESHIPS ON THE BOARD]" << endl;
        initializeBoard(player);
        initializeBoard(enemy);
        populateBoardWithBattleships(player);
        populateBoardWithBattleships(enemy);
        round = 1;
        finished = 0;

        while (finished != 1) {
            cout << endl << "------------- [ROUND " << round << "] -------------";

            showPlayerBoard(player);
            showEnemyBoard(enemy);

            doPlayerTurn(enemy);
            doEnemyTurn(player);

            if (winnerExists(player, enemy)) {
                finished = 1;
                int playAgain;
                cout << endl << "Do you want to play again ? [1 for Yes, 0 for No]: ";
                cin >> playAgain;
                if (playAgain == 0) {
                    playing = 0;
                }
            }
            round++;
        }
    }
    return 0;
}