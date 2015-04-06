app = angular.module('app')
app.directive 'ticTacToe', ->
#    template: 'Name: {{customer.name}} Address: {{customer.address}}'
    scope: {}
    templateUrl: 'app/directives/tic_tac_toe.html'
    controller: ($scope, $http)->
        $scope.totalWins = 0
        $scope.totalLoss = 0
        $scope.totalDraws = 0
        $scope.playerLetter = 'X'
        $scope.computerLetter = 'O'
        $scope.startingLetter = 'X'
        $scope.moves = []
        $scope.request_next_move = ->
            params =
                starting_letter: $scope.startingLetter
                positions: $scope.moves
            request = $http.get('/tic_tac_toe/next_move/', {params: params}
            ).then( (response)->
                if response.status is 200
                    if response.data.progress == 'ongoing'
                        $scope.computerMove(response.data.next_move)
                    else
                        if response.data.progress == 'draw'
                            $scope.draw()
                        else if response.data.progress == 'player_win'
                            $scope.playerWin()
                        else if response.data.progress == 'computer_win'
                            $scope.computerWin()
            )
        $scope.length = @length = 3
        $scope.board = $scope.board = []
        $scope.master = angular.copy($scope.board)
        $scope.reset = ->
            console.debug '$scope.reset'
            angular.copy($scope.master, $scope.board)
            $scope.moves = []
            for position in _.range($scope.length * $scope.length)
                cell =
                    position: position
                    active: false
                    letter: ' '
                $scope.board.push(cell)

        @playerMove = (cell)->
            console.debug 'playerMove', cell
            $scope.request_next_move()
            cell.letter = $scope.playerLetter
            $scope.moves.push(cell.position)

        $scope.computerMove = (position)->
            console.debug '$scope.computerMove', position, $scope.board[position]
            $scope.board[position].letter = $scope.computerLetter
            $scope.board[position].active = true
            $scope.moves.push(position)

        @isComputer = (cell)->
            console.log cell.letter, $scope.computerLetter
            cell.letter == $scope.computerLetter

        @isPlayer = (cell)->
            cell.letter == $scope.playerLetter

        $scope.computerWin = (resigned=false)->
            console.debug 'computerWin'
            $scope.totalLoss += 1
            if !resigned
                alert("You Lost~")
            $scope.reset()

        $scope.playerWin = ->
            $scope.totalWins += 1
            alert("You Won!")
            $scope.reset()

        $scope.draw = ->
            alert("Draw!")
            $scope.totalDraws += 1
            $scope.reset()

        $scope.reset()
        $scope.computerWin = $scope.computerWin
        $scope.reset = $scope.reset