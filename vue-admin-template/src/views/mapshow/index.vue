<template>
  <div class="map-data">
    <div id="main"></div>
    <div id="histogram"></div>
    <div id="piecharts"></div>
    <el-button
      type="primary"
      style="margin-left: 20px"
      @click="test"
      >查看柱状图和饼图?</el-button>
<!--    <el-button-->
<!--    type="primary"-->
<!--    @click="openFullScreen">-->
<!--    服务方式-->
<!--  </el-button>-->
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
import geoJson from '../../template/world.json'
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
      histogramsitetype: []
    }
  },
  created() {
    this.GetSitesMap()
    // setTimeout(function() {
    //   this.InitSiteData;
    // }, 500)
    if(this.firstPlayFlag) {
      console.log(this.firstPlayFlag)
      this.InitSiteData()
      this.firstPlayFlag = false
      console.log(this.firstPlayFlag)
    }
    this.interval  =  setInterval(this.openFullScreen, 2000);
    // this.openFullScreen()
  },
  mounted() {
    setTimeout(async () => {
        var myChart = echarts.init(document.getElementById('main'))
        var histogram = echarts.init(document.getElementById('histogram'))
        var piecharts = echarts.init(document.getElementById('piecharts'))
        echarts.registerMap('china', geoJson)

        //设置背景图片
        // let img = document.createElement('img')
        //     img.src = require('@/template/image/background.jpg')

        // 地图上散点数据
        //那个站点的数据不是在地图上的经纬度
        var points = this.resdata
        // console.log(points)

        // var points = [
        //   {value: [86.9023, 41.1482], itemStyle: {color: '#d26309'}},
        //   {value: [87.8695, 31.6846], itemStyle: {color: '#d26309'}},
        //   {value: [95.2402, 35.4199], itemStyle: {color: '#d26309'}},
        //   {value: [101.0652, 24.680], itemStyle: {color: '#d26309'}},
        //   {value: [102.7129, 38.166], itemStyle: {color: '#d26309'}},
        //   {value: [108.7813, 23.6426], itemStyle: {color: '#d26309'}},
        //   {value: [110.3467, 41.4899], itemStyle: {color: '#d26309'}},
        //   {value: [111.5332, 27.3779], itemStyle: {color: '#d26309'}},
        //   {value: [113.8668, 22.8076], itemStyle: {color: '#d26309'}},
        //   {value: [115.4004, 38.1688], itemStyle: {color: '#d26309'}},
        //   {value: [116.4551, 40.2539], itemStyle: {color: '#d26309'}},
        //   {value: [118.8062, 31.9208], itemStyle: {color: '#d26309'}},
        //   {value: [125.8154, 44.2584], itemStyle: {color: '#d26309'}},
        //   {value: [126.1746, 43.5938], itemStyle: {color: '#d26309'}},
        //   {value: [127.9688, 45.368], itemStyle: {color: '#d26309'}},
        //   {value: [128.1445, 46.7156], itemStyle: {color: '#d26309'}},
        // ]

        // 地图上线图数据
        var linesdata = [
          // {coords: [[118.8062, 31.9208], [119.4543, 25.9444]], lineStyle: {color: '#4ab2e5'}},
          // {coords: [[127.9688, 45.3684], [119.4543, 25.9444]], lineStyle: {color: '#4fb6d2'}},
          // {coords: [[110.3467, 41.4899], [119.4543, 25.9444]], lineStyle: {color: '#52b9c7'}},
          // {coords: [[125.8154, 44.2584], [119.4543, 25.9444]], lineStyle: {color: '#5abead'}},
          // {coords: [[116.4551, 40.2539], [119.4543, 25.9444]], lineStyle: {color: '#f34e2b'}},
          {coords: [[86.9023, 41.1482], [119.4543, 25.9444]], lineStyle: {color: '#b2d22a'}},
          {coords: [[87.8695, 31.6846], [119.4543, 25.9444]], lineStyle: {color: '#b2d22a'}},
          {coords: [[95.2402, 35.4199], [119.4543, 25.9444]], lineStyle: {color: '#b2d22a'}},
          {coords: [[101.0652, 24.680], [119.4543, 25.9444]], lineStyle: {color: '#b2d22a'}},
          {coords: [[102.7129, 38.166], [119.4543, 25.9444]], lineStyle: {color: '#b2d22a'}},
          {coords: [[108.7813, 23.6426], [119.4543, 25.9444]], lineStyle: {color: '#b2d22a'}},
          {coords: [[110.3467, 41.4899], [119.4543, 25.9444]], lineStyle: {color: '#b2d22a'}},
          {coords: [[111.5332, 27.3779], [119.4543, 25.9444]], lineStyle: {color: '#b2d22a'}},
          {coords: [[113.8668, 22.8076], [119.4543, 25.9444]], lineStyle: {color: '#b2d22a'}},
          {coords: [[115.4004, 38.1688], [119.4543, 25.9444]], lineStyle: {color: '#b2d22a'}},
          {coords: [[116.4551, 40.2539], [119.4543, 25.9444]], lineStyle: {color: '#b2d22a'}},
          {coords: [[118.8062, 31.9208], [119.4543, 25.9444]], lineStyle: {color: '#b2d22a'}},
          {coords: [[125.8154, 44.2584], [119.4543, 25.9444]], lineStyle: {color: '#b2d22a'}},
          {coords: [[126.1746, 43.5938], [119.4543, 25.9444]], lineStyle: {color: '#b2d22a'}},
          {coords: [[127.9688, 45.368], [119.4543, 25.9444]], lineStyle: {color: '#b2d22a'}},
          {coords: [[128.1445, 46.7156], [119.4543, 25.9444]], lineStyle: {color: '#b2d22a'}},
        ]
        //var planePath = 'arrow';
        var plane_path = 'path://M1705.06,1318.313v-89.254l-319.9-221.799l0.073-208.063c0.521-84.662-26.629-121.796-63.961-121.491c-37.332-0.305-64.482,36.829-63.961,121.491l0.073,208.063l-319.9,221.799v89.254l330.343-157.288l12.238,241.308l-134.449,92.931l0.531,42.034l175.125-42.917l175.125,42.917l0.531-42.034l-134.449-92.931l12.238-241.308L1705.06,1318.313z';
        // var xaxisdata = ['亚洲', '欧洲', '北美洲', '南美洲', '非洲', '大洋洲']
        var xaxisdata = ["河北省", "北京市", "天津市"]
        // var xaxisdata = this.xaxisdata
        // var histogramsitenum = this.histogramsitenum
        var histogramsitenum = [37, 51, 12]

        var histogramsitetype = this.histogramsitetype

        var piedata = [{
          value: 5,
          name: '亚洲',
        },
          {
            value: 2,
            name: '欧洲'
          },
          {
            value: 3,
            name: '北美洲'
          },
          {
            value: 4,
            name: '南美洲'
          },
          {
            value: 5,
            name: '非洲'
          },
          {
            value: 6,
            name: '大洋洲'
          },
          {
            value: 8,
            name: '南极洲'
          },
        ]

        var option = {
          backgroundColor: '#1e90ff',
          geo: {
            map: 'china', //地图类型
            aspectScale: 0.75, //地图长宽比
            zoom: 1.1, //当前视角缩放比
            roam: true,
            itemStyle: {
              normal: {
                areaColor: {
                  type: 'radial', //径向渐变
                  x: 0.5,
                  y: 0.5,
                  r: 0.8,
                  colorStops: [{
                    offset: 0,
                    color: 'rgb(255, 255, 255)' //0处的颜色
                  }, {
                    offset: 1,
                    color: 'rgb(85,190,182)' //100%处的颜色
                  }],
                  toGlobalCoord: true
                },
                // shadowColor: 'rgb(58, 115, 192)',
                // shadowOffsetX: 10,  //阴影
                // shadowOffsetY: 11
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
                  color: '#cb4e60',
                  width: 1,
                  curveness: 0.35,
                  opacity: 0.5,
                  type: 'solid'

                }
              },
              data: linesdata
            }
          ]
        }
        var option1 = {
          title: {
            text: '站点分布情况'
          },
          xAxis: {
            type: 'category',
            data: xaxisdata,
            // data: ['亚洲', '欧洲', '北美洲', '南美洲', '非洲', '大洋洲', '南极洲']
          },
          yAxis: {
            type: 'value'
          },
          legend: {
            data: ['站点个数', '站点类型(种)']
          },
          series: [{
            name: '站点个数',
            data: histogramsitenum,
            itemStyle: {
              normal: {
                color: '#4ad2ff'
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
            text: '站点分布情况'
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
        myChart.setOption(option)
        histogram.setOption(option1)
        piecharts.setOption(option2)
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
          if (res.flag === true){
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
  width: 800px;

  #main {
    width: 100%;
    height: 500px;
  }

  #histogram {
    height: 300px;
    width: 100%;
  }

  #piecharts {
    height: 300px;
    width: 100%;
  }
}

</style>
