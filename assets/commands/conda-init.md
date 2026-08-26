# TAGLINE

Shell 集成初始化设置

# TLDR

为当前 shell **初始化 conda**

```conda init```

**针对特定 shell 初始化**

```conda init [bash|zsh|fish|powershell]```

**为所有 shell 初始化**

```conda init --all```

**撤销初始化**

```conda init --reverse```

# SYNOPSIS

**conda** **init** [_options_] [_shells..._]

# PARAMETERS

**--all**
> 为所有可用的 shell 初始化。

**--reverse**
> 撤销 shell 初始化。

**-d**, **--dry-run**
> 显示将要执行的操作但不实际更改。

# CONFIGURATION

**~/.condarc**
> 用户级 conda 配置，涵盖频道、软件包设置和求解器选项。

**/opt/conda/.condarc**
> 系统级 conda 配置。

# DESCRIPTION

**conda init** 为 conda 设置 shell 集成，修改 shell 配置文件以启用 **conda activate** 命令和自动激活 base 环境。

安装 conda 后必须运行一次本命令才能获得完整功能。

# CAVEATS

运行后需要重启 shell 或重新 source 配置文件。

# INSTALL

```dnf: sudo dnf install conda```

```nix: nix profile install nixpkgs#conda```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[conda](/man/conda)(1), [conda-activate](/man/conda-activate)(1)

# RESOURCES

```[Source code](https://github.com/conda/conda)```

```[Documentation](https://docs.conda.io/projects/conda/en/stable/commands/init.html)```

<!-- verified: 2026-06-22 -->
