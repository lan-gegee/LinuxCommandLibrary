# TAGLINE

文件系统挂载配置文件

# TLDR

**查看 fstab**

```cat /etc/fstab```

**检查 fstab 语法**

```sudo mount -a```

**显示已挂载的文件系统**

```findmnt```

# DESCRIPTION

**/etc/fstab** 是一个配置文件，定义文件系统在启动时如何挂载。每一行描述一个文件系统的设备、挂载点、类型、选项以及备份/检查设置。

该文件由 **mount** 和 **systemd** 读取，用于在系统启动期间自动挂载文件系统。

# FILE FORMAT

```
<device>        <mountpoint>  <type>  <options>           <dump> <pass>
/dev/sda1       /boot         ext4    defaults            0      2
UUID=abc123     /home         ext4    defaults,noatime    0      2
/dev/sda3       none          swap    sw                  0      0
//server/share  /mnt/share    cifs    credentials=/etc/creds  0  0
```

# FIELDS

**device**
> 设备、UUID、LABEL 或网络路径。

**mountpoint**
> 挂载位置（目录；swap 使用 "none"）。

**type**
> 文件系统类型（ext4、xfs、btrfs、nfs、cifs、swap）。

**options**
> 挂载选项，以逗号分隔。

**dump**
> 备份标志（通常为 0）。

**pass**
> fsck 检查顺序（0=跳过，1=根分区，2=其他）。

# COMMON OPTIONS

```
defaults    - rw,suid,dev,exec,auto,nouser,async
noauto      - Don't mount at boot
nofail      - Don't fail boot if device missing
ro          - Read-only
noexec      - Don't allow execution
nosuid      - Ignore setuid bits
noatime     - Don't update access times
user        - Allow non-root users to mount
```

# CAVEATS

配置错误可能导致无法启动。重启前务必用 `mount -a` 测试。使用 UUID 或 LABEL 以可靠地标识设备。网络挂载需要特殊处理。

# SEE ALSO

[mount](/man/mount)(8), [findmnt](/man/findmnt)(8), [blkid](/man/blkid)(8)
