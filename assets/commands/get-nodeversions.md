# TAGLINE

Node.js 版本发现工具

# TLDR

**列出本地已安装的版本**

```Get-NodeVersions```

**列出可安装的远程版本**

```Get-NodeVersions -Remote```

**按 semver 范围筛选版本**

```Get-NodeVersions -Remote -Filter ">=18.0.0 <19.0.0"```

**列出匹配过滤条件的本地版本**

```Get-NodeVersions -Filter ">=16.0.0"```

# SYNOPSIS

**Get-NodeVersions** [**-Remote**] [**-Filter** _range_]

# PARAMETERS

**-Remote**
> 列出可从 Node.js 发布服务器下载的版本，而非本地已安装的版本。

**-Filter** _range_
> 用于筛选结果的 semver 版本范围（例如 ">=18.0.0 <19.0.0"）。

# DESCRIPTION

**Get-NodeVersions** 列出本地已安装的 Node.js 版本或远程可供安装的版本。它是 **ps-nvm**（PowerShell Node Version Manager）模块的一部分。

版本以 SemVer.Version 对象的形式返回，按从高到低排序，可与 PowerShell 比较运算符配合使用。使用 **-Remote** 查询 Node.js 发布服务器，使用 **-Filter** 按 semver 范围缩小结果。

# CAVEATS

**-Remote** 标志需要网络访问以查询 Node.js 发布服务器。此命令为 ps-nvm 所特有；其他版本管理器使用不同的命令（例如 `nvm ls-remote`）。

# HISTORY

get-nodeversions 是 **ps-nvm** PowerShell 模块提供的 Node.js 版本管理工具。

# SEE ALSO

[nvm](/man/nvm)(1), [fnm](/man/fnm)(1), [node](/man/node)(1), [ps-nvm](/man/ps-nvm)(1)
