# TAGLINE

面向结构化数据的交互式 TUI 树形查看器

# TLDR

**查看 JSON 文件**

```otree [path/to/file.json]```

**从 stdin 查看 YAML**

```cat [file.yaml] | otree```

**查看 TOML 文件**

```otree [path/to/file.toml]```

**查看 XML 文件**

```otree [path/to/file.xml]```

# SYNOPSIS

**otree** [_options_] [_file_]

# PARAMETERS

**--debug**
> 将调试日志写入文件。

**-h**, **--help**
> 显示帮助信息。

**-V**, **--version**
> 显示版本信息。

# DESCRIPTION

**otree** 是一款命令行工具，可在交互式 TUI 树形控件中查看结构化数据对象（JSON、YAML、TOML、XML）。它的设计目标是处理嵌套很深的 Kubernetes YAML 文件及类似的复杂配置。它支持切换根节点、缩放和剪贴板操作。

导航键和颜色可通过 **~/.config/otree.toml** 配置。

# CAVEATS

仅支持结构化数据格式（JSON、YAML、TOML、XML）。纯文本文件无法显示。

# HISTORY

**otree** 由 **fioncat** 创建，使用 **Rust** 编写。

# INSTALL

```apk: sudo apk add otree```

```brew: brew install otree```

```nix: nix profile install nixpkgs#otree```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[jq](/man/jq)(1), [yq](/man/yq)(1), [jnv](/man/jnv)(1), [fx](/man/fx)(1)
