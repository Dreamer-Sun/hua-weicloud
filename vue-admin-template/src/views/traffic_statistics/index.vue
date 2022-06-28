<template>

  <!-- 2. 为ECharts准备一个具备大小（宽高）的Dom -->


  <div>
    <el-button type="primary" @click="queryTopN">请选择需查询终端TopN应用流量:</el-button>
    <el-cascader :options="topNlist" v-model="select_topN"clearable></el-cascader>

    <div id="main" style="width: 600px; height: 600px"> </div>
  </div>


</template>

<script>
// 1.导入echarts
import * as echarts from 'echarts';

export default {
  data() {
    return {
        select_topN : [],
        topN_child: [{
            value: 'app',
            label: 'app',
            children: [{
              value: 'day',
              label: 'day',
              children: [{
                value: 1,
                label: 1
              },
                {
                value: 2,
                label: 2
              },
                {
                value: 3,
                label: 3
              },
                {
                value: 4,
                label: 4
              },
                {
                value: 5,
                label: 5
              }]
            }, {
              value: 'week',
              label: 'week',
              children: [{
                value: 1,
                label: 1
              },
                {
                value: 2,
                label: 2
              },
                {
                value: 3,
                label: 3
              },
                {
                value: 4,
                label: 4
              },
                {
                value: 5,
                label: 5
              }]
            }, {
              value: 'month',
              label: 'month',
              children: [{
                value: 1,
                label: 1
              },
                {
                value: 2,
                label: 2
              },
                {
                value: 3,
                label: 3
              },
                {
                value: 4,
                label: 4
              },
                {
                value: 5,
                label: 5
              }]
            }]
          }, {
            value: 'apptype',
            label: 'apptype',
            children: [{
              value: 'day',
              label: 'day',
              children: [{
                value: 1,
                label: 1
              },
                {
                value: 2,
                label: 2
              },
                {
                value: 3,
                label: 3
              },
                {
                value: 4,
                label: 4
              },
                {
                value: 5,
                label: 5
              }]
            }, {
              value: 'week',
              label: 'week',
              children: [{
                value: 1,
                label: 1
              },
                {
                value: 2,
                label: 2
              },
                {
                value: 3,
                label: 3
              },
                {
                value: 4,
                label: 4
              },
                {
                value: 5,
                label: 5
              }]
            }, {
              value: 'month',
              label: 'month',
              children: [{
                value: 1,
                label: 1
              },
                {
                value: 2,
                label: 2
              },
                {
                value: 3,
                label: 3
              },
                {
                value: 4,
                label: 4
              },
                {
                value: 5,
                label: 5
              }]
            }]
          }],
        topNlist: [{
          value: 'zhinan',
          label: '指南',
          children: this.topN_child
        }, {
          value: 'zujian',
          label: '组件',
          children: [{
            value: 'basic',
            label: 'Basic',
            children: [{
              value: 'layout',
              label: 'Layout 布局'
            }, {
              value: 'color',
              label: 'Color 色彩'
            }, {
              value: 'typography',
              label: 'Typography 字体'
            }, {
              value: 'icon',
              label: 'Icon 图标'
            }, {
              value: 'button',
              label: 'Button 按钮'
            }]
          }, {
            value: 'form',
            label: 'Form',
            children: [{
              value: 'radio',
              label: 'Radio 单选框'
            }, {
              value: 'checkbox',
              label: 'Checkbox 多选框'
            }, {
              value: 'input',
              label: 'Input 输入框'
            }, {
              value: 'input-number',
              label: 'InputNumber 计数器'
            }, {
              value: 'select',
              label: 'Select 选择器'
            }, {
              value: 'cascader',
              label: 'Cascader 级联选择器'
            }, {
              value: 'switch',
              label: 'Switch 开关'
            }, {
              value: 'slider',
              label: 'Slider 滑块'
            }, {
              value: 'time-picker',
              label: 'TimePicker 时间选择器'
            }, {
              value: 'date-picker',
              label: 'DatePicker 日期选择器'
            }, {
              value: 'datetime-picker',
              label: 'DateTimePicker 日期时间选择器'
            }, {
              value: 'upload',
              label: 'Upload 上传'
            }, {
              value: 'rate',
              label: 'Rate 评分'
            }, {
              value: 'form',
              label: 'Form 表单'
            }]
          }, {
            value: 'data',
            label: 'Data',
            children: [{
              value: 'table',
              label: 'Table 表格'
            }, {
              value: 'tag',
              label: 'Tag 标签'
            }, {
              value: 'progress',
              label: 'Progress 进度条'
            }, {
              value: 'tree',
              label: 'Tree 树形控件'
            }, {
              value: 'pagination',
              label: 'Pagination 分页'
            }, {
              value: 'badge',
              label: 'Badge 标记'
            }]
          }, {
            value: 'notice',
            label: 'Notice',
            children: [{
              value: 'alert',
              label: 'Alert 警告'
            }, {
              value: 'loading',
              label: 'Loading 加载'
            }, {
              value: 'message',
              label: 'Message 消息提示'
            }, {
              value: 'message-box',
              label: 'MessageBox 弹框'
            }, {
              value: 'notification',
              label: 'Notification 通知'
            }]
          }, {
            value: 'navigation',
            label: 'Navigation',
            children: [{
              value: 'menu',
              label: 'NavMenu 导航菜单'
            }, {
              value: 'tabs',
              label: 'Tabs 标签页'
            }, {
              value: 'breadcrumb',
              label: 'Breadcrumb 面包屑'
            }, {
              value: 'dropdown',
              label: 'Dropdown 下拉菜单'
            }, {
              value: 'steps',
              label: 'Steps 步骤条'
            }]
          }, {
            value: 'others',
            label: 'Others',
            children: [{
              value: 'dialog',
              label: 'Dialog 对话框'
            }, {
              value: 'tooltip',
              label: 'Tooltip 文字提示'
            }, {
              value: 'popover',
              label: 'Popover 弹出框'
            }, {
              value: 'card',
              label: 'Card 卡片'
            }, {
              value: 'carousel',
              label: 'Carousel 走马灯'
            }, {
              value: 'collapse',
              label: 'Collapse 折叠面板'
            }]
          }]
        }, {
          value: 'ziyuan',
          label: '资源',
          children: [{
            value: 'axure',
            label: 'Axure Components'
          }, {
            value: 'sketch',
            label: 'Sketch Templates'
          }, {
            value: 'jiaohu',
            label: '组件交互文档'
          }]
        }]
    }
  },
  created() {},
  //  此时，页面上的元素，已经被渲染完毕了
  //   DOM元素初始化完毕后，执行mounted
  mounted() {
      var chartDom = document.getElementById('main');
      var myChart = echarts.init(chartDom);
      var option;

      option = {
        tooltip: {
          trigger: 'item'
        },
        legend: {
          top: '5%',
          left: 'center'
        },
        series: [
          {
            name: '终端TopN应用流量',
            type: 'pie',
            radius: ['40%', '70%'],
            avoidLabelOverlap: false,
            itemStyle: {
              borderRadius: 10,
              borderColor: '#fff',
              borderWidth: 2
            },
            label: {
              show: false,
              position: 'center'
            },
            emphasis: {
              label: {
                show: true,
                fontSize: '40',
                fontWeight: 'bold'
              }
            },
            labelLine: {
              show: true
            },
            data: [
              { value: 100, name: 'Tiktok' },
              { value: 300, name: 'WeiXin' },
              { value: 580, name: 'QQ' },
              { value: 484, name: '王者荣耀' },
              { value: 300, name: '绝地求生' }
            ]
          }
        ]
      };

      option && myChart.setOption(option);
  },
  methods: {
    queryTopN(){
      console.log("here is query topN", this.select_topN)
    }
  },
}
</script>

<style lang="less" scoped>
</style>
