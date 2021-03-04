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

## The data
We are creating 5 datasets: `access_events`, `clients`, `locations`, `opportunities`, and `organizations`.

### `clients`

* id (INT11)
* is_admin (TINYINT1)
* created_at (DATETIME)
* updated_at (DATETIME)
* last_login (DATETIME)

### `organizations`

* id INT(11)
* client_id INT(11)
* name VARCHAR(255)
* website VARCHAR(255)
* description MEDIUMTEXT
* created_at DATETIME
* updated_at DATETIME
* slug VARCHAR(255)
* searchable_by_organizations VARCHAR(255)
* is_searchable TINYINT(1)
* region VARCHAR(255)
* lat FLOAT
* lng FLOAT
* last_verified_at DATETIME
* marked_deleted TINYINT(1)
* deleter_id INT(11)
* is_closed TINYINT(1)

### `locations`

* id INT(11)
* locatable_id INT(11)
* locatable_type VARCHAR(255)
* name VARCHAR(255)
* address VARCHAR(255)
* unit VARCHAR(255)
* city VARCHAR(255)
* state VARCHAR(255)
* zip_code VARCHAR(255)
* is_primary TINYINT(1)
* lat FLOAT
* long FLOAT
* created_at DATETIME
* updated_at DATETIME
* show_on_organization TINYINT(1)

### `opportunities`

* id INT(11)
* organization_id INT(11)
* title VARCHAR(255)
* description MEDIUMTEXT
* is_appointment TINYINT(1)
* created_at DATETIME
* updated_at DATETIME
* slug VARCHAR(255)
* searchable_by_organizations VARCHAR(255)
* is_searchable TINYINT(1)
* last_verified_at DATETIME
* marked_deleted TINYINT(1)
* deleter_id INT(11)
* region VARCHAR(255)

### `access_events`

* user_id INT(4)
* status INT(4)
* accessed_at DATETIME
* reviewed BOOL
* reviewed_at DATETIME
* created_at DATETIME
* updated_at DATETIME
* referred_organization_id INT(4)
* direct_access BOOL
* utilized_at DATETIME