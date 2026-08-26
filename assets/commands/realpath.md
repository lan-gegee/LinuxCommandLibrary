# TAGLINE

解析文件的绝对规范路径

# TLDR

**获取文件**的绝对路径

```realpath [file.txt]```

**解析符号链接**并获取规范路径

```realpath [symlink]```

**不解析符号链接**直接获取路径

```realpath -s [symlink]```

**获取相对于**另一目录的路径

```realpath --relative-to=[/base/path] [/full/path/file]```

**获取相对基准路径**

```realpath --relative-base=[/base] [/base/subdir/file]```

**获取多个文件**的绝对路径

```realpath [file1] [file2] [file3]```

**要求所有路径组成部分都存在**

```realpath -e [path/to/file]```

**安静模式**（抑制错误输出）

```realpath -q [file]```

# SYNOPSIS

**realpath** [_options_] _file_...

# DESCRIPTION

**realpath** 输出文件解析后的绝对路径名。它会展开所有符号链接，解析 /./、/../ 引用，并去除多余的斜杠，从而生成规范路径。

在 shell 脚本中，当你需要文件的绝对路径而不论其指定方式（相对路径、符号链接等）时，该工具非常有用。它还可以计算两个位置之间的相对路径。

realpath 是 GNU coreutils 的一部分，提供与 readlink 命令加 -f 标志类似的功能。

# PARAMETERS

**-e**, **--canonicalize-existing**
> 所有路径组成部分都必须存在。

**-m**, **--canonicalize-missing**
> 路径组成部分无需存在。

**-L**, **--logical**
> 在符号链接之前先解析 ..。

**-P**, **--physical**
> 先解析符号链接（默认）。

**-s**, **--strip**, **--no-symlinks**
> 不解析符号链接。

**--relative-to=** _dir_
> 输出相对于指定目录的路径。

**--relative-base=** _dir_
> 若位于基准目录之下则输出相对路径。

**-q**, **--quiet**
> 抑制错误消息。

**-z**, **--zero**
> 用 NUL 结束每行输出。

# CAVEATS

GNU coreutils 与 BSD 版本之间的行为可能有所不同。不加 -e 时路径可以不存在。使用相对路径选项时需要仔细指定基准目录。

# HISTORY

**realpath** 作为独立命令自 **8.15** 版起成为 **GNU coreutils** 的一部分（发布于 **2012 年**）。在此之前，C 库中已存在 realpath() 函数，readlink 命令也提供了类似功能。独立命令的出现简化了常见的 shell 脚本任务。

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

[readlink](/man/readlink)(1), [dirname](/man/dirname)(1), [basename](/man/basename)(1), [pwd](/man/pwd)(1)
