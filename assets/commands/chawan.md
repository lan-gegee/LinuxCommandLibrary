# TAGLINE

文本模式网页浏览器与终端分页器

# TLDR

在终端浏览器中**打开**网站

```cha [example.org]```

**查看** Markdown 文件

```cha [README.md]```

以无头模式将网页**转储**到 stdout

```cha -d [https://example.org]```

以可视化模式打开主页

```cha -V```

通过管道输入 HTML 内容并指定其内容类型

```cat [file.html] | cha -T text/html```

临时**覆盖**某个配置选项

```cha -o display.color-mode=eight-bit [example.org]```

# SYNOPSIS

**cha** [_options_] [_URL(s) or file(s)..._]

# PARAMETERS

**-c**, **--css** _stylesheet_
> 将 CSS 样式表临时附加到用户样式表。

**-d**, **--dump**
> 无头模式；将打开的文件依次输出到 stdout。当 stdout 不是 tty 时隐式启用。

**-o**, **--opt** _config_
> 传递临时的 TOML 配置选项。

**-r**, **--run** _script_
> 执行 JavaScript 字符串或文件；.mjs 文件作为 ES 模块运行。

**-v**, **--version**
> 显示版本并退出。

**-C**, **--config** _file_
> 覆盖默认配置文件的搜索路径。

**-I**, **--input-charset** _charset_
> 覆盖所有文件的输入字符集。

**-M**, **--monochrome**
> 强制单色输出。

**-O**, **--output-charset** _charset_
> 覆盖输出字符集。

**-T**, **--type** _content-type_
> 覆盖所有输入文件的内容类型。

**-V**, **--visual**
> 以可视化模式启动，打开所配置的主页。

**-h**, **--help**
> 输出帮助并退出。

# DESCRIPTION

**Chawan**（日语意为"茶碗"）是一个文本模式网页浏览器和终端分页器，拥有用 Nim 从零构建的自主浏览器引擎。尽管是终端浏览器，它能以接近图形浏览器的布局保真度显示许多网站。

其特性包括：支持多种编码的 HTML5、支持流式布局、表格和 flexbox 的 CSS 布局引擎、通过 Sixel 或 Kitty 图形协议显示内联图像（默认禁用）、通过 QuickJS 提供的可选 JavaScript（默认禁用），以及对 HTTP(S)、FTP、Gopher、Gemini、Finger 和 Spartan 的多协议支持。它使用类似 vi(m) 的按键绑定，支持鼠标输入，具有支持增量文档加载的多进程架构，并在 FreeBSD、OpenBSD 和 Linux 上提供 syscall 沙箱隔离。

# CONFIGURATION

基于 TOML 的配置按以下顺序查找：**-C** 参数指定的路径、**$CHA_DIR/config.toml**、**${XDG_CONFIG_HOME:-~/.config}/chawan/config.toml** 或 **~/.chawan/config.toml**。

# CAVEATS

JavaScript 和内联图像默认禁用，必须显式启用。需要类 Unix 操作系统（Linux、FreeBSD、OpenBSD、macOS、Haiku）；Windows 用户必须使用 WSL。从源码构建需要 Nim 编译器 2.0.0+、OpenSSL/LibreSSL 和 libssh2。

# HISTORY

**Chawan** 由 **bptato** 开发，用 Nim 编写。它受 **w3m** 启发，但不共享任何代码，不过 UI 和功能集与之相似。当前版本为 v0.3.3，采用公有领域许可（UNLICENSE）。可在 Alpine Linux、Arch Linux (AUR)、FreeBSD、Homebrew、NixOS 和 Void Linux 中获取。

# INSTALL

```pacman: sudo pacman -S chawan```

```zypper: sudo zypper install chawan```

```brew: brew install chawan```

```nix: nix profile install nixpkgs#chawan```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[w3m](/man/w3m)(1), [lynx](/man/lynx)(1), [links](/man/links)(1), [elinks](/man/elinks)(1)
