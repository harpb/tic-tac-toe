// Generated by CoffeeScript 1.8.0
(function() {
  var DetailController;

  DetailController = (function() {
    DetailController.prototype.name = 'Friend';

    function DetailController($routeParams) {
      console.debug('DetailController constructor', arguments, this);
      this.hello = 'toYou';
      this.id = $routeParams.id;
    }

    return DetailController;

  })();

  angular.module('app.detail', []).controller('DetailController', ['$routeParams', DetailController]);

}).call(this);
