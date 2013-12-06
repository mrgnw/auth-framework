'use strict';

angular.module('angularProject', ['ui.bootstrap']);


// Declare app module and Appendages
angular.module('angularProject', ['angularProject.filters', 'angularProject.services', 'angularProject.directives', 'angularProject.controllers'])
  .config(['$routeProvider', function($routeProvider) {
    $routeProvider
      .when('/home', {
      	title: 'Home',
      	templateUrl: 'partials/home.html',
      	controller: 'homeCtrl'
      })
      .otherwise({redirectTo: '/home'});
  }]); // If cookieStore is there, add to headers. If you watch, you can determine if it's been deleted and remove from the header.