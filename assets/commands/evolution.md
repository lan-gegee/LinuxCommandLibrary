# TAGLINE

GNOME 个人信息管理应用

# TLDR

**启动 Evolution**

```evolution```

**以指定组件启动**

```evolution --component=[mail|calendar|contacts]```

**撰写新邮件**

```evolution mailto:[user@example.com]```

**导入文件**

```evolution --import [file.ics]```

**强制离线模式**

```evolution --force-offline```

# SYNOPSIS

**evolution** [_options_] [_URI_]

# PARAMETERS

**--component** _name_
> 以指定组件启动：mail、calendar、contacts、tasks、memos。

**--import** _file_
> 导入文件（vCard、iCal 等）。

**--force-online**
> 强制在线模式。

**--force-offline**
> 强制离线模式。

**--quit**
> 请求正在运行的实例退出。

**--express**
> 以快速（express）模式启动。

**--help**
> 显示帮助。

# DESCRIPTION

**Evolution** 是 GNOME 的个人信息管理应用。它将电子邮件、日历、联系人、任务和备忘录整合到单一应用中，类似 Microsoft Outlook。

Evolution 支持多种邮件协议（IMAP、POP、SMTP、Exchange）、日历标准（CalDAV、ICS）和联系人格式（CardDAV、LDAP）。它包含加密（GPG、S/MIME）、垃圾邮件过滤和搜索文件夹等功能。

# FEATURES

- 多个邮件账户
- CalDAV 与 Exchange 日历
- CardDAV 与 LDAP 联系人
- 任务与备忘录管理
- GPG 与 S/MIME 加密
- 垃圾邮件过滤

# CAVEATS

与更简洁的客户端相比资源占用较高。部分 Exchange 功能需要额外的软件包。首次使用必须经过设置向导。关闭窗口后后台进程可能继续运行。

# HISTORY

Evolution 最初由 **Ximian** 于 **1999 年**开始开发，2003 年被 Novell 收购，后来成为 GNOME 项目的一部分。它是最早提供完整群件功能的 Linux 应用之一。

# INSTALL

```apt: sudo apt install evolution```

```dnf: sudo dnf install evolution```

```pacman: sudo pacman -S evolution```

```apk: sudo apk add evolution```

```zypper: sudo zypper install evolution```

```nix: nix profile install nixpkgs#evolution```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[thunderbird](/man/thunderbird)(1)
