# TAGLINE

可配置且可扩展的终端邮件客户端

# TLDR

**启动邮件客户端**

```meli```

**使用指定的配置文件**

```meli --config [path/to/config.toml]```

从标准输入**创建或编辑草稿**

```meli compose < [draft.txt]```

**输出一份示例配置**

```meli --print-default-config```

**列出可用主题**

```meli --print-default-theme```

# SYNOPSIS

**meli** [_options_]

# DESCRIPTION

**meli** 是一款拥有合理默认设置的终端邮件客户端，兼顾新手与高级用户。它支持多账户，集成了邮件存储、SMTP、联系人管理和内嵌终端编辑器。

支持的协议和格式包括 **Maildir**、**mbox**、**notmuch**、**IMAP**、**JMAP** 和 **NNTP**（Usenet）。它具有强大的搜索功能和自定义主题，并可通过内嵌的 xterm 兼容终端模拟器在 meli 内运行外部编辑器。

# CONFIGURATION

**${XDG_CONFIG_HOME}/meli/config.toml**
> 主配置文件，用于设置账户、按键绑定、主题和行为。

# CAVEATS

从源码构建需要 Rust 1.65 及以上版本。使用前需要先完成邮箱账户的初始配置。

# HISTORY

**meli** 使用 **Rust** 编写，支持 BSD、Linux 和 macOS。

# INSTALL

```apt: sudo apt install meli```

```apk: sudo apk add meli```

```zypper: sudo zypper install meli```

```brew: brew install meli```

```nix: nix profile install nixpkgs#meli```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[mutt](/man/mutt)(1), [neomutt](/man/neomutt)(1), [himalaya](/man/himalaya)(1)
