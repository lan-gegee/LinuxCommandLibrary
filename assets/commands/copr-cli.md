# TAGLINE

COPR 构建系统客户端

# TLDR

**显示已认证的用户**

```copr-cli whoami```

**创建新的 COPR 项目**

```copr-cli create [project_name] --chroot [fedora-rawhide-x86_64] --chroot [epel-9-x86_64]```

**从本地 SRPM 构建软件包**

```copr-cli build [project_name] [package.src.rpm]```

**从 SRPM URL 构建**

```copr-cli build [project_name] [https://example.com/package.src.rpm]```

**从 PyPI 软件包构建**

```copr-cli buildpypi [project_name] --packagename [requests]```

**监视进行中的构建**

```copr-cli watch-build [build_id]```

**列出你的 COPR 项目**

```copr-cli list```

**检查构建状态**

```copr-cli status [build_id]```

**取消正在运行的构建**

```copr-cli cancel [build_id]```

**下载已构建的软件包**

```copr-cli download-build [build_id]```

**删除项目**

```copr-cli delete [project_name]```

# SYNOPSIS

**copr-cli** _command_ [_options_] [_arguments_]

# PARAMETERS

**whoami**
> 打印由所配置 API token 认证的用户。

**list** [_OWNER_]
> 列出当前用户或指定所有者的项目。

**list-chroots**
> 列出 COPR 服务器上可用的 chroot。

**create** _NAME_
> 创建新的 COPR 项目（至少需要一个 --chroot）。

**modify** _PROJECT_
> 修改现有项目的设置。

**delete** _PROJECT_
> 删除项目。

**build** _PROJECT_ _SRPM_|_URL_
> 从本地 SRPM 或 SRPM URL 提交构建。

**buildpypi** _PROJECT_
> 从 PyPI 源码包构建。

**buildgem** _PROJECT_
> 从 RubyGems gem 构建。

**buildscm** _PROJECT_
> 从远程 SCM 仓库（git/svn）构建。

**build-distgit** _PROJECT_
> 从 DistGit 仓库构建软件包。

**status** _BUILD_ID_
> 打印构建的当前状态。

**watch-build** _BUILD_ID_
> 跟踪构建直到其完成。

**cancel** _BUILD_ID_
> 取消正在运行的构建。

**download-build** _BUILD_ID_ [_DEST_]
> 下载指定构建产出的 RPM。

**regenerate-repos** _PROJECT_
> 为项目重新生成仓库元数据。

**-r**, **--chroot** _CHROOT_
> 指定构建目标（如 fedora-rawhide-x86_64、epel-9-x86_64）。可重复使用。

**--nowait**
> 提交构建但不等待其完成。

**--background**
> 在后台运行构建（优先级低于普通构建）。

**--after-build-id** _ID_
> 让本次构建在指定构建完成后运行（批量依赖）。

**--timeout** _SECONDS_
> 覆盖默认的构建超时时间。

**--config** _FILE_
> 使用其他配置文件（默认：~/.config/copr）。

# CONFIGURATION

**~/.config/copr**
> 用于 COPR 构建系统身份验证的 API token 配置。

# DESCRIPTION

**copr-cli** 是 Fedora 的 COPR 构建系统的命令行客户端。开发者可以用它创建项目、提交构建、管理仓库并自动化软件包分发，而无需使用网页界面。

该工具处理完整的软件包生命周期：创建带指定构建目标（chroot）的项目、提交源码 RPM 进行构建、监控构建进度，以及下载最终的软件包。它支持从本地文件、URL 或 SCM 仓库构建。

对于自动构建并向 COPR 发布软件包的 CI/CD 流水线而言，copr-cli 至关重要。身份验证通过配置文件中的 API token 完成，因此可以进行脚本化操作。

# CAVEATS

需要 Fedora Account System（FAS）账户，以及在 **~/.config/copr** 中配置好的 API token。构建前必须为项目启用相应的构建 chroot。大型构建可能耗时较长；异步操作请使用 **--nowait**。

# HISTORY

copr-cli 与 COPR 构建服务一同由 Fedora 项目开发。它以编程方式提供与 **copr.fedorainfracloud.org** 网页界面相同的功能，便于实现自动化并与开发工作流集成。

# INSTALL

```dnf: sudo dnf install copr-cli```

```pacman: sudo pacman -S copr-cli```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[copr](/man/copr)(1), [rpmbuild](/man/rpmbuild)(1), [mock](/man/mock)(1), [dnf](/man/dnf)(1)
