# TAGLINE

用于 dotfiles 的符号链接农场管理器

# TLDR

**Stow 软件包**（创建符号链接）

```stow [package]```

**Stow 到指定目标**

```stow -t [/target/directory] [package]```

**Unstow 软件包**（移除符号链接）

```stow -D [package]```

**Restow**（先 unstow 再 stow）

```stow -R [package]```

**模拟 stow**（dry run）

```stow -n [package]```

**以详细输出执行 stow**

```stow -v [package]```

**从指定目录执行 stow**

```stow -d [/path/to/stow/dir] [package]```

**收编现有文件**

```stow --adopt [package]```

# SYNOPSIS

**stow** [_options_] _package_...

# DESCRIPTION

**stow** 是一个符号链接农场管理器，它创建从源目录树到目标目录的符号链接。它常用于管理 dotfiles、整理安装在 /usr/local 中的软件以及维护配置文件。

软件包是按其在目标位置应有的结构组织文件的目录。stow 在目标目录中创建指向软件包目录内文件的符号链接，并保持目录结构。

在 dotfiles 管理方面，stow 目录通常镜像主目录结构，从而可以对配置进行版本控制，同时通过符号链接使其保持生效。

# PARAMETERS

**-d** _dir_, **--dir=** _dir_
> Stow 目录（默认为当前目录）。

**-t** _dir_, **--target=** _dir_
> 目标目录（默认为 stow 目录的父目录）。

**-S**, **--stow**
> Stow 软件包（默认操作）。

**-D**, **--delete**
> Unstow 软件包。

**-R**, **--restow**
> Restow（先 unstow 再 stow）。

**-n**, **--no**, **--simulate**
> 演练运行，不做任何更改。

**-v**, **--verbose**
> 增加输出详细程度。

**--adopt**
> 将现有文件收编进软件包。

**--ignore=** _regex_
> 忽略匹配模式的文件。

**--defer=** _regex_
> 让位于现有文件。

**--override=** _regex_
> 覆盖现有文件。

# CAVEATS

不会自动处理冲突。目标目录必须存在。默认情况下符号链接指向绝对路径。某些应用程序不能正确处理符号链接。adopt 模式会移动文件，可能引发问题。

# HISTORY

**GNU Stow** 由 **Bob Glickstein** 于 **1993 年**编写，用于管理编译到独立目录中的软件。它最初是为 /usr/local/stow 组织方式设计的。后来该工具被 dotfiles 管理社区采用，用于组织纳入版本控制的配置文件。

# INSTALL

```dnf: sudo dnf install stow```

```pacman: sudo pacman -S stow```

```apk: sudo apk add stow```

```zypper: sudo zypper install stow```

```brew: brew install stow```

```nix: nix profile install nixpkgs#stow```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ln](/man/ln)(1), [dotfiles](/man/dotfiles)(1), [chezmoi](/man/chezmoi)(1), [yadm](/man/yadm)(1)
