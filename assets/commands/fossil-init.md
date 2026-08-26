# TAGLINE

创建新的 Fossil 仓库

# TLDR

**创建新仓库**

```fossil init [repo.fossil]```

**创建并设置管理员密码**

```fossil init --admin-user [admin] [repo.fossil]```

**创建并设置项目名称**

```fossil init --project-name "[name]" [repo.fossil]```

# SYNOPSIS

**fossil** **init** [_options_] _repository_

# PARAMETERS

**--admin-user** _name_
> 设置管理员用户名。

**--project-name** _name_
> 设置项目名称。

**--project-desc** _text_
> 设置项目描述。

**--template** _repo_
> 使用模板仓库。

**--date-override** _datetime_
> 覆盖初始 check-in 的日期。

# DESCRIPTION

**fossil init** 创建一个新的 Fossil 仓库文件。该仓库是一个单独的 SQLite 数据库，包含所有历史记录、wiki、工单和项目元数据。

初始化后，使用 **fossil open** 创建工作目录。仓库文件可以通过 **fossil ui** 托管以供 Web 访问，或通过 HTTP 提供服务以支持远程协作。

仓库设置包括项目名称、描述和管理员凭证。**--template** 选项允许基于现有仓库创建新仓库并继承其配置。

# INSTALL

```apt: sudo apt install fossil```

```dnf: sudo dnf install fossil```

```pacman: sudo pacman -S fossil```

```apk: sudo apk add fossil```

```zypper: sudo zypper install fossil```

```brew: brew install fossil```

```nix: nix profile install nixpkgs#fossil```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[fossil](/man/fossil)(1)
