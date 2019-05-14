#UFCStats: A Python API for fighers stats on ufcstats.com

`ufcstats` provides a simple api to retrieve stats from figherse pages on ufcstats.com 

##Requirements

This package requires [beautifulsoup4](https://pypi.org/project/beautifulsoup4/) and [urllib3](https://pypi.org/project/urllib3/)

##Installation
Use `pip` to install the package from PyPi:

```bash
pip install ufcstats
```

##Usage
Import the package and retrieve stats for a certain fighter:

```python
import ufcstats
stats = ufcstats.getStats("Jon Jones")
print(stats)
```

```bash
{
    "Name": "Jon Jones",
    "Nick": "Bones",
    "Height:": "6' 4\"",
    "Weight:": "205 lbs.",
    "Reach:": "84\"",
    "STANCE:": "Orthodox",
    "DOB:": "Jul 19, 1987",
    "SLpM:": "4.48",
    "Str. Acc.:": "57%",
    "SApM:": "2.05",
    "Str. Def:": "64%",
    "TD Avg.:": "2.07",
    "TD Acc.:": "47%",
    "TD Def.:": "95%",
    "Sub. Avg.:": "0.5"
}
```