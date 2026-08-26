# TAGLINE

轻量级极简网页浏览器

# TLDR

**启动 Dillo** 浏览器

```dillo```

**打开一个 URL**

```dillo [https://example.com]```

**打开本地 HTML** 文件

```dillo [file.html]```

**以全窗口模式打开**（隐藏地址栏、菜单和按钮）

```dillo -f [url]```

**以指定的窗口几何尺寸打开**

```dillo -g [800x600] [url]```

**以本地模式打开**（不加载远程图片，不跟随重定向）

```dillo -l [path/to/file.html]```

# SYNOPSIS

**dillo** [_options_] [_URL_|_file_]

# PARAMETERS

_URL_
> 要打开的网址。

_FILE_
> 要打开的本地 HTML 文件。

**-f**, **--fullwindow**
> 以全窗口模式启动，隐藏地址栏、导航按钮、菜单和状态栏。

**-g** _WxH[+X+Y]_
> 窗口几何尺寸（宽 x 高及可选位置）。

**-l**, **--local**
> 不加载远程图片或样式表，也不跟随重定向。

**-v**, **--version**
> 显示版本信息。

**-h**, **--help**
> 显示帮助信息。

# CONFIGURATION

**~/.dillo/dillorc**
> 主配置文件，用于浏览器偏好、字体和行为设置。

**~/.dillo/keysrc**
> 键盘快捷键映射。

**~/.dillo/domainrc**
> 针对特定域名的规则与设置。

# DESCRIPTION

**Dillo** 是一个用 C 语言编写、基于 FLTK 工具包的快速小巧且资源占用低的网页浏览器。它将速度和隐私置于功能完整性之上，适合老旧硬件或极简环境。

该浏览器有条件地支持 HTML 4.01 和 CSS 2.1，专注于核心浏览功能。它不包含 JavaScript 支持，这提升了性能并缩小了攻击面，但也限制了对现代网站的兼容性。

Dillo 具备标签页浏览、书签和表单处理功能。其极低的资源占用使它在嵌入式系统、老旧电脑以及偏爱轻量应用的用户中很有价值。

# CAVEATS

不支持 JavaScript 限制了对现代网站的兼容性。CSS 支持不完整。没有插件系统。HTTPS 支持可能需要额外的库。媒体播放能力有限。

# HISTORY

Dillo 由 **Jorge Arellano Cid** 于 **1999** 年发起。开发重点一直是打造能在低资源系统上运行的极简浏览器。经历数段沉寂期后，该项目目前由社区维护。

# INSTALL

```apt: sudo apt install dillo```

```dnf: sudo dnf install dillo```

```pacman: sudo pacman -S dillo```

```apk: sudo apk add dillo```

```brew: brew install dillo```

```nix: nix profile install nixpkgs#dillo```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[firefox](/man/firefox)(1), [links](/man/links)(1), [lynx](/man/lynx)(1), [surf](/man/surf)(1)
