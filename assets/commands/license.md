# TAGLINE

生成开源许可证文件

# TLDR

**列出许可证**

```license list```

**生成 MIT 许可证**

```license mit```

**生成 Apache 许可证**

```license apache-2.0```

**生成 GPL 许可证**

```license gpl-3.0```

**生成并重定向到文件**

```license mit > LICENSE```

**指定作者名和年份**

```license -n "[Your Name]" -y [2025] mit```

**将许可证保存到文件**

```license -o LICENSE.txt mit```

# SYNOPSIS

**license** [_command_] [_options_]

# PARAMETERS

_LICENSE_
> 要生成的许可证类型（例如 mit、apache-2.0、gpl-3.0、bsd-2-clause、isc、mpl-2.0、unlicense）。

**list**
> 列出所有可用的许可证类型。

**-n**, **-name** _NAME_
> 许可证中的作者姓名。依次回退到 LICENSE_FULL_NAME 环境变量，再回退到 git config。

**-y**, **-year** _YEAR_
> 版权声明的年份。默认为当前年份。

**-o** _FILE_
> 将许可证保存到指定文件而不是输出到 stdout。

**-help**
> 显示帮助信息。

# DESCRIPTION

**license** 从命令行生成开源许可证文件。它支持 GitHub Licenses API 上列出的所有许可证类型及更多，包括 MIT、Apache-2.0、GPL-3.0、BSD-2-Clause、ISC、MPL-2.0 和 Unlicense。

该工具默认将许可证文本输出到 stdout。使用 **-o** 可直接保存到文件。作者姓名依次从命令行选项、**LICENSE_FULL_NAME** 环境变量或 git/hg 配置中解析。

# CAVEATS

存在多种许可证生成器的实现（nishanths/license、azu/license-generator 等），它们的选项约定各不相同。本页记录的是用 Go 编写的 **nishanths/license**。可用 **license -help** 检查安装的是哪个工具。

# HISTORY

**license**（nishanths/license）由 **Nishanth Shanmugham** 创建，使用 **Go** 编写。

# INSTALL

```aur: yay -S license```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[licensor](/man/licensor)(1), [git](/man/git)(1)
