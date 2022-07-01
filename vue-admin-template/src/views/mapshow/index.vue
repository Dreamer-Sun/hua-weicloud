<template>
  <div>
    <div class="map-data">
      <div id="piecharts"></div>
      <div id="main"></div>
      <div id="histogram"></div>
      <div id="lineChartSeven">
      </div>
      <div id="div2"></div>
      <div id="div3"></div>
    </div>
  </div>
</template>
<el-dialog
  title="提示"
  :visible.sync="dialogVisible"
  width="30%"
  :before-close="handleClose">
<span>这是一段信息</span>
<span slot="footer" class="dialog-footer">
    <el-button @click="dialogVisible = false">取 消</el-button>
    <el-button type="primary" @click="dialogVisible = false">确 定</el-button>
  </span>
</el-dialog>


<script>
import echarts from 'echarts'
import geoJson from '../../template/data.json'
import {getList} from "@/api/table";
import {getsitemap, getsitetypedata, queryresultbyquerysitesdata} from "@/api/getSiteData";
import {mount} from "@vue/test-utils";

export default {
  data() {
    return {
      name: "index",
      list: '',
      resdata: [],
      dialogVisible: false,
      fullscreenLoading: false,
      firstPlayFlag: true, //播放标记,
      interval: '',
      xaxisdata: [],
      histogramsitenum: [],
      histogramsitetype: [],
      tableData: [{
        date: '2016-05-02',
        name: '王小虎',
        address: '上海市普陀区金沙江路 1518 弄'
      }, {
        date: '2016-05-04',
        name: '王小虎',
        address: '上海市普陀区金沙江路 1517 弄'
      }, {
        date: '2016-05-01',
        name: '王小虎',
        address: '上海市普陀区金沙江路 1519 弄'
      }, {
        date: '2016-05-03',
        name: '王小虎',
        address: '上海市普陀区金沙江路 1516 弄'
      }]

    }
  },
  created() {
    this.GetSitesMap()
    // setTimeout(function() {
    //   this.InitSiteData;
    // }, 500)
    if (this.firstPlayFlag) {
      console.log(this.firstPlayFlag)
      this.InitSiteData()
      this.firstPlayFlag = false
      console.log(this.firstPlayFlag)
    }
    this.interval = setInterval(this.openFullScreen, 2000);
    // this.openFullScreen()
  },
  mounted() {
    setTimeout(async () => {
        var myChart = echarts.init(document.getElementById('main'))
        var histogram = echarts.init(document.getElementById('histogram'))
        var piecharts = echarts.init(document.getElementById('piecharts'))
        var lineChartSeven = echarts.init(document.getElementById("lineChartSeven"))
        echarts.registerMap('china', geoJson)

        //设置背景图片
        // let img = document.createElement('img')
        //     img.src = require('@/template/image/background.jpg')

        // 地图上散点数据
        //那个站点的数据不是在地图上的经纬度

        // var points = this.resdata
        // console.log(points)

        var points = [
          {value: [86.9023, 41.1482], itemStyle: {color: '#d26309'}},
          {value: [87.8695, 31.6846], itemStyle: {color: '#d26309'}},
          {value: [95.2402, 35.4199], itemStyle: {color: '#d26309'}},
          {value: [101.0652, 24.680], itemStyle: {color: '#d26309'}},
          {value: [102.7129, 38.166], itemStyle: {color: '#d26309'}},
          {value: [108.7813, 23.6426], itemStyle: {color: '#d26309'}},
          {value: [116.4551, 40.2539], itemStyle: {color: '#d26309'}},
          {value: [118.8062, 31.9208], itemStyle: {color: '#d26309'}},
          {value: [125.8154, 44.2584], itemStyle: {color: '#d26309'}},
          {value: [126.1746, 43.5938], itemStyle: {color: '#d26309'}},
          {value: [127.9688, 45.368], itemStyle: {color: '#d26309'}},
          {value: [128.1445, 46.7156], itemStyle: {color: '#d26309'}},
        ]

        // 地图上线图数据
        var linesdata = [
          {coords: [[86.9023, 41.1482], [116.4551, 40.2539]], lineStyle: {color: '#de6a18'}},
          {coords: [[87.8695, 31.6846], [116.4551, 40.2539]], lineStyle: {color: '#de6a18'}},
          {coords: [[95.2402, 35.4199], [116.4551, 40.2539]], lineStyle: {color: '#de6a18'}},
          {coords: [[101.0652, 24.680], [116.4551, 40.2539]], lineStyle: {color: '#de6a18'}},
          {coords: [[102.7129, 38.166], [116.4551, 40.2539]], lineStyle: {color: '#de6a18'}},
          {coords: [[108.7813, 23.6426], [116.4551, 40.2539]], lineStyle: {color: '#de6a18'}},
          {coords: [[116.4551, 40.2539], [116.4551, 40.2539]], lineStyle: {color: '#de6a18'}},
          {coords: [[118.8062, 31.9208], [116.4551, 40.2539]], lineStyle: {color: '#de6a18'}},
          {coords: [[125.8154, 44.2584], [116.4551, 40.2539]], lineStyle: {color: '#de6a18'}},
          {coords: [[126.1746, 43.5938], [116.4551, 40.2539]], lineStyle: {color: '#de6a18'}},
          {coords: [[127.9688, 45.368], [116.4551, 40.2539]], lineStyle: {color: '#de6a18'}},
          {coords: [[128.1445, 46.7156], [116.4551, 40.2539]], lineStyle: {color: '#de6a18'}},
        ]
      var linesdata1 = [
          {coords: [[116.4551, 40.2539], [86.9023, 41.1482]], lineStyle: {color: '#de6a18'}},
          {coords: [[116.4551, 40.2539], [87.8695, 31.6846]], lineStyle: {color: '#de6a18'}},
          {coords: [[116.4551, 40.2539], [95.2402, 35.4199]], lineStyle: {color: '#de6a18'}},
          {coords: [[116.4551, 40.2539], [101.0652, 24.680]], lineStyle: {color: '#de6a18'}},
          {coords: [[116.4551, 40.2539], [102.7129, 38.166]], lineStyle: {color: '#de6a18'}},
          {coords: [[116.4551, 40.2539], [108.7813, 23.6426]], lineStyle: {color: '#de6a18'}},
          {coords: [[116.4551, 40.2539], [116.4551, 40.2539]], lineStyle: {color: '#de6a18'}},
          {coords: [[116.4551, 40.2539], [118.8062, 31.9208]], lineStyle: {color: '#de6a18'}},
          {coords: [[116.4551, 40.2539], [125.8154, 44.2584]], lineStyle: {color: '#de6a18'}},
          {coords: [[116.4551, 40.2539], [126.1746, 43.5938]], lineStyle: {color: '#de6a18'}},
          {coords: [[116.4551, 40.2539], [127.9688, 45.368]], lineStyle: {color: '#de6a18'}},
          {coords: [[116.4551, 40.2539], [128.1445, 46.7156]], lineStyle: {color: '#de6a18'}},
        ]
        //var planePath = 'arrow';
        var plane_path = 'path://M1705.06,1318.313v-89.254l-319.9-221.799l0.073-208.063c0.521-84.662-26.629-121.796-63.961-121.491c-37.332-0.305-64.482,36.829-63.961,121.491l0.073,208.063l-319.9,221.799v89.254l330.343-157.288l12.238,241.308l-134.449,92.931l0.531,42.034l175.125-42.917l175.125,42.917l0.531-42.034l-134.449-92.931l12.238-241.308L1705.06,1318.313z';
        // var xaxisdata = ['亚洲', '欧洲', '北美洲', '南美洲', '非洲', '大洋洲']
        var xaxisdata = ["北京市", "黑龙江", "吉林", "青海", "新疆", "西藏", "云南", "广西", "江苏", "甘肃"]
        // var xaxisdata = this.xaxisdata
        // var histogramsitenum = this.histogramsitenum
        var histogramsitenum = [45, 9, 10, 2, 1, 6, 8, 14, 1, 3]

        // var histogramsitetype = this.histogramsitetype
        var histogramsitetype = [50, 9, 4, 1, 4, 12, 1, 3, 7, 1]
        var piedata = [{
          value: 45,
          name: '北京市',
        },
          {
            value: 9,
            name: '黑龙江'
          },
          {
            value: 10,
            name: '吉林'
          },
          {
            value: 2,
            name: '青海'
          },
          {
            value: 1,
            name: '新疆'
          },
          {
            value: 6,
            name: '西藏'
          },
          {
            value: 8,
            name: '云南'
          },
          {
            value: 14,
            name: '广西',
          },
          {
            value: 1,
            name: '江苏',
          },
          {
            value: 3,
            name: '甘肃',
          }
        ]

        var option = {
          backgroundColor: '#030f28',
          geo: {
            map: 'china', //地图类型
            aspectScale: 0.75, //地图长宽比
            zoom: 1.1, //当前视角缩放比
            roam: true,
            label: {
              emphasis: {
                show: false
              }
            },
            itemStyle: {
              normal: {
                borderColor: 'rgba(147, 235, 248, 1)',
                borderWidth: 1,
                areaColor: {
                  type: 'radial', //径向渐变
                  x: 0.5,
                  y: 0.5,
                  r: 0.8,
                  colorStops: [{
                    offset: 0,
                    color: 'rgb(147,235,248,0)' //0处的颜色
                  }, {
                    offset: 1,
                    color: 'rgb(147,235,248,.2)' //100%处的颜色
                  }],
                  toGlobalCoord: true
                },
                shadowColor: 'rgb(128, 217, 248, 1)',
                shadowOffsetX: -2,  //阴影
                shadowOffsetY: 2,
                shadowBlur: 10
              },
              emphasis: {
                areaColor: '#389BB7',
                borderWidth: 0
              }
            },
            regions: [{
              name: '南海诸岛',
              itemStyle: {
                opacity: 0
              }
            }]
          },
          series: [
            //配置地图相关参数，绘制地图
            {
              type: 'map',
              label: {
                normal: {
                  show: true,
                  textStyle: {
                    color: '#1DE9B6'
                  }
                },
                emphasis: {
                  textStyle: {
                    color: 'rgb(183, 185, 14)'
                  }
                }
              },
              itemStyle: { //地图区域图样形式
                normal: {
                  borderColor: 'rgb(147, 235, 248)',
                  borderWidth: 1,
                  areaColor: {
                    type: 'radial',
                    x: 0.5,
                    y: 0.5,
                    r: 0.8,
                    colorStops: [{
                      offset: 0,
                      color: 'rgb(31, 54, 150)' //0%颜色
                    }, {
                      offset: 1,
                      color: 'rgb(89, 128, 142)'
                    }],
                    toGlobalCoord: true
                  }
                },
                emphasis: {
                  areaColor: 'rgb(46, 229, 206)',
                  borderWidth: 0.1
                }
              },
              zoom: 1.1,
              map: 'china',
              geoIndex: 0,
              // center: [116.4551, 40.2539],
              // roam: true,
              // scaleLimit: {
              // min: 1,
              // max: 2
              // },
            },
            //地图散点图的配置
            {
              type: 'effectScatter',
              coordinateSystem: 'geo',
              showEffectOn: 'emphasis',
              zlevel: 1,
              symbolSize: 8, //散点大小
              // data: test_point,
              data: points,
              rippleEffect: { //涟漪特效配置
                period: 15, //动画周期，秒数
                scale: 4,  // 动画中波纹的最大缩放比例
                brushType: 'fill'
              }
            },
            // 地图线图的配置
            {
              type: 'lines',
              zlevel: 2,
              effect: {
                show: true,
                period: 4,
                trailLength: 0,
                symbol: plane_path,
                symbolSize: 15,

              },
              lineStyle: {
                normal: {
                  color: '#179f12',
                  width: 1,
                  curveness: 0.35,
                  opacity: 0.5,
                  type: 'solid'

                }
              },
              data: linesdata1
            }
          ]
        }
        var option1 = {
          title: {
            text: '站点分布情况',
            textStyle: {
              color: '#ddd'
            }
          },
          xAxis: {
            type: 'category',
            data: xaxisdata,
            axisLabel: {
              show: true,
              textStyle: {
                color: '#ddd'
              }
            }
            // data: ['亚洲', '欧洲', '北美洲', '南美洲', '非洲', '大洋洲', '南极洲']
          },
          yAxis: {
            type: 'value',
            axisLabel: {
              show: true,
              textStyle: {
                color: '#ddd'
              }
            }
          },
          legend: {
            data: ['站点个数', '站点类型(种)'],
            textStyle: {
              color: '#ddd'
            }
          },
          series: [{
            name: '站点个数',
            data: histogramsitenum,
            textStyle: {
              color: '#ddd'
            },
            itemStyle: {
              normal: {
                color: 'rgba(47,173,255,0.51)'
              }
            },
            type: 'bar',
            label: {
              show: true,
              position: 'top'
            }
          },
            {
              name: '站点类型(种)',
              data: histogramsitetype,
              textStyle: {
                color: '#ddd'
              },
              type: 'bar',
              itemStyle: {
                normal: {
                  color: '#c959ef'
                }
              },
              label: {
                show: true,
                position: 'top'
              }
            }]
        };
        var option2 = {
          title: {
            text: '站点分布情况',
            textStyle: {
              color: '#ddd'
            }
          },
          legend: {
            orient: "vertical",
            left: "right",
            // top: "top",
            data: ['亚洲', '欧洲', '北美洲', '南美洲', '非洲', '大洋洲', '南极洲']
          },
          series: [{
            type: 'pie',
            data: piedata,
            textStyle: {
              color: '#ddd'
            },
            itemStyle: {
              normal: {
                label: {
                  show: true,
                  formatter: '{b} : {d}%',
                  position: 'inside',
                  color: '#fff'
                },
                labelLine: {show: true}
              }
            }
          }],
          // silent: true,
          // animation: true,
          cursor: "pointer",
          // showEmptyCircle: true //占位园
        }
        var option3 = {
          title: {
            text: "",
            left: "1%",
          },
          tooltip: {
            trigger: "axis",
            backgroundColor: "",
            borderWidth: 0,
            axisPointer: {
              type: "line",
              lineStyle: {
                width: 2,
                type: "solid",
                color: "white",
                shadowColor: "rgba(255, 255, 255, 0.8)",
                shadowBlur: 20,
                shadowOffsetX: -5,
              },
            },
            textStyle: {align: "center"},
          },
          grid: {
            left: "3%",
            right: "4%",
            bottom: "10%",
            top: "18%",
            containLabel: true,
          },
          legend: {
            itemWidth: 10,
            itemHeight: 10,
            itemGap: 20,
            top: "top",
            right: "left",
            icon: "roundRect",
            textStyle: {
              fontSize: 14,
              fontWight: "bold",
              fontFamily: "SourceHanSansCN-Regular",
              color: "white",
            },
          },
          xAxis: {
            type: "category",
            boundaryGap: false,
            data: ["北京市", "黑龙江", "吉林", "青海", "新疆", "西藏", "云南", "广西", "江苏", "甘肃"],
            axisLine: {
              lineStyle: {
                type: "solid",
                color: "#00CCFF",
                width: "2",
                opacity: "0.4",
              },
            },
            axisLabel: {
              textStyle: {
                color: "#319899",
                fontSize: "14",
              },
            },
            interval: 1,
          },
          yAxis: {
            name: "个数",
            type: "value",
            splitNumber: 5,
            splitLine: {
              show: true,
              lineStyle: {
                type: "dashed",
                width: "2",
                color: "#00CCFF",
                opacity: "0.2",
              },
            },
            axisLine: {
              lineStyle: {
                type: "solid",
                color: "#00CCFF",
                width: "2",
                opacity: "0.4",
              },
            },
            axisLabel: {
              textStyle: {
                color: "#319899",
                fontSize: "14",
              },
            },
          },
          dataZoom: [
            {
              show: true,
              height: 10,
              bottom: 0,
              realtime: true,
              start: 0,
              end: 100,
            },
            {
              type: "inside",
              realtime: true,
              start: 35,
              end: 100,
            },
          ],
          series: [
            {
              name: "站点个数",
              type: "line",
              showSymbol: false,
              symbol: "circle",
              symbolSize: 10,
              smooth: true,
              itemStyle: {
                normal: {
                  color: "#56F5D1",
                  lineStyle: {
                    width: 2,
                  },
                },
              },
              areaStyle: {
                //折线图颜色半透明
                color: {
                  type: "linear",
                  x: 0,
                  y: 0,
                  x2: 0,
                  y2: 1,
                  colorStops: [
                    {
                      offset: 0,
                      color: "rgba(86,245,209, 0.5)", // 0% 处的颜色
                    },
                    {
                      offset: 0.5,
                      color: "rgba(86,245,209, 0.1)", // 100% 处的颜色
                    },
                  ],
                  global: false, // 缺省为 false
                },
              },
              data: [45, 9, 10, 2, 1, 6, 8, 14, 1, 3],
            },
            {
              name: "站点类型(种)",
              type: "line",
              symbol: "circle",
              showSymbol: false,
              symbolSize: 10,
              smooth: true,
              itemStyle: {
                normal: {
                  color: "#FFC71E",
                  lineStyle: {
                    width: 2,
                  },
                },
              },
              areaStyle: {
                //折线图颜色半透明
                color: {
                  type: "linear",
                  x: 0,
                  y: 0,
                  x2: 0,
                  y2: 1,
                  colorStops: [
                    {
                      offset: 0,
                      color: "rgba(255,199,30, 0.5)", // 0% 处的颜色
                    },
                    {
                      offset: 0.5,
                      color: "rgba(255,199,30, 0.1)", // 100% 处的颜色
                    },
                  ],
                  global: false, // 缺省为 false
                },
              },
              data: [50, 9, 4, 1, 4, 12, 1, 3, 7, 1],
            },
          ],
        }
        myChart.setOption(option)
        histogram.setOption(option1)
        piecharts.setOption(option2)
        lineChartSeven.setOption(option3)
      }, 1000
    )
    ;
  },
  methods: {
    GetSitesMap() {
      getsitemap().then((res) => {
        // this.resdata = JSON.stringify(res.points);
        this.resdata = res.points;

        // console.log(this.resdata)
        this.$message({
          message: "查询成功!",
          type: "success"
        })
        // console.log("接到的数据",resdata);
      })
    },
    InitSiteData() {
      console.log("执行线程")
      getsitetypedata().then((res) => {
        // console.log(res)
      })
    },
    handleClose(done) {
      this.confirm('确认关闭?')
        .then(_ => {
          done();
        })
        .catch(_ => {
        });
    },

    openFullScreen() {
      const loading = this.$loading({
        lock: true,
        text: '努力加载中',
        spinner: 'el-icon-loading',
        background: 'rgba(0, 0, 0, 0.7)'
      });
      queryresultbyquerysitesdata().then((res) => {
        console.log(res)
        if (res.flag === true) {
          clearTimeout(this.interval);
          this.xaxisdata = JSON.stringify(res.data.xaxisdata);
          this.histogramsitenum = JSON.stringify(res.data.sitenum);
          this.histogramsitetype = JSON.stringify(res.data.sitetype);
          loading.close();
        }
      })
    },
    test() {
      console.log("测试用函数")
      console.log(this.xaxisdata[0])
      console.log(this.histogramsitenum[0])
      console.log(this.histogramsitetype[0])
    }
  }
}
</script>

<style lang="scss">
.map-data {
  width: 100%;
  height: 100%;
  background-color: #030f28;

  #main {
    width: 50%;
    height: 500px;
    display: inline-block;
  }

  #histogram {
    height: 350px;
    width: 25%;
    background-color: #030f28;
    display: inline-block;
    border: 1px solid #3585ef;
    margin-bottom: 80px;
  }

  #piecharts {
    height: 350px;
    width: 25%;
    background-color: #030f28;
    display: inline-block;
    border: 1px solid #3585ef;
    margin-bottom: 80px;
  }
}

#lineChartSeven {
  height: 400px;
  width: 100%;
  background-color: #030f28;
}

#div2 {
  height: 100px;
  width: 50%;
  background-color: #030f28;
}

#div3 {
  height: 100px;
  width: 50%;
  background-color: #030f28;
}
</style>
