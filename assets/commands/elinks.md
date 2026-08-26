# TAGLINE

功能丰富的文本模式网页浏览器

# TLDR

**在文本浏览器中打开 URL**

```elinks [https://example.com]```

**在新窗口而非标签页中打开**

```elinks -new-window [https://example.com]```

**将页面内容转储到 stdout**（非交互）

```elinks -dump [https://example.com]```

**以指定输出宽度转储**

```elinks -dump -dump-width [120] [https://example.com]```

**从书签文件打开**

```elinks [path/to/bookmarks.html]```

**以指定配置启动**

```elinks -config-dir [/path/to/config]```

**渲染来自 stdin 的 HTML**

```echo "[<h1>Hello</h1>]" | elinks -dump```

**不加载配置打开**

```elinks -no-home [https://example.com]```

# SYNOPSIS

**elinks** [_-dump_] [_-source_] [_-no-home_] [_-config-dir path_] [_url_]

# PARAMETERS

**-dump**
> 将页面渲染到 stdout 后退出（非交互）。

**-dump-width** _n_
> 转储输出的宽度（默认：80）。

**-dump-charset** _codepage_
> 格式化转储输出时使用的代码页。

**-source**
> 打印页面源码而不是渲染。

**-no-home**
> 不使用也不创建配置主目录。

**-config-dir** _path_
> 使用替代的配置目录。

**-anonymous**
> 限制为安全操作（适用于公共终端）。

**-no-connect**
> 作为独立实例运行，而不是连接到已有实例。

**-new-window**
> 在新窗口而非标签页中打开 URL。

**-remote** _command_
> 向正在运行的 ELinks 实例发送命令。

**-localhost**
> 仅限本地地址（不允许远程连接）。

**-version**
> 打印版本信息。

**-help**
> 显示帮助。

# DESCRIPTION

**ELinks** 是一款面向终端的功能丰富的文本模式网页浏览器。它渲染 HTML 页面，支持表格、框架、颜色和表单，在没有图形界面的情况下也能提供可用的网页体验。

该浏览器支持标签页浏览、书签、历史记录、Cookie、HTTP 认证和下载。导航使用键盘快捷键：**g** 跳转到 URL，**d** 下载，**Tab** 在链接之间移动，**Enter** 打开链接，**q** 退出。

ELinks 可以执行 JavaScript（编译时需包含 SpiderMonkey 支持），能在一定程度上处理 CSS 样式，其复杂布局渲染能力优于 Lynx 这类更简单的浏览器。表单（包括多选和文件上传）都能正常工作。

**-dump** 模式对脚本特别有用，可将网页转换为纯文本。结合 shell 管道，它可以实现命令行网页抓取。输出会遵循终端宽度并将表格格式化为文本。

# CONFIGURATION

**~/.elinks/elinks.conf**
> 浏览器设置和行为的主配置文件。

**~/.elinks/bookmarks**
> 存储的书签和收藏。

**~/.elinks/cookies**
> 网站的 Cookie 存储。

**~/.elinks/history**
> 浏览历史和 URL 历史。

设置管理器（在浏览器中按 **o**）提供了交互式的自定义界面。

# CAVEATS

与现代浏览器相比 JavaScript 支持有限。某些重度依赖 CSS 的网站可能无法正常显示。HTTPS 需要正确的 SSL 库支持。多标签页时内存占用可能较高。不支持 Flash 及其他插件。

# HISTORY

**ELinks** 是 **Links** 浏览器的一个分支，始于 **2001 年**，增加了标签页、鼠标支持和改进的渲染等特性。名字意为 "Extended Links"。虽然活跃开发已经放缓，它在服务器管理和以终端为中心的工作流中仍然流行。

# INSTALL

```apt: sudo apt install elinks```

```dnf: sudo dnf install elinks```

```pacman: sudo pacman -S elinks```

```apk: sudo apk add elinks```

```zypper: sudo zypper install elinks```

```nix: nix profile install nixpkgs#elinks```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[lynx](/man/lynx)(1), [w3m](/man/w3m)(1), [links](/man/links)(1), [curl](/man/curl)(1), [wget](/man/wget)(1)
