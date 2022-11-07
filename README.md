# pythonProject
五天编程

用户体验设计考虑的因素：
1.实用性（Useful）本软件能够为用户带来良好的使用体验，用户使用该软件不需要通过繁琐的步骤，注册登录即可享受核心功能
2.适用性（Usable）本软件使用起来十分的便捷，并且由于专注于一种功能，对于用户来说可以强烈满足单一期望
3.可寻性（Findable）由于本软件只提供一种功能，所以对于有这方面需要的用户来说可以轻易寻找到自己需要的方面
4.可靠性（Credible）本产品并不会索取用户的信息并且指挥提供建议，主动权掌握在用户手上
5.理想性（Desirable）本产品由于不通过具体的模型，所以用户比较容易受到心里状况的影响，可以激起购买欲望
6.无障碍性（Accessible）本产品属于只需要简单操作即可获得结果的软件，所以对于用户来说除非极严重的残疾，其余的不会有太大影响
7.有价值性（Valuable）本产品可以获取用户的打赏或者使用会员等级制度，当然前期属于免费


产品所用编程语言及IDE、平台、框架等：
编程语言：python
IDE：Pycharm 
平台：Windows10 专业版，github
框架：Django
版本号：数据库版本号（Mysql 8.0.15），python3.10，Django4.1.3


代码仓库链接及代码提交历史截图:
代码仓库链接：https://github.com/yyb12/pythonProject
代码提交历史截图：
 

安装、设计、开发中遇到的主要问题及解决方法汇总:
1.安装pip：如果cmd没有识别到pip需要到官网下载，并且配置系统变量
2.安装Django：这里推荐使用cmd下载，前提是需要安装pip，安装完成pip后去cmd下载Django，再到新建的项目中运行命令建立Django框架
3.建立远程仓库：这里运用的是git-bash与github结合建立远程仓库，用git-bash生产密钥，用github建立远程仓库，再用git-bash建立本地仓库，用git-bash链接github即可（记得要在pycharm中连接git与github）

软件概要设计：
•	 人工智能类模型设计方法  CNN卷积神经网络
•	数据库设计  E-R图
•	接口设计
    UI界面调用神经网络算法：getCNN(用户选择参数)，返回图片结果
    UI界面调用数据库：put_account（用户账号，密码）无返回结果
                      put_special(用户选择过的参数) 无返回结果
•	前端设计 Django框架
