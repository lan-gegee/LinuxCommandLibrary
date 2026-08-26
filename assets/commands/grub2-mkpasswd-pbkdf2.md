# TAGLINE

生成 PBKDF2 密码哈希以保护 GRUB

# TLDR

为 GRUB 2 创建**密码哈希**

```sudo grub2-mkpasswd-pbkdf2```

以自定义**迭代次数**和**盐长度**创建哈希

```sudo grub2-mkpasswd-pbkdf2 -c [10000] -s [64]```

# SYNOPSIS

**grub2-mkpasswd-pbkdf2** [_options_]

# PARAMETERS

**-c**, **--iteration-count** _COUNT_
> PBKDF2 迭代次数（越高越安全但越慢）。默认为 10000。

**-s**, **--salt** _LENGTH_
> 盐的长度（字节）。默认为 64。

**-l**, **--buflen** _LENGTH_
> 生成的哈希长度（字节）。默认为 64。

# DESCRIPTION

**grub2-mkpasswd-pbkdf2** 生成用于保护 GRUB 2 引导加载程序配置的哈希密码。输出的哈希可用在 grub.cfg 中，为启动条目或 GRUB 命令行提供密码保护。

PBKDF2（Password-Based Key Derivation Function 2）通过多次迭代和随机盐提供对抗暴力破解的强保护。生成的哈希可以安全地存储在配置文件中。

# CAVEATS

需要 root 权限才能运行。生成的哈希必须手动添加到 GRUB 配置中。更高的迭代次数会提高安全性，但也会增加启动时密码验证的延迟。在 RHEL/Fedora 上该工具名为 **grub2-mkpasswd-pbkdf2**，以匹配 grub2 软件包的命名；它与上游称为 **grub-mkpasswd-pbkdf2** 的是同一工具。

# HISTORY

grub2-mkpasswd-pbkdf2 是 GRUB 2 的一部分。引入 GRUB 密码保护是为了防止未授权用户修改启动参数或进入单用户模式。PBKDF2 取代了较简单的哈希方法以提升安全性。

# SEE ALSO

[grub-mkconfig](/man/grub-mkconfig)(8), [grub-install](/man/grub-install)(8), [grub-editenv](/man/grub-editenv)(1)

# RESOURCES

```[Homepage](https://www.gnu.org/software/grub/)```

```[Source code](https://git.savannah.gnu.org/cgit/grub.git)```

```[Documentation](https://www.gnu.org/software/grub/manual/grub/grub.html)```

<!-- verified: 2026-07-17 -->
