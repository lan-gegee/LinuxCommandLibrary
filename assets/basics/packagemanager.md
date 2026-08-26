# 软件包管理器

## 该用哪个软件包管理器？
每个发行版家族都自带自己的软件包管理器。在表格中找到你的发行版，然后在下方各小节中使用对应的命令。大多数安装/卸载操作需要 **sudo**。

| 软件包管理器 | 发行版 |
|-----|-------------|
| **apt**、**apt-get**、**dpkg** | Debian、Ubuntu、Mint |
| **dnf**、**yum**、**rpm** | Fedora、RHEL、CentOS |
| **pacman** | Arch、Manjaro |
| **zypper** | openSUSE |
| **emerge** | Gentoo |
| **apk** | Alpine |
| **pkg** | FreeBSD、Termux |
| **snap**、**flatpak** | 跨发行版的应用格式 |

**apt** 是 **apt-get**/**apt-cache** 更友好的前端，交互使用时也是更好的选择。在 Fedora 上，**dnf** 已取代 **yum**。

## 从软件仓库安装
```[apt](/man/apt) install [packageName]```
```[dnf](/man/dnf) install [packageName]```
```[yum](/man/yum) install [packageName]```
```[pacman](/man/pacman) -S [packageName]```
```[zypper](/man/zypper) install [packageName]```
```[emerge](/man/emerge) -av [packageName]```
```[apk](/man/apk) add [packageName]```
```[pkg](/man/pkg) install [packageName]```
```[snap](/man/snap) install [packageName]```
```[flatpak](/man/flatpak) install [remote] [packageName]```

## 从本地文件安装
```[dpkg](/man/dpkg) -i [package.deb]```
```[apt](/man/apt) install ./[package.deb]```
```[dnf](/man/dnf) install [package.rpm]```
```[rpm](/man/rpm) -i [package.rpm]```
```[pacman](/man/pacman) -U [package.pkg.tar.zst]```
```[flatpak](/man/flatpak) install [package.flatpakref]```
```[pkg](/man/pkg) add [package.txz]```

优先使用 **apt install ./package.deb** 而不是 **dpkg -i**：apt 会解析并安装缺失的依赖，dpkg 则不会。

## 移除/卸载
```[apt](/man/apt) remove [packageName]```
```[dnf](/man/dnf) remove [packageName]```
```[yum](/man/yum) remove [packageName]```
```[pacman](/man/pacman) -Rs [packageName]```
```[zypper](/man/zypper) remove [packageName]```
```[emerge](/man/emerge) --depclean [packageName]```
```[apk](/man/apk) del [packageName]```
```[pkg](/man/pkg) delete [packageName]```
```[snap](/man/snap) remove [packageName]```
```[flatpak](/man/flatpak) uninstall [packageName]```

**apt purge** 还会删除该软件包的系统级配置文件；**pacman -Rs** 在移除软件包的同时删除不再被其他软件需要的依赖。

清理不再被任何软件需要的依赖。
```[apt](/man/apt) autoremove```
```[dnf](/man/dnf) autoremove```
```[pacman](/man/pacman) -Qdtq```

## 查找软件包
```[apt](/man/apt) search [query]```
```[apt-cache](/man/apt-cache) search [query]```
```[dnf](/man/dnf) search [query]```
```[yum](/man/yum) search [query]```
```[pacman](/man/pacman) -Ss [query]```
```[zypper](/man/zypper) search [query]```
```[emerge](/man/emerge) -S [query]```
```[apk](/man/apk) search [query]```
```[pkg](/man/pkg) search [query]```
```[snap](/man/snap) find [query]```
```[flatpak](/man/flatpak) search [query]```

## 查看软件包信息
```[apt](/man/apt) show [packageName]```
```[apt-cache](/man/apt-cache) show [packageName]```
```[dpkg](/man/dpkg) -s [packageName]```
```[dnf](/man/dnf) info [packageName]```
```[yum](/man/yum) info [packageName]```
```[pacman](/man/pacman) -Si [packageName]```
```[zypper](/man/zypper) info [packageName]```
```[apk](/man/apk) info [packageName]```
```[pkg](/man/pkg) info [packageName]```
```[snap](/man/snap) info [packageName]```
```[pip](/man/pip) show [packageName]```

## 更新软件包列表
刷新可用软件包及其版本的列表，但不安装任何东西。
```[apt](/man/apt) update```
```[dnf](/man/dnf) check-update```
```[yum](/man/yum) check-update```
```[zypper](/man/zypper) refresh```
```[emerge](/man/emerge) --sync```
```[apk](/man/apk) update```
```[pkg](/man/pkg) update```

## 升级已安装的软件包
```[apt](/man/apt) upgrade```
```[dnf](/man/dnf) upgrade```
```[yum](/man/yum) update```
```[pacman](/man/pacman) -Syu```
```[zypper](/man/zypper) update```
```[emerge](/man/emerge) -avuDN @world```
```[apk](/man/apk) upgrade```
```[pkg](/man/pkg) upgrade```
```[snap](/man/snap) refresh```
```[flatpak](/man/flatpak) update```

**在 Arch 上，务必把同步与升级放在一起执行**，即使用 **pacman -Syu**。先用 **-Sy** 刷新数据库再单独安装软件包可能损坏系统（部分升级）。

## 文件属于哪个软件包？
```[dpkg](/man/dpkg) -S /usr/bin/[file]```
```[dnf](/man/dnf) provides /usr/bin/[file]```
```[rpm](/man/rpm) -qf /usr/bin/[file]```
```[pacman](/man/pacman) -Qo /usr/bin/[file]```

列出某个软件包安装的文件。
```[dpkg](/man/dpkg) -L [packageName]```
```[rpm](/man/rpm) -ql [packageName]```
```[pacman](/man/pacman) -Ql [packageName]```

## 添加软件仓库源
```[add-apt-repository](/man/add-apt-repository) ppa:[userName]/[ppaName]```
```[dnf](/man/dnf) config-manager --add-repo [url]```
```[yum-config-manager](/man/yum-config-manager) --add-repo [url]```
```[zypper](/man/zypper) addrepo [url] [alias]```
```[flatpak](/man/flatpak) remote-add flathub https://flathub.org/repo/flathub.flatpakrepo```

## 列出已安装的软件包
```[apt](/man/apt) list --installed```
```[dpkg](/man/dpkg) -l```
```[dnf](/man/dnf) list installed```
```[rpm](/man/rpm) -qa```
```[pacman](/man/pacman) -Q```
```[zypper](/man/zypper) packages --installed-only```
```[apk](/man/apk) list --installed```
```[snap](/man/snap) list```
```[flatpak](/man/flatpak) list```
```[pip](/man/pip) list```

## AUR 助手
在 Arch 上，**yay** 和 **paru** 使用与 pacman 相同的选项从 AUR 安装社区软件包。
```[yay](/man/yay) -S [packageName]```
```[paru](/man/paru) -S [packageName]```
