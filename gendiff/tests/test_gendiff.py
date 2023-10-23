from gendiff.scripts.gendiff import gendiff

expected_result = """{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}"""
fixture_1 = """{
  "host": "hexlet.io",
  "timeout": 50,
  "proxy": "123.234.53.22",
  "follow": false
}"""
fixture_2 = """{
  "timeout": 20,
  "verbose": true,
  "host": "hexlet.io"
}"""

def test_gendiff() -> None:
    assert gendiff(fixture_1, fixture_2) == expected_result