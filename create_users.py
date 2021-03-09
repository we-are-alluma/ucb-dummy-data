"""Single script to create a `Users` dataset."""
import pandas as pd
import numpy as np


def create_users_table(
    n: int = 50, latitude: float = 33.7815, longitude: float = -119.4198
) -> None:
    """Creates a dummy _users_ dataset of `n` observations with corresponding geo coordinates centered around `latitude` and `longitude`

    Parameters
    ----------
    n : int, optional
        Number of observations, by default 50
    latitude : float, optional
        Latitude to center made up points around, by default 33.7815
    longitude : float, optional
        Longitude to center made up points around, by default -119.4198
    """

    # TODO
    # uid, gender, location, longitude, latitude, region, county, state, active
    _uid = np.random.randint(low=1_000, high=9_999, size=n)
    _gender = np.random.choice(["M", "F"], size=n)
    _location = ["Los Angeles, CA"] * n
    _longitude = 1.5 * np.random.randn(n) + longitude
    _latitude = 1.5 * np.random.randn(n) + latitude
    _region = ["Los Angeles, CA"] * n
    _county = ["Los Angeles"] * n
    _state = ["CA"] * n
    _active = np.random.randint(low=0, high=2, size=n)

    data = pd.DataFrame(
        data={
            "uid": _uid,
            "gender": _gender,
            "location": _location,
            "longitude": _longitude,
            "latitude": _latitude,
            "region": _region,
            "county": _county,
            "state": _state,
            "active": _active,
        }
    )

    data.to_csv("users.csv", index = False, encoding = "utf-8")
    return None

if __name__ == "__main__":
    print("Creating users table...")
    create_users_table()
    print("Done!")
