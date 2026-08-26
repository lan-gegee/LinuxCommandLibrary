# TAGLINE

从文本或邮件中提取并浏览 URL

# TLDR

**从邮件中提取 URL**

```urlscan < [email.txt]```

**将内容通过管道传给 urlscan**

```cat [file.txt] | urlscan```

**紧凑列表视图**

```urlscan -c < [email.txt]```

**打印 URL 而不打开浏览器**

```urlscan -n < [email.txt]```

**去除重复的 URL**

```urlscan -d < [email.txt]```

**对 URL 执行自定义命令**

```urlscan --run "[wget {}]" < [email.txt]```

**生成配置文件**

```urlscan --genconf```

# SYNOPSIS

**urlscan** [_options_] < _message_

# PARAMETERS

**-c**, **--compact**
> 显示不带上下文的简单列表。

**-d**, **--dedupe**
> 去除重复的 URL。

**-n**, **--no-browser**
> 把 URL 打印到 stdout，不进入交互模式。

**-r**, **--run** _command_
> 以 URL 作为参数运行命令（使用 {} 占位符）。

**-f**, **--run-safe** _command_
> 以安全方式将 URL 传给命令运行。

**-p**, **--pipe**
> 通过管道而非参数把 URL 传给命令。

**-R**, **--reverse**
> 反转显示顺序。

**-s**, **--single**
> 打开一个 URL 后即退出。

**-w**, **--width** _n_
> 设置显示宽度。

**-W**, **--whitespace-off**
> 压缩显示输出。

**-H**, **--nohelp**
> 启动时隐藏帮助页眉。

**-g**, **--genconf**
> 生成默认配置文件。

**-E**, **--regex** _pattern_
> 用于 URL 提取的自定义正则表达式。

# KEYBOARD SHORTCUTS

**Enter**: 在浏览器中打开 URL

**c**: 切换上下文视图

**C**: 复制 URL 到剪贴板

**P**: 复制 URL 到主选择区

**R**: 反转 URL 顺序

**q**: 退出

**F1**: 显示帮助

# DESCRIPTION

**urlscan** 从邮件消息或文本文件中提取 URL，并在交互式终端界面中展示。它主要是为配合 mutt 及其他终端邮件客户端而设计的。

该工具解析输入内容中的 URL，并将它们连同上下文一并呈现在一个可导航的列表里。你可以用浏览器打开 URL、复制到剪贴板，或者传给自定义命令处理。

配置保存在 ~/.config/urlscan/config.json 中。可通过 --regex 定义自定义 URL 匹配模式，实现特定的提取需求。

# CAVEATS

只能从 stdin 读取输入。主要为邮件消息设计。不借助自定义正则表达式时，某些 URL 形式可能无法识别。打开浏览器时使用 Python webbrowser 模块或 xdg-open。

# HISTORY

**urlscan** 作为 urlview 的替代品而诞生，提供了更强的 URL 提取能力和更现代的界面。它与 mutt 以及其他基于终端的邮件阅读器集成良好，延续了 Unix 传统。

# INSTALL

```dnf: sudo dnf install urlscan```

```pacman: sudo pacman -S urlscan```

```apk: sudo apk add urlscan```

```zypper: sudo zypper install urlscan```

```brew: brew install urlscan```

```nix: nix profile install nixpkgs#urlscan```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[mutt](/man/mutt)(1), [urlview](/man/urlview)(1), [xdg-open](/man/xdg-open)(1)
