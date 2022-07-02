<template>

  <!-- 1  -->
  <div id="main" style="background-color: #081832;width: 1850px;height: 1100px;margin-top: 0px">
    <br/>
    <el-container id="container1"
                  style="box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);border-radius: 4px;border: #00F7DE 1px solid;margin-right:50%;margin-top: 10px;margin-left: 10px;margin-bottom: 10px">
      <div id="myChart" :style="{width: '990px', height: '500px'}"
           style="background-color:#081832;height: 400px;margin-top: 20px;margin-left: 10px;">
      </div>
      <el-container style="margin-top: 50px">
        <div id="LinerChart1" :style="{width: '800px', height: '430px'}"
             style="background-color: #081832;width:700px;height: 400px;margin-right: 20px;margin-top: -15px;">
        </div>
      </el-container>
    </el-container>
    <!-- 2 -->
    <div style="border:#00F7DE 1px solid; border-radius: 4px;margin-top: -530px;;margin-left: 940px;margin-right: 10px">
      <el-container id="container2" style="margin-right:15%;margin-bottom: -10px">
        <div id="piechart1" :style="{width: '900px', height: '510px'}"
             style="margin-left: 0px;height: 400px;border-radius: 4px;"></div>
      </el-container>
      <el-container id="container3" style="margin-top:20px">
        <div
             >
            <el-select class="select_btn" v-model="value" style="width: 240px" :popper-append-to-body="false" placeholder="请选择站点ID" filterable>
              <el-option
                v-for="item in options"
                :key="item.value"
                :label="item.label"
                :value="item.value">
              </el-option>
            </el-select>
          <el-select  class="select_btn2" v-model="value2" style="width: 130px" :popper-append-to-body="false" placeholder="请选择设备类型" filterable>
              <el-option
                v-for="item in options2"
                :key="item.value"
                :label="item.label"
                :value="item.value">
              </el-option>
            </el-select>

        </div>
        <div >
          <el-button class="select_button" type="primary"  @click="updateChart">点击刷新图表</el-button>
        </div>
      </el-container>
    </div>
    <!--3-->
    <div style="">
      <el-container id="container4">
        <div id="BarChart1" :style="{width: '915px', height: '500px'}"
             style="margin-right:10px;margin-left:10px;margin-top:20px;border:1px solid #00F7DE ;height: 400px;border-radius: 4px;"></div>
      </el-container>
    </div>

    <!--4-->
    <div
      style="border:#00F7DE 1px solid; border-radius: 4px;width: 900px; height:500px;margin-left: 940px;margin-top: -500px">
      <el-container id="container5">
        <div id="AgeRange" :style="{width: '500px', height: '500px'}"
             style="margin-left:1px;margin-top:10px;margin-right:-21px;height: 400px;"></div>
      </el-container>
      <!--5-->
      <el-container id="container6">
        <div id="SexRange" :style="{width: '400px', height: '490px'}"
             style="background-color:#081832;margin-right:-21px;margin-left:500px;margin-top:-500px;height: 400px;"></div>
      </el-container>
    </div>
  </div>

</template>

<style scopted>
</style>

<script>
import * as echarts from 'echarts';
import {equipmentAlarm,equipmentAlarm2, getSiteId} from "@/api/EquipmentAlarm";

export default {
  name: 'Analyse',
  data() {
    return {
      src: '',
      now_device:[],
      picture_1_data:[],
      picture_2_data:[],
      picture_3_date:[],
      picture_3_data:[],
      picture_4_data_1:[],
      picture_4_data_2:[],
      SiteId: [],
      SiteIdNum:'',
      equipment:[],
      options2:[{
          value: 'AP',
          label: 'AP'
        },
        {
          value: 'LSW',
          label: 'LSW'
        },{
          value: 'FW',
          label: 'FW'
        },{
          value: 'AR',
          label: 'AR'
        },{
          value: 'WAC',
          label: 'WAC'
        },{
          value: 'ALL',
          label: 'ALL'
        }],
      value2:'',
      // options为选中的站点 value为对应的值
      options: [],
        value: ''
    }
  },
  mounted() {
    this.getIDs();
    this.drawLine();
    this.drawLiner();
    this.PieChart1();
    this.BarChart1();
    this.AgeRange();
    this.SexRange();
    this.dataFix();
  },
  methods: {
    updateChart(){
      console.log("here updateChart")
      console.log(this.value)
      console.log(this.value2)
      var formData = new FormData;
      formData.append("siteId", this.value)
      formData.append("deviceCategory", this.value2)
      equipmentAlarm2(formData).then((res)=>{
        this.now_device = res.now_device;
        let previewChart = echarts.init(document.getElementById('piechart1'))
          previewChart.setOption({
             series: [{
                data: [
                    {value: this.now_device[0], name: '设备总数'},
                    {value: this.now_device[1], name: '正常设备总数'},
                    {value: this.now_device[2], name: '提示设备总数'},
                    {value: this.now_device[3], name: '故障设备总数'},
                    {value: this.now_device[4], name: '离线设备总数'},
                    {value: this.now_device[5], name: '未注册设备总数'},
                    {value: this.now_device[6], name: '紧急告警总数'},
                    {value: this.now_device[7], name: '严重告警总数'},
                    {value: this.now_device[8], name: '一般告警总数'},
                    {value: this.now_device[9], name: '提示告警总数'}]
             }]
          });
      })
    },
    getIDs(){
      getSiteId().then((res)=>{
          console.log("getSiteId");
          console.log(res.data);
          console.log(res.totalRecords);
          let tmp = {}
          for(let i =0;i<res.data.length;i++){
            tmp["value"] = res.data[i];
            tmp["label"] = res.data[i];
            this.options.push(tmp)
            tmp = {}
          }
          this.SiteId = res.data;
          console.log(this.SiteId)
          this.SiteIdNum = res.totalRecords;
      })
    },
    dataFix(){


      var formData = new FormData;
      formData.append("siteId", "")
      formData.append("deviceCategory", "")
      equipmentAlarm(formData).then((res)=>{
          console.log("---equipmentAlarm---");
          console.log("res.data", res.data);
          this.equipment = res.data;
          console.log("this.equipment", res.data);
          this.picture_1_data = res.picture_1_data;
          console.log(this.picture_1_data);
          //再次实例化图表左上角第一个图
          let previewChart = echarts.init(document.getElementById('myChart'))
          previewChart.setOption({
             series: [{
                data: this.picture_1_data
             }]
          });
          //再次实例化图表左上角第二个图
          this.picture_2_data = res.picture_2_data;
          let previewChart2 = echarts.init(document.getElementById('LinerChart1'))
          previewChart2.setOption({
             series: [{
                data: this.picture_2_data
             }]
          });

          this.picture_3_date = res.picture_3_date;
          this.picture_3_data = res.picture_3_data;
          //再次实例化图表左下角第一个图
          let previewChart3 = echarts.init(document.getElementById('BarChart1'))
            previewChart3.setOption({
               series: [{
                  data: this.picture_3_data
               }],
              yAxis:{
                 data:this.picture_3_date
              }
            });

          this.picture_4_data_1 = res.picture_4_data_1;
          this.picture_4_data_2 = res.picture_4_data_2;
          //再次实例化图表右下角第一个图
          let previewChart4 = echarts.init(document.getElementById('AgeRange'))
            previewChart4.setOption({
               series: [{
                  data: [
                      {value:this.picture_4_data_1[0], name:'正常设备'},
                      {value: this.picture_4_data_1[1], name: '提示设备'},
                      {value: this.picture_4_data_1[2], name: '故障设备'},
                      {value: this.picture_4_data_1[3], name: '离线设备'},
                      {value: this.picture_4_data_1[4], name: '未注册设备'}]
               }]
            });
          //再次实例化图表右下角第二个图
          let previewChart5 = echarts.init(document.getElementById('SexRange'))
            previewChart5.setOption({
               series: [{
                  data: [
                      {value: this.picture_4_data_2[0], name: '紧急告警'},
                      {value: this.picture_4_data_2[1], name: '严重告警'},
                      {value: this.picture_4_data_2[2], name: '一般告警'},
                      {value: this.picture_4_data_2[3], name: '提示告警'}]
               }]
            });
      })

    },
    drawLine() {
      /**********左上第一个表格**************/
        // 基于准备好的dom，初始化echarts实例
      let myChart = echarts.init(document.getElementById('myChart'))
      // 绘制图表
      myChart.setOption({
        title: {
          text: '所有站点设备总数统计',
          textStyle: {   //标题颜色
            color: '#ffffff'
          },
        },
        tooltip: {},
        xAxis: [{
          //横坐标值
          data: ["正常设备总数", "提示设备总数", "故障设备总数", "离线设备总数", "未注册设备总数", "紧急告警设备总数", "严重告警总数", "一般告警总数", "提示告警总数"],
          axisLabel: {
            //下面的函数让x轴文字纵向显示
            formatter: function (value) {
              return value.split("").join("\n");
            },
            show: true,
            textStyle: {
              color: '#ffffff'
            },
          }
        },
          //控制y轴均分，白色分割线
          {
            type: 'value',
            scale: 'true',
            max: '200',
            min: '0',
            splitNumber: 5,
            boundaryGap: [0.2, 0.2]

          }
        ],
        //管理Y轴坐标格式。
        yAxis: {
          //不管是横坐标还是纵坐标，我们要是想调整坐标轴的label的文字颜色，就要设置axisLabel参数
          axisLabel: {
            show: true,
            textStyle: {
              color: '#ffffff'
            }
          }
        },
        //  legend用于控制说明图表标注部分的参数。
        //  修改左边的legend。增加itemWidth  设置宽度，itemHeight设置高度，itemGap设置间距，可以根据需要设置图形的大小以及间距。
        legend: {
          itemWidth: 30,
          itemGap: 40, itemHeight: 30,

        },
        //grid参数用于控制坐标整体位置，上下左右的方向调整。
        grid: [
          {
            top: '15%',  // 组件离容器上侧的距离,百分比字符串或整型数字
            left: '5%',    // 组件离容器左侧的距离,百分比字符串或整型数字
            right: '25%',
            bottom: '3%',
            containLabel: true //grid 区域是否包含坐标轴的刻度标签，
          }
        ],
        series: [
          {
            barWidth: '30',
            type: 'bar',
            //设置柱状图的柱形宽度
            barGap: '10%',
            data: [100, 250, 140, 110, 210, 250, 140, 200, 100],
            itemStyle: {
              normal: {
                color: function (params) {
                  var colorList = ['#5ac1df', '#fbf64e', '#fdc55b', '#c7b5fb', '#f8f5e9'];
                  return colorList[params.dataIndex % colorList.length];//想到取余可以快捷的实现对已有的颜色循环
                }
              }
            }
          }
        ],
      });
    },

    /**********左上第二个表格**************/
    drawLiner() {
      let LinerChart1 = echarts.init(document.getElementById('LinerChart1'));
      LinerChart1.setOption({
        title: {
          text: '严重告警设备趋势图', textStyle: {   //标题颜色
            color: '#ffffff', left: 'center'
          },
        },
        xAxis: {
          type: 'category',
          boundaryGap: false,
          data: ['2022-3', '2022-5', '2022-7', '2022-9', '2022-10', '2022-11', '2022-12'],
          axisLabel: {
            //下面的函数让x轴文字纵向显示
            show: true,
            textStyle: {
              color: '#ffffff'
            },
          }
        },
        yAxis: {
          type: 'value',     //不管是横坐标还是纵坐标，我们要是想调整坐标轴的label的文字颜色，就要设置axisLabel参数
          axisLabel: {
            show: true,
            textStyle: {
              color: '#ffffff'
            }
          }
        },
        series: [{
          //纵坐标值。
          data: [220, 120, 220, 330, 300, 290, 190],
          type: 'line',
          //填充颜色设置
          areaStyle: {
            color: {
              type: 'linear',
              x: 0,
              y: 0,
              x2: 0,
              y2: 1,
              colorStops: [{
                offset: 0, color: 'red' // 0% 处的颜色
              }, {
                offset: 1, color: 'yellow' // 100% 处的颜色
              }],
              global: false // 缺省为 false
            }
          }
        }],
        grid: [
          {
            top: '25%',  // 组件离容器上侧的距离,百分比字符串或整型数字
            left: '5%',    // 组件离容器左侧的距离,百分比字符串或整型数字
            right: '25%',
            bottom: '3%',
            containLabel: true //grid 区域是否包含坐标轴的刻度标签，
          }
        ]
      })
    },

    /***************右上第一个图********************/
    PieChart1() {
      let piechart1 = echarts.init((document.getElementById('piechart1')));
      piechart1.setOption({
        title: {
          text: '该站点下的告警设备分布',
          left: 'center', textStyle: {   //标题颜色
            color: '#ffffff'
          }
        },
        tooltip: {
          trigger: 'item'
        },
        legend: {
          orient: 'vertical',
          left: 'left',
          textStyle: { //图例文字的样式，在饼状图的左上角
            color: '#fdff85',
            fontSize: 16
          },
        },
        series: [
          {

            radius: '75%',//饼图的半径大小
            center: ['60%', '60%'],//饼图的位置
            name: '访问来源',
            type: 'pie',
            data: [
              {value: 1048, name: '设备总数'},
              {value: 1529, name: '正常设备总数'},
              {value: 365, name: '提示设备总数'},
              {value: 484, name: '故障设备总数'},
              {value: 254, name: '离线设备总数'},
              {value: 193, name: '未注册设备总数'},
              {value: 523, name: '紧急告警总数'},
              {value: 745, name: '严重告警总数'},
              {value: 610, name: '一般告警总数'},
              {value: 351, name: '提示告警总数'}
            ],
            emphasis: {
              itemStyle: {
                shadowBlur: 10,
                shadowOffsetX: 0,
                shadowColor: 'rgba(0, 0, 0, 0.5)'
              }
            }
          }
        ]
      })
    },

    /*左下图；直线统计图*/
    BarChart1() {
      let barchart1 = echarts.init(document.getElementById('BarChart1'));
      barchart1.setOption({
        title: {
          text: '近一周设备告警数量分布统计',
          textStyle: {   //标题颜色
            color: '#ffffff'
          }
        },
        tooltip: {
          trigger: 'axis',
          axisPointer: {
            type: 'shadow'
          }
        },

        legend: {
          data: ['告警次数'], textStyle: { //图例文字的样式
            color: '#fff',
            fontSize: 16
          },

        },
        grid: {
          left: '3%',
          right: '4%',
          bottom: '3%',
          containLabel: true
        },
        xAxis: {
          type: 'value',
          boundaryGap: [0, 0.01], axisLabel: {
            //下面的函数让x轴文字纵向显示
            show: true,
            textStyle: {
              color: '#ffffff'
            },
          }
        },
        yAxis: {
          type: 'category',
          data: ['周一', '周二', '周三', '周四', '周五', '周六', '周天'],
          axisLabel: {
            //下面的函数让x轴文字纵向显示
            show: true,
            textStyle: {
              color: '#ffffff'
            },

          }
        },
        series: [
          {
            name: '告警次数',
            type: 'bar',
            data: [160, 110, 12, 42, 50, 20, 70, 96, 113],
            label: {
              textStyle: {
                color: '#fff'
              }
            }
          },
        ]
      })
    },
    /*右下角第一个图：年龄分布图*/
    AgeRange() {
      let agerange = echarts.init(document.getElementById('AgeRange'));
      agerange.setOption({
        title: {
          text: '设备状态分布',
          subtext: '',
          left: 'center', textStyle: {   //标题颜色
            color: '#ffffff'
          }
        },
        tooltip: {
          trigger: 'item',
          formatter: '{a} <br/>{b} : {c} ({d}%)'
        },
        toolbox: {
          show: true,
          feature: {
            mark: {show: true},
            dataView: {show: true, readOnly: false},
            restore: {show: true},
            saveAsImage: {show: true}
          }
        },
        series: [
          {
            tooltip: {
              trigger: 'item'
            },
            legend: {
              top: '5%',
              left: 'center'
            },
            name: '设备状态分布',
            type: 'pie',
            radius: '60%',//饼图的半径大小
            center: ['50%', '50%'],
            roseType: 'area',
            //图例label样式
            label: {
              normal: {
                textStyle: {
                  color: '#fff',
                  fontSize: 20
                }
              }
            }, emphasis: {
              label: {
                show: true,
                fontSize: '20',
                fontWeight: 'bold'
              }
            },
            labelLine: {
              show: false
            },
            itemStyle: {
              borderRadius: 5
            },
            data: [
              {value: 30, name: '正常设备'},
              {value: 28, name: '提示设备'},
              {value: 26, name: '故障设备'},
              {value: 24, name: '离线设备'},
              {value: 22, name: '未注册设备'},
            ]
          }
        ]

      });
    },
    /*右下角第二个图：性别比例分布图*/
    SexRange() {
      let sexRange = echarts.init(document.getElementById('SexRange'));
      sexRange.setOption({
        title: {
          text: '告警状态分布',
          left: 'center', textStyle: {   //标题颜色
            color: '#ffffff'
          }
        },
        tooltip: {
          trigger: 'item'
        },
        legend: {
          orient: 'vertical',
          left: 'left',
          textStyle: {
            color: '#fdff85'
          }

        },
        series: [
          {
            name: '告警状态分布',
            type: 'pie',
            radius: '58%',
            data: [
              {value: 484, name: '紧急告警'},
              {value: 300, name: '严重告警'},
              {value: 220, name: '一般告警'},
              {value: 360, name: '提示告警'}
            ], label: {
              normal: {
                textStyle: {
                  color: '#fff',
                  fontSize: 13
                },
                show: true,
                formatter: '{d}%' //自定义显示格式(b:name, c:value, d:百分比)
              },

            }
            ,

            emphasis: {
              itemStyle: {
                shadowBlur: 10,
                shadowOffsetX: 0,
                shadowColor: 'rgba(0, 0, 0, 0.5)'
              }
            }
          }
        ]
      });
    }
  }
}
</script>
<style scoped>
.container3 {
  margin-right: 10px;
}

.title1 {
  background-color: #ffff43;
  border-radius: 5px;
  font-family: 幼圆;
  width: 120px;
  height: 20px;
}

.select_btn {
  position: absolute;
  top: 60px;
  right: 60px;
  background: rgb(21, 47, 72);
}
.select_btn2 {
  position: absolute;
  top: 120px;
  right: 60px;
  background: rgb(21, 47, 72);
}
.select_button{
  position: absolute;
  top: 180px;
  right: 60px;
  color: #fff;
  background-color: rgb(21, 47, 72);
  border-color: rgb(21, 47, 72);
}

.select_button:hover,
.select_button:focus {
  background: rgb(65, 102, 141);
}
  /*下拉框*/
  .el-select-dropdown {
    border: none;
    background-color: rgba(139, 155, 186, 0.8);
  }

  /*输入框*/
  .el-input__inner {
    color: #6c2a2a;
    border-color: #00fff6;
    background-color: rgba(1, 28, 82, 0.8);
  }

  /*聚焦时的样式*/
  .el-select .el-input.is-focus .el-input__inner {
    border-color: #0B61AA;
    background-color: rgba(1, 28, 82, 0.8);
    color: #00D3E9;
  }

  /*下拉框选中*/
  .el-select-dropdown__item {
    color: #1c32c9;
  }

  /*鼠标经过下拉框*/

  .el-select-dropdown__item:hover {
    color: #00D3E9;
    background-color: #0F3360;
  }




</style>


