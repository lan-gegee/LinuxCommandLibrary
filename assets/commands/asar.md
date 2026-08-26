# TAGLINE

打包和提取 Electron 应用归档。

# TLDR

**创建** asar 归档

```asar pack [dir/] [output.asar]```

**提取** asar 归档

```asar extract [archive.asar] [output_dir/]```

**列出**内容

```asar list [archive.asar]```

提取**单个文件**

```asar extract-file [archive.asar] [path/in/archive] [output_file]```

打包时将部分文件保持为**不打包**状态

```asar pack [dir/] [output.asar] --unpack [*.node]```

# SYNOPSIS

**asar** _pack_|_extract_|_list_|_extract-file_ [_options_] _arguments_

# DESCRIPTION

**asar** 用于创建和提取 Electron 归档文件。ASAR（Atom Shell Archive）是一种类似 tar 的格式，Electron 应用用它把源文件打包成单个文件，同时保持随机访问能力。

这种格式让 Electron 无需解包即可直接从归档中读取文件，从而缩短加载时间。该工具以 **@electron/asar** 的名义发布在 npm 上（前身为独立的 **asar** 软件包）。

# PARAMETERS

**pack** _dir_ _output_（别名 **p**）
> 从目录创建归档

**extract** _archive_ _dest_（别名 **e**）
> 将归档提取到目录

**list** _archive_（别名 **l**）
> 列出归档内容

**extract-file** _archive_ _file_ _dest_（别名 **ef**）
> 提取单个文件

**--unpack** _glob_
> 让匹配 glob 的文件保持不打包状态（存放在同级的 app.asar.unpacked 目录）

**--unpack-dir** _glob_
> 让匹配 glob 的目录保持不打包状态

**--exclude-hidden**
> 将隐藏文件（点文件）排除在归档之外

**--ordering** _file_
> 按给定文件中所列的顺序打包文件

# CAVEATS

ASAR 归档未加密，其内容很容易被提取。某些 Electron 应用可能对自身归档做完整性校验。不适合存放敏感数据。

# HISTORY

**ASAR** 为 Atom 文本编辑器（即后来的 Electron 框架）而开发，用于高效地打包 Node.js 应用。

# INSTALL

```pacman: sudo pacman -S asar```

```zypper: sudo zypper install asar```

```nix: nix profile install nixpkgs#asar```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[tar](/man/tar)(1), [npm](/man/npm)(1), [electron](/man/electron)(1)

# RESOURCES

```[Source code](https://github.com/electron/asar)```

```[Homepage](https://www.electronjs.org)```

<!-- verified: 2026-06-16 -->
