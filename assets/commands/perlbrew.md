# TAGLINE

在用户空间管理多个 Perl 安装

# TLDR

**安装 Perl 版本**

```perlbrew install perl-[5.38.0]```

**列出可用版本**

```perlbrew available```

**列出已安装版本**

```perlbrew list```

**切换到某个 Perl 版本**

```perlbrew switch perl-[5.38.0]```

**在当前 Shell 中使用某版本**

```perlbrew use perl-[5.38.0]```

**安装 cpanm**

```perlbrew install-cpanm```

**创建库**

```perlbrew lib create perl-[5.38.0]@[mylib]```

**用指定的 Perl 运行命令**

```perlbrew exec --with perl-[5.38.0] [perl script.pl]```

# SYNOPSIS

**perlbrew** [_install_] [_switch_] [_use_] [_list_] [_options_] [_args_]

# PARAMETERS

**install** _VERSION_
> 安装 Perl 版本。

**available**
> 列出可用版本。

**list**
> 列出已安装版本。

**switch** _VERSION_
> 设置默认版本。

**use** _VERSION_
> 在当前 Shell 中使用某版本。

**off**
> 在当前 Shell 中停用 perlbrew。

**lib create** _NAME_
> 创建库。

**lib list**
> 列出库。

**exec** _CMD_
> 用指定 Perl 版本运行命令。

**uninstall** _VERSION_
> 卸载某个 Perl 版本。

**alias** _create_ _name_ _alias_
> 给某个 Perl 安装起新名字。

**info**
> 显示 perlbrew 的安装信息。

**install-cpanm**
> 安装 cpanminus。

**install-multiple**
> 安装多个版本和变体。

**self-upgrade**
> 升级 perlbrew 本身。

**clean**
> 清除 tar 包和构建目录。

**--notest**
> 安装过程中跳过测试。

**--thread**
> 构建 Perl 时启用 usethreads。

**-j** _N_
> 并行构建的任务数。

**-q**, **--quiet**
> 抑制提示性输出。

**-v**, **--verbose**
> 更详细的输出。

# DESCRIPTION

**perlbrew** 在用户空间管理多个 Perl 安装。它让用户无需系统权限就能在不同版本之间切换。

各个安装都会在 ~/perl5/perlbrew 下从源码编译 Perl。每个版本彼此独立，拥有各自的模块和库。

库为同一个 Perl 版本提供了相互隔离的模块集合。这样可以实现项目专属的依赖而互不冲突。

switch 会为新 Shell 设置默认版本。use 只改变当前 Shell。这种灵活性便于跨版本进行开发。

cpanm 集成简化了模块安装。它只需安装一次，即可配合所有受管的 Perl 版本工作。

exec 可以针对特定版本运行命令，适合测试兼容性或构建软件包。

# CAVEATS

从源码构建 Perl 很耗时。磁盘占用会随着版本增加而累积。切换版本时某些模块可能需要重新编译。并不适合用来替代系统自带的 Perl。

# HISTORY

**perlbrew** 由 **Kang-min Liu**（gugod）于 **2010 年**前后创建，灵感来自 Ruby 的 rvm 与 rbenv。它解决了开发中需要多个 Perl 版本的问题，尤其是测试 CPAN 模块兼容性的需求。

# INSTALL

```dnf: sudo dnf install perlbrew```

```pacman: sudo pacman -S perlbrew```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[plenv](/man/plenv)(1), [cpanm](/man/cpanm)(1), [carton](/man/carton)(1), [perl](/man/perl)(1)
