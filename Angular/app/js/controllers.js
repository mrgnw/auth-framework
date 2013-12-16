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
            $scope.recipe_photo = response.photo;

//            Grab a tag
//            TODO: Make a tags API
            Restangular.one('tags', $scope.recipe.tag).get().then(function(response){
                $scope.tag = response;
            })
        })
    })

    .controller('addRecipeCtrl', function($scope, $http, Recipe, $routeParams, Restangular, $window) {

        $scope.recipe = Object();
        $scope.recipeList = null;
        $scope.tag = null;
        $scope.name = null;
        $scope.submitted = false;

        Restangular.all('tags').getList().then(function(response) {
                $scope.tags = response;
        });


        Restangular.all('recipe-lists').getList().then(function(response) {
                $scope.recipeLists = response;
        });


        $scope.uploadFile = function(files) {
            $scope.recipe.photo = files[0];
//            alert(files[0])
        }

        $scope.save = function() {
            if($scope.submitted == false){
                $scope.recipe.recipe_name = $scope.name;

//                alert($scope.photo);
                $scope.recipe.recipe_description = $scope.description;
                $scope.recipe.recipe_prep_time = $scope.prep;
                $scope.recipe.recipe_cook_time = $scope.cook;
                $scope.recipe.recipe_total_time = $scope.total;
                $scope.recipe.tag = $scope.tag;
                $scope.recipe.recipe_list = $scope.list;
                $scope.recipe.user = 1;
                Restangular.one('recipes').customPOST($scope.recipe).then(function(data){
                    $scope.submitted = true;
                    }
            )};
        };

        $scope.addTag = function() {
            $scope.newTag = Object();
            $scope.newTag.tag_name = tagName;

        }

    })

