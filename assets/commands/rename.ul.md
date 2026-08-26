# TAGLINE

使用简单字符串替换重命名文件（util-linux 版本）

# TLDR

将所有匹配文件名中的 "foo" 替换为 "bar"

```rename.ul foo bar *.txt```

预览更改而不实际执行任何操作

```rename.ul -n foo bar *```

只替换每个文件名中第一次出现的内容

```rename.ul -o foo bar *```

# SYNOPSIS

**rename.ul** [_options_] _from_ _to_ _file_...

# PARAMETERS

**-n**, **--no-act**  
> 显示将要执行的操作，但不实际重命名

**-v**, **--verbose**  
> 打印被重命名的文件名

**-o**, **--one**  
> 只替换每个文件名中第一次出现的 _from_

**-i**, **--interactive**  
> 每次重命名前进行提示

**-f**, **--force**  
> 必要时覆盖已存在的文件

# DESCRIPTION

**rename.ul** 是 util-linux 提供的简单批量重命名工具。它在所列文件的基本名中将 _from_ 字符串的第一次（或全部）出现替换为 _to_。

它有意比 Debian 系统上基于 Perl 的 `rename` 更简单。其语法更接近基础的查找替换，而非完整的 Perl 表达式引擎。

由于它只操作基本名，且默认不跨越目录边界，因此对日常批量重命名任务非常安全。

# CAVEATS

- 除非提供 **--force**，否则拒绝覆盖已存在的文件。
- 只修改文件名部分；目录部分不受影响。
- `from` 和 `to` 字符串按字面处理——不会对其执行正则表达式或通配符展开。

# INSTALL

```apt: sudo apt install util-linux```

```dnf: sudo dnf install util-linux```

```pacman: sudo pacman -S util-linux```

```zypper: sudo zypper install util-linux```

```brew: brew install util-linux```

```nix: nix profile install nixpkgs#util-linux```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[rename](/man/rename)(1), [mmv](/man/mmv)(1), [prename](/man/prename)(1)
