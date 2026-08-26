# TAGLINE

获取并筛选 Arch Linux 镜像列表

# TLDR

按**速度**排序并保存

```sudo reflector --sort rate --save /etc/pacman.d/mirrorlist```

获取指定**国家**的 **HTTPS** 镜像

```reflector -c [Germany] -p https```

获取**最近同步**的镜像

```reflector -l [10]```

使用**配置文件**

```sudo reflector @/etc/xdg/reflector/reflector.conf```

显示**帮助**

```reflector -h```

# SYNOPSIS

**reflector** [**-c** _country_] [**-p** _protocol_] [**-l** _num_] [**--sort** _method_] [**--save** _file_]

# PARAMETERS

**-c, --country _country_**
> 按国家筛选

**-p, --protocol _proto_**
> 按协议筛选（http、https、ftp）

**-l, --latest _num_**
> 获取 N 个最近同步的镜像

**--sort _method_**
> 排序依据：rate、country、score、delay

**--save _file_**
> 将输出保存到文件

**--age _hours_**
> 只保留 N 小时内同步过的镜像

**-f, --fastest _num_**
> 返回 N 个最快的镜像

# DESCRIPTION

**reflector** 用于获取和筛选最新的 Arch Linux 镜像列表。它可以测试镜像速度并按多种标准排序，然后为 pacman 保存一份优化后的镜像列表。

该工具适合为你的位置寻找快速、可靠的镜像。可以通过 systemd 定时器定期运行它，以保持镜像列表最新。

# CONFIGURATION

**/etc/xdg/reflector/reflector.conf**
> 默认配置文件，包含国家、协议、排序方法和输出路径等持久化选项。在命令行中用 **@** 前缀引用。

**reflector.service** / **reflector.timer**
> Systemd 单元，按计划自动运行 reflector 以保持镜像列表最新。

**/etc/pacman.d/mirrorlist**
> 生成的镜像列表的输出目标，供 pacman 下载软件包时使用。

# CAVEATS

仅适用于 Arch Linux。速度测试需要时间。网络状况各不相同。建议定期运行以获得最佳效果。需要联网。

# HISTORY

**reflector** 为 Arch Linux 而创建，用于自动化镜像选择。它以基于速度和同步状态的智能自动化选择取代了手动编辑镜像列表。

# INSTALL

```pacman: sudo pacman -S reflector```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pacman](/man/pacman)(8), [rankmirrors](/man/rankmirrors)(1), [pacman-mirrors](/man/pacman-mirrors)(1)
