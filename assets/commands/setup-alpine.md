# TAGLINE

交互式 Alpine Linux 系统安装器

# TLDR

**运行完整的交互式安装器**

```setup-alpine```

采用合理默认值的**快速模式**（DHCP、无 SSH、不安装到磁盘）

```setup-alpine -q```

从先前保存的文件**重放**回答

```setup-alpine -f [/path/to/answers]```

**生成**带默认值的模板回答文件

```setup-alpine -c [/path/to/answers.new]```

**打印**内嵌的帮助文本

```setup-alpine -h```

# SYNOPSIS

**setup-alpine** [**-ahq**] [**-c** _file_ | **-f** _file_]

# PARAMETERS

**-a**
> 以 **diskless**（"alpine"）模式运行：配置正在运行的系统而不安装到磁盘。

**-c** _FILE_
> 在 _FILE_ 处**创建**一个预填当前默认回答的回答文件，然后退出。

**-f** _FILE_
> 从 _FILE_ **读取**回答而不是交互式询问（支持无人值守安装）。

**-q**
> **快速**模式：仅配置键盘布局、主机名、DHCP 网络、/etc/hosts 和默认软件仓库。

**-h**
> 显示用法并退出。

# DESCRIPTION

**setup-alpine** 是随每张官方 Alpine Linux ISO 提供的标准首启安装器。它从 live 环境中运行，引导操作员完成搭建可用 Alpine 系统所需的各个步骤：键盘布局、主机名、网络接口、DNS 服务器、root 密码、时区、HTTP 代理、NTP 守护进程、软件包镜像、SSH 服务器和磁盘布局。

在内部，**setup-alpine** 是一个小的 POSIX shell 脚本，负责调度一系列专用的 **setup-***step* 辅助脚本（如 **setup-keymap**、**setup-hostname**、**setup-interfaces**、**setup-disk**、**setup-sshd**、**setup-ntp**、**setup-apkrepos**、**setup-lbu** 和 **setup-apkcache**）。每个辅助脚本也可以在安装完成后单独调用，以重新配置系统的相应方面。

磁盘步骤运行时会提供三种安装目标：**sys** 表示传统的持久化安装，**data** 表示通过 **lbu** 备份状态的无盘系统，**none** 表示完全跳过磁盘设置。其结果是形成一个小巧、可重复且可脚本化的 Alpine 部署方案。

# ANSWER FILE

先用 **setup-alpine -c answers.new** 导出模板，然后编辑各变量，再用 **setup-alpine -f answers** 重放。常见的键包括 **KEYMAPOPTS**、**HOSTNAMEOPTS**、**INTERFACESOPTS**、**DNSOPTS**、**TIMEZONEOPTS**、**PROXYOPTS**、**APKREPOSOPTS**、**SSHDOPTS**、**NTPOPTS**、**DISKOPTS**、**LBUOPTS** 和 **APKCACHEOPTS**。将某个键设为 **none** 可跳过该步骤。

# CAVEATS

快速模式（**-q**）只配置 DHCP——Wi-Fi 必须用 **setup-interfaces** 或 **wpa_supplicant** 手动设置。在已安装的系统上运行 **setup-alpine** 会就地重新配置它，包括覆盖 **/etc/network/interfaces** 和 **/etc/hostname**。磁盘模式 **sys** 会清空所选磁盘。该脚本必须以 **root** 身份运行，并假定使用标准的 Alpine BusyBox 用户空间。

# HISTORY

**setup-alpine** 自该项目在 2000 年代后期引入"轨道式安装"方法以来便随 **Alpine Linux** 一同发布，取代了早期的手动安装流程。它是 **alpine-conf** 软件包的一部分，以 POSIX shell 编写，还被 **setup-bootable**、**setup-acf** 以及 LXC/Docker minirootfs 构建流水线复用。

# INSTALL

```apk: sudo apk add alpine-conf```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[lbu](/man/lbu)(8), [apk](/man/apk)(8)
