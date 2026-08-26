# TAGLINE

文件与目录比较及合并工具

# TLDR

**比较两个文件**

```kdiff3 [file1] [file2]```

**三方比较**

```kdiff3 [base] [file1] [file2]```

**比较目录**

```kdiff3 [dir1] [dir2]```

**合并并输出结果**

```kdiff3 [base] [file1] [file2] -o [merged]```

**自动选择无冲突的变更**

```kdiff3 [base] [file1] [file2] --auto```

# SYNOPSIS

**kdiff3** [_options_] [_files/directories_...]

# PARAMETERS

**-o** _file_
> 输出合并后的文件。

**--auto**
> 自动选择非冲突的变更。

**-m**, **--merge**
> 合并模式。

**--cs** _setting=value_
> 配置设置项。

**--qall**
> 安静模式（仅自动模式）。

**-L1**, **-L2**, **-L3** _label_
> 输入内容的标签。

# DESCRIPTION

**KDiff3** 是一个文件与目录比较及合并工具。它支持双向和三方比较，适合解决合并冲突和审阅变更。

KDiff3 用颜色高亮差异，并允许为每个冲突选择要采用的版本。它可以作为合并工具集成到版本控制系统中。

# GIT INTEGRATION

```bash
# Configure as merge tool
git config --global merge.tool kdiff3
git config --global mergetool.kdiff3.path /usr/bin/kdiff3

# Configure as diff tool
git config --global diff.tool kdiff3
```

# CAVEATS

需要 KDE 库。三方合并需要共同祖先。大文件可能较慢。不比较二进制文件。

# HISTORY

KDiff3 由 **Joachim Eibl** 创建，是一个用于比较和合并文件的 Qt/KDE 应用。它是解决版本控制冲突的热门选择。

# INSTALL

```apt: sudo apt install kdiff3```

```dnf: sudo dnf install kdiff3```

```pacman: sudo pacman -S kdiff3```

```apk: sudo apk add kdiff3```

```zypper: sudo zypper install kdiff3```

```nix: nix profile install nixpkgs#kdiff3```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[diff](/man/diff)(1), [meld](/man/meld)(1), [vimdiff](/man/vimdiff)(1), [git-mergetool](/man/git-mergetool)(1)
