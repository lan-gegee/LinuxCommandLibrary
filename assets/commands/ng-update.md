# TAGLINE

更新 Angular 软件包并运行自动迁移

# TLDR

**列出**已安装 Angular 软件包的可用更新

```ng update```

**一起更新 Angular core 和 CLI**

```ng update @angular/core @angular/cli```

**更新指定软件包**

```ng update [package-name]```

**更新到 next/预发布版本**

```ng update @angular/core --next```

**强制更新**，忽略对等依赖版本不匹配

```ng update @angular/core --force```

**仅运行迁移**，不更改已安装的版本

```ng update @angular/core --migrate-only --from=[15] --to=[16]```

**为每个更新步骤创建 git 提交**

```ng update @angular/core @angular/cli --create-commits```

# SYNOPSIS

**ng** **update** [_packages_...] [_options_]

# DESCRIPTION

**ng update** 将 Angular 软件包及其依赖更新到更新的版本，并运行相应的原理图（schematics），以迁移应用代码中的破坏性变更。它是 **Angular CLI** 的一部分。

不带参数运行 **ng update** 时，会列出所有有新版本可用的已安装软件包，以及建议使用的更新命令。给定一个或多个包名时，它会执行更新并运行相关的迁移原理图。

默认情况下，若仓库存在未提交的更改，该命令会拒绝运行；可传入 **--allow-dirty** 覆盖这一行为，或者先提交/暂存改动。

# PARAMETERS

**--allow-dirty**
> 当工作树中存在修改过或未跟踪的文件时仍允许更新（默认：false）。

**-C**, **--create-commits**
> 为每次更新和迁移步骤创建版本控制提交（默认：false）。

**--force**
> 绕过对等依赖版本不匹配的问题（默认：false）。

**--from** _version_
> 迁移的起始版本。仅在更新单个包并配合 **--migrate-only** 时有效。

**--to** _version_
> 迁移的目标版本。必须与 **--from** 和 **--migrate-only** 一起使用；默认为检测到的已安装版本。

**--migrate-only**
> 仅运行迁移原理图，不更改实际安装的版本。

**--name** _name_
> 指定要运行的某个具体迁移。仅对单个包的更新有效。

**--next**
> 解析目标版本时采用预发布版本（beta / 候选发布版）。

**--verbose**
> 显示额外的执行细节。

**--help**
> 打印帮助信息。

# CAVEATS

运行 **ng update** 之前，务必先提交或暂存正在进行的工作；携带 **--allow-dirty --force** 运行可能使仓库陷入难以恢复的状态。迁移脚本按一次前进一步（一个次版本）的方式编写和测试，因此不支持用单条命令跨越多个大版本：请逐个大版本依次升级。

# HISTORY

**ng update** 随 **2018 年**的 **Angular CLI 6** 重构版推出，取代了此前手动的升级流程。它属于驱动 Angular 自动化迁移体系的一套基于原理图的工具链。

# SEE ALSO

[ng](/man/ng)(1), [ng-add](/man/ng-add)(1)
