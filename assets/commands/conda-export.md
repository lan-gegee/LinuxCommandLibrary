# TAGLINE

环境规格导出器

# TLDR

**导出当前环境**

```conda export > [environment.yml]```

**导出时不包含构建信息**

```conda export --no-builds > [environment.yml]```

仅根据**历史记录导出**

```conda export --from-history > [environment.yml]```

# SYNOPSIS

**conda** **export** [_options_]

# PARAMETERS

**-n**, **--name** _name_
> 要导出的环境名称。默认为当前活动的环境。

**-p**, **--prefix** _path_
> 要导出的环境的完整路径（**--name** 的替代方式）。

**-f**, **--file** _file_
> 将输出写入文件。格式会根据文件名自动识别。默认输出到标准输出。

**--format** _format_
> 输出格式：yaml（默认）、json、explicit 或 requirements。

**--no-builds**
> 从依赖列表中排除构建字符串，使文件更具可移植性。

**--from-history**
> 只包含显式请求的软件包，省略传递依赖。

**-c**, **--channel** _channel_
> 导出中包含的附加频道。

**--override-channels**
> 不包含来自 .condarc 的频道。

**--ignore-channels**
> 不在软件包规格前添加频道名称。

**--json**
> 以 JSON 格式报告输出，适合程序化使用。

# CONFIGURATION

**~/.condarc**
> 用户级 conda 配置，涵盖频道、软件包设置和求解器选项。

**/opt/conda/.condarc**
> 系统级 conda 配置。

# DESCRIPTION

**conda export** 默认以 YAML 格式输出当前环境的环境规格。可用于在其他系统上通过 **conda env create -f environment.yml** 重建该环境。

**conda export** 是较新的子命令，通过 **--format** 支持多种输出格式。传统的 **conda env export** 仍然受支持，并生成等价的 YAML。

使用 **--from-history** 可以获得更可移植的导出结果，其中省略了传递依赖和平台相关的构建字符串。

# INSTALL

```dnf: sudo dnf install conda```

```nix: nix profile install nixpkgs#conda```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[conda](/man/conda)(1), [conda-env](/man/conda-env)(1), [conda-list](/man/conda-list)(1)
