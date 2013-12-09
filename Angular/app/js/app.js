'use strict';

angular.module('angularProject', ['ui.bootstrap']);

// Declare app module and Appendages
angular.module('angularProject', ['angularProject.filters', 'angularProject.services', 'angularProject.directives', 'angularProject.controllers', 'restangular'])
  .config(['$routeProvider', 'RestangularProvider', function($routeProvider, RestangularProvider) {
    $routeProvider
      .when('/home', {
      	title: 'Home',
      	templateUrl: 'partials/home.html',
      	controller: 'homeCtrl'
      })
        .when('/recipes/:recipeID',{
            title: 'A recipe',
            templateUrl: 'partials/recipe.html',
            controller: 'recipeCtrl'
        })
      .otherwise({redirectTo: '/home'});
      RestangularProvider.setBaseUrl('http://localhost:8001');
  }])

    .factory
//    .factory('Page', function(){
//        var title = 'default';
//        return {
//            getTitle: function() { return title; },
//            setTitle: function(newTitle) { title = newTitle };
//        }
//    })
;
  // If cookieStore is there, add to headers. If you watch, you can determine if it's been deleted and remove from the header.
