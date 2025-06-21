# 开始前准备

## 开发环境

1. Node.js，以及Node.js自带的npm包管理器
2. Vite，通过npm安装
3. 趁手的代码编辑器（指VSCode）+ Volar插件
4. chrome浏览器插件vue-devtools（可从github下载源码安装或从chrome网上应用店安装）

## 可用的参考资料

1. vue.js中文文档 https://cn.vuejs.org/guide/introduction.html
2. vuetify中文文档 https://vuetifyjs.com/zh-Hans/introduction/why-vuetify/
3. pinia中文文档https://pinia.web3doc.top/

## 在克隆后启动项目

在项目的工作目录下使用以下命令：

### Project setup（安装依赖的包）

```
# yarn
yarn

# npm
npm install

# pnpm
pnpm install
```

### Compiles and hot-reloads for development（启动本地调试服务器）

```
# yarn
yarn dev

# npm
npm run dev

# pnpm
pnpm dev
```

### Compiles and minifies for production（构建项目）

```
# yarn
yarn build

# npm
npm run build

# pnpm
pnpm build
```

### Lints and fixes files

```
# yarn
yarn lint

# npm
npm run lint

# pnpm
pnpm lint
```

# 约定与说明

1. 这次项目使用的语言是typescript，与javascript相比，它有严格的静态类型检查机制，所以在编写代码的时候可能需要做出一些类型声明。
2. 项目文件夹约定：

```
DetailsH5
├──node_modules			//存放公共的包
├──public
├──src					//存放项目文件
	├──components		//存放子组件
	├──router 			//存放路由
	├──store			//存放储存的数据
	├──styles			//存放css文件
	├──type				//存放定义的类型
	├──utils			//存放一些工具
	├──views			//存放页面
```

3. 关于"component"（组件）的说明

   - 项目中的每一个“.vue”文件都可以视为是一个组件（views中的那些“页面”其实也是组件），而每一个组件都可以被用作独立的网页。

   - 一个网页通常是通过多个组件的套娃实现的
   - 每个组件（.vue文件）由三个部分组成：\<script\>（typescript）负责业务逻辑；\<template\>（HTML）负责组件的页面布局；\<style\>（CSS）对应组件的页面样式

4. 关于”router“（路由）的说明

   - 项目通过vue-router来管理路由

   - 可以认为“路由”完成的是页面与网址的对应。比如将“\schedule”这个网址指定给组件"ScheduleTable.vue"
   - 路由在router/index.ts中定义
   - 因为还没有设置重定向，所以需要访问http://localhost:3000/schedule才能看见应用的页面

5. 关于“store”（储存）的说明

   - 项目通过pinia来储存数据
   - pinia实现了在不同组件之间传递、储存数据

6. 关于axios与网络请求与异步的说明

   - 项目通过axios来实现网络请求，即通过web应用向details后端请求数据

   - 在utils中声明了axios的示例，有关如何发送网络请求可以参考store/ScheduleStore.ts的代码

   - typescript可以进行异步请求（通过创建一个异步函数来实现）

   - ```javascript
     const applyUpdate = async() => {
         try {
             loading = true
             const response = await axiosInstance.get("/schedule", { params: {id:ID} });
             console.log(response.data);
         }
         catch (error) {
             console.log(error);
         }
         loading = false
     }
     //以下是我对异步函数的理解：
     //这是异步函数的其中一种写法，关键字为async/await
     //在执行到await所在语句后，这个函数的执行会卡在await直至网络请求完成，但函数外的代码会继续执行。
     //利用这一性质，可以在执行网络请求时作出一些反馈,比如在loading = true时显示一个旋转的环形进度条
     ```

# 分工与计划

关于开发过程有几个建议：

1. 尽量使用Vuetify已经提供的组件；
2. 在实现每个功能之后写一个文档记录一下代码的大致结构、手搓了哪些子组件、数据是如何储存的等等，**强调一下定义了哪些有复用价值的模块**,这个文档放在src/documents中；
3. 已经实现的模块、搓好的子组件尽量复用；
4. 多看看其他人写的代码，~~**很可能有很多部分是可以直接拷出来用的**~~；
5. 善用ChatGPT、github Copilot等工具，可以省很多事。
6. 解决不了的问题丢到群里，大家一起~~坐牢~~思考

下面是需要完成的功能：

|  页面  |       子页面       |                    备注                     | 负责人 |          状态          |
| :----: | :----------------: | :-----------------------------------------: | :----: | :--------------------: |
| 日程表 |       时间线       |           按时间顺序展示本人日程            | Retro  | 时间线的基本功能已实现 |
|        |      日程总览      |          日程的分类筛选、周视图等           | Retro  |          ToDo          |
|        |      日程详情      |                                             | Retro  |          ToDo          |
|        |   日程创建、删除   |                                             | Retro  |          ToDo          |
|        |    从课程表导入    |            真的有空实现这个吗😅😅😅            |        |                        |
|        | 日程附件加入日程表 |                                             |        |                        |
|  通知  |      通知总览      |            通知的分类查看、筛选             |        |                        |
|        |      通知详情      |                                             |        |                        |
|        |   通知创建、删除   |                                             |        |                        |
|        |      通知推送      |       可以先实现已读\未读通知这一功能       |        |                        |
|  组织  |     加入的组织     |           展示本人加入了哪些组织            |        |                        |
|        |      组织详情      |                                             |        |                        |
|        |      组织修改      | 增加\删除组织，加入、退出组织等等麻烦的操作 |        |                        |
|  用户  |         /          |                 登录什么的                  |        |                        |
|  设置  |         /          |             目前看来没啥用.....             |        |                        |

**时间紧迫，任务艰巨，诸君頑張って！**

# 吐槽

- typescript和javascript的语法总感觉有些诡异，特别是那个“=>"的用法以及隐式声明函数需要时间来适应。——Retro

