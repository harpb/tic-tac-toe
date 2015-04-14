class DetailController
    name: 'Friend'

    constructor: ($routeParams)->
        console.debug 'DetailController constructor', arguments, @
        @hello = 'toYou'
        @id = $routeParams.id

angular.module('app.detail', [])
    .controller('DetailController', ['$routeParams', DetailController]
)