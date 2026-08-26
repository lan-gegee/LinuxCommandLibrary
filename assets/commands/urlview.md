# TAGLINE

从文本文件中交互式选取 URL

# TLDR

**从文件提取 URL**并显示交互式菜单

```urlview [path/to/file]```

**从多个文件提取 URL**

```urlview [file1] [file2] [file3]```

**从 stdin 提取 URL**（例如由 mutt 管道传入）

```cat [path/to/email.txt] | urlview```

用连字符显式**从 stdin 读取**

```command | urlview -```

**跳转到 URL 列表中的指定行号**

```urlview -[5] [path/to/file]```

# SYNOPSIS

**urlview** _filename_ [_filename_...]

# PARAMETERS

_filename_
> 一个或多个待扫描 URL 的文本文件。未指定文件时从 stdin 读取。可用 `-` 显式指定从 stdin 读取。

**-**_number_
> 跳转到 URL 列表中的指定行号。

# DESCRIPTION

**urlview** 是一个面向屏幕的工具，它从文本文件中提取 URL，并显示一个交互式菜单以便在浏览器中打开。它使用正则表达式扫描输入来识别 URL，然后呈现一份可导航的列表。

该工具常与 **mutt** 等终端邮件客户端配合使用，方便用户快速访问邮件内嵌的链接。当从菜单中选中某个 URL 时，urlview 会调用已配置的浏览器或 URL 处理程序。

配置从 ~/.urlview 或 /etc/urlview/system.urlview 读取。配置文件支持以下指令：REGEXP（自定义 URL 匹配模式）、COMMAND（URL 启动命令，含 %s 占位符）、WRAP（yes/no，控制长 URL 是否折行）、QUITONLAUNCH（启动某个 URL 后退出）。

默认的处理程序是 url_handler.sh，但可以用 BROWSER 环境变量将其覆盖为某个浏览器命令，或一组以冒号分隔、依次尝试的浏览器列表。

# CAVEATS

默认的 URL 正则表达式未必能匹配所有合法的 URL 格式。含有特殊字符的复杂 URL 可能需要调整配置。urlview 处理纯文本的效果最好；对于带有 MIME 编码的邮件，建议改用 **urlscan**，它能处理 quoted-printable 和 base64 编码。

# HISTORY

**urlview** 由 mutt 邮件客户端的作者 **Michael Elkins** 于 **1990 年代末**编写。它被设计成 mutt 的补充工具，在终端环境中提供便捷的 URL 处理功能。此后该工具由多位贡献者共同维护，至今仍是基于终端的邮件工作流中的标准实用程序。

# INSTALL

```apt: sudo apt install urlview```

```dnf: sudo dnf install urlview```

```apk: sudo apk add urlview```

```zypper: sudo zypper install urlview```

```brew: brew install urlview```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[urlscan](/man/urlscan)(1), [mutt](/man/mutt)(1), [lynx](/man/lynx)(1), [xdg-open](/man/xdg-open)(1)
