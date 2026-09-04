from dataclasses import dataclass

@dataclass(frozen=True)
class Finding:
    line:int
    code:str
    message:str

def lint(text:str):
    out=[]
    for n,line in enumerate(text.splitlines(),1):
        if 'rm -rf $' in line: out.append(Finding(n,'SCX001','unquoted variable used with recursive removal'))
        if 'eval ' in line: out.append(Finding(n,'SCX002','eval requires careful input handling'))
        if 'curl ' in line and '|' in line: out.append(Finding(n,'SCX003','review piping downloaded content directly'))
    return out
