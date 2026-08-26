# TAGLINE

从 CPAN 安装 Perl 模块

# TLDR

**安装 Perl 模块**

```cpan [Module::Name]```

**安装多个模块**

```cpan [Module::One] [Module::Two]```

**启动交互式 CPAN shell**

```cpan```

**强制安装模块**（忽略测试失败）

```cpan -f [Module::Name]```

**从指定镜像安装**

```cpan -M [http://cpan.org] [Module::Name]```

**升级所有已安装的模块**

```cpan -u```

**获取模块信息**

```cpan -D [Module::Name]```

**跳过测试直接安装**

```cpan -T [Module::Name]```

# SYNOPSIS

**cpan** [_-cfFiOstTu_] [_-D module_] [_-M mirror_] [_module ..._]

# PARAMETERS

**-f**
> 强制安装，忽略测试失败。

**-F**
> 关闭 CPAN.pm 的锁定尝试（谨慎使用）。

**-i**
> 安装指定模块（默认动作）。

**-T**
> 安装前不测试模块。

**-t**
> 为指定模块运行测试。

**-u**
> 升级所有已安装的模块。

**-D** _module_
> 显示模块详情和安装状态。

**-M** _mirror_
> 使用指定的 CPAN 镜像。

**-O**
> 显示过时的模块。

**-a**
> 为已安装的模块创建 autobundle。

**-r**
> 重新编译动态加载的模块。

**-j** _file_
> 使用其他配置文件。

**-g** _module_
> 下载到当前目录而不安装。

**-v**
> 打印 CPAN.pm 版本。

# DESCRIPTION

**cpan** 是从综合 Perl 归档网络（CPAN）安装 Perl 模块的标准命令行界面。它负责处理 Perl 模块及其依赖的依赖解析、下载、构建、测试和安装。

首次运行时，cpan 会进入配置模式，设置镜像、构建偏好等选项。该配置保存在 **~/.cpan/CPAN/MyConfig.pm** 中。之后可以在交互式 shell 中用 **o conf** 命令重新配置。

交互式 shell 提供搜索（m /pattern/）、安装（install Module）、检视（look Module）以及管理本地 CPAN 缓存等命令。shell 支持 Tab 补全和命令历史。

CPAN.pm 将模块发行包下载到 **~/.cpan/sources/**，在 **~/.cpan/build/** 中解压并构建，然后安装到 Perl 库路径。当用户对系统 Perl 目录没有写权限时，可考虑使用 **local::lib** 或 **perlbrew** 进行用户级安装。

# CONFIGURATION

**~/.cpan/CPAN/MyConfig.pm**
> CPAN 主配置文件，保存镜像 URL、构建偏好、代理设置和安装目录。

# CAVEATS

系统级安装可能需要 root/sudo 权限。某些模块需要 C 编译器或系统库。带 -f 忽略测试失败可能装上损坏的模块。首次运行的配置向导可能令人困惑。想要更简单的用法可以考虑 cpanm（App::cpanminus）。

# HISTORY

**CPAN.pm** 由 Andreas König 于 **1995** 年创建，距 CPAN 本身建立不久。它成为安装 Perl 模块的标准方式，并集成到 Perl 核心发行版中。虽然 cpanm 等较新的工具提供了更简单的界面，但 CPAN.pm 仍是功能最完整、配置选项最丰富的客户端。

# INSTALL

```apt: sudo apt install perl```

```dnf: sudo dnf install perl```

```pacman: sudo pacman -S perl```

```apk: sudo apk add perl-utils```

```zypper: sudo zypper install perl```

```brew: brew install perl```

```nix: nix profile install nixpkgs#perl```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[cpanm](/man/cpanm)(1), [perl](/man/perl)(1), [perlbrew](/man/perlbrew)(1), [carton](/man/carton)(1)
