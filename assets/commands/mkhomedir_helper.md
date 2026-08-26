# TAGLINE

**pam_mkhomedir** PAM 模块的辅助程序

# TLDR

基于 /etc/skel 并使用 umask 022 为用户创建**家目录**

```sudo mkhomedir_helper [username]```

以**自定义 umask** 创建家目录（037 = 所有者全部权限、组只读）

```sudo mkhomedir_helper [username] [037]```

基于**自定义骨架**目录创建家目录

```sudo mkhomedir_helper [username] [umask] [path/to/skeleton_directory]```

创建带**指定权限**的家目录

```sudo mkhomedir_helper [username] [umask] [/etc/skel] [0700]```

# SYNOPSIS

**mkhomedir_helper** _user_ [_umask_ [_path-to-skel_ [_home_mode_ [_path-to-vendor-skel_]]]]

# PARAMETERS

**user**
> 要为其创建家目录的用户名

**umask**
> 内容的文件创建掩码；默认为 0022

**path-to-skel**
> 从中复制内容的骨架目录；默认为 /etc/skel

**home_mode**
> 家目录本身的权限；未指定时由 umask 计算得出

**path-to-vendor-skel**
> 次级骨架目录；设置后先从 path-to-skel 填充家目录，再从这个目录填充

# DESCRIPTION

**mkhomedir_helper** 是 **pam_mkhomedir** PAM 模块的辅助程序。它创建家目录并用指定骨架目录的内容进行填充。

该工具将骨架目录（通常是 /etc/skel）中的文件复制到新的家目录，并对文件权限应用指定的 umask。它会将所有权设为目标用户，并创建 .bashrc、.profile 等标准配置文件。

出于安全原因，该辅助程序在架构上与 PAM 模块分离，允许执行期间进行 SELinux 域转换，并防止登录域直接访问家目录内容。

# CAVEATS

该工具从不修改已存在的家目录，从而避免意外覆盖。执行需要 root 权限。骨架目录必须存在且可读。运行此命令前用户必须已存在于系统中。

# HISTORY

**mkhomedir_helper** 属于 **Linux-PAM**（Pluggable Authentication Modules，可插拔认证模块）项目。它是为 pam_mkhomedir 模块设计的注重安全的辅助二进制程序，用于在集中管理的认证系统（如 LDAP）中于用户登录时自动创建家目录。

# INSTALL

```apt: sudo apt install libpam-modules-bin```

```apk: sudo apk add linux-pam```

```brew: brew install linux-pam```

```nix: nix profile install nixpkgs#linux-pam```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[useradd](/man/useradd)(1), [adduser](/man/adduser)(1)
