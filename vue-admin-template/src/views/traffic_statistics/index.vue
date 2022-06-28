<template>

  <!-- 2. 为ECharts准备一个具备大小（宽高）的Dom -->


  <div>
    <el-button type="primary" @click="GetTopN">请点击获取需查询终端TopN应用流量列表:</el-button>
    <el-cascader :options="topNlist" v-model="select_topN" filterable clearable></el-cascader>
    <el-button type="primary" @click="queryTopN">点击查询</el-button>

      <el-table
      :data="tableData"
      style="width: 100%">
      <el-table-column
        prop="siteId"
        label="siteId/站点ID"
        width="360">
      </el-table-column>
      <el-table-column
        prop="appDimension"
        label="appDimension/查询维度"
        width="fix">
      </el-table-column>
      <el-table-column
        prop="timeDimension"
        label="timeDimension/统计周期"
        width="fix">
      </el-table-column>
        <el-table-column
        prop="top"
        label="top/top流量数据个数"
        width="fix">
      </el-table-column>
    </el-table>

    <div id="main" style="width: 600px; height: 600px"> </div>





  </div>


</template>

<script>
// 1.导入echarts
import * as echarts from 'echarts';
import {getSiteData} from "@/api/getSiteData";
import {traffic_statistic} from "@/api/traffic_statistics";
export default {
  data() {

    return {
        tableData: [],
        select_topN : [],
        siteDataList:[],
        //饼状图列表
        applicationList:[
              { value: 100, name: 'Tiktok' },
              { value: 300, name: 'WeiXin' },
              { value: 580, name: 'QQ' },
              { value: 484, name: '王者荣耀' },
              { value: 300, name: '绝地求生' }
            ],
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
        //级联选择器
        topNlist: [],
        temp:{
        }
    }
  },
  created() {
    this.GetTopN()
  },
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
            data: this.applicationList
          }
        ]
      };

      option && myChart.setOption(option);
  },
  methods: {
    queryTopN(){
      this.temp["siteId"] = this.select_topN[0].slice(9)
      this.temp["appDimension"] = this.select_topN[1]
      this.temp["timeDimension"] = this.select_topN[2]
      this.temp["top"] = this.select_topN[3]
      this.tableData = []
      if(this.temp["siteId"]!=null)
        this.tableData.push(this.temp)
      this.temp={}
      console.log("this.tableData", this.tableData)

      var formData = new FormData;
      formData.append('siteId', this.select_topN[0].slice(9))
      formData.append('appDimension', this.select_topN[1])
      formData.append('timeDimension', this.select_topN[2])
      formData.append('top', this.select_topN[3])

      traffic_statistic(formData).then((res)=>{
        console.log(res.data)
        console.log("调用traffic_statistic成功")
        this.applicationList = []
        let tmp = {}
        for(let i=0;i<res.data.length;i++){
          tmp["value"] = res.data[i]["traffic"];
          tmp["name"] = res.data[i]["name"];
          this.applicationList.push(tmp);
          tmp = {};

        }
        //再次实例化图表
        let previewChart = echarts.init(document.getElementById('main'))
        previewChart.setOption({
             series: [{
                data: this.applicationList
             }]
         })


      })
    },

    GetTopN(){
      getSiteData().then((res) => {
        console.log(res.data)
        for (var i= 0;i<res.data.length;i++){
          this.siteDataList.push(res.data[i]["label"])
        }
      });
      //构造级联选择器
      for(var i =0;i<this.siteDataList.length;i++){
        this.temp["value"] = this.siteDataList[i];
        this.temp["label"] = this.siteDataList[i];
        this.temp["children"] = this.topN_child;
        this.topNlist.push(this.temp);
        this.temp = {}
      }

      console.log("SiteDataList", this.siteDataList)
      console.log("here is query topN", this.select_topN)
    }
  },
}
</script>

<style lang="less" scoped>
</style>
