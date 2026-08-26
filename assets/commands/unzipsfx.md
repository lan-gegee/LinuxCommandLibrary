# TLDR

# TAGLINE

创建自解压的 ZIP 可执行文件

# TLDR

创建**自解压**二进制文件

```cat $(which unzipsfx) [path/to/archive.zip] > [filename] && chmod 755 [filename]```

**解压**自解压二进制文件

```./[path/to/binary]```

**检测**错误

```./[path/to/binary] -t```

不解压而直接**打印**文件内容

```./[path/to/binary] -c [path/to/file]```

显示**注释**

```./[path/to/binary] -z```

# SYNOPSIS

**unzipsfx** 通常与一个 ZIP 归档拼接在一起使用

# PARAMETERS

**-t**
> 检测归档中的错误

**-c** _FILE_
> 不解压而直接打印文件内容

**-z**
> 打印归档注释

# DESCRIPTION

**unzipsfx** 通过在 ZIP 归档前面拼接一段自解压引导程序来创建自解压的压缩二进制文件。生成的可执行文件无需安装 unzip 即可自行解压。

这段引导程序通常使用 cat 与 ZIP 归档拼接在一起，随后再被赋予可执行权限。

# CAVEATS

自解压二进制文件与平台相关。引导程序会增加归档的体积。某些系统可能会阻止执行自解压归档。

# INSTALL

```apt: sudo apt install unzip```

```dnf: sudo dnf install unzip```

```pacman: sudo pacman -S unzip```

```apk: sudo apk add unzip```

```zypper: sudo zypper install unzip```

```brew: brew install unzip```

```nix: nix profile install nixpkgs#unzip```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[zip](/man/zip)(1), [unzip](/man/unzip)(1)
