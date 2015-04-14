from swampdragon import route_handler
from swampdragon.route_handler import ModelRouter, ModelPubRouter
from tic_tac_toe.models import TicTacToe, TicTacToeMove
import tic_tac_toe


class TicTacToeRouter(ModelPubRouter):
    route_name = 'tic-tac-toe'
    model = TicTacToe
    serializer_class = model.serializer_class

    def get_initial(self, verb, **kwargs):
        if verb == 'create':
            return {'creator': self.connection.user}
        return dict()

    def get_object(self, **kwargs):
        return self.model.objects.get(pk = kwargs['id'])

    def get_query_set(self, **kwargs):
        return self.model.objects.all()


class TicTacToeMoveRouter(ModelPubRouter):
    route_name = 'tic-tac-toe-move'
    model = TicTacToeMove
    serializer_class = model.serializer_class

    def get_initial(self, verb, **kwargs):
        if verb == 'create':
            try:
                tic_tac_toe = TicTacToe.objects.get(id = kwargs.get('tic_tac_toe_id'))
                return {'tic_tac_toe': tic_tac_toe}
            except TicTacToe.DoesNotExist:
                pass
        return dict()


    def get_object(self, **kwargs):
        return self.model.objects.get(pk = kwargs['id'])

    def get_query_set(self, **kwargs):
        return self.model.objects.filter(tic_tac_toe = kwargs['tic_tac_toe_id'])


route_handler.register(TicTacToeRouter)
route_handler.register(TicTacToeMoveRouter)
