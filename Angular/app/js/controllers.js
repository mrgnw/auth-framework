'use strict';

var controllersModule = angular.module('angularProject.controllers', [])

    .controller('homeCtrl', function($scope, $http, User, Address, Recipe) {

//        $scope.$on('event:login-confirmed', function() {
//            $scope.users = User.query();
//            $scope.addresses = Address.query();
//            $scope.recipes = Recipe.query();
//        });

    $scope.users = User.query();
    $scope.addresses = Address.query();
    $scope.recipes = Recipe.query();

});
