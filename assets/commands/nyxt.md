# TAGLINE

以键盘为中心的网页浏览器

# TLDR

**启动浏览器**

```nyxt```

**打开 URL**

```nyxt [https://example.com]```

**带配置启动**

```nyxt --config [config.lisp]```

**以无头模式启动**

```nyxt --headless```

# SYNOPSIS

**nyxt** [_options_] [_url_]

# PARAMETERS

_URL_
> 要打开的 URL。

**--config** _FILE_
> 使用指定的配置文件。

**--headless**
> 无图形界面运行。

**--script** _FILE_
> 执行 Lisp 脚本。

**--help**
> 显示帮助信息。

**--version**
> 显示版本。

# DESCRIPTION

**nyxt** 是一款以键盘为中心的网页浏览器，可通过 Common Lisp 扩展。

该浏览器具有可编程的快捷键绑定和命令，设计灵感来自 Emacs 和 Vim。

# CAVEATS

使用 Common Lisp 配置。自定义有一定学习成本。后端为 WebKitGTK。

# HISTORY

Nyxt 的诞生是为了给高级用户提供一款**键盘驱动的浏览器**，灵感来自 Emacs。

# INSTALL

```pacman: sudo pacman -S nyxt```

```apk: sudo apk add nyxt```

```zypper: sudo zypper install nyxt```

```nix: nix profile install nixpkgs#nyxt```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[firefox](/man/firefox)(1), [qutebrowser](/man/qutebrowser)(1), [surf](/man/surf)(1)
