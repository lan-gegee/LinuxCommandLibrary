# TAGLINE

离线定制虚拟机磁盘镜像

# TLDR

**设置 root 密码**

```virt-customize -a [image.qcow2] --root-password password:[newpass]```

**安装软件包**

```virt-customize -a [image.qcow2] --install [nginx,vim]```

**上传文件到镜像**

```virt-customize -a [image.qcow2] --upload [local.conf]:[/etc/app.conf]```

**运行 shell 脚本**

```virt-customize -a [image.qcow2] --run [setup.sh]```

**运行命令**

```virt-customize -a [image.qcow2] --run-command "[systemctl enable nginx]"```

**注入 SSH 密钥**

```virt-customize -a [image.qcow2] --ssh-inject [root]:file:[~/.ssh/id_rsa.pub]```

**设置时区**

```virt-customize -a [image.qcow2] --timezone [America/New_York]```

**设置主机名**

```virt-customize -a [image.qcow2] --hostname [myserver]```

# SYNOPSIS

**virt-customize** **-a** _image_ [_options_]

# PARAMETERS

**-a**, **--add** _file_
> 要定制的磁盘镜像文件。

**--root-password** _method:arg_
> 设置 root 密码。

**--password** _user:method:arg_
> 设置用户密码。

**--install** _packages_
> 安装软件包（逗号分隔）。

**--uninstall** _packages_
> 移除软件包。

**--update**
> 更新所有软件包。

**--upload** _local:remote_
> 上传文件到镜像。

**--copy-in** _local:remotedir_
> 将文件/目录复制进镜像。

**--run** _script_
> 在镜像中运行 shell 脚本。

**--run-command** _cmd_
> 运行单条命令。

**--ssh-inject** _user:file:keyfile_
> 注入 SSH 公钥。

**--timezone** _tz_
> 设置时区。

**--hostname** _name_
> 设置主机名。

**--edit** _file:expr_
> 使用 Perl 表达式编辑文件。

**--delete** _path_
> 删除文件或目录。

**--commands-from-file** _file_
> 从文件读取命令。

**-v**, **--verbose**
> 启用详细输出。

# DESCRIPTION

**virt-customize** 通过安装软件包、编辑配置、上传文件和运行脚本来修改虚拟机磁盘镜像。它是 libguestfs 工具集的一部分。

该工具使用 libguestfs 挂载磁盘镜像，并在安全隔离的环境中执行操作。定制前虚拟机必须处于关机状态。

定制脚本在一个小型 appliance 中运行，并以 chroot 方式进入客户机文件系统。下载软件包时可使用有限的网络访问。

此工具适合准备云镜像、创建黄金镜像以及自动化虚拟机供应流程。

# CAVEATS

虚拟机必须处于关机状态。除非必要，不要以 root 身份运行。修改生产环境镜像前先做快照。某些操作需要特定客户机操作系统的支持。可能需要 SELinux 重新打标签。

# HISTORY

**virt-customize** 是 libguestfs 的一部分，由 Red Hat 开发用于操作虚拟机镜像。该工具集提供对虚拟机磁盘镜像的安全、可脚本化访问，无需客户机处于运行状态。

# INSTALL

```apt: sudo apt install guestfs-tools```

```dnf: sudo dnf install guestfs-tools```

```pacman: sudo pacman -S guestfs-tools```

```zypper: sudo zypper install guestfs-tools```

```nix: nix profile install nixpkgs#guestfs-tools```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[virt-sysprep](/man/virt-sysprep)(1)
