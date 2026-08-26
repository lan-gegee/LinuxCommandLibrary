# TAGLINE

面向嵌入式 Linux 的稳健自动更新控制器

# TLDR

**从内容目录创建并签名更新包**

```rauc bundle --cert=[cert.pem] --key=[key.pem] [content_dir/] [update.raucb]```

**在运行中的系统上安装更新包**（本地路径或 HTTP URL）

```rauc install [update.raucb]```

**显示所有槽位的当前更新状态**

```rauc status```

以 JSON 格式**显示状态**，便于脚本处理

```rauc status --output-format=json-pretty```

**打印更新包的元数据**

```rauc info [update.raucb]```

更新成功后**将当前启动的槽位标记为良好**

```rauc status mark-good booted```

**将某个槽位标记为损坏**，强制下次启动时回滚

```rauc status mark-bad other```

**将更新包内容解压**到目录以便检查

```rauc extract [update.raucb] [output_dir/]```

# SYNOPSIS

**rauc** [_global-options_] _command_ [_command-options_] [_arguments_]

# PARAMETERS

**-c** _FILE_, **--conf=**_FILE_
> 使用替代的 _system.conf_。

**-C** _SECTION:KEY=VALUE_, **--confopt=**_SECTION:KEY=VALUE_
> 在运行时覆盖配置值。

**--keyring=**_PEM_
> 用于验证更新包签名的信任锚。

**--mount=**_PATH_
> 更新包的挂载点前缀（默认 _/mnt/rauc_）。

**-d**, **--debug**
> 启用调试输出。

**-h**, **--help**
> 打印用法信息。

**--version**
> 打印 RAUC 版本并退出。

# COMMANDS

**bundle** _INPUTDIR_ _BUNDLE_
> 创建并签名更新包。需要 **--cert** 和 **--key**。

**resign** _IN_ _OUT_
> 替换（或 **--append**）已有更新包的签名。

**convert** _IN_ _OUT_
> 将经典包转换为 verity/casync 包。

**encrypt** _IN_ _OUT_ **--to** _PEM_
> 为指定的接收者证书加密更新包。

**extract** _BUNDLE_ _DIR_
> 解压更新包的原始内容（需要验证）。

**extract-signature** _BUNDLE_ _SIGFILE_
> 将分离式 CMS 签名写入文件。

**install** _BUNDLE_
> 将更新包安装到非活动槽位组。接受本地路径、_file://_ URI 和 _http(s)://_ URL。使用 **--progress** 可显示 TTY 进度条。

**info** _BUNDLE_
> 显示清单、镜像和签名链。

**status** [_SLOT_], **mark-good**|**mark-bad**|**mark-active** [**booted**|**other**|_SLOT_]
> 查询槽位状态或更改槽位的启动状态。

**write-slot** _SLOT_ _IMAGE_
> 将镜像直接写入槽位（用于生产制造或恢复）。

**mount** _BUNDLE_
> 挂载更新包以便调试（开发用途）。

# DESCRIPTION

**rauc** 既是目标机上的更新客户端，也是主机侧的打包工具，面向嵌入式 Linux 系统。它通过将签名的更新包写入非活动槽位组，并在完整性验证通过后才切换活动启动目标，实现原子性、故障安全的 A/B 更新。如果新系统无法启动或确认，引导加载程序会回退到之前的槽位。

更新包（_.raucb_）是一个 SquashFS 归档，包含根文件系统镜像、内核/initrd 和清单文件，使用 x509 证书签名。在目标机上，**rauc install** 会对照预装的密钥环验证签名，确保该包与设备**兼容**（compatible），并将每个镜像分发到对应的槽位（ext4、UBIFS、裸块设备、boot 分区等）。D-Bus 服务会向其他服务暴露进度和状态。

# CONFIGURATION

rauc 在目标机上的行为由 **/etc/rauc/system.conf** 控制。代表性片段：

```
[system]
compatible=my-device-v1
bootloader=uboot
bundle-formats=-plain

[keyring]
path=/etc/rauc/ca.cert.pem

[slot.rootfs.0]
device=/dev/mmcblk0p2
type=ext4
bootname=A

[slot.rootfs.1]
device=/dev/mmcblk0p3
type=ext4
bootname=B
```

引导加载程序集成（**bootname**、标记槽位 good/bad）支持 U-Boot、GRUB、Barebox、EFI 以及自定义脚本。

# CAVEATS

基于 RAUC 的设计需要提前规划：目标机必须至少有两个根槽位、一个能在两者之间切换的引导加载程序，以及烧录进 rootfs 的信任锚。更新包与 **compatible** 字符串绑定；不匹配将被拒绝。加密（crypt）包在安装时需要对应的私钥。签名证书应离线保存，并通过 **rauc resign** 进行轮换。

# HISTORY

RAUC 由 **Pengutronix** 的 **Jan Lübbe** 和 **Enrico Jörns** 创建，于 **2015 年**作为开源软件发布，旨在为嵌入式 Linux 项目提供一个厂商中立的安全更新框架。此后它已成为 **Yocto** 和 **Buildroot** 生态中事实上的标准，并附带集成层（**meta-rauc**、**hawkBit** 连接器），可将设备接入大规模更新服务器。

# INSTALL

```apt: sudo apt install rauc```

```dnf: sudo dnf install rauc```

```pacman: sudo pacman -S rauc```

```nix: nix profile install nixpkgs#rauc```

<!-- packages: 2026-07-22 -->

# SEE ALSO
