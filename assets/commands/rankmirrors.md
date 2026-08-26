# TAGLINE

按速度为 Arch Linux 的 pacman 镜像排名

# TLDR

**对镜像列表排名**

```rankmirrors [/etc/pacman.d/mirrorlist]```

输出前 **N** 个镜像

```rankmirrors -n [5] [/etc/pacman.d/mirrorlist]```

**详细**输出

```rankmirrors -v [/etc/pacman.d/mirrorlist]```

测试**指定 URL**

```rankmirrors -u [url]```

只显示**响应时间**

```rankmirrors -t [/etc/pacman.d/mirrorlist]```

# SYNOPSIS

**rankmirrors** [**-n** _number_] [**-v**] [**-t**] [**-u** _url_] _mirrorlist_

# PARAMETERS

**-n _number_**
> 只输出前 N 个镜像

**-v, --verbose**
> 排名过程中输出详细信息

**-t, --times**
> 输出响应时间而不是镜像列表

**-u, --url _url_**
> 仅测试指定 URL

**-r, --repo _repo_**
> 指定用于测试的软件仓库

# DESCRIPTION

**rankmirrors** 通过测量连接速度和响应时间来测试 Arch Linux 的 pacman 软件包镜像，然后输出按速度排序的镜像列表（最快的排在前面）。它会连接输入文件中的每个镜像，下载一个小测试文件，并按传输速率对结果排序，帮助用户根据自己的地理位置优化软件包下载性能。

输出遵循标准镜像列表格式，可以重定向后直接替换 **/etc/pacman.d/mirrorlist**。**-n** 标志将输出限制为仅前 N 个最快的镜像，**-t** 则显示原始响应时间供对比，而不生成新的镜像列表。

# CAVEATS

测试需要逐一联系每个镜像，耗时较长。网络状况可能变化多端。它属于 pacman-contrib 的一部分，而非 pacman 本身。若要自动化更新可考虑 reflector。

# HISTORY

**rankmirrors** 是 Arch Linux 工具集的一部分，帮助用户优化镜像选择。虽然仍然可用，但许多用户现在更倾向于使用 reflector 进行自动化的镜像管理。

# INSTALL

```aur: yay -S rankmirrors```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pacman](/man/pacman)(8), [reflector](/man/reflector)(1), [pacman-mirrors](/man/pacman-mirrors)(1)
