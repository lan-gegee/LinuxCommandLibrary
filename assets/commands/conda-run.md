# TAGLINE

环境命令执行器

# TLDR

在环境中**运行命令**

```conda run -n [env_name] [command]```

在环境中**运行 Python 脚本**

```conda run -n [env_name] python [script.py]```

**实时显示输出地运行**

```conda run --live-stream -n [env_name] [command]```

# SYNOPSIS

**conda** **run** [_options_] _command_

# PARAMETERS

**-n**, **--name** _name_
> 在具名环境中运行。

**-p**, **--prefix** _path_
> 在指定路径的环境运行。

**--live-stream**
> 实时流式输出结果。

**--no-capture-output**
> 不捕获 stdout/stderr。

# CONFIGURATION

**~/.condarc**
> 用户级 conda 配置，涵盖频道、软件包设置和求解器选项。

**/opt/conda/.condarc**
> 系统级 conda 配置。

# DESCRIPTION

**conda run** 在 conda 环境内执行命令，而无需激活该环境。对于需要在不同环境中运行命令的脚本和自动化场景很有用。

# INSTALL

```dnf: sudo dnf install conda```

```nix: nix profile install nixpkgs#conda```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[conda](/man/conda)(1), [conda-activate](/man/conda-activate)(1)

# RESOURCES

```[Source code](https://github.com/conda/conda)```

```[Homepage](https://docs.conda.io)```

```[Documentation](https://docs.conda.io/projects/conda/en/stable/commands/index.html)```

<!-- verified: 2026-06-23 -->
