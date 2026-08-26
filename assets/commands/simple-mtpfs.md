# TAGLINE

MTP 设备的 FUSE 文件系统驱动

# TLDR

**列出**已连接的 MTP 设备

```simple-mtpfs --list-devices```

**挂载**第一个可用的 MTP 设备

```simple-mtpfs [mountpoint]```

按编号**挂载**指定设备

```simple-mtpfs --device [number] [mountpoint]```

使用 libmtp 设备文件**挂载**

```simple-mtpfs /dev/libmtp-[id] [mountpoint]```

**卸载** MTP 文件系统

```fusermount -u [mountpoint]```

# SYNOPSIS

**simple-mtpfs** [_options_] [_device_] _mountpoint_

# PARAMETERS

**-l**, **--list-devices**
> 列出可用的 MTP 设备及其顺序编号和名称。

**--device** _number_
> 按顺序编号选择要挂载的设备。

**-h**, **--help**
> 打印帮助并退出。

**-V**, **--version**
> 打印版本并退出。

**-o** _options_
> 逗号分隔的挂载选项。SIMPLE-MTPFS 特有的选项包括 **enable-move**（允许移动操作，可能很慢）。也支持标准 FUSE 选项，如 **allow_other**、**allow_root**、**default_permissions**、**uid=**、**gid=** 和 **umask=**。

**-f**
> 在前台运行。

**-d**
> 启用调试输出（隐含 **-f**）。

# DESCRIPTION

**simple-mtpfs** 是一个基于 FUSE 的文件系统驱动，把通过 USB 连接的 MTP（Media Transfer Protocol，媒体传输协议）设备上的文件以普通目录树的形式呈现在 Linux、macOS 及其他支持 FUSE 的系统上。挂载后，你就可以用标准 shell 工具浏览、复制、重命名和删除手机、相机及其他支持 MTP 的硬件上的文件。

该驱动通过 **libmtp** 与设备通信，并通过 **FUSE** 把设备存储呈现为用户空间文件系统。从设备下载的临时文件保存在可配置的目录中（默认 **/tmp**）。连接多个 MTP 设备时，先用 **--list-devices** 查看它们的顺序编号，再传入 **--device** 或一个 **/dev/libmtp-*** 特殊文件来选择要挂载的设备。

使用 **fusermount -u** 卸载挂载点。该项目上游已不再积极维护；许多发行版仍在打包它，但对于新环境，**jmtpfs** 或 **gvfs-mtp** 等替代方案可能更合适。

# CAVEATS

移动操作默认禁用，因为它们在 MTP 设备上可能非常慢；如有需要可用 **-o enable-move** 启用。性能比原生块设备挂载慢，因为每次文件访问都要经过 MTP 协议。上游项目无人维护，在某些软件包管理器中已被标记弃用。构建时需要 **libfuse**（2.7.3 或更高版本）和 **libmtp**。

# HISTORY

**simple-mtpfs** 由 **Peter Hatina** 编写，于 **2013 年**前后首次发布，作为较重的 MTP 浏览工具之外的轻量替代品。**0.2 版**于 **2015 年 1 月**附带手册页发布。项目达到过 **0.4.0**，此后上游几乎无活动；Homebrew 和多个 Linux 发行版仍在分发它，但同时将其标记为弃用。

# INSTALL

```zypper: sudo zypper install simple-mtpfs```

```brew: brew install simple-mtpfs```

```nix: nix profile install nixpkgs#simple-mtpfs```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[fusermount](/man/fusermount)(1), [mount](/man/mount)(8), [sshfs](/man/sshfs)(1), [mtp-detect](/man/mtp-detect)(1)

# RESOURCES

```[Source code](https://github.com/phatina/simple-mtpfs)```

<!-- verified: 2026-06-29 -->
