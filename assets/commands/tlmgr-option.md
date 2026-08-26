# TAGLINE

配置 TeX Live 安装选项

# TLDR

**显示所有选项**

```tlmgr option```

**显示特定选项**

```tlmgr option [optionname]```

**设置选项值**

```tlmgr option [optionname] [value]```

**显示可用选项**

```tlmgr option showall```

# SYNOPSIS

**tlmgr option** [_option_ [_value_]]

# PARAMETERS

**repository**
> 软件包仓库 URL。

**autobackup**
> 保留备份的数量。

**backupdir**
> 备份目录。

**docfiles**
> 安装文档（0/1）。

**srcfiles**
> 安装源文件（0/1）。

# DESCRIPTION

**tlmgr option** 管理 TeX Live 的安装选项。配置仓库、备份设置以及要安装的内容。TeX Live Manager 的组成部分。

# SEE ALSO

[tlmgr-conf](/man/tlmgr-conf)(1), [tlmgr](/man/tlmgr)(1)
