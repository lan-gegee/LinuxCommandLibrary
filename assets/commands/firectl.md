# TAGLINE

Firecracker microVM 的命令行启动器

# TLDR

**使用内核和根磁盘启动 VM**

```firectl --kernel=[./vmlinux] --root-drive=[/path/image.img]```

**自定义 Firecracker 二进制**路径

```firectl --firecracker-binary=[/usr/local/bin/firecracker] --kernel=[./vmlinux] --root-drive=[disk.img]```

**更多的 CPU 和内存**

```firectl --kernel=[./vmlinux] --root-drive=[disk.img] -c [2] -m [1024]```

**使用 TAP 网络**

```firectl --kernel=[./vmlinux] --root-drive=[disk.img] --tap-device=[tap0/AA:FC:00:00:00:01]```

**可写根磁盘**与自定义内核命令行

```firectl --kernel=[./vmlinux] --root-drive=[disk.img:rw] --kernel-opts="console=ttyS0 reboot=k panic=1 pci=off nomodules rw"```

# SYNOPSIS

**firectl** [*OPTIONS*]

# DESCRIPTION

**firectl** 是一款基础的命令行工具，用来运行带有控制台访问、磁盘 I/O 和可选网络的 Firecracker microVM。它是对 **firecracker** 二进制的封装：你需要提供 Linux 内核镜像（**vmlinux**）和根文件系统镜像，此外还可以选择附加磁盘、TAP 网卡、vsock、CPU/内存以及 MMDS 元数据。

默认情况下，它会在 **PATH** 中搜索 **firecracker**。需使用 Go 1.23+ 构建（**go build** 或 **make build-in-docker**）。需要 KVM 访问权限（例如通过 **setfacl** 设置 **/dev/kvm**）。

# PARAMETERS

**--firecracker-binary=**_path_

> firecracker 二进制文件的路径。

**--kernel=**_path_

> 内核镜像（默认 **./vmlinux**）。

**--kernel-opts=**_cmdline_

> 内核命令行。

**--root-drive=**_path_[:ro|:rw]

> 根磁盘镜像，可选 **:ro** 或 **:rw** 后缀。

**--add-drive=**_path_[:ro|:rw]

> 附加磁盘（可重复使用）。

**--tap-device=**_DEVICE/MAC_

> TAP 网卡配置。

**--vsock-device=**_PATH:CID_

> vsock 接口（可重复使用）。

**-c**, **--ncpus=**_n_ / **-m**, **--memory=**_MiB_

> vCPU 数量（默认 1），以及以 MiB 为单位的内存大小（默认 512）。

**--cpu-template=**_C3|T2_

> Firecracker CPU 模板。

**-t**, **--disable-smt**

> 禁用同时多线程（SMT）。

**-s**, **--socket-path=**_path_

> Firecracker API 套接字路径。

**-d**, **--debug**

> 调试输出。

日志 FIFO、指标、元数据 JSON 以及分区选项请参见 **firectl --help**。

# CAVEATS

需要硬件虚拟化（KVM）和已正确安装的 Firecracker。内核和 rootfs 必须与 Firecracker 兼容。涉及 root 与网络的设置通常需要提权。它不是一套完整的编排工具（生产环境的大规模部署请参阅 Firecracker 文档以及 flintlock 之类的工具）。

# INSTALL

```zypper: sudo zypper install firectl```

```nix: nix profile install nixpkgs#firectl```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[firecracker](/man/firecracker)(1), [qemu](/man/qemu)(1), [cloud-hypervisor](/man/cloud-hypervisor)(1)

# RESOURCES

```[Source code](https://github.com/firecracker-microvm/firectl)```

```[Homepage](https://firecracker-microvm.github.io/)```

<!-- verified: 2026-07-19 -->
