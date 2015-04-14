var TodoControllers = angular.module('TicTacToeControllers', []);

TodoControllers.controller('TicTacToeCtrl', ['$scope', '$dragon', function ($scope, $dragon) {
    $scope.ticTacToe = {};
    $scope.ticTacToeMoves = [];
    $scope.gameChannel = 'game';
    $scope.moveChannel = 'move';
    $scope.positions = _.range(9);

    $dragon.onReady(function() {
        $dragon.subscribe('tic-tac-toe', $scope.gameChannel).then(function(response) {
            console.debug('subscribe tic-tac-toe', response);
            $scope.gameMapper = new DataMapper(response.data);
        });

        $dragon.subscribe('tic-tac-toe-move', $scope.moveChannel).then(function(response) {
            console.debug('subscribe tic-tac-toe-move', response);
            $scope.moveMapper = new DataMapper(response.data);
        });

        $dragon.getSingle('tic-tac-toe', {id:1}).then(function(response) {
            console.debug('getSingle tic-tac-toe', response);
            $scope.ticTacToe = response.data;
        });

        $dragon.getList('tic-tac-toe-move', {tic_tac_toe_id:1}).then(function(response) {
            console.debug('getList tic-tac-toe-move', response);
            $scope.ticTacToeMoves = response.data;
        });

    });

    $dragon.onChannelMessage(function(channels, message) {
        console.debug('onChannelMessage', channels, message);
        if (indexOf.call(channels, $scope.gameChannel) > -1) {
            $scope.$apply(function() {
                $scope.gameMapper.mapData($scope.ticTacToe, message);
            });
        }
        if (indexOf.call(channels, $scope.moveChannel) > -1) {
            $scope.$apply(function() {
                console.debug('map', message, 'to', $scope.ticTacToeMoves)
                //$scope.ticTacToeMoves.push(message.data)
                $scope.gameMapper.mapData($scope.ticTacToe, message);
                $scope.moveMapper.mapData($scope.ticTacToeMoves, message);
            });
        }
    });


    $scope.makeMove = function(position) {
        request = $dragon.create('tic-tac-toe-move',
            {
                position: position,
                tic_tac_toe_id: $scope.ticTacToe.id
            });
        request.then(function(){
            console.debug('newGame then', arguments)
        }).catch(function(){
            console.debug('newGame catch', arguments)
        }).finally(function(){
            console.debug('newGame finally', arguments)
        })
    }

    $scope.newGame = function() {
        request = $dragon.create('tic-tac-toe');
        request.then(function(){
            console.debug('newGame then', arguments)
        }).catch(function(){
            console.debug('newGame catch', arguments)
        }).finally(function(){
            console.debug('newGame finally', arguments)
        })
    }
}]);