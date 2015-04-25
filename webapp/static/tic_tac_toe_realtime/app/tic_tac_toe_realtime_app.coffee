AppController = ($router)->
    $router.config([
        {
            path: '/',
            redirectTo: '/dual/7'
        }
        {
            path: '/home',
            component: 'home'
        }
        {
            path: '/detail/:id',
            component: 'detail'
        }
        {
            as: 'dual'
            path: '/dual/:id',
            components:
                master: 'home',
                details: 'detail'
        }
        {
            as: 'double'
            path: '/double/:id',
            components: {}
#                master: 'detail',
        }
    ])

app = angular.module('app',[
    'ui.router'
])
app.controller('AppController', [AppController])
