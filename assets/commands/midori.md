# TAGLINE

轻量级网页浏览器

# TLDR

**打开浏览器**

```midori```

**打开 URL**

```midori [https://example.com]```

**隐私浏览**

```midori --private```

**打开文件**

```midori [file.html]```

**新建窗口**

```midori --new-window [url]```

**便携模式**

```midori --portable```

# SYNOPSIS

**midori** [_options_] [_urls_]

# PARAMETERS

_URLS_
> 要打开的 URL。

**--private**
> 隐私浏览模式。

**--new-window**
> 打开新窗口。

**--portable**
> 便携模式。

**--version**
> 显示版本。

**--help**
> 显示帮助信息。

# DESCRIPTION

**midori** 是一个轻量级网页浏览器。它的设计目标是低资源占用。

该工具基于 WebKitGTK。适用于老旧硬件和精简系统。

# CAVEATS

基于 WebKitGTK。扩展支持有限。可能无法正确渲染所有网站。

# HISTORY

Midori 作为面向 Xfce 及其他精简环境的轻量级 **GTK+** 网页浏览器而诞生。

# SEE ALSO

[firefox](/man/firefox)(1), [surf](/man/surf)(1)
