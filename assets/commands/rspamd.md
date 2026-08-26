# TAGLINE

高级垃圾邮件过滤守护进程

# TLDR

**启动 Rspamd**

```rspamd```

**使用配置文件启动**

```rspamd -c [/etc/rspamd/rspamd.conf]```

**测试模式**

```rspamd -t```

**前台模式**

```rspamd -f```

**通过 systemd 启动**

```sudo systemctl start rspamd```

# SYNOPSIS

**rspamd** [_options_]

# PARAMETERS

**-c**, **--config** _file_
> 指定配置文件。

**-f**, **--no-fork**
> 在前台运行。

**-t**, **--test-config**
> 测试配置。

**-u**, **--user** _user_
> 以指定用户运行。

**-g**, **--group** _group_
> 以指定组运行。

# DESCRIPTION

**Rspamd** 是一个用 C 编写的快速、免费的垃圾邮件过滤系统。它综合运用机器学习、神经网络和各种规则来识别垃圾邮件，准确率高且资源占用低。

# EXAMPLES

```bash
# Start daemon
rspamd

# Test configuration
rspamd -t

# Via systemctl
sudo systemctl start rspamd
sudo systemctl enable rspamd

# Check message
rspamc < message.eml

# Check message with details
rspamc -v < message.eml

# Web interface (default)
# http://localhost:11334/
```

# CONFIGURATION

**/etc/rspamd/rspamd.conf**
> 主配置文件，定义 worker、模块和全局设置。

**/etc/rspamd/local.d/**
> 存放本地配置覆盖的目录，内容与默认设置合并。是放置自定义规则的首选位置。

**/etc/rspamd/override.d/**
> 存放完全覆盖配置的目录，会彻底替换指定模块的默认设置。

# PORTS

```
11333 - Worker (milter)
11334 - Web interface
11335 - Controller
```

# CAVEATS

需要配置与 MTA 的 milter 集成。想要最佳效果请训练 Bayes 分类器。Web UI 密码在 worker-controller.inc 中设置。

# HISTORY

Rspamd 由 **Vsevolod Stakhov** 自 2008 年起创建，是一个快速、可扩展的垃圾邮件过滤系统。

# INSTALL

```apt: sudo apt install rspamd```

```pacman: sudo pacman -S rspamd```

```apk: sudo apk add rspamd```

```zypper: sudo zypper install rspamd```

```nix: nix profile install nixpkgs#rspamd```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[rspamadm](/man/rspamadm)(1), [rspamc](/man/rspamc)(1)
