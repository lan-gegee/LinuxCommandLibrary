# TAGLINE

GPU 加速的 WPA/WPA2 密码审计

# TLDR

显示 **基准测试**速度

```pyrit benchmark```

列出**可用核心**

```pyrit list_cores```

设置目标 **ESSID**

```pyrit -e "[ESSID]" create_essid```

**分析**抓包文件

```pyrit -r [file.cap] analyze```

**导入**密码到数据库

```pyrit -i [wordlist.txt] import_passwords```

**导出**密码

```pyrit -o [output.txt] export_passwords```

为密码生成 **PMK**

```pyrit batch```

**使用数据库发起攻击**

```pyrit -r [file.cap] attack_db```

# SYNOPSIS

**pyrit** [**-e** _essid_] [**-r** _file_] [**-i** _file_] [**-o** _file_] _command_

# COMMANDS

**benchmark**
> 测试破解速度

**list_cores**
> 显示可用的计算单元

**create_essid**
> 在数据库中创建 ESSID

**analyze**
> 分析抓包文件

**import_passwords**
> 将字典导入数据库

**export_passwords**
> 从数据库导出密码

**batch**
> 为所有密码计算 PMK

**attack_db**
> 使用预计算的 PMK 破解密码

**attack_passthrough**
> 直接使用密码进行破解

# DESCRIPTION

**pyrit** 利用 GPU 计算加速 WPA/WPA2 密码破解。它预先从密码和 ESSID 计算成对主密钥（PMK），存储在数据库中，以便针对捕获的握手包快速验证。

该工具利用 CUDA、OpenCL 和 CPU 核心来最大化计算吞吐量，使针对 WPA 的字典攻击显著提速。

# CAVEATS

仅限授权的安全测试。GPU 支持需要相应驱动。数据库可能增长得很大。效果取决于密码是否在字典之中。

# HISTORY

**pyrit** 为 WiFi 安全研究和渗透测试而创建。它展示了弱 WPA 密码面对 GPU 加速攻击时的脆弱性。

# INSTALL

```aur: yay -S pyrit```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[aircrack-ng](/man/aircrack-ng)(1), [hashcat](/man/hashcat)(1), [wifite](/man/wifite)(1)
