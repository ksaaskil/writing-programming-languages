# Python compiler

Based on the [PythonCompiler](https://github.com/marcelogdeandrade/PythonCompiler) repository of Marcelo Andrade.

## Instructions

### Requirements

1. Install [llvmlite](https://github.com/numba/llvmlite): `pip install llvmlite`
1. Download [LLVM](http://releases.llvm.org/download.html#8.0.0)
1. Install [RPLY](https://github.com/alex/rply): `pip install rply`

### Compilation

1. `python main.py` to generate `output.ll`
1. `llc -filetype=obj output.ll`
1. `gcc output.o -o output`
1. `./output`
