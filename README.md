# ShellCheckr

A local shell-script quality checker focused on safe, readable, portable scripting practices.

## Features

- Basic shell syntax checks through local tooling when available
- Common quoting and portability warnings
- Dangerous command-pattern warnings without executing the script
- Line-numbered diagnostics
- JSON output for editor integrations

ShellCheckr only reads source files. It does not execute scripts.

## Usage

```bash
shellcheckr script.sh
shellcheckr script.sh --json
```

## Development

```bash
python -m unittest discover -s tests -v
```

## License

MIT

## Credits

Built by Medu: https://guns.lol/meduu
