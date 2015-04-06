from django.test import TestCase
from tic_tac_toe.models import Board

class TestBoard(TestCase):

    #===========================================================================
    # has_winner
    #===========================================================================
    def test_has_winner__true(self):
        board = Board.from_signature('XXX;  O; OO')
        # CALL & ASSERT
        self.assertTrue(board.has_winner)

        board = Board.from_signature('   ;XXX;   ')
        # CALL & ASSERT
        self.assertTrue(board.has_winner)

        board = Board.from_signature('   ;   ;XXX')
        # CALL & ASSERT
        self.assertTrue(board.has_winner)

        board = Board.from_signature('X  ;X  ;X  ')
        # CALL & ASSERT
        self.assertTrue(board.has_winner)

        board = Board.from_signature(' X ; X ; X ')
        # CALL & ASSERT
        self.assertTrue(board.has_winner)

        board = Board.from_signature('  X;  X;  X')
        # CALL & ASSERT
        self.assertTrue(board.has_winner)

        board = Board.from_signature('X  ; X ;  X')
        # CALL & ASSERT
        self.assertTrue(board.has_winner)

        board = Board.from_signature('  X; X ;X  ')
        # CALL & ASSERT
        self.assertTrue(board.has_winner)

    def test_has_winner__false(self):
        board = Board.from_signature('XX ;  O; OO')
        # CALL & ASSERT
        self.assertFalse(board.has_winner)

        board = Board.from_signature('   ;X X;   ')
        # CALL & ASSERT
        self.assertFalse(board.has_winner)

        board = Board.from_signature('   ;   ;X X')
        # CALL & ASSERT
        self.assertFalse(board.has_winner)

        board = Board.from_signature('X  ; X ;X  ')
        # CALL & ASSERT
        self.assertFalse(board.has_winner)

        board = Board.from_signature(' X ;X  ; X ')
        # CALL & ASSERT
        self.assertFalse(board.has_winner)

        board = Board.from_signature('  X; X ;  X')
        # CALL & ASSERT
        self.assertFalse(board.has_winner)

        board = Board.from_signature('X  ;X  ;  X')
        # CALL & ASSERT
        self.assertFalse(board.has_winner)

        board = Board.from_signature('  X;X  ;X  ')
        # CALL & ASSERT
        self.assertFalse(board.has_winner)


