# 时间线模块概述
这个模块主要基于vuetify的Timeline控件开发
## 数据类型定义
- 在type中定义了一个ScheduleItem，这个类型可以通用与所有的日程、任务
- 在store中定义了SchdeuleStore，这个储存的主体是一个日程的列表，之外还有几个辅助量来标记储存加载的状态
- 在这个store中也定义了一个异步函数，用于从服务器获取日程的数据。
## 滚动事件处理
- 实际上滚动的并不是Timeline，而是包裹Timeline的Window（注：这里需要特别注意到底是什么东西在滚动，如果可以的话，最好把自己写的内容用一个v-container包起来，然后只滚动这个container）
- 为Window注册了一个@scroll事件处理器，之后可以用事件处理函数来处理拖动到最底下的事件。
- 在检测到滚动到最下方时从服务器获取数据,在获取数据的过程中显示timeline下方的转圈圈加载图标,在获取完之后直接将新数据插入store中,vue的响应式系统就会自动向Timeline渲染新加入的日程.如此可以实现"拖动到最底后加载"的效果.
- 这个效果后来被放弃了，因为最终决定一次性在时间线内加载完所有的日程
- 通过监听滚动事件，将窗口滚动的距离记录下来，并且在窗口的updated钩子内将窗口滚动到原来的位置，可以实现切换页面之后窗口滚动的位置不变。
```
script:
const handleScroll = (e: Event) => {
	//检测滚动到最底部
	if ((e.target as Element).scrollTop + (e.target as Element).clientHeight >= (e.target as Element).scrollHeight - 20) {
		console.log('到底了');
		if(!ScheduleStore.noMore)
			ScheduleStore.setUpdate();
			ScheduleStore.applyUpdate();
	}
}
template:
<v-window class="ScheduleWindow" v-model="tab" @scroll="handleScroll">
		<v-window-item value="TimeLine">
			<timeline />
		</v-window-item>

		<v-window-item value="Summary">
			Summary
		</v-window-item>
</v-window>

```