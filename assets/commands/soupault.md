# TAGLINE

HTML 原生的静态网站生成器

# TLDR

**构建站点**

```soupault```

**使用配置构建**

```soupault --config [soupault.toml]```

**强制重新构建**

```soupault --force```

**详细输出**

```soupault --verbose```

**显示版本**

```soupault --version```

**初始化项目**

```soupault --init```

# SYNOPSIS

**soupault** [_--config file_] [_--force_] [_options_]

# PARAMETERS

**--config** _FILE_
> 配置文件路径。

**--force**
> 强制重建所有页面。

**--verbose**
> 详细输出。

**--init**
> 初始化项目。

**--site-dir** _DIR_
> 站点目录。

**--build-dir** _DIR_
> 输出目录。

# DESCRIPTION

**soupault** 是一款静态网站生成器和 HTML 处理器，它直接处理 HTML 文件而非使用模板语言。它以纯 HTML 作为输入，使用 CSS 选择器操作 DOM 树，并输出修改后的 HTML，因此可以兼容任何现有的 HTML 内容。

该工具采用 TOML 配置的小部件（widget）系统来执行转换，例如向页面插入内容、生成目录表和添加元数据。自定义小部件可用 Lua 编写，以满足项目特定的处理需求。

与大多数静态网站生成器不同，soupault 不对站点结构或内容格式做任何假设。它可以直接处理现有 HTML 网站而无需转换，既适用于新项目，也适用于迁移遗留网站。

# CAVEATS

学习曲线独特。以 HTML 为中心的方法。使用 OCaml 编写。

# HISTORY

**soupault** 作为一个直接处理真实 HTML 而非模板语言的网站生成器和 HTML 处理器诞生。

# INSTALL

```apk: sudo apk add soupault```

```nix: nix profile install nixpkgs#soupault```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[hugo](/man/hugo)(1), [jekyll](/man/jekyll)(1), [pandoc](/man/pandoc)(1)
