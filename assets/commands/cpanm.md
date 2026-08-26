# TAGLINE

零配置的 CPAN 安装器

# TLDR

**安装 Perl 模块**

```cpanm [Module::Name]```

**本地安装模块**（无需 root）

```cpanm -l ~/perl5 [Module::Name]```

**从 cpanfile 安装**

```cpanm --installdeps .```

**安装指定版本**

```cpanm [Module::Name]@[1.23]```

**从 Git 仓库安装**

```cpanm [git://github.com/user/repo.git]```

**卸载模块**

```cpanm -U [Module::Name]```

**查看将安装的内容**

```cpanm --info [Module::Name]```

**静默安装**

```cpanm -q [Module::Name]```

# SYNOPSIS

**cpanm** [_options_] _Module_...

# PARAMETERS

**-l**, **--local-lib** _path_
> 将模块安装到本地目录。

**-L**, **--local-lib-contained** _path_
> 安装到目录，且依赖也包含在内。

**-n**, **--notest**
> 跳过测试。

**-q**, **--quiet**
> 静默输出。

**-v**, **--verbose**
> 详细输出。

**-f**, **--force**
> 即使测试失败也强制安装。

**-U**, **--uninstall**
> 卸载模块。

**--installdeps**
> 只安装依赖。

**--info**
> 显示模块信息而不安装。

**--look**
> 下载并解包，然后打开 shell。

**--mirror** _url_
> CPAN 镜像 URL。

**--sudo**
> 使用 sudo 进行安装。

# DESCRIPTION

**cpanm**（cpanminus）是一个从 CPAN（综合 Perl 归档网络）安装 Perl 模块的脚本。它以极少的依赖和配置，提供了比传统 CPAN shell 更简单、更快速的替代方案。

该工具自动解析并安装依赖、从 CPAN 镜像下载模块、运行测试，然后安装到合适的位置。它支持通过 local::lib 进行无需 root 权限的用户级安装。

cpanm 可以按名称、从 tarball、Git 仓库或 URL 安装模块。**cpanfile** 格式允许声明项目依赖，cpanm 可用 **--installdeps** 一并安装。

# CAVEATS

除非使用 local::lib，全局安装需要 root 权限。某些模块有系统级依赖（库、头文件），需要单独安装。测试失败可能表明系统配置不兼容。应谨慎使用 --notest 标志，因为它可能装上损坏的模块。

# HISTORY

cpanminus 由 **Tatsuhiko Miyagawa** 于 **2010** 年创建，是一个零配置的 CPAN 安装器。由于受够了 CPAN.pm 和 CPANPLUS 的复杂性，他设计了 cpanm，让它凭合理的默认值"开箱即用"。凭借简洁和速度，它成为安装 Perl 模块事实上的标准。

# INSTALL

```apk: sudo apk add perl-app-cpanminus```

```brew: brew install cpanm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[cpan](/man/cpan)(1), [carton](/man/carton)(1), [perl](/man/perl)(1)
