# ShellCheckr

> Review shell scripts for common safety, portability, and readability issues.

ShellCheckr is a local shell-script quality checker that produces line-numbered diagnostics without executing the script being inspected.

## Highlights

- Basic shell syntax checks through local tooling when available
- Common quoting and portability warnings
- Dangerous command-pattern warnings
- Line-numbered diagnostics
- JSON output for editor and automation integrations
- Read-only source analysis

## Usage

```bash
shellcheckr script.sh
shellcheckr script.sh --json
```

## Analysis flow

```text
shell script
     ↓
static checks
     ↓
line-level findings
     ↓
review + fix
```

## Use Cases

- Shell-script review
- Development workflows
- CI quality checks
- Portability checks
- Security-conscious scripting

ShellCheckr does not execute the inspected script.

## Development

```bash
python -m unittest discover -s tests -v
```

## License

MIT

Built by **Meduuv**.

[More projects](https://github.com/meduuv?tab=repositories) · [guns.lol/meduu](https://guns.lol/meduu)
