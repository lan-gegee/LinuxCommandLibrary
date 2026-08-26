# TAGLINE

自动化 SQL 注入检测工具

# TLDR

**测试 URL 是否存在 SQL 注入**

```sqlmap -u "[https://example.com/page?id=1]"```

**以更高的检测等级测试**

```sqlmap -u "[url?id=1]" --level [5] --risk [3]```

**枚举数据库**

```sqlmap -u "[url?id=1]" --dbs```

**导出特定表的数据**

```sqlmap -u "[url?id=1]" -D [database] -T [table] --dump```

**用数据测试 POST 请求**

```sqlmap -u "[url]" --data="[username=admin&password=test]"```

**从文件加载请求**（从代理抓取）

```sqlmap -r [request.txt]```

**通过 SQL 注入获取 OS shell**

```sqlmap -u "[url?id=1]" --os-shell```

**以批处理模式运行**（无交互提示）

```sqlmap -u "[url?id=1]" --batch```

# SYNOPSIS

**sqlmap** [_options_] -u _URL_

**sqlmap** [_options_] -r _REQUEST_FILE_

# PARAMETERS

**-u** _URL_
> 包含可注入参数的目标 URL

**-r** _FILE_
> 从文件加载 HTTP 请求

**--data** _DATA_
> POST 数据字符串

**--cookie** _COOKIE_
> HTTP Cookie 头的值

**-p** _PARAM_
> 可测试的参数

**--level** _LEVEL_
> 测试彻底程度（1-5，默认：1）

**--risk** _RISK_
> 测试风险级别（1-3，默认：1）

**--technique** _TECH_
> 注入技术（B、E、U、S、T、Q）

**--dbms** _DBMS_
> 强制指定数据库类型

**--dbs**
> 枚举数据库

**--tables**
> 枚举表

**--columns**
> 枚举列

**--dump**
> 导出表条目

**-D** _DB_
> 目标数据库

**-T** _TABLE_
> 目标表

**-C** _COLUMNS_
> 目标列

**--os-shell**
> 获取交互式 OS shell

**--os-cmd** _CMD_
> 执行操作系统命令

**--batch**
> 非交互模式

**--threads** _NUM_
> 并发请求数（默认：1）

**-v** _LEVEL_
> 详细程度（0-6）

**--wizard**
> 面向初学者的交互式向导

# DESCRIPTION

**sqlmap** 是一款自动化 SQL 注入与数据库接管工具。它能检测并利用 Web 应用中的 SQL 注入漏洞，支持多种数据库系统，包括 MySQL、PostgreSQL、Oracle、Microsoft SQL Server 和 SQLite。

该工具使用多种注入技术：布尔盲注、报错注入、UNION 查询注入、堆叠查询注入、时间盲注和内联查询注入。它可以枚举数据库、表、列并导出数据。高级功能包括通过数据库函数获得操作系统访问权限。

检测级别（**--level**）控制测试的彻底程度——级别越高会测试更多注入点，包括 cookie 和请求头。风险级别（**--risk**）控制是否使用可能有危害的测试（例如长时间延迟）。

# CAVEATS

只能在获得明确授权的情况下使用——未经授权的测试属于违法行为。过高的 level/risk 设置可能导致误报或服务器故障。某些注入类型可能会修改数据库数据。Web 应用防火墙可能拦截或限制请求速率。结果应人工核实以确保准确。

# HISTORY

sqlmap 由 **Daniele Bellucci** 和 **Bernardo Damele A. G.** 创建，开发始于 **2006 年**。它已成为使用最广泛的 SQL 注入渗透测试工具之一。该项目开源、使用 Python 编写，目前仍在活跃开发。sqlmap 默认包含在 Kali Linux 及其他注重安全的发行版中。

# INSTALL

```pacman: sudo pacman -S sqlmap```

```zypper: sudo zypper install sqlmap```

```brew: brew install sqlmap```

```nix: nix profile install nixpkgs#sqlmap```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[burpsuite](/man/burpsuite)(1), [nikto](/man/nikto)(1), [skipfish](/man/skipfish)(1), [wpscan](/man/wpscan)(1)
