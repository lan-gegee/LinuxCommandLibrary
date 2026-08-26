# TAGLINE

基于内容的文件类型识别

# TLDR

**判断文件类型**

```file [filename]```

**检查多个文件**

```file [file1] [file2] [file3]```

**显示 MIME 类型**

```file --mime-type [filename]```

**跟随符号链接**

```file -L [symlink]```

**从标准输入读取**

```cat [file] | file -```

# SYNOPSIS

**file** [_options_] _files_...

# PARAMETERS

_FILES_
> 要识别的文件。

**-b**, **--brief**
> 输出中省略文件名。

**-i**, **--mime**
> 输出 MIME 类型和编码。

**--mime-type**
> 仅输出 MIME 类型。

**-L**, **--dereference**
> 跟随符号链接。

**-z**, **--uncompress**
> 查看压缩文件内部。

**-f** _FILE_
> 从文件中读取文件名列表。

**--help**
> 显示帮助信息。

# DESCRIPTION

**file** 通过检查文件内容而非扩展名来判断文件类型。它利用魔数（magic number）模式以及数据库中的启发式规则来识别各种格式。

该工具能识别数千种文件类型，包括可执行文件、归档、文档、图像和文本编码。它检查的是文件头和内容模式，而不是轻信文件名扩展名。

无论是识别未知文件，还是在脚本中验证文件类型，file 都是必不可少的工具。

# CAVEATS

可能误判损坏或异常的文件。自定义格式可能无法被识别。不同环境下魔数数据库的完备程度不一。

# HISTORY

file 的历史可以追溯到 **Unix Version 6**（1975 年）。magic 文件数据库的方法正是为了应对 Unix 系统上日益增多的文件格式而发展起来的。

# INSTALL

```apt: sudo apt install file```

```dnf: sudo dnf install file```

```pacman: sudo pacman -S file```

```apk: sudo apk add file```

```zypper: sudo zypper install file```

```brew: brew install file```

```nix: nix profile install nixpkgs#file```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[stat](/man/stat)(1), [hexdump](/man/hexdump)(1), [identify](/man/identify)(1)

# RESOURCES

```[Homepage](https://www.darwinsys.com/file/)```

```[Source code](https://github.com/file/file)```

<!-- verified: 2026-07-15 -->
