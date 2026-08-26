# TAGLINE

基于字符界面的电子邮件和新闻客户端

# TLDR

**启动 Pine 邮件客户端**

```pine```

**向指定地址撰写邮件**

```pine [user@example.com]```

**打开指定文件夹**而不是 INBOX

```pine -f [folder]```

**在文件夹索引中启动**而不是主菜单

```pine -i```

**将全新配置输出到文件**

```pine -conf > [pinerc.new]```

# SYNOPSIS

**pine** [_options_] [_address ..._]

# PARAMETERS

**-f** _folder_
> 打开指定文件夹而不是 INBOX。

**-i**
> 启动时进入文件夹索引屏幕而不是主菜单。

**-I** _keystrokes_
> 启动时执行以逗号分隔的初始按键序列（如 CR、SPACE、^C）。

**-conf**
> 将全新的 pinerc 配置输出到 stdout。

**-p** _file_
> 用 file 作为个人配置文件，替代 ~/.pinerc。

**-P** _file_
> 用 file 作为系统级配置文件，替代 /usr/local/lib/pine.conf。

**-r**
> 以只读模式打开第一个文件夹。

**-attach** _file_
> 发送邮件并以 file 作为附件。

**-d** _level_
> 设置诊断输出的调试级别 (0-9)。

**-h**
> 显示有效命令行选项的帮助列表。

# DESCRIPTION

**pine** (Program for Internet News and Email) 是一个基于字符界面的电子邮件和新闻客户端。由华盛顿大学开发，凭借友好的用户界面曾被广泛使用。

# MAIN MENU

```
?  HELP
C  COMPOSE MESSAGE
I  MESSAGE INDEX
L  FOLDER LIST
A  ADDRESS BOOK
S  SETUP
Q  QUIT
```

# CONFIGURATION

配置存储于 ~/.pinerc。可从主菜单使用 S (Setup) 进行交互式配置。系统级配置位于 /usr/local/lib/pine.conf。

# CAVEATS

Pine 已过时；请改用 Alpine。并非所有功能都能与现代化邮件服务器配合工作。许可证问题导致了 Alpine 分支的诞生。

# HISTORY

Pine 由 **Mark Crispin** 于 1989 年起在**华盛顿大学**开发，后来被采用 Apache 许可证的 **Alpine** 取代。

# SEE ALSO

[alpine](/man/alpine)(1), [mutt](/man/mutt)(1), [mail](/man/mail)(1)
