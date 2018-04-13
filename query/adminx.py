from .models import Record, TestType, StubInfo,BoardInfo
import xadmin
from django.db import connection
from django.db.models import Count
from xadmin import views
from xadmin.layout import Main, TabHolder, Tab, Fieldset, Row, Col, AppendedText, Side

from xadmin.plugins.batch import BatchChangeAction


@xadmin.sites.register(views.BaseAdminView)
class BaseSetting(object):

    enable_themes = True

    use_bootswatch = True

class MainDashboard(object):

    widgets = [

        [

            {"type": "html", "title": "Test Widget",
             "content": "<h3> 欢迎来到广州万城万充新能源生产测试系统! </h3>"},
            {"type": "html", "title": "测试数据分析",
             "content": "<!DOCTYPE html>  \r\n<html>  \r\n<head>  \r\n<script src=\"static/js/jquery-3.2.1.min.js\"></script>\r\n<script src=\"//cdn.bootcss.com/Chart.js/2.1.6/Chart.bundle.js\"></script>\r\n</head>  \r\n<body>  \r\n<div style=\"width: 800px;\">\r\n    <canvas id=\"myChart2\" style=\"width:800px; height:800px;\"     ></canvas>\r\n</div>\r\n    <script type=\"text/javascript\">     //在body中插入  \r\nvar data1 = {\r\n            labels:[],\r\n            datasets: [\r\n            {\r\n            label: \"全部数据\",\r\n            fill: false,\r\n            lineTension: 0.1,\r\n            backgroundColor: \"rgba(75,192,192,0.4)\",\r\n            borderColor: \"rgba(75,192,192,1)\",\r\n            borderCapStyle: 'butt',\r\n            data:[]\r\n            },  {\r\n            label: \"安规\",\r\n            fill: false,\r\n            lineTension: 0.1,\r\n            backgroundColor: \"rgba(255,255,0,0.4)\",\r\n            borderColor: \"rgba(255,255,0,1)\",\r\n            borderCapStyle: 'butt',\r\n            data:[]\r\n            },  {\r\n            label: \"整机\",\r\n            fill: false,\r\n            lineTension: 0.1,\r\n            backgroundColor: \"rgba(255,106,106,0.4)\",\r\n            borderColor: \"rgba(255,106,106,1)\",\r\n            borderCapStyle: 'butt',\r\n            data:[]\r\n            },  {\r\n            label: \"板级\",\r\n            fill: false,\r\n            lineTension: 0.1,\r\n            backgroundColor: \"rgba(144,238,144,0.4)\",\r\n            borderColor: \"rgba(144,238,144,1)\",\r\n            borderCapStyle: 'butt',\r\n            data:[]\r\n            }\r\n            ]\r\n            };\r\n   //var labelArray = new Array();\r\n   //var dataArray = new Array();\r\n      $.get(\"http://120.78.222.124/query/data\",function(result){\r\n           //console.log(result)\r\n           //console.log(result['data']);\r\n          for(var key in result['data']['全部'])\r\n         {\r\n                //labelArray.push(key);\r\n              // dataArray .push(result['data'][key]);\r\n                data1.labels.push(key);\r\n                data1.datasets[0].data.push(result['data']['全部'][key]);\r\n                data1.datasets[1].data.push(result['data']['安规'][key]);\r\n                data1.datasets[2].data.push(result['data']['整机'][key]);\r\n                data1.datasets[3].data.push(result['data']['板级'][key]);\r\n         }\r\n        var ctx2 = document.getElementById(\"myChart2\").getContext(\"2d\");\r\n        var myBarChart = new Chart(ctx2, {\r\n                                            type: \"bar\",\r\n                                            data:data1,\r\n                                            // options: options\r\n                                    });   \r\n      });\r\n    </script>  \r\n</body>  \r\n</html>  \r\n"},
            {"type": "qbutton", "title": "Quick Start","btns": [{"title": "旧版本", "url": "http://120.78.222.124/admin/"}]},
        ],
    ]


xadmin.site.register(views.website.IndexView, MainDashboard)


class GlobelSetting(object):
    site_title = "广州万城万充新能源科技有限公司"
    site_footer = "广州万城万充新能源科技有限公司"
    #menu_style = 'accordion'
    global_models_icon = {
        Record:"fa fa-laptop",TestType:"fa fa-cloud"
    }


xadmin.site.register(views.CommAdminView, GlobelSetting)


#flot.js
class RecordAdmin(object):
    def resultshow(self, obj):
        return "%d%%"%(obj.result_integer)
    resultshow.short_description="合格率"

    def ftppathshow(self,obj):
        return """<a href="%s" target="_blank">下载测试报告</a>"""%obj.report_text

    ftppathshow.short_description = '测试报告'
    ftppathshow.allow_tags = True
    ftppathshow.is_column = True

    list_editable = (

        "approved_bool",

    )

    list_display = ['sn_text', 'test_type', 'resultshow', 'ftppathshow', 'pub_date', 'approved_bool']
    search_fields = ['sn_text', ]
    list_filter = ('sn_text', 'test_type', 'approved_bool', 'pub_date')
    list_export = ('xls', )

    actions = [BatchChangeAction, ]

    batch_fields = ('sn_text', 'test_type', 'approved_bool', 'pub_date')
    list_bookmarks = [{

        "title": "待审核",

        "query": {"factory_text": "广州锐速"},

        "order": ("-pub_date",),

        "cols": ("sn_text", "pub_date", "test_type"),

    }]
'''
    wizard_form_list = [

        ("First's Form", ("sn_text",)),

        ("Second Form", ("test_type", )),

        ("Thread Form", ("approved_bool",))

    ]
'''

class StubInfoAdmin(object):
    list_display = ['stub_text', 'pub_date']
    search_fields = ['stub_text', ]
    list_filter = ('stub_text', 'pub_date')
    list_export = ('xls', )

class BoardInfoAdmin(object):
    list_display = ['board_text', 'pub_date']
    search_fields = ['board_text', ]
    list_filter = ('board_text', 'pub_date')
    list_export = ('xls', )


xadmin.site.register(BoardInfo,BoardInfoAdmin)
xadmin.site.register(StubInfo,StubInfoAdmin)
xadmin.site.register(Record, RecordAdmin, )
xadmin.site.register(TestType)
