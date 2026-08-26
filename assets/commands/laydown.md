# TAGLINE

管理配置分层

# TLDR

**创建层**

```laydown create [layer-name]```

**列出层**

```laydown list```

**应用层**

```laydown apply [layer-name]```

**移除层**

```laydown remove [layer-name]```

# SYNOPSIS

**laydown** _command_ [_options_]

# PARAMETERS

**create** _NAME_
> 创建新层。

**list**
> 列出所有层。

**apply** _NAME_
> 应用某个层。

**remove** _NAME_
> 移除某个层。

**--help**
> 显示帮助信息。

# DESCRIPTION

**laydown** 用于管理配置分层。它以可组合的层来组织设置和文件。

该工具支持模块化的配置管理。各个层可以独立地应用和移除。

# CAVEATS

针对特定配置场景。采用分层系统的思路。具体行为可能因实现而异。

# HISTORY

laydown 提供分层配置管理能力，用于组织复杂的系统环境配置。

# SEE ALSO

[stow](/man/stow)(1), [chezmoi](/man/chezmoi)(1)
