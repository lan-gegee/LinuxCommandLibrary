# TAGLINE

格式化 Haskell 源代码

# TLDR

**格式化文件并输出到标准输出**

```brittany [source.hs]```

从标准输入**格式化**

```cat [source.hs] | brittany```

**就地格式化**文件

```brittany --write-mode=inplace [*.hs]```

只检查格式而不修改

```brittany --check-mode [source.hs]```

使用指定的配置文件

```brittany --config-file [brittany.yaml] [source.hs]```

设置列数上限

```brittany --columns [100] [source.hs]```

# SYNOPSIS

**brittany** [_options_] [_files_]

# DESCRIPTION

**brittany** 是一款注重水平空间利用的 Haskell 源码格式化工具。它重新编排代码，在避免行过长的前提下最大化利用可用宽度。

该格式化工具以 ghc-exactprint 作为解析器，支持包括扩展在内的完整 GHC Haskell。

# PARAMETERS

**--write-mode** _mode_
> 输出模式：stdout、inplace 或 display。

**--check-mode**
> 若格式化会产生变化则以错误退出。

**--columns** _n_
> 最大行宽（默认：80）。

**--indent** _n_
> 缩进宽度（默认：2）。

**--config-file** _file_
> 使用指定的配置文件。

**--no-user-config**
> 忽略用户配置文件。

# CONFIGURATION

默认用户配置：**~/.config/brittany/config.yaml**。

项目配置：当前目录或父目录中找到的第一个 **brittany.yaml**。

可在配置中启用 GHC 扩展：
```yaml
conf_forward:
  options_ghc:
    - -XLambdaCase
    - -XMultiWayIf
```

# CAVEATS

部分不常见的 Haskell 语法元素未获完整支持。源码内注释偶尔会被移动或丢失。该项目实际上已停止维护；可考虑改用 Ormolu 或 Fourmolu。

# INSTALL

```aur: yay -S brittany```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ghc](/man/ghc)(1)
