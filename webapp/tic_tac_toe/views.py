from tic_tac_toe.models import Board, BoardException
from common.class_views import JsonView

# Create your views here.
class NextMoveView(JsonView):

    def get_data(self, context):
        positions = [int(item) for item in self.request.GET.getlist('positions')]
        starting_letter = self.request.GET.get('starting_letter')
        board = Board.from_positions(positions, starting_letter)
        context['next_move'] = board.next_computer_position()
        try:
            board.computer_move(context['next_move'])
        except BoardException:
            pass
        context['progress'] = board.progress
        return context

