# TAGLINE

带标签页与内嵌终端的终端邮件客户端

# TLDR

**启动 aerc**

```aerc```

**仅加载指定账户**打开

```aerc -a [account_name]```

向某地址**撰写新邮件**

```aerc mailto:[user@example.com]```

**打开 mbox 文件**

```aerc mbox:[path/to/file.mbox]```

**使用自定义配置文件**

```aerc -C [path/to/aerc.conf]```

# SYNOPSIS

**aerc** [**-h**] [**-v**] [**-a** _name_] [**-C** _file_] [**-A** _file_] [**-B** _file_] [**-I**] [_mailto:..._|_mbox:file_|_:command_]

# PARAMETERS

**-h**, **--help**
> 显示用法帮助并退出

**-v**, **--version**
> 打印已安装的版本并退出

**-a** _name_, **--account** _name_
> 只加载指定的账户；可用逗号分隔或重复该选项

**-C** _path_, **--aerc-conf** _path_
> 使用自定义的 aerc.conf 配置文件

**-A** _path_, **--accounts-conf** _path_
> 使用自定义的 accounts.conf 文件

**-B** _path_, **--binds-conf** _path_
> 使用自定义的按键绑定配置文件

**-I**, **--no-ipc**
> 直接运行命令，而不是通过 IPC 发送给已有实例

# DESCRIPTION

**aerc** 是一个用 Go 编写的终端邮件客户端，面向高级用户和开发者。它拥有标签页界面，可以同时打开多个账户和多封邮件；内嵌终端模拟器让你能在处理邮件的同时运行 Shell 命令；还提供 vim 风格的按键绑定和 ex 命令系统。

aerc 支持 IMAP、JMAP、Maildir、Notmuch 和 Mbox 后端，发送时可使用 SMTP 和 sendmail。它能处理邮件会话（threading）、通过 GnuPG 实现 PGP 签名与加密、借助外部过滤器渲染 HTML 邮件、补丁与 diff 的语法高亮、CardDAV 联系人查询以及基于模板的邮件撰写。得益于异步 IMAP 和 JMAP 支持，界面绝不会因网络问题而卡死。

# CONFIGURATION

配置文件存放在 **$XDG_CONFIG_HOME/aerc/**（通常为 ~/.config/aerc/）：

**aerc.conf** -- 主应用配置（UI、日志、过滤器）
**accounts.conf** -- 邮件账户定义（服务器、凭据、后端类型）
**binds.conf** -- 按键绑定自定义

# CAVEATS

渲染 HTML 邮件需要安装 **w3m**。macOS 上的 Homebrew 构建不包含 notmuch 支持；如有需要请从源码编译。该项目通过 git-send-email 采用基于邮件列表的补丁提交流程，而不使用拉取请求。

# HISTORY

**aerc** 最初由 **Drew DeVault**（sircmpwn）创建，首次提交于 **2018 年 1 月**，0.1.0 预发布版于 **2019 年 6 月**公布。在原项目无人维护之后，**Robin Jarry** 分叉并接管了活跃维护工作。项目托管在 SourceHut 上，采用 MIT 许可证。

# INSTALL

```apt: sudo apt install aerc```

```dnf: sudo dnf install aerc```

```pacman: sudo pacman -S aerc```

```apk: sudo apk add aerc```

```zypper: sudo zypper install aerc```

```brew: brew install aerc```

```nix: nix profile install nixpkgs#aerc```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[mutt](/man/mutt)(1), [alpine](/man/alpine)(1), [neomutt](/man/neomutt)(1), [notmuch](/man/notmuch)(1)
