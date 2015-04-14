// Generated by CoffeeScript 1.8.0
(function() {
  var AppController, app;

  AppController = function($router) {
    return $router.config([
      {
        path: '/',
        redirectTo: '/dual/7'
      }, {
        path: '/home',
        component: 'home'
      }, {
        path: '/detail/:id',
        component: 'detail'
      }, {
        as: 'dual',
        path: '/dual/:id',
        components: {
          master: 'home',
          details: 'detail'
        }
      }, {
        as: 'double',
        path: '/double/:id',
        components: {}
      }
    ]);
  };

  app = angular.module('app', ['ngNewRouter', 'app.home', 'app.detail']);

  app.controller('AppController', ['$router', AppController]);

}).call(this);
