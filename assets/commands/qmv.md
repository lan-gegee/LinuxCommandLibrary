# TAGLINE

通过在文本编辑器中编辑文件名来重命名文件

# TLDR

在编辑器中**重命名列出的文件**（双栏，默认）

```qmv [files]```

**重命名当前目录中的所有内容**

```qmv *```

为本次运行**指定编辑器**

```qmv -e [vim] [files]```

**使用单栏格式**（源与目标交替成行）

```qmv -f sc [files]```

**使用仅目标格式**

```qmv -f do [files]```

**试运行**：显示将要发生的更改而不实际重命名

```qmv --dummy [files]```

**详细输出**

```qmv -v [files]```

# SYNOPSIS

**qmv** [_options_] [_files_...]

# PARAMETERS

**-f**, **--format=**_FORMAT_
> 要使用的编辑格式：`dc`（双栏，默认）、`sc`（单栏）或 `do`（仅目标）。

**-o**, **--options=**_OPTIONS_
> 向所选编辑格式传递逗号分隔的选项（如 `swap`、`blank`、`autowidth`）。用 `--options=help` 查看列表。

**-e**, **--editor=**_PROGRAM_
> 用于打开文件列表的文本编辑器。依次回退到 `$VISUAL`、`$EDITOR`，再回退到内置默认值。

**--command=**_COMMAND_
> 使用 _COMMAND_ 执行重命名，而不是 `mv`。

**--ls=**_PROGRAM_
> 用于列出目录内容的 `ls` 程序路径。

**-i**, **--interactive**
> 以命令模式启动，而不是立即调用编辑器。

**-v**, **--verbose**
> 在每次重命名执行时将其打印出来。

**--dummy**
> 除实际重命名外照常执行一切（试运行）。

**--help**
> 显示选项摘要。

**--version**
> 显示版本信息。

# FORMATS

**dc** — 双栏（默认）：源在左，目标在右。只编辑右侧。
**sc** — 单栏：源与目标交替成行。
**do** — 仅目标：每行一个目标名称；依赖文件顺序与源列表一致。

# DESCRIPTION

**qmv**（quick move）会在文本编辑器中打开文件名列表，让你通过编辑目标列来批量重命名。编辑器退出后，qmv 会将编辑后的文件与原始文件比较，并将每处变化应用为一次重命名。这样你就能用熟悉的编辑器功能——查找替换、宏、多光标——进行批量重命名。

qmv 会检测潜在冲突（循环、碰撞），并通过中间重命名来解决。如果目标已存在，覆盖前会提示确认。

# CAVEATS

属于 **renameutils** 软件包的一部分。编辑器必须是基于文本的。默认 `dc` 格式下不要编辑源列——只能改目标一侧。未列出的目录内的重命名不会被应用。

# HISTORY

**qmv** 属于由 **Oskar Liljeblad** 开发并以 GPL 发布的 **renameutils** 软件包。配套工具 **qcp** 以相同的工作流复制文件。

# INSTALL

```apt: sudo apt install renameutils```

```dnf: sudo dnf install renameutils```

```pacman: sudo pacman -S renameutils```

```zypper: sudo zypper install renameutils```

```brew: brew install renameutils```

```nix: nix profile install nixpkgs#renameutils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[qcp](/man/qcp)(1), [rename](/man/rename)(1), [mmv](/man/mmv)(1), [vidir](/man/vidir)(1), [mv](/man/mv)(1)
