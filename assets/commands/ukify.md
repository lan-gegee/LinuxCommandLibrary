# TAGLINE

构建并签名为 UEFI 设计的统一内核镜像（UKI）

# TLDR

从内核、initrd 和内核命令行**构建 UKI**

```ukify build --linux=[/boot/vmlinuz] --initrd=[/boot/initrd.img] --cmdline=["root=/dev/sda1 ro"] --output=[uki.efi]```

为 Secure Boot **构建并签名**镜像

```ukify build --linux=[vmlinuz] --initrd=[initrd.img] --secureboot-private-key=[sb.key] --secureboot-certificate=[sb.crt]```

**生成** Secure Boot 和 PCR 签名密钥及证书

```ukify genkey --secureboot-private-key=[sb.key] --secureboot-certificate=[sb.crt]```

**检查**现有 UKI 的各个节区

```ukify inspect [/boot/EFI/Linux/uki.efi]```

**改用配置文件构建**，避免冗长的命令行

```ukify build --config=[/etc/kernel/uki.conf]```

# SYNOPSIS

**ukify** [_options_] **build**

**ukify** [_options_] **genkey**

**ukify** [_options_] **inspect** _file..._

# DESCRIPTION

**ukify** 将内核、initrd、内核命令行、**systemd-stub** UEFI 引导存根（stub）及其他资源组合成单个**统一内核镜像**（Unified Kernel Image，UKI）。UKI 是一个 PE/COFF EFI 可执行文件，固件可以直接引导它，或由 **systemd-boot** 列出它，从而无需为内核和 initrd 单独编写引导加载器配置。

由于所有内容都位于一个文件中，整个镜像（包括内嵌的命令行）可以为 **Secure Boot** 一次性签名，其内容也可以被度量到 TPM **PCR** 中，用于可度量启动和基于 TPM 的磁盘解锁。ukify 将各组件嵌入为命名的 PE 节区（如 **.linux**、**.initrd**、**.cmdline**、**.osrel** 和 **.uname**），可选地添加启动画面和 devicetree，并将结果写入 .efi 文件。

该工具提供三个动词：**build** 组装镜像并可选择签名，**genkey** 创建 Secure Boot 和 PCR 签名密钥材料，**inspect** 打印现有 UKI 的节区及其大小和 SHA256 摘要。

# PARAMETERS

**--linux=** _PATH_
> 作为 **.linux** 节区嵌入的内核镜像路径。

**--initrd=** _PATH_
> initrd 路径；可以多次指定以拼接多个 initrd。

**--cmdline=** _TEXT_|_@PATH_
> 内核命令行，可直接给出或从文件读取。

**--os-release=** _TEXT_|_@PATH_
> 操作系统标识信息；省略时取自主机的 **os-release**。

**--output=** _FILENAME_
> 生成镜像的目标路径。

**--stub=** _PATH_
> 要使用的 **systemd-stub** EFI 存根路径。

**--config=** _PATH_
> 从配置文件读取构建设置。

**--secureboot-private-key=** _KEY_
> 用于对生成的二进制文件进行 Secure Boot 签名的私钥。

**--secureboot-certificate=** _CERT_
> 与 Secure Boot 私钥匹配的证书。

**--signtool=** _SIGNER_
> 签名后端：**sbsign**、**pesign** 或 **systemd-sbsign**（默认为 sbsign）。

**--pcr-private-key=** _PATH_
> 用于签署 PCR 策略的私钥；可重复指定。

**--measure**
> 通过 **systemd-measure** 预计算并嵌入预期的 PCR 值。

# CAVEATS

UKI 将命令行打包进已签名的镜像中，因此修改启动参数意味着要重新构建（并重新签名）镜像，而不是编辑加载器条目。Secure Boot 签名要求密钥已注册到固件中，且所选的 **--signtool**（sbsign/pesign）必须已安装。ukify 使用 Python 实现，依赖 **objcopy** 等工具来组装 PE 节区。

# HISTORY

**ukify** 在 **systemd v253** 中作为组装统一内核镜像的实验性辅助工具引入，并在后续版本（v254 及以后）中扩展了更多动词和签名选项。它在 systemd 的 UEFI 启动工具链中与 **kernel-install** 和 **systemd-boot** 相辅相成。

# INSTALL

```apk: sudo apk add ukify```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[bootctl](/man/bootctl)(1), [kernel-install](/man/kernel-install)(8), [dracut](/man/dracut)(8), [objcopy](/man/objcopy)(1), [efibootmgr](/man/efibootmgr)(8)
