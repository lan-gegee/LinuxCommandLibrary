# TAGLINE

激活一个 conda 环境

# TLDR

**激活环境**

```conda activate [env_name]```

**激活**指定路径下的**环境**

```conda activate [/path/to/env]```

**激活 base 环境**

```conda activate base```

**激活**环境并确认其已生效

```conda activate [env_name] && conda info --envs```

# SYNOPSIS

**conda** **activate** [_env_name_|_path_]

# DESCRIPTION

**conda activate** 将当前 shell 会话切换为使用指定的 conda 环境，它会修改 PATH 环境变量及其他 shell 变量，使该环境的二进制文件、库和软件包获得优先权。这是使用隔离 conda 环境的主要机制。

环境被激活后，shell 提示符通常会被修改，以括号形式显示当前活动的环境名称，直观地提示当前正在使用哪个环境。激活过程会将环境的 bin 目录置于 PATH 最前面，设置 CONDA_PREFIX 和 CONDA_DEFAULT_ENV 等环境专属变量，并可能执行某些软件包附带的激活脚本。

conda 环境可以按名称激活（如果存放在默认的 envs 目录中），也可以通过环境目录的完整路径激活。base 环境是 conda 的根环境，默认会被自动激活，除非在 conda 配置中禁用了 auto_activate_base。必须先通过 conda init 初始化 shell 集成，激活功能才能在 bash、zsh、fish 或 PowerShell 中正常工作。

# CAVEATS

需要先运行 conda init 完成 shell 集成。某些 shell 可能需要手动 source 激活脚本。

# INSTALL

```dnf: sudo dnf install conda```

```nix: nix profile install nixpkgs#conda```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[conda](/man/conda)(1), [conda-deactivate](/man/conda-deactivate)(1), [conda-create](/man/conda-create)(1), [conda-env](/man/conda-env)(1), [conda-init](/man/conda-init)(1)
