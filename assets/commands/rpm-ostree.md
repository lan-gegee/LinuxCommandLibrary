# TAGLINE

面向不可变操作系统的镜像与软件包混合系统

# TLDR

显示**部署状态**

```rpm-ostree status```

**预览**可用的升级

```rpm-ostree upgrade --preview```

**升级**并重启

```rpm-ostree upgrade -r```

**回滚**到上一个部署

```rpm-ostree rollback -r```

**安装**软件包并重启

```rpm-ostree install [package] -r```

**安装**软件包并以 **live** 方式应用，无需重启

```rpm-ostree install -A [package]```

**变基**到不同的镜像或操作系统变体

```rpm-ostree rebase [ostree-remote:branch]```

# SYNOPSIS

**rpm-ostree** [**status**|**upgrade**|**rollback**|**install**|**uninstall**] [**-r**] [_options_]

# COMMANDS

**status**
> 显示当前部署

**upgrade**
> 下载并准备升级

**rollback**
> 切换到上一个部署

**install**
> 在基础镜像上层叠安装软件包

**uninstall**
> 移除层叠安装的软件包

**rebase**
> 切换到不同的基础镜像

**override** _subcommand_
> 覆盖基础软件包：`replace`、`remove`、`reset`

**deploy**
> 基于特定版本/分支/提交创建新的部署

**kargs**
> 管理内核启动参数

**initramfs**
> 处理客户端侧 initramfs 的重新生成

**cleanup**
> 清除待处理的部署和缓存数据

**db** _subcommand_
> RPM 数据库操作（diff、list、version）

**cancel**
> 停止一个待处理的事务

**apply-live**
> 将更改应用到已启动的部署，无需重启

**usroverlay**
> 在 /usr 上创建临时可写的 overlay，供短期测试使用

# PARAMETERS

**-r, --reboot**
> 操作完成后重启

**--preview**
> 显示将会升级的内容

**--check**
> 仅检查更新

**--cache-only**
> 只使用缓存数据

**--idempotent**
> 如果请求已经应用过则跳过操作

**--allow-inactive**
> 允许已存在于基础层中的软件包

**--apply-live**, **-A**
> 将更改应用到已启动的部署，无需重启（仅限 install/uninstall）

**--force-replacefiles**
> 安装时允许覆盖属于其他软件包的文件

**--download-only**
> 只下载软件包而不进行部署

**-n**, **--dry-run**
> 预览更改但不执行

**--json**
> 以 JSON 格式输出（status 命令）

# DESCRIPTION

**rpm-ostree** 把基于 OSTree 的镜像部署与 RPM 软件包层叠结合在一起。它管理不可变的基础镜像，同时允许对软件包进行定制，被 Fedora Silverblue、CoreOS 及类似系统所采用。

更改会创建新的部署，而不是修改正在运行的系统。多个部署可以共存，因此可以轻松回滚到之前的状态。

# CAVEATS

更改需要重启才能生效。基础系统是不可变的。软件包层叠存在额外开销。某些软件包可能与不可变模型冲突。

# HISTORY

**rpm-ostree** 由 Red Hat 开发，目的是将 OSTree 镜像部署的可靠性与 RPM 包管理的灵活性结合起来，服务于注重容器和不可变桌面的发行版。

# INSTALL

```dnf: sudo dnf install rpm-ostree```

```nix: nix profile install nixpkgs#rpm-ostree```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ostree](/man/ostree)(1), [rpm](/man/rpm)(8), [flatpak](/man/flatpak)(1)
