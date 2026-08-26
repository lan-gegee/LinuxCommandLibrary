# 单行命令

## 用 sudo 运行上一条命令
```[sudo](/man/sudo) !!```

## 重复上一条命令
```!!```

## 修正上一条命令的拼写错误
```^wrong^correct^```

## 交互式搜索命令历史
```Ctrl+R```

## 在编辑器中编辑当前命令行
```Ctrl+X Ctrl+E```

## 用于重复上一条命令的别名
```alias r='fc -s'```

## 显示最常用的命令
```history | awk '{print $2}' | sort | uniq -c | sort -nr | head```

## 重新加载 Shell 配置
```source ~/.bashrc```

## 检查命令是否存在
```command -v cmd >/dev/null && echo yes```

## 切换到上一个目录
```[cd](/man/cd) -```

## 创建目录并进入
```[mkdir](/man/mkdir) dir && [cd](/man/cd) dir```

## 创建 100 个带编号的目录
```[mkdir](/man/mkdir) project{01..100}```

## 快速备份一个文件
```[cp](/man/cp) file{,.bak}```

## 清空/截断文件
```> file.txt```

## 批量重命名文件
```for f in *.txt; do mv "$f" "${f%.txt}.bak"; done```

## 创建符号链接
```[ln](/man/ln) -s target link```

## 只显示目录
```[ls](/man/ls) -d */```

## 按修改时间列出文件
```[ls](/man/ls) -lt```

## 统计目录中的文件数
```[ls](/man/ls) | [wc](/man/wc) -l```

## 树状查看目录
```[tree](/man/tree)```

## 带行号显示文件
```[nl](/man/nl) file.txt```

## 统计文件行数
```[wc](/man/wc) -l file.txt```

## 去除重复行
```[sort](/man/sort) file | [uniq](/man/uniq)```

## 在文件中查找并替换
```[sed](/man/sed) -i 's/old/new/g' *.txt```

## 递归搜索并忽略大小写
```[grep](/man/grep) -ir "text" .```

## 按名称查找文件
```[find](/man/find) . -iname "*.log"```

## 查找大于 100MB 的文件
```[find](/man/find) . -type f -size +100M```

## 删除 30 天前的旧文件
```[find](/man/find) . -mtime +30 -delete```

## 查找并删除空目录
```[find](/man/find) . -type d -empty -delete```

## 查找失效的符号链接
```[find](/man/find) . -xtype l```

## 查找最大的文件和目录
```[du](/man/du) -ah . | [sort](/man/sort) -hr | [head](/man/head) -20```

## 按大小排序列出目录占用空间
```[du](/man/du) -sh * | [sort](/man/sort) -hr```

## 以人类可读格式显示磁盘用量
```[df](/man/df) -h```

## 监控文件变化
```[tail](/man/tail) -f logfile```

## 每 2 秒刷新一次命令输出
```[watch](/man/watch) command```

## 在终端显示时钟
```[watch](/man/watch) -n 1 date```

## 创建 tar.gz 备份
```[tar](/man/tar) czf backup.tar.gz directory/```

## 解压 tar.gz 归档
```[tar](/man/tar) xzf archive.tar.gz```

## 解压任意格式的归档
```[atool](/man/atool) -x archive```

## 分割大文件
```[split](/man/split) -b 1G largefile part-```

## 重组被分割的文件
```[cat](/man/cat) part-* > largefile```

## 校验文件校验和
```[sha256sum](/man/sha256sum) file```

## 用 gpg 加密文件
```[gpg](/man/gpg) -c file```

## 生成随机密码
```< /dev/urandom [tr](/man/tr) -dc A-Za-z0-9 | [head](/man/head) -c 32; echo```

## 带进度条复制
```[rsync](/man/rsync) -ah --progress src dest```

## 给任意管道加进度条
```[pv](/man/pv) largefile | [gzip](/man/gzip) > largefile.gz```

## 创建 10GB 稀疏文件
```[truncate](/man/truncate) -s 10G file.img```

## 将 DOS 换行符转换为 Unix 格式
```[dos2unix](/man/dos2unix) file```

## 美化打印标准输入的 JSON
```[jq](/man/jq) .```

## 美化打印 XML
```[xmllint](/man/xmllint) --format file.xml```

## 通过管道将输出发送到剪贴板
```command | [xclip](/man/xclip) -sel clip```

## 在后台运行命令
```command &```

## 脱离终端运行
```[nohup](/man/nohup) command &```

## 按名称杀掉进程
```[pkill](/man/pkill) process_name```

## 按 CPU 排序查看进程
```[top](/man/top)```

## 查看系统运行时长
```[uptime](/man/uptime)```

## 列出 cron 任务
```[crontab](/man/crontab) -l```

## 列出硬件信息
```[lshw](/man/lshw) -short```

## 监控 CPU 温度
```[sensors](/man/sensors)```

## 查看电池电量百分比
```[upower](/man/upower) -i $(upower -e | grep BAT) | grep percentage```

## 显示当前时区
```[timedatectl](/man/timedatectl)```

## 显示日历
```[cal](/man/cal)```

## 显示上月、本月和下月
```[cal](/man/cal) -3```

## 创建内存盘
```[mount](/man/mount) -t tmpfs -o size=1G tmpfs /mnt/ram```

## 磁盘速度测试
```[dd](/man/dd) if=/dev/zero of=test bs=1G count=1 oflag=dsync```

## 将 ISO 刻录到 USB
```[dd](/man/dd) if=iso.iso of=/dev/sdX bs=4M status=progress```

## 安全擦除磁盘
```[shred](/man/shred) -v /dev/sdX```

## 录制终端会话
```[script](/man/script) --log-timing timing.log session.log```

## 回放终端会话
```[scriptreplay](/man/scriptreplay) --log-timing timing.log session.log```

## 获取你的公网 IP 地址
```[curl](/man/curl) ifconfig.me```

## 列出开放的网络端口
```[ss](/man/ss) -tuln```

## 断点续传下载文件
```[wget](/man/wget) -c url```

## 通过 SSH 挂载远程目录
```[sshfs](/man/sshfs) user@host:/remote /local```

## 快速启动本地 HTTP 服务器
```[python3](/man/python3) -m http.server 8000```

## 用 Ruby 快速启动 HTTP 服务器
```[ruby](/man/ruby) -run -e httpd . -p 8000```

## 用 PHP 快速启动 HTTP 服务器
```[php](/man/php) -S localhost:8000```

## 用 Node.js 快速启动 HTTP 服务器
```[npx](/man/npx) http-server```

## 用 bash 写的单行 Web 服务器
```while true; do echo -e "HTTP/1.1 200 OK\n\n$(date)" | nc -l 8080; done```

## 在终端查看天气
```[curl](/man/curl) wttr.in```

## 获取完整天气信息
```[curl](/man/curl) v2.wttr.in```

## 生成二维码
```[qrencode](/man/qrencode) -t ANSI "text"```

## 下载 YouTube 视频
```[yt-dlp](/man/yt-dlp) url```

## 在终端播放 YouTube 视频
```[mpv](/man/mpv) url```

## 以 ASCII 字符在终端播放视频
```[mplayer](/man/mplayer) -vo caca video.mp4```

## 转换图片格式
```[convert](/man/convert) input.jpg output.png```

## 用图片创建动画 GIF
```[convert](/man/convert) -delay 10 -loop 0 *.png animation.gif```

## 将视频转换为 GIF
```[ffmpeg](/man/ffmpeg) -i input.mp4 output.gif```

## 合并多个 PDF
```[gs](/man/gs) -dBATCH -dNOPAUSE -sDEVICE=pdfwrite -sOutputFile=out.pdf in1.pdf in2.pdf```

## 在终端查看 PDF
```[pdftotext](/man/pdftotext) file.pdf - | [less](/man/less)```

## 显示当前 git 分支
```[git](/man/git) branch --show-current```

## 简洁显示 git 状态
```[git](/man/git) status -sb```

## 用 ASCII 字符画显示系统信息
```[neofetch](/man/neofetch)```
```[screenfetch](/man/screenfetch)```

## 显示 fortune 格言和奶牛
```[fortune](/man/fortune) | [cowsay](/man/cowsay)```

## 彩虹文字
```echo "text" | [lolcat](/man/lolcat)```

## 模拟慢速打字
```echo "text" | [pv](/man/pv) -qL 10```

## 黑客帝国数字雨
```[cmatrix](/man/cmatrix)```

## 播放火车动画
```[sl](/man/sl)```

## 发出蜂鸣声
```echo -e "\a"```
