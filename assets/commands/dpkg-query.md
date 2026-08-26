# TAGLINE

查询 dpkg 数据库信息

# TLDR

**列出**所有已安装的软件包

```dpkg-query -l```

列出**匹配模式的**软件包

```dpkg-query -l '[libc6*]'```

列出某个包安装的**文件**

```dpkg-query -L [libc6]```

显示软件包**信息**

```dpkg-query -s [libc6]```

**查找**文件的所属软件包

```dpkg-query -S [/etc/ld.so.conf.d]```

以**自定义格式**打印软件包，每行一个

```dpkg-query -W -f='${Package} ${Version}\n'```

按大小列出**最大的已安装软件包**

```dpkg-query -W -f='${Installed-Size}\t${Package}\n' | sort -rn | head```

找出移除后**遗留的软件包**（配置文件仍在）

```dpkg-query -W -f='${db:Status-Abbrev} ${Package}\n' | grep '^rc'```

# SYNOPSIS

**dpkg-query** _action_ [_options_] [_pattern_|_package_]

# DESCRIPTION

**dpkg-query** 查询 dpkg 数据库以获取基于 Debian 的系统上已安装软件包的信息。它提供对软件包数据库的只读接口，可用于搜索软件包、查看元数据以及确定文件的归属。

在验证软件包安装情况、排查文件冲突和生成软件包清单等系统管理任务中，该工具不可或缺。与 dpkg 本身不同，dpkg-query 只读取信息，从不修改软件包数据库，因此无需提权即可安全使用。

它的自定义输出格式能力使其在脚本和自动化工作流中格外有用。

# PARAMETERS

**-l**, **--list** [_pattern_...]
> 列出匹配模式的软件包，每行显示状态、版本、体系结构和描述。

**-L**, **--listfiles** _package_...
> 列出某个软件包安装的所有文件。

**-s**, **--status** _package_...
> 显示完整的状态条目：版本、依赖关系、描述和维护者。

**-S**, **--search** _pattern_...
> 查找匹配模式的文件属于哪个软件包。

**-p**, **--print-avail** _package_...
> 从 *available* 软件包文件而非已安装状态中显示详情。

**-W**, **--show** [_pattern_...]
> 按 **--showformat** 给定的格式显示软件包。这是供脚本调用的接口。

**-f**, **--showformat**=_format_
> 自定义输出格式。字段引用形如 `${Package}`、`${Version}`、`${Architecture}`、`${Installed-Size}`、`${binary:Summary}`、`${db:Status-Abbrev}` 等；`\n` 和 `\t` 会被识别。

**-c**, **--control-list** _package_
> 列出某软件包的控制文件。

**--control-show** _package_ _control-file_
> 打印单个控制文件的内容，如 `conffiles` 或 `md5sums`。

**--control-path** _package_ [_control-file_]
> 打印软件包控制文件的路径。

**--no-pager**
> 不将输出通过分页器显示。

**--admindir**=_dir_
> 使用其他 dpkg 数据库目录替代 `/var/lib/dpkg`。

# CAVEATS

**-l** 的列宽会被截断到终端宽度，长软件包名和版本号会被悄悄切断；解析时请改用带显式 **--showformat** 的 **-W**，不要去抓取 **-l** 的输出。

模式是 **shell 通配符**而非正则表达式，不加引号的 `*` 会在 dpkg-query 看到之前就被 shell 展开：务必给模式加引号，如 `dpkg-query -l 'libc6*'`。

它只查询 dpkg 已知的信息，也就是本系统上安装的软件包。它无法回答仓库里有哪些可用的软件包，那是 `apt-cache` 的职责。**-S** 也只匹配记录在某包文件清单中的文件，因此维护脚本运行时生成的文件以及 `/usr/local` 下的任何内容都查不到，并会被正确地报告为不属于任何软件包。

注意 **-l** 列出的软件包不一定处于已安装状态：开头的状态字符很关键，`rc` 表示已卸载但配置文件仍留在磁盘上。

# INSTALL

```apt: sudo apt install dpkg```

```dnf: sudo dnf install dpkg```

```pacman: sudo pacman -S dpkg```

```apk: sudo apk add dpkg```

```zypper: sudo zypper install dpkg```

```brew: brew install dpkg```

```nix: nix profile install nixpkgs#dpkg```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[dpkg](/man/dpkg)(1), [dpkg-deb](/man/dpkg-deb)(1), [apt-cache](/man/apt-cache)(8), [apt-file](/man/apt-file)(1), [aptitude](/man/aptitude)(8)

# RESOURCES

```[Source code](https://git.dpkg.org/cgit/dpkg/dpkg.git/)```

```[Homepage](https://wiki.debian.org/Teams/Dpkg)```

<!-- verified: 2026-07-14 -->
