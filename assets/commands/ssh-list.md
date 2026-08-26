# TAGLINE

快速访问的 TUI SSH 连接管理器

# TLDR

**启动连接管理器**

```ssh-list```

# SYNOPSIS

**ssh-list**

# DESCRIPTION

**ssh-list** 是一个 TUI SSH 连接管理器，它以菜单形式显示已保存的主机，可通过键盘导航快速连接。它支持添加、编辑、复制和排序 SSH 条目、从 ~/.ssh/config 导入、在远程主机上执行命令以及过滤连接。它不存储密码，而是依赖 SSH 密钥。

# CONFIGURATION

**~/.ssh/ssh-list.json**
> 存储 SSH 连接条目。

**~/.ssh/ssh-list_config.toml**
> 存储应用设置和外观选项。

# HISTORY

**ssh-list** 由 **akinoiro** 创建，使用 **Rust** 编写。

# INSTALL

```apt: sudo apt install openssh-client```

```apk: sudo apk add dropbear-ssh```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[sshs](/man/sshs)(1), [ssh](/man/ssh)(1), [sshclick](/man/sshclick)(1)
