# TAGLINE

Podman 容器的终端 UI

# TLDR

**启动** Podman TUI

```podman-tui```

**确保** Podman API 套接字正在运行（用户级）

```systemctl --user start podman.socket```

**或者**在没有 systemd 的情况下启动 API 服务

```podman system service --time=0```

# SYNOPSIS

**podman-tui**

# DESCRIPTION

**podman-tui** 是面向 Podman 环境的终端用户界面。它使用 Podman Go 绑定与本地或远程的 Podman 主机通信（包括通过 SSH）。你无需离开终端即可浏览和管理容器、镜像、pod、卷、网络及相关资源。

兼容性：release-2.x 对应 Podman v6，release-1.x 对应 Podman v5，release-0.x 对应 Podman v4。可从软件包安装或从源码构建（参见上游安装指南）。

# PARAMETERS

交互式应用；主要通过按键绑定而非 CLI 子命令控制。常用按键：

**m**

> 命令菜单

**s**

> 排序菜单

**l** / **h**

> 下一个 / 上一个屏幕

**k** / **j**

> 上移 / 下移

**Tab**

> 切换控件

**Esc**

> 关闭活动对话框

**Ctrl+c**

> 退出

# CAVEATS

API 需要 **podman.socket**（或 **podman system service**）。SSH 密钥口令需要设置 **CONTAINER_PASSPHRASE**。在类 Unix 系统上使用 256 色模式。请让 **podman-tui** 的主版本与你的 Podman 主版本匹配。

# INSTALL

```dnf: sudo dnf install podman-tui```

```apk: sudo apk add podman-tui```

```brew: brew install podman-tui```

```nix: nix profile install nixpkgs#podman-tui```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[podman](/man/podman)(1), [docker](/man/docker)(1), [lazydocker](/man/lazydocker)(1), [ctop](/man/ctop)(1)

# RESOURCES

```[Source code](https://github.com/containers/podman-tui)```

```[Homepage](https://podman.io)```

<!-- verified: 2026-07-19 -->
