
# WeLink-SDK-Python

软件开发工具包（SDK）包括代码和示例，用户可以按照示例代码调用封装好的模块请求[WeLink开放平台的服务端API](https://open-doc.welink.huaweicloud.com/docs/serverapi/readme/serverapi_index.html?type=internal)

# 开发

当开发一个新的接口时，步骤如下：  
1. 实现一个接口class，继承RestApi  
2. 在__init__定义好接口需要的参数名, 一般一个请求会涉及method，path，header，body_params,query_params。
   - 参数名: 使用python的下划线风格, 不带下划线的都默认为接口的参数名，如果需要自定义一些参数，请在变量名前使用下划线: _your_param
   - method: 如实填写get_rest_method的方法
   - path: 如实填写get_valid_path的方法, 返回的是一个元组 
   - header: RestApi有默认方法，一般可以不用管
   - body_params: RestApi有默认方法（get_body_params），作用是将所有下划线风格的参数转为驼峰风格，然后加入到请求中，如果body参数中有子object，需要把驼峰风格的实际子参数放到self._body_object_params中，RestApi会自动判断object子参数是否已实例化，没有就会删除body中此参数，有就会调用参数的get_data方法(可以参考KnowledgeV2ArticlesAddRequest)。如果请求没有没有body参数，请override get_body_params，并返回None。在WeLink中，一般而言GET和DELETE请求都没有body_params。
   - query_params: RestApi有默认方法(get_params)，作用是取类中self.__params，如果需要override，可以使用return super().get_body_params(), 对于GET的请求，get_params和get_body_params是必须override的
3. 默认参数在get_body_params中生成，也可以自定义get_params和get_body_params的方法,其他的什么参数是否非必填之类的就不管了
4. 然后在welink/api目录的`__init.py` import一下类
5. 可以参考`ContactV1UserSimplelistRequest`和`WelinkIMV1ImServiceChatGroupChatRequest`和`MessagesV1CardWecodeRequest`和`WeopenFormScopeRequest`
