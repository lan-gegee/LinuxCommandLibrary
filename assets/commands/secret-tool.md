# TAGLINE

通过桌面密钥环存储和检索机密信息

# TLDR

**存储**机密（从 stdin 读取值），并附带标签和属性对

```secret-tool store --label="[My password]" [attribute] [value]```

按属性**查找**已存储的机密

```secret-tool lookup [attribute] [value]```

**搜索**匹配属性的机密（仅元数据）

```secret-tool search [attribute] [value]```

**搜索并解锁**，显示所有匹配的机密

```secret-tool search --all --unlock [attribute] [value]```

**清除**所有匹配属性的机密

```secret-tool clear [attribute] [value]```

# SYNOPSIS

**secret-tool store** **--label**=_label_ [_attribute_ _value_]...

**secret-tool lookup** [_attribute_ _value_]...

**secret-tool search** [**--all**] [**--unlock**] [_attribute_ _value_]...

**secret-tool clear** [_attribute_ _value_]...

# COMMANDS

**store**
> 存储机密。密码从 stdin 读取。需要 **--label** 以及一个或多个用于标识该条目的属性/值对。

**lookup**
> 打印与给定属性/值对匹配的机密的密码。

**search**
> 列出与属性/值对匹配的机密。默认只显示第一个匹配项且不解锁。

**clear**
> 移除所有与给定属性/值对匹配的机密。

# PARAMETERS

**--label** _label_
> 机密的人类可读标签（**store** 必需）。

**--all**
> 显示所有匹配的机密，而不只是第一个（仅限 search）。

**--unlock**
> 在搜索过程中解锁被锁定的集合。

# DESCRIPTION

**secret-tool** 使用 Freedesktop Secret Service API 存储和检索密码。它通过 D-Bus 与正在运行的密钥环守护进程（如 gnome-keyring 或 KWallet）通信。

机密不是通过名称寻址，而是通过任意的属性/值对（例如 `service mybackup user alice`）。查找或删除机密时必须提供与存储时相同的属性/值对。

# CAVEATS

需要有正在运行的 Secret Service 提供者（gnome-keyring-daemon 或 kwalletd）。存储的机密在磁盘上是加密的，但以该用户身份运行的任何应用都可以访问。**store** 时密码从 stdin 读取，以避免通过进程列表泄露。

# HISTORY

属于 **libsecret**——实现 Freedesktop Secret Service 规范的 GNOME 库。**secret-tool** 是作为便捷 CLI 加入的，让密钥环可以通过脚本操作而无需编写 D-Bus 代码。

# INSTALL

```apt: sudo apt install libsecret-tools```

```dnf: sudo dnf install libsecret```

```pacman: sudo pacman -S libsecret```

```apk: sudo apk add libsecret```

```zypper: sudo zypper install secret-tool```

```brew: brew install libsecret```

```nix: nix profile install nixpkgs#libsecret```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gnome-keyring](/man/gnome-keyring)(1), [pass](/man/pass)(1)
