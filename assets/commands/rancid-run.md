# TAGLINE

采集网络设备配置并进行版本控制

# TLDR

**为所有组运行 RANCID**

```rancid-run```

**为指定组运行**

```rancid-run [group_name]```

**带邮件通知运行**

```rancid-run -m [email@example.com]```

# SYNOPSIS

**rancid-run** [_options_] [_group_...]

# PARAMETERS

**-m** _email_
> 将结果发送到指定邮箱。

**-r** _device_
> 只处理单台设备。

**-f**
> 强制运行。

# DESCRIPTION

**rancid-run** 执行 RANCID（Really Awesome New Cisco confIg Differ），采集网络设备配置并进行版本控制。它会连接路由器、交换机和防火墙以备份其配置。

# EXAMPLES

```bash
# Run all groups
rancid-run

# Specific group
rancid-run routers

# Multiple groups
rancid-run routers switches firewalls

# With email
rancid-run -m admin@example.com routers
```

# SETUP

```bash
# 1. Create group
/var/lib/rancid/bin/rancid-cvs groupname

# 2. Add devices to router.db
# /var/lib/rancid/groupname/router.db
router1.example.com:cisco:up

# 3. Configure credentials
# ~/.cloginrc
add user router1.example.com admin
add password router1.example.com {password}

# 4. Run
rancid-run groupname
```

# CONFIGURATION

**/etc/rancid/rancid.conf**
> 主配置文件，定义设备组、版本控制系统和工作目录路径。

**~/.cloginrc**
> 设备登录凭据文件，为每台网络设备指定用户名、密码和 enable 密码。

**router.db**
> 每个组的设备清单，列出主机名、设备类型（cisco、juniper 等）和 up/down 状态。

# CAVEATS

需要 CVS 或 Git 进行版本控制。设备凭据存放在 .cloginrc 中。通常通过 cron 定时运行。

# HISTORY

RANCID 由 **Shrubbery Networks** 开发，用于自动化网络设备的配置备份和变更跟踪。

# INSTALL

```apt: sudo apt install rancid```

```dnf: sudo dnf install rancid```

```apk: sudo apk add rancid```

```brew: brew install rancid```

```nix: nix profile install nixpkgs#rancid```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[clogin](/man/clogin)(1), [rancid-cvs](/man/rancid-cvs)(1)
