# TAGLINE

更新 SSL 证书颁发机构捆绑包

# TLDR

**更新** CA 证书捆绑包

```sudo update-ca-certificates```

**执行全新更新**，先移除已有的符号链接

```sudo update-ca-certificates --fresh```

以**详细输出**更新并显示细节

```sudo update-ca-certificates --verbose```

# SYNOPSIS

**update-ca-certificates** [_options_]

# PARAMETERS

**-h**, **--help**
> 显示选项摘要。

**-v**, **--verbose**
> 详细输出。显示 c_rehash 的结果。

**-f**, **--fresh**
> 全新更新。重新生成前先移除 **/etc/ssl/certs** 中的所有符号链接。

# DESCRIPTION

**update-ca-certificates** 更新目录 **/etc/ssl/certs** 以存放 SSL 证书，并生成 **ca-certificates.crt**——一个把受信任证书颁发机构合并在一起的单文件列表。它用于维护应用程序验证 TLS/SSL 连接时所依赖的系统级 CA 证书集合。

该程序读取 **/etc/ca-certificates.conf**，其中每一行指定 **/usr/share/ca-certificates** 下一个应被信任的 CA 证书路径名。以 **#** 开头的行是注释，会被忽略。以 **!** 开头的行表示取消选择相应证书，使其失效。

证书必须带有 **.crt** 扩展名才会被纳入。在 **/usr/local/share/ca-certificates** 下找到的所有带 **.crt** 扩展名的证书也会被隐式信任并纳入其中，因此该目录是添加自定义 CA 证书的推荐位置。

更新完成后，程序会通过 **run-parts** 执行 **/etc/ca-certificates/update.d** 中的钩子脚本，并向其传递新增（以 **+** 为前缀）和移除（以 **-** 为前缀）证书的列表。

# CONFIGURATION

要**添加自定义 CA 证书**，请将 **.crt** 文件放入 **/usr/local/share/ca-certificates/** 目录，然后运行 **update-ca-certificates**。该证书将被自动信任。

要**禁用系统自带的证书**，编辑 **/etc/ca-certificates.conf** 并在对应行的开头加上 **!** 前缀，然后运行 **update-ca-certificates**。

```
# Example /etc/ca-certificates.conf entries
mozilla/DigiCert_Global_Root_G2.crt
!mozilla/Untrusted_CA.crt
```

# CAVEATS

该命令主要在基于 **Debian** 和 **Ubuntu** 的发行版上可用。在 **Red Hat** 和 **Fedora** 系统上，请改用 **update-ca-trust**。修改系统证书目录通常需要 **root 权限**。更改只对更新之后启动的应用程序生效；已在运行的服务可能需要重启才能使用新的证书捆绑包。

# HISTORY

**update-ca-certificates** 是为 **Debian** 项目编写的，属于 **ca-certificates** 软件包的一部分，该软件包提供了来自 **Mozilla NSS** 项目的 CA 根证书精选集。ca-certificates 软件包自 **2000 年代初**起就是 Debian 的核心组件，确保系统级 TLS 验证开箱即用。后来，包括 **Ubuntu** 和 **Linux Mint** 在内的所有 Debian 衍生发行版都采用了这一工具。

# INSTALL

```dnf: sudo dnf install ca-certificates```

```pacman: sudo pacman -S ca-certificates```

```apk: sudo apk add ca-certificates```

```zypper: sudo zypper install ca-certificates```

```brew: brew install ca-certificates```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[openssl](/man/openssl)(1)
