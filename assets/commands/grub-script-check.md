# TAGLINE

校验 GRUB 配置脚本语法

# TLDR

检查 GRUB 脚本文件的**语法错误**

```grub-script-check [path/to/grub.cfg]```

读取后显示输入的每一行（**详细模式**）

```grub-script-check -v [path/to/grub.cfg]```

从 **stdin** 检查脚本

```cat [path/to/script] | grub-script-check```

显示**帮助**

```grub-script-check --help```

# SYNOPSIS

**grub-script-check** [_options_] [_file_]

# PARAMETERS

**-v**, **--verbose**
> 读取后显示输入的每一行

**--help**
> 显示帮助信息

**--version**
> 显示版本信息

# DESCRIPTION

**grub-script-check** 校验 GRUB 配置脚本是否存在语法错误。它会解析 grub.cfg 等配置文件所用的 GRUB 脚本语言，并报告任何语法问题。

若未提供文件路径，该工具将从标准输入读取。这可用于校验生成的配置或在部署前测试脚本片段。

# CAVEATS

只检查语法，不检查语义正确性。语法有效并不能保证配置能够正常启动。也无法验证引用的文件或模块是否存在。

# HISTORY

grub-script-check 是 GRUB 2 的一部分，用于校验 GRUB 的配置脚本语言。脚本能力是在 GRUB 2 中引入的，用以取代 GRUB Legacy 较简单的配置格式。

# INSTALL

```apt: sudo apt install grub-common```

```pacman: sudo pacman -S grub```

```apk: sudo apk add grub```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[grub-mkconfig](/man/grub-mkconfig)(8), [grub-install](/man/grub-install)(8), [update-grub](/man/update-grub)(8)

# RESOURCES

```[Homepage](https://www.gnu.org/software/grub/)```

```[Source code](https://git.savannah.gnu.org/cgit/grub.git)```

```[Documentation](https://www.gnu.org/software/grub/manual/grub/grub.html)```

<!-- verified: 2026-07-17 -->
