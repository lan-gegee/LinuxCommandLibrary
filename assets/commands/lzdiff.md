# TAGLINE

比较两个 lzip 压缩文件并显示差异

# TLDR

**比较两个 lzip 压缩文件**

```lzdiff [file1.lz] [file2.lz]```

**显示统一格式差异（unified diff）**

```lzdiff -u [file1.lz] [file2.lz]```

**显示上下文格式差异（context diff）**

```lzdiff -c [file1.lz] [file2.lz]```

# SYNOPSIS

**lzdiff** [_options_] _file1_ _file2_

# PARAMETERS

**-u**
> 统一格式差异（unified diff）。

**-c**
> 上下文格式差异（context diff）。

支持所有 diff 选项。

# DESCRIPTION

**lzdiff** 比较两个 lzip 压缩文件并显示差异。它会在比较前自动解压，相当于对解压后的内容运行 diff。选项会透传给 diff。

# INSTALL

```dnf: sudo dnf install xz```

```pacman: sudo pacman -S xz```

```apk: sudo apk add xz```

```zypper: sudo zypper install xz```

```brew: brew install xz```

```nix: nix profile install nixpkgs#xz```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[lzip](/man/lzip)(1), [lzcmp](/man/lzcmp)(1), [diff](/man/diff)(1)
