# TAGLINE

解压 Microsoft cabinet 归档

# TLDR

**解压** cabinet 文件

```cabextract [file.cab]```

**只列出内容不解压**

```cabextract -l [file.cab]```

**解压到指定目录**

```cabextract -d [output_dir] [file.cab]```

**测试归档完整性**

```cabextract -t [file.cab]```

**按过滤模式解压**

```cabextract -F "*.dll" [file.cab]```

**以小写文件名解压**

```cabextract -L [file.cab]```

**从 exe 中内嵌的 cabinet 解压**

```cabextract [setup.exe]```

# SYNOPSIS

**cabextract** [_options_] _cabinet_file_...

# DESCRIPTION

**cabextract** 从 Microsoft cabinet（.cab）归档中提取文件。它还能从可执行文件等其他文件中提取内嵌的 cabinet。支持所有 Microsoft cabinet 格式以及 Windows CE 安装文件。

# PARAMETERS

**-l**, **--list**
> 只列出内容，不解压

**-t**, **--test**
> 测试完整性并显示 MD5 校验和

**-d** _directory_, **--directory**=_directory_
> 解压到指定目录

**-F** _pattern_, **--filter**=_pattern_
> 只解压匹配 shell 模式的文件

**-f**, **--fix**
> 尝试修复损坏的归档

**-L**, **--lowercase**
> 将文件名转换为小写

**-p**, **--pipe**
> 将解压出的文件通过管道输出到 stdout

**-s**, **--single**
> 不跟随多分卷 cabinet 链接

**-q**, **--quiet**
> 抑制常规输出

**-v**, **--version**
> 显示版本

# MULTI-PART CABINETS

对于多分卷 cabinet 归档，只需指定第一个文件。cabextract 会自动定位并处理其余分卷。

# CAVEATS

只能解压归档，不能创建归档。创建 cabinet 文件请使用 **gcab**。会保留内部目录结构、权限和日期。

# INSTALL

```apt: sudo apt install cabextract```

```dnf: sudo dnf install cabextract```

```pacman: sudo pacman -S cabextract```

```apk: sudo apk add cabextract```

```zypper: sudo zypper install cabextract```

```brew: brew install cabextract```

```nix: nix profile install nixpkgs#cabextract```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[unzip](/man/unzip)(1), [7z](/man/7z)(1)
