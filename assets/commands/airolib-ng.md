# TAGLINE

预计算 WPA/WPA2 PMK 数据库以加速破解

# TLDR

**创建**一个新数据库

```airolib-ng [database.db] --init```

**导入**字典文件

```airolib-ng [database.db] --import passwd [wordlist.txt]```

**导入**一个 ESSID

```airolib-ng [database.db] --import essid [essid_file.txt]```

**批量处理**（预计算 PMK）

```airolib-ng [database.db] --batch```

**验证**数据库完整性

```airolib-ng [database.db] --verify```

显示数据库**统计信息**

```airolib-ng [database.db] --stats```

# SYNOPSIS

**airolib-ng** _database_ _operation_ [_options_]

# DESCRIPTION

**airolib-ng** 管理用于 WPA/WPA2 破解的成对主密钥（PMK）预计算数据库。PMK 计算是 WPA 破解中最耗时的部分；针对常见 ESSID 和密码预先计算 PMK 可以显著加快攻击速度。

该工具创建 aircrack-ng 可直接使用的 SQLite 数据库，用存储空间换取破解速度。

# PARAMETERS

**--init**
> 初始化一个新数据库

**--import passwd** _file_
> 从字典文件导入密码

**--import essid** _file_
> 从文件导入 ESSID

**--import cowpatty** _file_
> 导入 cowpatty 哈希文件

**--batch**
> 计算所有缺失的 PMK

**--batch --essid** _name_
> 为特定 ESSID 计算 PMK

**--verify** [_all_]
> 验证数据库完整性

**--stats**
> 显示数据库统计信息

**--clean** [_all_]
> 移除已计算的 PMK

**--sql** _query_
> 执行 SQL 查询

# CAVEATS

预计算只对已知 ESSID 有帮助。数据库文件可能非常大。PMK 与 ESSID 绑定；通用字典攻击无法受益。计算 PMK 非常消耗 CPU。

# HISTORY

**airolib-ng** 被加入 aircrack-ng 套件，是为了通过预计算开销巨大的 PBKDF2 运算，使对 WPA/WPA2 网络的实用化攻击成为可能。

# INSTALL

```apt: sudo apt install aircrack-ng```

```dnf: sudo dnf install aircrack-ng```

```pacman: sudo pacman -S aircrack-ng```

```apk: sudo apk add aircrack-ng```

```zypper: sudo zypper install aircrack-ng```

```brew: brew install aircrack-ng```

```nix: nix profile install nixpkgs#aircrack-ng```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[aircrack-ng](/man/aircrack-ng)(1), [airodump-ng](/man/airodump-ng)(1), [genpmk](/man/genpmk)(1), [cowpatty](/man/cowpatty)(1)

# RESOURCES

```[Source code](https://github.com/aircrack-ng/aircrack-ng)```

```[Homepage](https://www.aircrack-ng.org/)```

```[Documentation](https://www.aircrack-ng.org/documentation.html)```

<!-- verified: 2026-06-11 -->
