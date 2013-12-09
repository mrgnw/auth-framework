'use strict';

var controllersModule = angular.module('angularProject.controllers', [])

    .controller('homeCtrl', function($scope, $http, User, Address, Recipe, Restangular) {

//        $scope.$on('event:login-confirmed', function() {
//            $scope.users = User.query();
//            $scope.addresses = Address.query();
//            $scope.recipes = Recipe.query();
//        });

        $scope.users = User.query();
        $scope.addresses = Address.query();
        //$scope.recipes = Recipe.query(); // Using $http
        Restangular.all('recipes').getList().then(function(response) { // Using Restangular.
            $scope.recipes = response;
        })
})


    .controller('recipeCtrl', function($scope, $http, Recipe, $routeParams, Restangular, $window) {
        $scope.recipeID = $routeParams.recipeID;
        Restangular.one('recipes', $scope.recipeID).get().then(function(response) {
            $scope.recipe = response;
            $window.document.title = $scope.recipe.recipe_name;

//            Grab a tag
//            TODO: Make a tags API
            Restangular.one('tags', $scope.recipe.tag).get().then(function(response){
                $scope.tag = response;
            })
        })
});