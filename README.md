# Recipes

My collection of recipes I have tried and may (or may not) have enjoyed.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

You will need [Python 3](https://www.python.org/) and a markdown editor such as [VS Code](https://code.visualstudio.com/), but any text editor will do.

### Installing

1. Clone the repository and `cd` into the `Recipes/` directory.

    ```shell
    > git clone https://github.com/BTx123/Recipes.git
    > cd Recipes
    ```

1. Change to the `Recipes/` directory where you cloned the repository and install necessary Python packages using pip (or your preferred environment manager).

    ```shell
    > pip install -r requirements.txt
    ```

1. View help information with:

    ```shell
    > python make_recipe.py --help
    ```

1. Generate a new recipe template with:

    ```shell
    > python make_recipe.py "test recipe" other
    ```

    and you should see a new file called `test-recipe.md` in the `other/` directory.

1. Install the `make_recipe` command to the shell with:

    ```shell
    > pip install --editable .
    > make_recipe "test recipe 2" other
    ```

<!-- ## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
``` -->

<!-- ## Deployment

Add additional notes about how to deploy this on a live system -->

## Built With

* [Python 3](https://www.python.org) - Template generation

<!-- ## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us. -->

<!-- ## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). -->

## Authors

* Brian Tom

<!-- See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project. -->

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

<!-- ## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc -->
