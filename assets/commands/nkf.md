# TAGLINE

转换日文文本编码

# TLDR

**转换为 UTF-8**

```nkf -w [input.txt] > [output.txt]```

**转换为 Shift-JIS**

```nkf -s [input.txt] > [output.txt]```

**转换为 EUC-JP**

```nkf -e [input.txt] > [output.txt]```

**自动检测并转换**

```nkf -w --guess [input.txt]```

**原地转换**

```nkf -w --overwrite [file.txt]```

**显示输入编码**

```nkf --guess [file.txt]```

# SYNOPSIS

**nkf** [_options_] [_files_]

# PARAMETERS

_FILES_
> 要转换的文件。

**-w**
> 转换为 UTF-8。

**-s**
> 转换为 Shift-JIS。

**-e**
> 转换为 EUC-JP。

**--guess**
> 检测编码。

**--overwrite**
> 原地修改文件。

**--help**
> 显示帮助信息。

# DESCRIPTION

**nkf**（Network Kanji Filter）用于转换日文文本编码。支持 UTF-8、Shift-JIS、EUC-JP。

该工具可自动检测编码。是处理日文文本的必备工具。

# CAVEATS

专注于日文文本。自动检测可能失败。覆盖文件前请先备份。

# HISTORY

nkf 为**日文计算**而创建，用于处理日本使用的各种编码。

# INSTALL

```apt: sudo apt install nkf```

```dnf: sudo dnf install nkf```

```zypper: sudo zypper install nkf```

```brew: brew install nkf```

```nix: nix profile install nixpkgs#nkf```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[iconv](/man/iconv)(1), [uconv](/man/uconv)(1), [recode](/man/recode)(1)
