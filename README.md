# Launchcs.py

Launchcs.py is a python script that launches instances of CS2 multiserver. It is designed to be used with CS2 multiserver.

## Usage

```bash
python3 launchcs.py
```

or

```bash
./launchcs.py
```

## Requirements

- working installation of CS2 multiserver
- instances called `server1`, `server2`, `server3`, etc.
- python3

## Limitations

- Doesn't support killing instances launched outside of the script
- Doesn't support launching/killing instances with different names
- Doesn't recover from the server being rebooted without shutting down instances within the script (must delete the `serverlist.txt` file)
- Max number of instances is set in the script

