# TAGLINE

通过在文本编辑器中编辑目标文件名来复制文件

# TLDR

**编辑文件名**并复制当前目录中匹配的文件

```qcp```

**复制指定文件**，并在 $EDITOR 中编辑其目标名称

```qcp [*.txt]```

**使用双栏格式**（源与目标显示在同一行）

```qcp --format=dual [*.jpg]```

**预览将要执行的操作**而不实际复制

```qcp --dummy [*.log]```

像 `ls -R` 一样**递归列出**

```qcp -R [src/]```

# SYNOPSIS

**qcp** [_options_] [_file_...]

# PARAMETERS

**-f**, **--format=**_FORMAT_
> 编辑格式：**destination**（默认，仅编辑新名称）、**dual**（双栏，源在左侧）或 **single**（单栏，源/目标共用一列）。

**-o**, **--options=**_OPTIONS_
> 以逗号分隔的格式选项（例如 **source-comments**、**autodetect**）。

**-i**, **--interactive**
> 编辑完成后进入命令模式提示符，而不是立即执行。

**-e**, **--editor=**_PROGRAM_
> 覆盖编辑器（默认依次为 **$VISUAL**、**$EDITOR**、**vi**）。

**--ls=**_PROGRAM_
> 使用替代的 **ls** 实现来生成文件列表。

**--dummy**
> 打印将要执行的操作，但不实际复制任何内容。

**-v**, **--verbose**
> 在每次复制执行时将其显示出来。

**--help**, **--version**
> 显示帮助或版本信息。

许多 **ls** 风格的选项会直接透传：**-a**, **-A**, **-B**, **-d**, **-r**, **-R**, **-S**, **-t**, **-u**, **-U**, **-X**, **--sort=**_WORD_, **--time=**_WORD_。

# DESCRIPTION

**qcp**（quick copy）会在 **$EDITOR** 中打开一个临时缓冲区，列出你提供的文件（未给出时则列出当前目录的内容），让你就地输入目标名称。保存并退出后，**qcp** 会将每个源文件复制到编辑后的目标位置。

它是 **qmv** 的面向复制的姊妹工具，后者出自 Oskar Liljeblad 的 **renameutils** 软件包，用于重命名。由于所有编辑都在文本编辑器中进行，常见的编辑器功能——查找替换、多光标编辑、宏——都成为强大的批量复制手段。

# CAVEATS

属于 **renameutils** 软件包的一部分。与任何"快速复制"进度条工具无关；**qcp** 不显示传输进度。默认情况下，已存在的目标文件会被直接覆盖且不作提示——如果不确定，请先使用 **--dummy**。

# INSTALL

```apt: sudo apt install renameutils```

```dnf: sudo dnf install renameutils```

```pacman: sudo pacman -S renameutils```

```zypper: sudo zypper install renameutils```

```brew: brew install renameutils```

```nix: nix profile install nixpkgs#renameutils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[qmv](/man/qmv)(1), [cp](/man/cp)(1), [mv](/man/mv)(1), [rsync](/man/rsync)(1)
