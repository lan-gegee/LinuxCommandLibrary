# TAGLINE

环境重命名工具

# TLDR

**重命名一个环境**

```conda rename -n [old_name] [new_name]```

# SYNOPSIS

**conda** **rename** [_options_] _new_name_

# PARAMETERS

**-n**, **--name** _name_
> 要重命名的环境的当前名称。

**-p**, **--prefix** _path_
> 要重命名的环境的当前路径。

# CONFIGURATION

**~/.condarc**
> 用户级 conda 配置，涵盖频道、软件包设置和求解器选项。

**/opt/conda/.condarc**
> 系统级 conda 配置。

# DESCRIPTION

**conda rename** 更改现有 conda 环境的名称。其实现方式是将环境克隆到新名称下，然后移除旧环境。

# CAVEATS

重命名前必须先停用该环境。

# SEE ALSO

[conda](/man/conda)(1), [conda-create](/man/conda-create)(1)

# RESOURCES

```[Source code](https://github.com/conda/conda)```

```[Documentation](https://docs.conda.io/projects/conda/en/stable/commands/rename.html)```

<!-- verified: 2026-06-22 -->
