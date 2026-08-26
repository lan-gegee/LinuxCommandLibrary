# TAGLINE

按上下文模式拆分文件

# TLDR

拆分文件，第二部分从**第 10 行**开始

```csplit [path/to/file] 10```

在第 7 行和第 23 行将文件拆分为**三部分**

```csplit [path/to/file] 7 23```

在**每第 5 行**开始一个新部分

```csplit [path/to/file] 5 {*}```

每 5 行拆分一次，并**忽略拆分错误**

```csplit -k [path/to/file] 5 {*}```

为输出文件使用**自定义前缀**

```csplit [path/to/file] 5 -f [prefix]```

在第一个匹配**正则表达式**的行之前拆分

```csplit [path/to/file] /[regex]/```

# SYNOPSIS

**csplit** [_options_] _file_ _pattern_...

# DESCRIPTION

**csplit** 根据上下文（行号或模式）把文件拆分为多份。默认生成的文件名为 xx00、xx01 等。

与按大小切分的 split 不同，csplit 按内容结构切分，因此适合在特定边界处拆分日志文件、配置文件或文档。

# PARAMETERS

**-f, --prefix** _prefix_
> 使用指定前缀代替 'xx'

**-k, --keep-files**
> 出错时不删除输出文件

**-n, --digits** _digits_
> 输出文件名中的数字位数

**-s, --quiet**
> 不打印字节数

**{n}**
> 将上一个模式重复 n 次

**{*}**
> 将上一个模式尽可能多地重复

# CAVEATS

属于 GNU coreutils。不带 -k 时，一旦出错输出文件会被删除。用 {*} 重复模式时，如果模式无法均匀划分文件则会失败（可用 -k 保留部分输出）。

# INSTALL

```apt: sudo apt install coreutils```

```dnf: sudo dnf install coreutils```

```pacman: sudo pacman -S coreutils```

```apk: sudo apk add coreutils```

```zypper: sudo zypper install coreutils```

```brew: brew install coreutils```

```nix: nix profile install nixpkgs#coreutils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[split](/man/split)(1), [cut](/man/cut)(1), [head](/man/head)(1)

# RESOURCES

```[Source code](https://git.savannah.gnu.org/cgit/coreutils.git)```

```[Homepage](https://www.gnu.org/software/coreutils/)```

```[Documentation](https://www.gnu.org/software/coreutils/manual/html_node/csplit-invocation.html)```

<!-- verified: 2026-06-26 -->
