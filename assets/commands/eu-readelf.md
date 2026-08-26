# TAGLINE

ELF 文件信息查看器

# TLDR

显示 ELF 文件的**全部**信息

```eu-readelf [-a|--all] [path/to/file]```

显示 ELF **文件头**

```eu-readelf [-h|--file-header] [path/to/file]```

显示**节区（section）**头

```eu-readelf [-S|--section-headers] [path/to/file]```

显示**符号**表

```eu-readelf [-s|--symbols] [path/to/file]```

显示 **NOTE** 段/节区

```eu-readelf [-n|--notes] [path/to/file]```

# SYNOPSIS

**eu-readelf** [_options_] _files_

# DESCRIPTION

**eu-readelf** 显示 ELF（Executable and Linkable Format）文件的信息。它是 elfutils 软件包的一部分，可展示文件头、节区、符号及其他 ELF 元数据。

它是 GNU readelf 的替代品，并带有用于调试和分析的额外功能。

# PARAMETERS

**-a, --all**
> 显示所有可提取的信息

**-n, --notes** [_section_]
> 显示 NOTE 段/节区

**-h, --file-header**
> 显示文件头

**-S, --sections**
> 显示节区头

**-s, --symbols**
> 显示符号表

**-d, --dynamic**
> 显示动态段

# CAVEATS

属于 elfutils 软件包。输出格式与 GNU readelf 略有差异。用于分析编译后的二进制文件和共享库。

# INSTALL

```apt: sudo apt install elfutils```

```dnf: sudo dnf install elfutils```

```pacman: sudo pacman -S elfutils```

```apk: sudo apk add elfutils```

```zypper: sudo zypper install elfutils```

```brew: brew install elfutils```

```nix: nix profile install nixpkgs#elfutils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[readelf](/man/readelf)(1), [objdump](/man/objdump)(1), [nm](/man/nm)(1)

# RESOURCES

```[Source code](https://sourceware.org/git/?p=elfutils.git)```

```[Homepage](https://sourceware.org/elfutils/)```

<!-- verified: 2026-07-15 -->
