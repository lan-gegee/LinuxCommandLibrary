# TAGLINE

使用 Koji 构建系统构建 RPM 软件包

# TLDR

从 **src.rpm** 构建

```koji build target path/to/package.src.rpm```

从 **SCM URL** 构建

```koji build target git+https://src.fedoraproject.org/rpms/pkg.git#commit```

执行 **scratch** 构建

```koji build target path/to/package.src.rpm --scratch```

构建并**等待**完成

```koji build target path/to/package.src.rpm --wait```

构建但**不等待**

```koji build target path/to/package.src.rpm --nowait```

显示**帮助**

```koji build --help```

# SYNOPSIS

**koji build** [_options_] _target_ _srpm_|_scm_url_

# DESCRIPTION

**koji build** 使用 Koji 构建系统构建 RPM 软件包。它可以从源码 RPM 构建，也可以从指向软件包仓库的 SCM（源码管理）URL 构建。

# PARAMETERS

**target**
> 定义构建环境的构建目标

**--scratch**
> 执行 scratch 构建（不会导入软件仓库）

**--wait**
> 即使在后台运行也等待构建完成

**--nowait**
> 提交构建后立即返回

**--arch-override ARCHES**
> 覆盖要为其构建的架构

**--repo-id REPO**
> 为构建使用指定的仓库

**--background**
> 以较低优先级运行构建

**-h, --help**
> 显示帮助信息

# CAVEATS

Scratch 构建是临时性的，不会导入 Koji 的软件包数据库。SCM URL 必须使用包含 commit 哈希的特定格式。需要正确的 Koji 凭据和权限。

# HISTORY

**koji** 是 Fedora 的构建系统，用于跨多种架构和发行版构建并跟踪软件包。

# INSTALL

```dnf: sudo dnf install koji```

```brew: brew install koji```

```nix: nix profile install nixpkgs#koji```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[koji](/man/koji)(1), [rpmbuild](/man/rpmbuild)(8), [mock](/man/mock)(1)
