# Lab 28: Django CRUD and Forms

*Author*: Kassie Bradshaw
[Link to my Pull Request](tbd)

## Overview

Add full CRUD functionality to your bag of tricks by building a Django project that allows creating, reading, updating and deleting.

## Feature Tasks & Requirements

* [ ] Create `snacks_crud_project`
* [ ] Create `snacks` app
* [ ] Create `Snack` model
  * [ ] Title field
  * [ ] Purchaser field
  * [ ] Description field
  * [ ] Register model with admin

* [ ] Create `SnackListView` that extends appropriate generic view
  * [ ] Associated URL path is an empty string

* [ ] Create `SnackDetailView` that extends appropriate generic view
  * [ ] Associated URL path is `<int:pk>/`

* Create `SnackCreateView` that extends appropriate generic view
  * [ ] Associated url path is `create/`

* Create `SnackUpdateView` that extends appropriate generic view
  * [ ] Associated url path is `<int:pk>/update/`

* Create `SnackDeleteView` that extends appropriate generic view
  * [ ] Associated URL path is `<int:pk>/delete/`

* [ ] Add urls to support all views, with appropriate names
* [ ] Add templates to support all views
* [ ] Add navigation links in appropriate locations to access all pages
* [ ] Make all necessary changes to project level files for project to run
  * [ ] In other words, make it work.

## Stret Goals

* [ ] Add multiple models
* [ ] Use an alternate test runner
* [ ] Add more advanced fields to the models, e.g.created timestamp
* [ ] Add styling

## User Acceptance Tests

* [ ] Test all Views
* [ ] Test Model
  * [ ] String representation
  * [ ] All fields


