# TAGLINE

基于终端的电子邮件和新闻组客户端。

# TLDR

打开 **alpine** 邮件客户端

```alpine```

直接进入**撰写邮件**界面启动 alpine

```alpine [email@example.net]```

**退出** alpine

```q y```

# SYNOPSIS

**alpine** [_options_] [_address_]

# DESCRIPTION

**alpine** 是一款电子邮件客户端和 Usenet 新闻组程序，其界面风格类似 pico/nano。它通过 IMAP 支持大多数现代邮件服务，并采用菜单驱动式界面，易于使用。

Alpine 是 Pine 的后继者，由华盛顿大学开发。

# PARAMETERS

**address**
> 直接进入邮件撰写界面，向指定地址发送邮件

**-i**
> 启动时直接进入 FOLDER INDEX 界面，而不是主菜单。

**-f** _folder_
> 打开指定的 _folder_ 而不是 INBOX（在第一个文件夹集合中）。

**-c** _number_
> **-f** 参数对应的文件夹集合编号。

**-d** _debug-level_
> 以调试级别 0 到 9 输出诊断信息。

**-p** _config-file_
> 使用指定的 _config-file_ 作为个人配置文件，而不是 ~/.pinerc。

**-n** _number_
> 启动时将编号为 _number_ 的消息设为当前消息。

**-z**
> 启用挂起功能（Ctrl-Z），将 Alpine 放入后台。

# CONFIGURATION

配置通常通过主菜单中的 **Setup** 命令（S）交互式编辑，更改会写回个人配置文件。

**~/.pinerc**
> Alpine 的个人配置文件。存储邮件服务器设置、文件夹集合、显示偏好和功能开关。

**~/.addressbook**
> 个人通讯录。

**/etc/pine.conf**
> 系统级默认配置。

**/etc/pine.conf.fixed**
> 由管理员设置的系统级不可覆盖配置。

# CAVEATS

配置默认存储在 ~/.pinerc 中。与 Gmail 等现代邮件服务商进行 OAuth2 认证时，Alpine 可能需要额外设置。

# HISTORY

Alpine 由**华盛顿大学**开发，作为 **Pine**（Program for Internet News & Email）的后续版本。它于 **2007** 年首次发布，旨在解决 Pine 的许可证问题。

# INSTALL

```apt: sudo apt install alpine```

```dnf: sudo dnf install alpine```

```aur: yay -S alpine```

```apk: sudo apk add alpine```

```zypper: sudo zypper install alpine```

```brew: brew install alpine```

```nix: nix profile install nixpkgs#alpine```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[mutt](/man/mutt)(1), [mail](/man/mail)(1), [pico](/man/pico)(1), [nano](/man/nano)(1), [pine](/man/pine)(1)

# RESOURCES

```[Source code](https://repo.or.cz/alpine.git)```

```[Homepage](https://alpineapp.email/)```

<!-- verified: 2026-06-11 -->
