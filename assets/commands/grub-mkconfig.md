# TAGLINE

生成 GRUB 引导加载程序配置文件

# TLDR

将配置打印到 **stdout**（试运行）

```sudo grub-mkconfig```

生成配置并写入**默认文件**

```sudo grub-mkconfig -o /boot/grub/grub.cfg```

在 **Red Hat/Fedora** 系统上生成配置

```sudo grub2-mkconfig -o /boot/grub2/grub.cfg```

显示**版本**

```grub-mkconfig --version```

# SYNOPSIS

**grub-mkconfig** [_OPTION_]

# PARAMETERS

**-o, --output=FILE**
> 将生成的配置写入 FILE 而不是 stdout

**-h, --help**
> 显示帮助信息并退出

**-V, --version**
> 显示版本信息并退出

# DESCRIPTION

**grub-mkconfig** 通过处理系统设置并检测已安装的操作系统来生成 GRUB 引导加载程序配置文件。通常在内核更新或修改启动参数后使用。

该命令从 /etc/default/grub 读取设置，并执行 /etc/grub.d/ 中的脚本，最终产出 grub.cfg 文件。

# CONFIGURATION

**/etc/default/grub**
> 主设置文件，控制超时时间、默认条目、内核参数和显示选项。

**/etc/grub.d/**
> 配置生成期间执行的脚本所在目录。可以在此添加自定义启动条目。

# CAVEATS

此命令必须以 root 身份运行。生成的配置依赖于 /etc/grub.d/ 中的脚本和 /etc/default/grub 中的设置。修改 GRUB 设置后，务必运行 grub-mkconfig 重新生成配置。在 Red Hat/Fedora 上，命令名为 **grub2-mkconfig**，配置路径为 /boot/grub2/grub.cfg。在 Debian/Ubuntu 上，**update-grub** 是 grub-mkconfig 的便捷封装。

# HISTORY

**grub-mkconfig** 是 **GRUB 2**（GRand Unified Bootloader）的一部分，取代了最初的 GRUB Legacy。它能够自动检测已安装的内核和操作系统。

# INSTALL

```apt: sudo apt install grub-common```

```pacman: sudo pacman -S grub```

```apk: sudo apk add grub```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[grub-install](/man/grub-install)(8), [update-grub](/man/update-grub)(8), [grub-set-default](/man/grub-set-default)(8)
