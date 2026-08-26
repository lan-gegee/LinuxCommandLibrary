# TAGLINE

可视化冲突解决工具

# TLDR

**运行合并工具**

```git mergetool```

**使用特定工具**

```git mergetool --tool=[vimdiff]```

**解决特定文件**

```git mergetool [file.txt]```

**不进行提示**

```git mergetool --no-prompt```

**使用已配置的工具**

```git mergetool -y```

# SYNOPSIS

**git mergetool** [_options_] [_file_]

# PARAMETERS

_FILE_
> 要解决的特定文件。

**--tool** _TOOL_
> 使用指定的合并工具。

**--tool-help**
> 列出可用工具。

**-y**, **--no-prompt**
> 处理每个文件前不提示。

**--prompt**
> 处理每个文件前提示。

**-g**, **--gui**
> 使用 `merge.guitool` 而非 `merge.tool`。

**--help**
> 显示帮助信息。

# DESCRIPTION

**git mergetool** 为每个存在冲突的文件运行可视化合并冲突解决工具。它会启动已配置的工具，如 vimdiff、meld 或 kdiff3，提供三方合并界面，将 base、本地和远程版本并排显示。

在工具中保存合并结果后，该文件即被标记为已解决。多个冲突文件会按顺序处理，你可以选择跳过个别文件。

# CONFIGURATION

**~/.gitconfig**
> 配置默认合并工具及各工具的专属设置。

```
[merge]
    tool = vimdiff
[mergetool]
    prompt = false
    keepBackup = false
```

# CAVEATS

需要配置好合并工具。会创建 .orig 备份文件。部分工具需另行安装。

# HISTORY

git mergetool 是 **Git** 的核心命令，提供对外部合并工具的集成，对复杂冲突解决至关重要。

# INSTALL

```apt: sudo apt install git```

```dnf: sudo dnf install git```

```pacman: sudo pacman -S git```

```apk: sudo apk add git```

```zypper: sudo zypper install git```

```brew: brew install git```

```nix: nix profile install nixpkgs#git```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[git-merge](/man/git-merge)(1), [git-difftool](/man/git-difftool)(1), [vimdiff](/man/vimdiff)(1)

# RESOURCES

```[Source code](https://github.com/git/git)```

```[Homepage](https://git-scm.com/)```

```[Documentation](https://git-scm.com/docs/git-mergetool)```

<!-- verified: 2026-07-17 -->
