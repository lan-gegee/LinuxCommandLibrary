# TAGLINE

扩展文件系统以填满分区

# TLDR

**将根文件系统扩展至填满分区**

```/usr/lib/systemd/systemd-growfs /```

**扩展挂载点处的文件系统**

```/usr/lib/systemd/systemd-growfs [/home]```

**启用开机时自动扩展**

```systemctl enable systemd-growfs-root.service```

**查看服务状态**

```systemctl status systemd-growfs-root.service```

# SYNOPSIS

**/usr/lib/systemd/systemd-growfs** _mountpoint_

# DESCRIPTION

**systemd-growfs** 是一个 systemd 工具，它指示内核将已挂载的文件系统扩展到填满其底层块设备。通常在调整分区大小之后使用，以扩展文件系统来利用新腾出的空间。

该工具通常由 systemd 服务依据 /etc/fstab 中的 **x-systemd.growfs** 挂载选项自动调用。也可以通过可发现分区规范（Discoverable Partitions Specification）中定义的 GPT 分区标志 59 触发。

支持的文件系统包括 ext4、btrfs、xfs 和 dm-crypt 加密分区。文件系统必须已经挂载，操作才能成功。

# FSTAB USAGE

向 /etc/fstab 添加 x-systemd.growfs 选项：

```
/dev/sda2  /  ext4  defaults,x-systemd.growfs  0  1
```

# RELATED SERVICES

**systemd-growfs@.service**：用于任意挂载点的模板服务。

**systemd-growfs-root.service**：用于扩展根文件系统的服务。

**systemd-makefs@.service**：在首次启动时创建文件系统。

# CAVEATS

仅适用于已挂载的文件系统。仅支持 ext4、btrfs、xfs 和 dm-crypt。在扩展文件系统之前必须先调整好底层分区的大小。扩展过程中出现的错误只会产生警告，不会导致挂载失败。

# HISTORY

**systemd-growfs** 是作为 systemd 基于镜像的部署与容器特性的一部分引入的。它为云实例和嵌入式系统提供自动的文件系统扩展能力，这类系统往往需要在初始配置后扩展其文件系统。

# SEE ALSO

[systemctl](/man/systemctl)(1), [resize2fs](/man/resize2fs)(8), [systemd-repart](/man/systemd-repart)(8), [parted](/man/parted)(8)
