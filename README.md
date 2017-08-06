<p align="center">
	<img src="https://raw.githubusercontent.com/hayorov/ororo2leo/master/assets/ororo2leo.png" alt="logo"/>
</p>

# ororo2leo
_A command line tool for exporting ororo.tv dictionary to lingualeo._

![pyversions](https://img.shields.io/pypi/pyversions/ororo2leo.svg) [![Build Status](https://img.shields.io/travis/hayorov/ororo2leo/master.svg)](https://travis-ci.org/hayorov/ororo2leo) [![PyPi Status](https://img.shields.io/pypi/v/ororo2leo.svg)](https://pypi.python.org/pypi/ororo2leo)


## How to install
```
pip3 install ororo2leo
```

## Usage

#### Export CSV dictionary from ororo.tv to lingualeo

- Download your ororo.tv dictionary file [https://ororo.tv/en/users/export_dictionary](https://ororo.tv/en/users/export_dictionary)
- Run `ororo2leo`

```
ororo2leo export --csv-dict CSV_DICT --leo-login LEO_LOGIN --leo-password LEO_PASSWORD
```

```
⇒  ororo2leo export /Users/allexx/ororo.tv\ dict\ 2017-08-06.csv user@lingualeo.com password
Discovered 71 word(s) for CSV file
[0/71] Word `uncork` exists.
[1/71] Word `crucified` added.
[2/71] Word `tricksiest` exists.
...
```
