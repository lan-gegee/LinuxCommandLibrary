# TAGLINE

读取 LLVM 汇编语言并输出 LLVM 位码的汇编器

# TLDR

**将 LLVM IR 汇编为位码**

```llvm-as [input.ll] -o [output.bc]```

**从 stdin 汇编**

```cat [input.ll] | llvm-as -o [output.bc]```

**仅检查语法**

```llvm-as -disable-output [input.ll]```

**输出到 stdout**

```llvm-as [input.ll] -o -```

# SYNOPSIS

**llvm-as** [_options_] [_filename_]

# PARAMETERS

**-o** _filename_
> 输出文件名。

**-f**
> 允许在终端上输出二进制数据。

**-disable-output**
> 不写输出（语法检查）。

**--data-layout** _layout_
> 覆盖数据布局字符串。

**--help**
> 显示帮助。

**--version**
> 显示版本。

# DESCRIPTION

**llvm-as** 是 LLVM 汇编器，读取 LLVM 汇编语言（.ll 文件）并输出 LLVM 位码（.bc 文件）。它是 llvm-dis 的逆过程。

该工具将人类可读的 LLVM 中间表示转换为其他 LLVM 工具使用的二进制位码格式。

# EXAMPLE

```llvm
; input.ll
define i32 @main() {
  ret i32 0
}
```

```bash
llvm-as input.ll -o output.bc
```

# CAVEATS

输入必须是有效的 LLVM IR。位码格式可能随 LLVM 版本而变化。反向操作请使用 llvm-dis。

# HISTORY

llvm-as 自 **2000 年** **Chris Lattner** 在伊利诺伊大学创立 LLVM 项目之初就是其组成部分。

# INSTALL

```apt: sudo apt install llvm```

```dnf: sudo dnf install llvm```

```pacman: sudo pacman -S llvm```

```apk: sudo apk add llvm```

```zypper: sudo zypper install llvm```

```brew: brew install llvm```

```nix: nix profile install nixpkgs#llvm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[llvm-dis](/man/llvm-dis)(1), [llc](/man/llc)(1), [lli](/man/lli)(1), [opt](/man/opt)(1), [clang](/man/clang)(1)
