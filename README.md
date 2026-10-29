# service-status-reporter

Check every TCP service in a CSV file and report which are UP or DOWN, with a summary count.

## How to run

```sh
python3 main.py services.csv
```

## Example output

```
web: UP (127.0.0.1:80)
db: DOWN (127.0.0.1:5432)
1/2 services up.
```

Standard library only. Run the tests with `python3 -m unittest discover`.
