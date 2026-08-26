# TAGLINE

已安装软件包查看器

# TLDR

在当前环境中**列出软件包**

```conda list```

在指定环境中**列出软件包**

```conda list -n [env_name]```

**列出**匹配模式的软件包

```conda list [pattern]```

**以修订版本显示**

```conda list --revisions```

**导出到文件**

```conda list --export > [packages.txt]```

# SYNOPSIS

**conda** **list** [_options_] [_regex_]

# PARAMETERS

**-n**, **--name** _name_
> 列出具名环境中的软件包。

**--export**
> 以适用于 conda create --file 的格式输出。

**--revisions**
> 列出修订历史。

**--json**
> 以 JSON 格式输出。

# CONFIGURATION

**~/.condarc**
> 用户级 conda 配置，涵盖频道、软件包设置和求解器选项。

**/opt/conda/.condarc**
> 系统级 conda 配置。

# DESCRIPTION

**conda list** 显示 conda 环境中已安装的软件包。默认显示当前活动环境中的软件包。

可使用正则表达式模式过滤列表。

# INSTALL

```dnf: sudo dnf install conda```

```nix: nix profile install nixpkgs#conda```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[conda](/man/conda)(1), [conda-search](/man/conda-search)(1), [conda-info](/man/conda-info)(1)

# RESOURCES

```[Source code](https://github.com/conda/conda)```

```[Documentation](https://docs.conda.io/projects/conda/en/stable/commands/list.html)```

<!-- verified: 2026-06-22 -->
