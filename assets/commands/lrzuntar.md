# TAGLINE

从 .tar.lrz 文件中解出完整的 tar 包

# TLDR

将 `.tar.lrz` 归档**解压到目录**

```lrzuntar [archive.tar.lrz]```

**解压到指定的输出目录**

```lrzuntar -O [output_directory] [archive.tar.lrz]```

# SYNOPSIS

**lrzuntar** [_options_] _directory.tar.lrz_

# DESCRIPTION

**lrzuntar** 从由 lrztar 创建的 `.tar.lrz` 文件中解出完整的 tar 包。它与运行 `lrztar -d` 完全相同，接受与 lrzip 相同的选项来控制解压行为。

# PARAMETERS

**-O** _directory_
> 指定解压文件的输出目录。

**-f**
> 强制覆盖已有文件。

**-v**
> 详细输出。

**-q**
> 安静运行。

**-h**
> 显示帮助。

# INSTALL

```apt: sudo apt install lrzip```

```pacman: sudo pacman -S lrzip```

```apk: sudo apk add lrzip-extra-scripts```

```zypper: sudo zypper install lrzip```

```brew: brew install lrzip```

```nix: nix profile install nixpkgs#lrzip```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[lrztar](/man/lrztar)(1), [lrzip](/man/lrzip)(1), [lrunzip](/man/lrunzip)(1), [tar](/man/tar)(1)
