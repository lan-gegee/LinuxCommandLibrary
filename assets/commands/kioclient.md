# TAGLINE

KDE 的命令行客户端，用于 KIO 网络透明文件操作

# TLDR

用默认的 KDE 处理程序**打开 URL**

```kioclient exec [url]```

将远程文件的内容**打印到 stdout**

```kioclient cat [sftp://user@host/path/to/file]```

**列出远程目录的内容**

```kioclient ls [smb://server/share]```

通过 KIO **复制一个或多个文件**

```kioclient cp [path/to/source1] [path/to/source2] [path/to/destination]```

通过 KIO **移动文件**

```kioclient mv [path/to/source] [path/to/destination]```

通过 KIO **删除文件**

```kioclient rm [url]```

通过 KIO **创建新目录**

```kioclient mkdir [url]```

为 URL **打开 KDE 属性对话框**

```kioclient5 openProperties [url]```

# SYNOPSIS

**kioclient** _command_ [_arguments_] [_options_]

**kioclient5** _command_ [_arguments_] [_options_]

**kioclient6** _command_ [_arguments_] [_options_]

# COMMANDS

**exec** _url_ [_mimetype_]
> 用为 MIME 类型注册的默认处理程序打开 _url_。若给出 _mimetype_，则使用该类型的处理程序而非自动检测的类型。

**cat** _url_
> 将 _url_ 处文件的内容写入标准输出。

**ls** _url_
> 列出 _url_ 处目录中的条目。

**cp** _source_ ... _destination_
> 通过 KIO 将一个或多个源复制到 _destination_。源和目标可以是任何受支持的 URL 方案。

**mv** _source_ ... _destination_
> 通过 KIO 将源移动到 _destination_。

**rm** _url_
> 通过 KIO 删除 _url_ 处的文件或目录。

**mkdir** _url_
> 在 _url_ 处创建新目录。

**download** [_url_]
> 将 _url_ 复制到通过保存对话框选择的本地文件。若未提供 URL，则会打开文件选择器。

**openProperties** _url_
> 显示 _url_ 的 KDE 属性对话框。

# PARAMETERS

**--commands**
> 打印可用命令列表。

**--overwrite**
> 复制或移动时覆盖目标文件。

**--interactive**
> 使用交互式对话框（GUI 使用时的默认行为）。

**--noninteractive**
> 不弹出对话框；便于编写脚本。

**--platform** _name_
> 选择 Qt 平台抽象插件（例如 _xcb_、_wayland_、_offscreen_）。

**--help**
> 打印帮助并退出。

**--version**
> 打印程序版本。

# DESCRIPTION

**kioclient** 是 **KIO** 框架的轻量级命令行前端，KIO 为整个 KDE（Dolphin、Konqueror、Gwenview 等）提供文件访问能力。它让 shell 脚本和用户能够调用 KDE 应用所使用的同一套网络透明虚拟文件系统，把远程共享、归档甚至回收站当作本地路径一样对待。

可以使用已安装的 KIO worker 所实现的任何 URL 方案：**file:** 用于本地路径，**sftp:** 和 **fish:** 用于基于 SSH 的访问，**smb:** 用于 Windows 共享，**ftp:** 和 **webdav:** 用于传统网络共享，**trash:** 用于回收站，**tar:** 和 **zip:** 用于归档内容，此外还有协议专属的方案如 **man:**、**info:**、**mtp:**、**gdrive:** 等等。实际可用的列表取决于安装了哪些 **kio-extras** 插件。

除了基本文件操作（**cp**、**mv**、**rm**、**mkdir**、**ls**、**cat**、**download**），kioclient 还能通过 **exec** 启动资源的默认 GUI 处理程序——这是脚本化"在正确的 KDE 应用中打开此 URL"的最简单方式。**openProperties** 命令显示的属性对话框与 Dolphin 右键菜单中的相同。

在现代发行版上，**kioclient** 被拆分为 Qt5 二进制文件（**kioclient5**）和 Qt6 二进制文件（**kioclient6**）。若存在不带版本号的 **kioclient** 符号链接，它指向发行版视为默认的那个构建版本。

# CAVEATS

**kioclient** 需要正在运行的 D-Bus 会话以及相应的 Qt 平台插件。在无头服务器上，请设置 _QT_QPA_PLATFORM=offscreen_ 或传入 **--platform offscreen**，否则命令可能无法连接到显示器。

远程协议的身份验证由 **kwalletd** / **kwallet6** 处理。首次需要凭据时会弹出图形化密码对话框；在非交互式 shell 中，除非凭据已被缓存，否则操作会挂起或失败。

可用的 URL 方案集合取决于已安装的 KIO worker 软件包。某个方案在 Dolphin 中可用但通过全新调用的 **kioclient** 却不可用，通常意味着 worker 插件已安装但其 D-Bus 会话尚未启动。

# HISTORY

**kioclient** 自 **KDE 3** 时代起就随 KDE 发布，供 shell 脚本和其他应用程序驱动 Konqueror 引入的 **KIO** 框架。它在 **KDE 4** 中与 KIO 一起被重写，并更名为 **kioclient4** 以便与 KDE 3 版本共存。基于 Qt5 的 **kioclient5** 随 **KDE Frameworks 5** 于 **2014 年**出现，而 **kioclient6** 则随 **KDE Frameworks 6** 于 **2024 年**发布。

# INSTALL

```apt: sudo apt install kde-cli-tools```

```dnf: sudo dnf install kde-cli-tools```

```pacman: sudo pacman -S kde-cli-tools```

```apk: sudo apk add kde-cli-tools```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[dolphin](/man/dolphin)(1), [kdialog](/man/kdialog)(1), [xdg-open](/man/xdg-open)(1), [gio](/man/gio)(1)
