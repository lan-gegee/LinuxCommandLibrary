# TAGLINE

检查 Samba smb.conf 配置文件的正确性

# TLDR

**检查默认 smb.conf** 中的错误

```testparm```

**检查指定的配置文件**

```testparm [path/to/smb.conf]```

**检查并抑制**各部分之间按回车的提示

```testparm -s```

**显示所有参数**，包括未显式设置的默认值

```testparm -v```

**查询特定参数**的值

```testparm --parameter-name "[server role]"```

从指定共享节**查询参数**

```testparm --parameter-name "[path]" --section-name "[myshare]"```

**检查特定主机**是否可访问服务

```testparm [path/to/smb.conf] [hostname] [host_ip]```

# SYNOPSIS

**testparm** [_-s_] [_-v_] [_-l_] [_-d LEVEL_] [_--parameter-name NAME_] [_--section-name NAME_] [_config filename_] [_hostname hostIP_]

# PARAMETERS

**-s**, **--suppress-prompt**
> 显示服务名后不再提示按回车。

**-v**, **--verbose**
> 显示所有选项，包括配置中未显式设置的默认值。

**-l**, **--skip-logic-checks**
> 跳过全局验证逻辑检查。

**--parameter-name** _NAME_
> 打印特定参数的值。可用冒号指定所在节。

**--section-name** _NAME_
> 将 **--parameter-name** 的输出限制在特定配置节。

**--show-all-parameters**
> 显示所有参数及其类型和可能取值。

**-d**, **--debuglevel** _LEVEL_
> 设置调试详细级别（0-10，默认 1）。

**--debug-stdout**
> 将调试输出发送到 stdout 而非 stderr。

**--configfile** _FILE_
> 指定配置文件的位置。

**--option** _NAME=VALUE_
> 在命令行设置特定的 smb.conf 选项。

**-V**, **--version**
> 打印版本信息。

**-?**, **--help**
> 显示帮助。

# DESCRIPTION

**testparm** 是一款 Samba 工具，用于验证 **smb.conf** 配置文件的内部正确性。它解析配置、检查语法错误和无效的参数值，并报告发现的任何问题。如果文件加载成功，它会显示所有已知的服务定义。

当以参数形式提供主机名和 IP 地址时，testparm 还会根据 **hosts allow** 和 **hosts deny** 指令，检查指定主机对每个已配置服务是允许还是拒绝访问。

该工具成功时返回退出码 **0**，出错时返回 **1**，因此适合在脚本和自动化部署流水线中使用。

# CONFIGURATION

默认配置文件为 **/etc/samba/smb.conf**。将其他路径作为第一个位置参数传入即可检查别的文件。校验期间可用 **--option** 覆盖个别设置。

# CAVEATS

testparm 检查的是**语法正确性**，但无法保证服务会按预期工作。通过验证的文件仍可能存在逻辑错误（例如指向不存在的路径或相互冲突的共享权限）。弱加密算法警告（DES、ARCFOUR、SHA1、MD5）仅供参考，与 Samba 的加密回退行为有关。

# HISTORY

**testparm** 自早期版本起就是 **Samba** 套件的一部分。Samba 由 **Andrew Tridgell** 于 **1992** 年编写，最初用于在 Unix 上提供 SMB/CIFS 文件和打印服务。testparm 工具的创建目的是帮助管理员在重启 Samba 守护进程前验证配置变更，减少因配置错误导致的停机。

# INSTALL

```apt: sudo apt install samba-common-bin```

```dnf: sudo dnf install samba-common-tools```

```apk: sudo apk add samba-common-tools```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[smbclient](/man/smbclient)(1), [samba](/man/samba)(7)
