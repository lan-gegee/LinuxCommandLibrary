# TAGLINE

Linux 上管理默认应用程序的 xdg-utils 现代替代品

# TLDR

用默认应用**打开** URL

```handlr open https://example.com```

用默认 PDF 查看器打开 **PDF**

```handlr open [path/to/file.pdf]```

**将** imv **设置**为 PNG 文件的默认应用

```handlr set .png imv.desktop```

将 MPV 设置为所有**音频文件**的默认应用

```handlr set 'audio/*' mpv.desktop```

**列出**所有默认应用

```handlr list```

**查询** PNG 文件的默认应用

```handlr get .png```

# SYNOPSIS

**handlr** _command_ [_arguments_]

# PARAMETERS

**open** _PATH|URL_
> 用默认应用打开文件或 URL

**set** _MIME|EXT_ _HANDLER_
> 为 MIME 类型或扩展名设置默认应用

**get** _MIME|EXT_
> 查询 MIME 类型或扩展名的默认应用

**list**
> 列出所有已配置的默认应用

**unset** _MIME|EXT_
> 移除默认应用设置

**add** _MIME|EXT_ _HANDLER_
> 将处理程序添加到列表而不设为默认

# DESCRIPTION

**handlr** 是 Linux 上管理默认应用程序的 xdg-utils 现代替代品。它通过 MIME 类型和文件扩展名处理文件与 URL 的关联。

该工具通过修改 ~/.config/mimeapps.list（以及可选的已废弃的 ~/.local/share/applications/mimeapps.list）来设置默认应用。它既支持具体的文件扩展名（.pdf、.png），也支持 MIME 类型模式（audio/*、video/*）。

handlr 力求比 xdg-open 和 xdg-mime 更简单、行为更可预测，并具备更好的终端集成和清晰的输出。

# CAVEATS

要求 .desktop 文件已正确安装在标准位置。可能无法被所有桌面环境识别。某些应用拥有自己的文件关联机制，可能会覆盖系统默认设置。

# HISTORY

handlr 是作为 xdg-utils 工具集的 Rust 替代品而创建的，注重简洁和可靠性。它解决了 xdg-open 行为不可预测、回退机制复杂等常见困扰。

# INSTALL

```apk: sudo apk add handlr```

```nix: nix profile install nixpkgs#handlr```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[xdg-open](/man/xdg-open)(1), [xdg-mime](/man/xdg-mime)(1)
