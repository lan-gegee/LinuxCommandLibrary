# TAGLINE

从 spec 文件构建 RPM 软件包

# TLDR

构建**二进制和源码**软件包

```rpmbuild -ba path/to/spec_file```

仅构建**二进制软件包**

```rpmbuild -bb path/to/spec_file```

仅构建**源码软件包**

```rpmbuild -bs path/to/spec_file```

使用**自定义宏**定义构建

```rpmbuild -bb --define "version 1.0" path/to/spec_file```

仅**准备**源码（解包并打补丁）

```rpmbuild -bp path/to/spec_file```

为**特定架构**构建

```rpmbuild -bb --target x86_64 path/to/spec_file```

从现有的**源码软件包重建**

```rpmbuild --rebuild path/to/package.src.rpm```

# SYNOPSIS

**rpmbuild** {**-ba**|**-bb**|**-bp**|**-bc**|**-bi**|**-bl**|**-bs**|**-br**|**-bd**} [_options_] _SPECFILE_

# DESCRIPTION

**rpmbuild** 基于 spec 文件构建二进制和源码软件包。软件包由文件归档以及用于安装和卸载这些归档文件的元数据组成。该工具通过多个构建阶段来处理 spec 文件。

# PARAMETERS

**-ba**
> 构建二进制和源码软件包

**-bb**
> 仅构建二进制软件包

**-bp**
> 仅解开源码并应用补丁（%prep 阶段）

**-bf**
> 配置源码（%conf 阶段，相当于 ./configure）

**-bc**
> 编译源码（%build 阶段）

**-bi**
> 将二进制文件安装到 build root 并运行 %check

**-bl**
> 校验 %files 中列出的所有文件是否存在

**-bs**
> 仅构建源码软件包

**-br**
> 构建源码软件包，并动态解析构建依赖

**-bd**
> 检查动态构建依赖并生成构建需求

**-D**, **--define** _'MACRO EXPR'_
> 定义一个带值的宏

**--target** _PLATFORM_
> 设置构建目标架构（例如 `x86_64`、`aarch64`）

**--buildroot** _DIRECTORY_
> 覆盖构建根目录

**--clean**
> 完成后移除构建目录树

**--nobuild**
> 跳过所有构建阶段（只检查 spec 文件语法）

**--noprep**
> 跳过 %prep 阶段

**--noclean**
> 跳过 %clean 阶段

**--nocheck**
> 跳过 %check 阶段

**--nodeps**
> 不校验构建依赖

**--short-circuit**
> 直接跳到指定的阶段（仅可与 -bc、-bi、-bb 搭配使用）

**--rebuild** _SOURCEPKG_
> 安装源码软件包、构建二进制软件包，然后清理

**--recompile** _SOURCEPKG_
> 与 --rebuild 类似，但执行到 install 阶段即停止，不生成二进制软件包

**--rmsource**
> 构建后移除源码文件

**--rmspec**
> 构建后移除 spec 文件

**--with** _OPTION_
> 启用 spec 文件中定义的条件构建选项

**--without** _OPTION_
> 禁用 spec 文件中定义的条件构建选项

# CONFIGURATION

**~/.rpmmacros**
> 用户级宏定义，可覆盖系统默认值；常用于设置 **%_topdir** 来指定构建目录树的位置。

**/etc/rpm/macros**
> 系统级宏覆盖，对机器上的所有用户生效。

**/usr/lib/rpm/macros**
> rpm 软件包自带的默认宏定义，规定了构建路径、编译器标志和平台默认值。

# CAVEATS

spec 文件定义了如何构建软件包。宏定义分布在 /usr/lib/rpm/macros、/etc/rpm/macros 和 ~/.rpmmacros 中。除非使用 --nodeps，否则构建前必须先装好构建依赖。

# HISTORY

**rpmbuild** 是 **RPM**（RPM Package Manager）体系的一部分，最初由 Red Hat 开发，用于管理 Linux 系统上的软件包。

# INSTALL

```apt: sudo apt install rpm```

```dnf: sudo dnf install rpm```

```apk: sudo apk add rpm```

```zypper: sudo zypper install rpm```

```brew: brew install rpm```

```nix: nix profile install nixpkgs#rpm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[rpm](/man/rpm)(8), [rpmspec](/man/rpmspec)(8), [rpmsign](/man/rpmsign)(8), [mock](/man/mock)(1)
