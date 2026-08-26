# TAGLINE

SELinux 布尔值状态查询工具

# TLDR

显示某个布尔值的**当前设置**

```getsebool httpd_can_connect_ftp```

显示**所有**布尔值的当前设置

```getsebool -a```

显示所有布尔值及其**说明**

```sudo semanage boolean -l```

# SYNOPSIS

**getsebool** [_-a_] [_boolean_]

# PARAMETERS

**-a**
> 列出所有 SELinux 布尔值及其当前值

**boolean**
> 要查询的特定布尔值名称

# DESCRIPTION

**getsebool** 检索 SELinux 布尔值的当前取值。SELinux 布尔值是开/关开关，可以在运行时修改 SELinux 策略行为，而无需重新编译策略。

布尔值控制着特定的策略特性，例如 Apache 能否连接外部网络（httpd_can_network_connect）、用户能否运行不受限进程，或某些服务能否访问主目录。

输出内容为布尔值名称及其当前状态（on/off）。修改取值请使用 **setsebool**。

# COMMON BOOLEANS

**httpd_can_network_connect**
> 允许 Apache 发起网络连接

**httpd_can_connect_ftp**
> 允许 Apache 连接 FTP 服务器

**allow_user_exec_content**
> 允许用户在 home/tmp 中执行内容

**virt_use_nfs**
> 允许虚拟机使用 NFS

**ssh_chroot_rw_homedirs**
> 允许 SSH 写入 chroot 后的主目录

**samba_enable_home_dirs**
> 允许 Samba 共享用户主目录

# CAVEATS

需要启用 SELinux。布尔值名称和可用性因发行版和已安装的策略模块而异。使用 **semanage boolean -l** 可查看每个布尔值控制内容的说明。

# HISTORY

SELinux 布尔值的引入使策略更具灵活性，无需修改策略源码。getsebool 是 libselinux-utils 软件包的一部分，为 SELinux 功能提供命令行访问方式。

# INSTALL

```apt: sudo apt install selinux-utils```

```dnf: sudo dnf install libselinux-utils```

```apk: sudo apk add libselinux-utils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[setsebool](/man/setsebool)(8), [semanage](/man/semanage)(8), [getenforce](/man/getenforce)(1), [sestatus](/man/sestatus)(8)
