# TAGLINE

在本地 Maildir 存储与 IMAP 邮箱之间同步邮件

# TLDR

**同步所有账户**

```offlineimap```

**同步特定账户**

```offlineimap -a [account_name]```

**同步特定文件夹**

```offlineimap -f [INBOX]```

**试运行**（显示将发生的操作）

```offlineimap --dry-run```

**快速同步**（跳过标志同步）

```offlineimap -q```

**同步一次后退出**

```offlineimap -o```

**使用自定义配置同步**

```offlineimap -c [/path/to/config]```

**显示文件夹列表**

```offlineimap --info```

# SYNOPSIS

**offlineimap** [_-a account_] [_-f folder_] [_-o_] [_-q_] [_options_]

# PARAMETERS

**-a** _ACCOUNT_
> 同步特定账户。

**-f** _FOLDER_
> 同步特定文件夹。

**-o**
> 单次同步（不重复执行）。

**-q**, **--quick**
> 快速同步，跳过标志。

**-c** _FILE_
> 配置文件。

**-u** _UI_
> 用户界面（quiet、basic、blinkenlights）。

**--dry-run**
> 只显示将要执行的操作，不实际执行。

**--info**
> 显示账户/文件夹信息。

**-l** _FILE_
> 日志文件。

**--version**
> 显示版本信息。

# DESCRIPTION

**offlineimap** 在本地 Maildir 存储与 IMAP 邮箱之间同步邮件，支持离线访问电子邮件以及备份 IMAP 账户。

双向同步使本地与远端保持一致。新邮件、删除操作和标志变更会向两个方向传播。冲突按配置处理。

Maildir 格式将每封邮件存储为一个文件，便于 mutt、notmuch 等邮件客户端直接访问。本地副本在离线时依然可用。

配置文件定义账户、服务器和文件夹映射。多个账户可以独立同步。文件夹过滤用于控制镜像哪些邮箱。

OAuth2 身份验证可用于 Gmail 及其他要求现代认证方式的提供商。密码可保存在系统密钥环中，或通过外部命令获取。

快速模式通过跳过未更改的文件夹来加速同步。单次模式只运行一次，不反复检查。

# CAVEATS

大型邮箱的初次同步耗时较长。配置可能比较复杂。该项目已弃用，建议改用 isstralsync。Gmail 的一些特殊行为可能需要额外处理。

# HISTORY

**offlineimap** 由 **John Googin** 于 **2002** 年前后创建，用于将 IMAP 邮件同步到本地存储，一度成为离线邮件工作流的必备工具。该项目目前处于维护模式，推荐的后继者是 **isstralsync**。

# INSTALL

```dnf: sudo dnf install offlineimap```

```pacman: sudo pacman -S offlineimap```

```apk: sudo apk add offlineimap```

```brew: brew install offlineimap```

```nix: nix profile install nixpkgs#offlineimap```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[mbsync](/man/mbsync)(1), [mutt](/man/mutt)(1), [notmuch](/man/notmuch)(1)
