# TAGLINE

删除文件和目录

# TLDR

**删除一个文件**

```rm [file]```

**删除多个文件**

```rm [file1] [file2] [file3]```

**删除文件前进行确认提示**

```rm -i [file]```

**递归删除目录及其内容**

```rm -r [directory]```

**强制删除而不确认**

```rm -f [file]```

**强制递归删除目录**（危险）

```rm -rf [directory]```

**详细模式删除文件**（显示正在删除的内容）

```rm -v [file]```

**删除匹配模式的文件**

```rm *.tmp```

# SYNOPSIS

**rm** [**-firvd**] _file_...

# PARAMETERS

**-f**, **--force**
> 忽略不存在的文件，从不提示。

**-i**
> 每次删除前都提示。

**-I**
> 在删除超过 3 个文件或递归删除前提示一次。

**-r**, **-R**, **--recursive**
> 递归删除目录及其内容。

**-d**, **--dir**
> 删除空目录。

**-v**, **--verbose**
> 解释正在进行的操作。

**--no-preserve-root**
> 不对 '/' 做特殊处理（危险）。

**--preserve-root**
> 不删除 '/'（默认）。

**--one-file-system**
> 递归删除时跳过位于其他文件系统上的目录。

# DESCRIPTION

**rm** 用于删除文件和目录。默认情况下它不会删除目录；请使用 **-r** 递归删除目录。

不带 **-f** 时，rm 在删除写保护的文件前会请求确认。使用 **-i** 则对每个文件都提示。**-I** 选项提供了一个折中方案，只在潜在危险操作时提示一次。

要删除以短横线开头的文件，可使用 **--** 终止选项解析：**rm -- -filename**，或使用路径形式：**rm ./-filename**。

该命令将文件从文件系统中解除链接。在被覆盖之前，数据仍可能被恢复。如需安全删除，请使用 **shred**。

# CAVEATS

**rm -rf /** 或类似命令可能摧毁整个系统。现代系统对此有保护，但某些变体可能绕过保护。

被删除的文件不会进入回收站。如果可能需要恢复，请使用 **trash-cli** 或桌面回收站。

使用通配符时要小心。在错误的目录中执行 **rm \*** 是毁灭性的。可用 **ls** 预览将被删除的内容。

root 用户使用 **rm** 时应格外谨慎。可以考虑设置默认附加 **-i** 的别名。

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

[rmdir](/man/rmdir)(1), [unlink](/man/unlink)(1), [shred](/man/shred)(1), [trash-cli](/man/trash-cli)(1)
