# TAGLINE

Gentoo 软件包构建接口

# TLDR

创建/更新软件包 **manifest**

```ebuild [path/to/file.ebuild] manifest```

**清理**临时构建目录

```ebuild [path/to/file.ebuild] clean```

**获取**源码

```ebuild [path/to/file.ebuild] fetch```

**解压**源码

```ebuild [path/to/file.ebuild] unpack```

**编译**源码

```ebuild [path/to/file.ebuild] compile```

**安装**到临时目录

```ebuild [path/to/file.ebuild] install```

安装到**实际文件系统**

```ebuild [path/to/file.ebuild] qmerge```

**完整构建**（fetch、unpack、compile、install、merge）

```ebuild [path/to/file.ebuild] merge```

# SYNOPSIS

**ebuild** _file_ _command_...

# DESCRIPTION

**ebuild** 是 Gentoo Portage 系统的低层接口。它处理 ebuild 文件，这是一类描述如何构建和安装软件包的 Bash 脚本。

该工具提供对各个构建阶段（fetch、unpack、compile、install、merge）的直接访问，让开发者可以逐步测试和调试软件包。这对创建或修改 ebuild 的包维护者至关重要。

常规的软件包管理使用 emerge，而 ebuild 则提供对构建过程的细粒度控制。它尤其适合在将新软件包加入 portage 树之前进行测试，或手动安装自定义 ebuild。

# PARAMETERS

**manifest**
> 创建/更新软件包 manifest

**clean**
> 移除临时构建文件

**fetch**
> 下载源文件

**unpack**
> 解压源码

**compile**
> 构建软件包

**install**
> 安装到临时目录

**qmerge**
> 合并到实际文件系统

**merge**
> 所有步骤的组合

**unmerge**
> 从实际文件系统移除

**setup**
> 运行构建前设置阶段

**prepare**
> 运行源码准备（打补丁等）

**configure**
> 运行 configure 阶段

**test**
> 运行软件包测试

**prerm**
> 执行卸载前任务

**postrm**
> 执行卸载后任务

**postinst**
> 执行安装后任务

**digest**
> 创建 manifest（manifest 的旧别名）

# CAVEATS

仅限 Gentoo。常规软件包管理请使用 **emerge**。ebuild 文件需要在 portage 树中有特定的目录结构。默认情况下，ebuild 会按顺序执行从开始直到指定阶段的全部阶段，并跳过之前调用中已完成的部分。

# SEE ALSO

[emerge](/man/emerge)(1), [equery](/man/equery)(1)
