from django.db import models
from copy import deepcopy

class BoardException(Exception):
    pass

class CostSystem(object):
    WIN = -100
    DRAW = -50
    LOSS = 100
    MOVE = 1
    BLOCK = 0

class Board(object):

    MINIMUM_LENGTH = 3
    FILLER_LETTER = '-'
    error_message = {
        'min_length': 'Length must be greater than %d.' % MINIMUM_LENGTH
    }

    def __init__(self, length):

        if length < self.MINIMUM_LENGTH:
            raise BoardException(self.error_message['min_length'])

        self.length = length
        self.total_cells = length * length
        self.cells = [self.FILLER_LETTER for i in xrange(self.total_cells)]
        self.free_cells = set(range(self.total_cells))
        self.player_letter = 'X'
        self.computer_letter = 'O'
        self.cost = 0
        self.last_move = {
            'position':-1,
            'letter': self.FILLER_LETTER,
            'cost': 0,
        }

    @classmethod
    def from_signature(cls, signature):
        rows = signature.split(',')
        board = Board(len(rows))
        i = 0
        for row in rows:
            for letter in row:
                board.move(i, letter)
                i += 1

        return board

    @classmethod
    def from_positions(cls, positions, starting_letter):
        board = Board(Board.MINIMUM_LENGTH)
        for position in positions:
            if board.last_move['letter'] != starting_letter:
                if board.computer_letter == starting_letter:
                    board.computer_move(position)
                else:
                    board.player_move(position)
            else:
                if board.computer_letter != starting_letter:
                    board.computer_move(position)
                else:
                    board.player_move(position)

        return board

#     def get_cost(self, position, letter):
#         if is_winner(position, letter)

    def states(self):
        '''
        All of the possible states of rows, columns and diagonals
        '''
        states = []
        # ROWS
        for i in xrange(0, self.total_cells, self.length):
            state = ''.join(self.cells[i:i + self.length])
            states.append(state)

        # COLUMNS
        for i in xrange(self.length):
            state = ''.join([self.cells[j * self.length + i] for j in range(self.length)])
            states.append(state)

        # Top-Right Diagonal
        state = ''.join([self.cells[i * self.length + i] for i in range(self.length)])
        states.append(state)

        # Top-Left Diagonal
        state = ''.join([self.cells[(self.length - 1) * (i + 1)] for i in range(self.length)])
        states.append(state)

        return states

    @property
    def has_winner(self):
        return self.player_win or self.computer_win

    @property
    def player_win(self):
        player_win = ''.join([self.player_letter for _ in xrange(self.length)])

        for state in self.states():
            if state == player_win:
                return True

        return False

    @property
    def computer_win(self):
        computer_win = ''.join([self.computer_letter for _ in xrange(self.length)])

        for state in self.states():
            if state == computer_win:
                return True

        return False

    def move(self, position, letter):
        if self.FILLER_LETTER not in self.cells[position]:
            raise BoardException('Position is occupied by %s' % self.cells[position])

        if position >= self.total_cells or position < 0:
            raise BoardException('Position is outside the board.')

        self.cells[position] = letter
        self.free_cells.remove(position)
        self.last_move['letter'] = letter
        self.last_move['position'] = position

        # Add the cost
        if self.player_win:
            self.last_move['cost'] = CostSystem.LOSS
#             print '**** PLAYER WIN ****'
#             self.display
        elif self.computer_win:
            self.last_move['cost'] = CostSystem.WIN
#             print '**** COMPUTER WIN ****'
#             self.display
        elif not self.free_cells:
            self.last_move['cost'] = CostSystem.DRAW
        elif letter == self.computer_letter:
            self.last_move['cost'] = CostSystem.MOVE
        else:
            self.last_move['cost'] = 0

    def player_move(self, position):
        return self.move(position, self.player_letter)

    def computer_move(self, position):
        return self.move(position, self.computer_letter)

    def display(self, title):
        print '#### %s' % title
        print 'self.free_cells', self.free_cells
        for i in xrange(self.total_cells):
            if i and i % self.length == 0:
                    print
            print self.cells[i],
            if i % self.length < self.length - 1:
                print '|',
        print

    def __eq__(self, board):
        return self.cost == board.cost

    def __lt__(self, board):
        return board.cost < self.cost

    @property
    def corners(self):
        return set([0, self.length - 1, self.total_cells - self.length, self.total_cells - 1])

    @property
    def sides(self):
        cells_without_corners = set(range(self.total_cells)) - self.corners
        cells_without_corners.remove(self.center)
        return cells_without_corners

    @property
    def center(self):
        return self.total_cells / 2

    def next_computer_position(self):
#         tree = DecisionTree(self)
#         tree.display_children()
#         if tree.children:
#             return tree.children[0].board.last_move

        # Computer is able to win
        for position in self.free_cells:
            board_copy = deepcopy(self)
            board_copy.computer_move(position)
            if board_copy.computer_win:
                return position


        # Block the player's win
        for position in self.free_cells:
            board_copy = deepcopy(self)
            board_copy.player_move(position)
            if board_copy.player_win:
                return position

        # Always take the corner, if possible
        if self.center in self.free_cells:
            return self.center

        # If player moved to the corner, then take a side, if we own the center
        if self.last_move['position'] in self.corners and self.cells[self.center] == self.computer_letter:
            available_sides = self.sides & self.free_cells
            if available_sides:
                return next(iter(available_sides))
        else:
            # Take a corner
            available_corners = self.corners & self.free_cells
            if available_corners:
                return next(iter(available_corners))

        # Pick any of the free cell
        if self.free_cells:
            return next(iter(self.free_cells))
        else:
            return -1

    @property
    def progress(self):
        if self.player_win:
            return 'player_win'
        if self.computer_win:
            return 'computer_win'
        if not self.free_cells:
            return 'draw'
        return 'ongoing'

class DecisionTree(object):

    def __init__(self, board):
        self.board = board
        self.children = []
        if not board.has_winner:
            for position in board.free_cells:
                new_board = deepcopy(board)
                if board.last_move['letter'] == board.computer_letter:
                    new_board.player_move(position)
                else:
                    new_board.computer_move(position)
                self.children.append(DecisionTree(new_board))

        self.cost = self.board.last_move['cost']
        if self.children:
            self.children.sort()
            self.cost += self.children[0].cost


    def display_children(self, level = 0):
        title = '%s:%s' % (self.board.total_cells - len(self.board.free_cells), level)
        self.board.display(title)
        print 'Cost:', self.cost, self.children
        if self.children:
            self.children[0].display_children()
#         for child in self.children:
#             child.display_children()
#             print
#             print
#             print

    def __eq__(self, other):
        return self.cost == other.cost

    def __lt__(self, other):
        return self.cost < other.cost

    def __repr__(self, *args, **kwargs):
        return 'Cost: %s (%s)' % (self.cost, self.board.last_move['position'])

if __name__ == '__main__':

    board = Board(3)
    board.player_move(1)
    board.computer_move(0)
    board.player_move(4)
    board.computer_move(7)
    board.player_move(6)
    board.computer_move(2)
    board.player_move(3)
    board.computer_move(5)
    board.player_move(8)
    board.display('---')
#     board.computer_move(4)
#     board.display
#     tree = DecisionTree(board)
#     tree.display_children()
    print board.next_computer_position()

