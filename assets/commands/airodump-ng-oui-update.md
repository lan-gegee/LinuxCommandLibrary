# TAGLINE

更新 IEEE OUI 厂商数据库

# TLDR

**更新** OUI 数据库

```sudo airodump-ng-oui-update```

# SYNOPSIS

**airodump-ng-oui-update**

# DESCRIPTION

**airodump-ng-oui-update** 下载最新的 IEEE OUI（Organizationally Unique Identifier，组织唯一标识符）数据库文件。该数据库将 MAC 地址前缀映射到厂商名称，使 airodump-ng 能够显示设备制造商。

该工具从 IEEE 网站获取数据库并将其安装到 aircrack-ng 数据目录中，通常是 /usr/share/aircrack-ng/ 或类似位置。

# CAVEATS

需要联网和 root 权限。IEEE OUI 数据库会定期更新；建议偶尔运行此命令，以便为新设备获取准确的厂商信息。

# HISTORY

**airodump-ng-oui-update** 是随 aircrack-ng 套件附带的辅助脚本，加入它是为了简化 OUI 数据库的更新，免去手动下载和放置文件的麻烦。

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

[airodump-ng](/man/airodump-ng)(1), [aircrack-ng](/man/aircrack-ng)(1)

# RESOURCES

```[Source code](https://github.com/aircrack-ng/aircrack-ng)```

```[Homepage](https://www.aircrack-ng.org/)```

```[Documentation](https://www.aircrack-ng.org/documentation.html)```

<!-- verified: 2026-06-11 -->
