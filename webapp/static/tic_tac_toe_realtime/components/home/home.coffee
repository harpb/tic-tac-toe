class HomeController
    name: 'Friend'

    constructor: ($routeParams, $http)->
        console.debug 'HomeController constructor', arguments, @
        @hello = 'toYou'

    onClick: ->
        console.debug 'HomeController onClick', arguments, @


angular.module('app.home', []).controller('HomeController', ['$routeParams', '$http', HomeController])