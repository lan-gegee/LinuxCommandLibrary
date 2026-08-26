# TAGLINE

dotfiles 引导自动化工具

# TLDR

使用配置**安装 dotfiles**

```dotbot -c [install.conf.yaml]```

**指定 dotfiles 目录**

```dotbot -d [~/dotfiles] -c [install.conf.yaml]```

**以详细输出运行**

```dotbot -v -c [install.conf.yaml]```

**使用指定插件**

```dotbot -p [plugin.py] -c [install.conf.yaml]```

**只运行特定指令**

```dotbot -c [install.conf.yaml] --only [link shell]```

**运行除指定指令外的所有指令**

```dotbot -c [install.conf.yaml] --except [shell]```

# SYNOPSIS

**dotbot** [_options_] **-c** _config_

# PARAMETERS

**-c**, **--config-file** _file_
> 配置文件（YAML 或 JSON）。

**-d**, **--base-directory** _dir_
> dotfiles 的基准目录。

**-p**, **--plugin** _plugin_
> 加载插件模块。

**-v**, **--verbose**
> 启用详细输出。

**-q**, **--quiet**
> 抑制大部分输出。

**-Q**, **--super-quiet**
> 抑制几乎所有输出。

**--plugin-dir** _dir_
> 加载某个目录下的所有插件。

**--only** _directives_
> 只运行指定的指令。

**--except** _directives_
> 运行除指定指令之外的所有指令。

**--no-color**
> 禁用彩色输出。

**--force-color**
> 强制彩色输出。

**--version**
> 显示版本。

# DESCRIPTION

**Dotbot** 是一个用于引导 dotfiles 的工具。它通过创建符号链接、运行 shell 命令以及执行 YAML 或 JSON 文件中定义的其他配置任务，自动完成新机器的环境搭建。

配置文件定义各种指令，如 **link**（创建符号链接）、**shell**（运行命令）、**create**（创建目录）和 **clean**（清除失效符号链接）。Dotbot 通常作为 git 子模块包含在 dotfiles 仓库中。

# CONFIGURATION EXAMPLE

```yaml
- link:
    ~/.bashrc: bashrc
    ~/.vimrc: vimrc
    ~/.config/nvim: nvim

- shell:
    - [git submodule update --init, Installing submodules]
    - command: ./install-packages.sh
      description: Installing packages

- create:
    - ~/.local/bin
    - ~/.config
```

# CAVEATS

需要 Python 3。创建符号链接可能需要相应权限。链接目标处已有的文件默认不会被覆盖。插件系统支持扩展但会增加复杂度。

# HISTORY

Dotbot 由 **Anish Athalye** 于 **2014 年**创建，是一个简洁、自包含的 dotfiles 管理工具。它被设计为以 git 子模块的形式包含，使 dotfiles 仓库除 Python 之外无需外部依赖即可自我引导。

# INSTALL

```brew: brew install dotbot```

```nix: nix profile install nixpkgs#dotbot```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[stow](/man/stow)(1), [chezmoi](/man/chezmoi)(1), [yadm](/man/yadm)(1), [ln](/man/ln)(1)
