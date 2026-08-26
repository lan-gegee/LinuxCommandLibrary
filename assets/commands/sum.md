# TAGLINE

计算旧式文件校验和及块计数

# TLDR

使用 BSD 算法**计算校验和**（默认）

```sum [file]```

配合 512 字节块**使用 System V 算法**

```sum -s [file]```

显式配合 1K 块**使用 BSD 算法**

```sum -r [file]```

**从标准输入读取**

```cat [file] | sum```

# SYNOPSIS

**sum** [_options_] [_file_...]

# PARAMETERS

**-r**
> 使用 BSD 算法，采用 1K 块（默认）

**-s**, **--sysv**
> 使用 System V 算法，采用 512 字节块

**--help**
> 显示帮助并退出

**--version**
> 输出版本信息并退出

# DESCRIPTION

**sum** 为每个 FILE 打印校验和与块计数。未指定 FILE 或 FILE 为 - 时，读取标准输入。默认的 BSD 算法使用 1024 字节块，而 System V 算法使用 512 字节块。

这是一个为兼容性保留的旧式工具。新应用建议改用 **cksum** 命令。

# CAVEATS

不具备密码学安全性。完整性校验请使用 sha256sum 或类似工具。该校验和算法不适合检测蓄意的数据篡改。

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

[cksum](/man/cksum)(1), [md5sum](/man/md5sum)(1), [sha256sum](/man/sha256sum)(1)
