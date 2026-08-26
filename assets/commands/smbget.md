# TAGLINE

从 SMB/CIFS 共享下载文件

# TLDR

从 SMB 服务器**下载**文件

```smbget smb://server/share/file```

**递归**下载

```smbget --recursive smb://server/share/```

使用**用户名和密码**下载

```smbget -U username%password smb://server/share/file```

带**加密**下载

```smbget -e smb://server/share/file```

**续传**中断的下载

```smbget -r smb://server/share/file```

只下载**较新**的文件

```smbget -u smb://server/share/file```

写入 **stdout**

```smbget --stdout smb://server/share/file```

# SYNOPSIS

**smbget** [_options_] _smb://host/share/file_

# DESCRIPTION

**smbget** 是一个语义类似 wget 的简单工具，可以从 SMB 服务器下载文件。文件使用 SMB URL 格式指定。

# PARAMETERS

**-r, --resume**
> 自动续传中断的下载

**--recursive**
> 递归下载目录及其内容

**-u, --update**
> 只下载比本地副本新的文件

**-o, --outputfile FILE**
> 指定输出文件名

**--stdout**
> 将下载的数据写入 stdout

**-U, --user=[DOMAIN/]USERNAME%[PASSWORD]**
> 指定 SMB 凭据

**-a, --guest**
> 以访客用户身份连接

**-e, --encrypt**
> 为传输启用 SMB 加密

**-N, --no-pass**
> 不提示输入密码

**-W, --workgroup=WORKGROUP**
> 指定 SMB 工作组/域

**-A, --authentication-file=FILE**
> 从文件读取凭据

**--limit-rate=INT**
> 限制下载带宽（KB/s）

**-q, --quiet**
> 抑制输出消息

**-v, --verbose**
> 启用详细输出

**-D, --dots**
> 显示进度点

# CAVEATS

在命令行中包含密码存在安全风险。为了更好的安全性，请使用交互式密码输入、Kerberos 身份验证或凭据文件。SMB URL 的格式为 smb://[user@]host/share/path。

# HISTORY

**smbget** 是 **Samba** 套件的一部分，提供类 wget 的接口，用于从 Windows/SMB 文件共享下载文件。

# INSTALL

```apt: sudo apt install smbclient```

```dnf: sudo dnf install samba-client```

```pacman: sudo pacman -S smbclient```

```apk: sudo apk add samba-client```

```zypper: sudo zypper install samba-client```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[smbclient](/man/smbclient)(1), [wget](/man/wget)(1), [curl](/man/curl)(1)
