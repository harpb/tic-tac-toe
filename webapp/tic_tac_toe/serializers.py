from swampdragon.serializers.model_serializer import ModelSerializer
from swampdragon.serializers.object_map import get_object_map

class TicTacToeSerializer(ModelSerializer):

    tictactoemove_set = 'TicTacToeMoveSerializer'

    class Meta:
        model = 'tic_tac_toe.TicTacToe'

    @classmethod
    def get_object_map(cls, include_serializers=None, ignore_serializers=None):
        object_map = get_object_map(cls, ignore_serializers)
        for mapping in object_map:
            if mapping['is_collection']:
                mapping['via'] += '_id'
        return object_map

class TicTacToeMoveSerializer(ModelSerializer):

    tic_tac_toe = TicTacToeSerializer

    class Meta:
        model = 'tic_tac_toe.TicTacToeMove'
        update_fields = ('position', 'tic_tac_toe_id')

    def serialize_tic_tac_toe_id(self, obj):
        return obj.tic_tac_toe_id
