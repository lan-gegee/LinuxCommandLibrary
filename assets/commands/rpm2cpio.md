# TAGLINE

将 RPM 软件包转换为 cpio 归档

# TLDR

**将 RPM 软件包转换为 cpio 归档**

```rpm2cpio [path/to/file.rpm] > [file.cpio]```

**直接从 RPM 软件包解压文件**

```rpm2cpio [path/to/file.rpm] | cpio -idmv```

**列出 RPM 软件包的内容**

```rpm2cpio [path/to/file.rpm] | cpio -t```

# SYNOPSIS

**rpm2cpio** [_file.rpm_]

# PARAMETERS

**file.rpm**
> 要转换的 RPM 软件包文件（省略时从 stdin 读取）

# DESCRIPTION

**rpm2cpio** 会从 `.rpm` 文件中剥离 RPM 的 lead、签名和头部区段，并把内嵌的 cpio 有效负载写到标准输出。这样一来，无需安装软件包、也不必依赖 `rpm` 数据库，就能提取 RPM 包中的内容。

cpio 归档采用 `newc` 格式（有效负载也可能经 `xz`/`lzma`/`zstd` 压缩，较新的 rpm 构建会透明地完成解压），并按照 RPM 本来要安装的方式保留所有者、权限模式和目录结构。它几乎总是被管道传给 **cpio**（或同样能识别这种格式的 **bsdtar**）来进行列出或解压。

# CAVEATS

不会执行安装前/安装后的脚本小程序（scriptlet）、不会运行触发器，也不会更新 rpm 数据库。存储在 RPM 头部中的文件能力（file capabilities）、SELinux 标签和文件摘要**不会**应用到解压出的文件上——只有 cpio 有效负载自身编码的内容才会生效。解压出的文件落在当前目录之下；当路径为绝对路径时，请谨慎使用 `cpio -id`（别加 `-D`），以免覆盖主机上的文件。

# INSTALL

```apt: sudo apt install rpm2cpio```

```dnf: sudo dnf install rpm```

```apk: sudo apk add rpm```

```zypper: sudo zypper install rpm```

```brew: brew install rpm2cpio```

```nix: nix profile install nixpkgs#rpm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[rpm](/man/rpm)(8), [cpio](/man/cpio)(1), [rpmkeys](/man/rpmkeys)(8)
