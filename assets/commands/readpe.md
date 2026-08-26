# TAGLINE

显示 PE 可执行文件的信息

# TLDR

显示 PE 文件的**全部信息**

```readpe path/to/executable```

显示 PE 文件中的**所有头部**

```readpe --all-headers path/to/executable```

显示 PE 文件中的**所有节**

```readpe --all-sections path/to/executable```

显示**特定头部**（dos、coff、optional）

```readpe --header dos path/to/executable```

列出所有**导入函数**

```readpe --imports path/to/executable```

列出所有**导出函数**

```readpe --exports path/to/executable```

# SYNOPSIS

**readpe** [_options_] _file_

# PARAMETERS

**--all-headers**
> 显示 PE 文件中存在的所有头部

**--all-sections**
> 显示 PE 文件中的所有节

**--header** _type_
> 显示特定头部（dos、coff、optional）

**--imports**
> 列出导入函数

**--exports**
> 列出导出函数

# DESCRIPTION

**readpe** 显示 PE（Portable Executable）文件的信息——这是 Windows 使用的可执行格式。它可以分析 EXE、DLL 及其他 PE 文件的头部、节、导入和导出。

该工具适用于二进制分析、逆向工程和理解可执行文件结构。

# CAVEATS

只支持有效的 PE 格式文件。畸形或损坏的 PE 文件可能无法正确解析。

# HISTORY

属于 **pev** 的一部分，后者是面向类 Unix 系统的 PE 文件分析工具集。

# INSTALL

```apt: sudo apt install readpe```

```apk: sudo apk add pev```

```zypper: sudo zypper install readpe```

```brew: brew install readpe```

```nix: nix profile install nixpkgs#pev```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[objdump](/man/objdump)(1), [readelf](/man/readelf)(1), [file](/man/file)(1)
