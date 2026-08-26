# TAGLINE

为 CIFS 挂载将 Windows SID 转换为 Linux UID/GID

# TLDR

**显示帮助信息**

```cifs.idmap --help```

**显示版本信息**

```cifs.idmap --version```

# SYNOPSIS

**cifs.idmap** [**-h**] [**-t** _timeout_] [**-v**] _key_id_

# DESCRIPTION

**cifs.idmap** 是 Linux CIFS 客户端文件系统的用户空间辅助程序。它将 Windows 安全标识符（SID）与 Linux UID/GID 相互转换，确保挂载 CIFS/SMB 共享时文件所有者和权限正确。

该程序不打算从命令行直接运行。当共享以 **cifsacl** 挂载选项挂载时，内核会通过 **request-key**(8) 调用它。

该工具依赖 **/etc/cifs-utils/idmap-plugin** 处的插件来执行实际的 ID 映射。支持的后端包括 sfu、rid、nss 和 tdb，通常配合 **sssd** 或 **winbind** 等服务使用。

# PARAMETERS

**-h, --help**
> 打印用法信息后退出

**-t, --timeout** _seconds_
> 以秒为单位设置密钥过期计时器（默认：600）。使用 0 表示不过期

**-v, --version**
> 打印版本号后退出

**key_id**
> 内核 upcall 提供的密钥标识符

# CONFIGURATION

**/etc/cifs-utils/idmap-plugin**
> 执行实际 SID 到 UID/GID 映射的符号链接或插件。必须指向受支持的后端（sfu、rid、nss 或 tdb）。

**/etc/request-key.conf**
> 内核密钥环配置，将 upcall 定向到 cifs.idmap。

# CAVEATS

如果 cifs.idmap 或其插件不可用，文件对象将被赋予挂载该共享的进程的 UID/GID。此时可使用 **uid** 和 **gid** 挂载选项指定默认值。

要使该工具正常工作，必须在 **/etc/cifs-utils/idmap-plugin** 处存在插件（或符号链接）。

# HISTORY

对 cifs.idmap 的 upcall 支持在 **Linux 内核 3.0** 中引入。该程序由 Shirish Pargaonkar 编写，是 **cifs-utils** 套件的一部分。

# INSTALL

```apt: sudo apt install cifs-utils```

```dnf: sudo dnf install cifs-utils```

```pacman: sudo pacman -S cifs-utils```

```apk: sudo apk add cifs-utils```

```zypper: sudo zypper install cifs-utils```

```nix: nix profile install nixpkgs#cifs-utils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[mount.cifs](/man/mount.cifs)(8), [cifscreds](/man/cifscreds)(1)
