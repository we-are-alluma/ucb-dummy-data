# Creating dummy data

We use a combination of `numpy` and `Faker` to create dummy data.

With `numpy` we can create _random_ numerical values for ids and such. `Faker` gives us the ability to create realisitic names, text, lat/long coordinates, urls, and other things. More on `Faker` [here](https://faker.readthedocs.io/en/master/index.html).

## Installing dependencies
Using conda
```shell
conda env create -f environment.yml
```
Using pip
```shell
pip install -r requirements.txt
```

