# TAGLINE

在干净的 chroot 环境中构建 Arch Linux 软件包

# TLDR

**使用干净的 chroot 构建当前目录中的 PKGBUILD**

```makechrootpkg -c -r [/var/lib/archbuild/extra-x86_64]```

**构建前不清理 chroot**

```makechrootpkg -r [/var/lib/archbuild/extra-x86_64]```

**构建前先更新 chroot**

```makechrootpkg -u -r [/var/lib/archbuild/extra-x86_64]```

**构建前将本地软件包安装到 chroot 中**

```makechrootpkg -r [chroot] -I [package.pkg.tar.zst]```

**对构建出的软件包运行 namcap 和 checkpkg**

```makechrootpkg -c -n -C -r [chroot]```

**以读写方式将目录绑定挂载到 chroot 中**

```makechrootpkg -d [/host/path] -r [chroot]```

**向 makepkg 传递额外参数**

```makechrootpkg -c -r [chroot] -- --skippgpcheck```

# SYNOPSIS

**makechrootpkg** [_options_] **-r** _chroot_ [**--**] [_makepkg-args_]

# PARAMETERS

**-r** _dir_
> 用于构建的 chroot 目录（必需）。

**-c**
> 构建前清理 chroot 副本。

**-u**
> 构建前更新工作副本（chroot）。

**-I** _pkg_
> 构建前将给定的软件包文件安装到工作副本中。

**-d** _dir[:dest]_
> 以读写方式将宿主机目录绑定挂载到 chroot。

**-D** _dir[:dest]_
> 以只读方式将宿主机目录绑定挂载到 chroot。

**-t** _dir[:opts]_
> 在 chroot 内的指定目录挂载 tmpfs。

**-l** _name_
> 工作副本目录的名称（默认为 `$USER`）。

**-n**
> 对构建出的软件包运行 **namcap** 质量检查。

**-C**
> 针对上一个软件包版本运行 **checkpkg** 校验。

**-T**
> 在临时副本中构建（构建完成后丢弃）。

**-U** _user_
> 以指定用户身份运行 **makepkg**。

**-x** _when_
> 在 chroot 内启动交互式 Shell：`never`、`always` 或 `failure`。

**-h**
> 显示用法信息。

# DESCRIPTION

**makechrootpkg** 在干净且隔离的 chroot 环境中构建 PKGBUILD。它将构建过程与宿主系统已安装的软件包和配置隔离开，从而保证构建的可复现性，这也是构建 Arch Linux 官方软件包的标准方法。

chroot 由一个 root 模板加上从它克隆出来的每用户工作副本组成。**-c** 和 **-u** 等选项用于刷新工作副本，而 **-I** 和 **-d** 则允许你自定义构建环境。

# SETUP

```bash
# Create the chroot template (once)
mkarchroot /var/lib/archbuild/extra-x86_64/root base-devel

# Build the package in the current directory
cd package-dir
makechrootpkg -c -r /var/lib/archbuild/extra-x86_64
```

# CAVEATS

需要安装 **devtools** 软件包。首次使用前必须用 **mkarchroot** 初始化 chroot。需要 root 权限；比直接运行 **makepkg** 慢，但能产生更干净、更可复现的构建结果。**--** 之后的所有内容都会转发给 **makepkg**。

# HISTORY

**makechrootpkg** 是 Arch Linux **devtools** 的一部分，由 Arch Linux 开发者和可信用户（Trusted Users）维护，用于在可复现的 chroot 环境中构建官方软件包。

# SEE ALSO

[makepkg](/man/makepkg)(8), [pacman](/man/pacman)(8), [devtools](/man/devtools)(7), [pkgctl](/man/pkgctl)(1), [systemd-nspawn](/man/systemd-nspawn)(1)
