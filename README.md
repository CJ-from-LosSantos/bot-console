# 关于Bot console

## 项目愿景

✨ 在一定时间内，希望bot console想成为Telegram一样拥有强大机器人社区的控制终端。它将会让各种群聊成为社区或板块，当然，它的强大不止于此，在于每位开发者的创造力

✨ 拥有丰富多彩的api指令，满足人们对生活的远方与诗

## 关于开发

✨ 该项目可能会用于申请优秀开源项目，希望有能力有想法有创意点子的人可以一起加入开发。如果你有丰富的后端、爬虫、架构设计非常愿意与您一起开发！

🚀 未来一段时间主要先把基础功能做好，在推出个性化的机器人模板文件，最后在奔向bot console最远大的目标

## 关于使用

- 下载对应版本的[微信客户端](https://github.com/tom-snow/wechat-windows-versions/releases/download/v3.6.0.18/WeChatSetup-3.6.0.18.exe)

- 初始化
  
  1. 下载代码后解压
  2. 在有`bot.exe`的目录下进入终端，执行`bot init test_robot`，建议第一次使用debug，cmd：`bot init --debug test_robot`
  3. 正常情况下初始化命令执行成功会生成了一些机器人启动的文件

- 启动
  
  1. 在有`bot.exe`的目录下进入终端，执行`bot start test_robot`如果您没有登录pc端微信，他将会弹出登录窗口，扫描即可，随后机器人将管控您的微信 (如果您已在pc端登陆，极有可能也会弹出扫码窗口，忽略即可)
  
  2. 验证机器人是否成功，在包含被机器人管控的群组中输入`/help`发送，将会收到机器人回复。注意：pc端登录的微信号是机器人，测试应该用另一个微信向机器人发送指令消息才会得到回复，如果未收到回复，请尝试退出微信以启动机器人后弹出的扫码界面扫码进入

- 关闭
  
  1. 在有`bot.exe`的目录下进入终端，执行`bot close`

- 个性化
  
  1. 可以自定义脚本命令，参考script/spider.py文件格式，同时记得同步修改配置文件（yaml）
  
  2. 可以自定义爬虫或者开放接口提供指令给机器人，参考script下的spider.py

## 添加开发者微信进入交流群

![](https://s1.328888.xyz/2022/10/11/gn24P.png)