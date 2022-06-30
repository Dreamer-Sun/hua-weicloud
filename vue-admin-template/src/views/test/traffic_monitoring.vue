<template>
  <div>
  <div style="width: 100%; height: 500px" ref="factor"></div>
  <div>
      <el-button type="info" @click="Stopupdatedata">点击刷新</el-button>
  </div>
  </div>
</template>
<script>
import request from '@/utils/request'
import echarts from 'echarts'
import {getnetworktraffic} from "@/api/devicemanage";

export default {
  inject: ['reload'],
  data() {
    return {        // 定义图表，各种参数
      name: "Micro_radar_target",
      data1: [],
      data2: [],
      interval: '',
    }
  },
  created() {
    this.GetData();
  },
  mounted() {
    // this.GetData()
    setTimeout(() => {
      var option = {
        backgroundColor: "lightblue",
        series: {
          type: "sankey",
          layout: "none",
          // data: [
          //   {
          //     name: "设备网络速率",
          //   },
          //   {
          //     name: "站点网络速率",
          //   },
          //   {
          //     name: "北京市",
          //   },
          //   {
          //     name: "天津市",
          //   },
          //   {
          //     name: "河北省",
          //   },
          //   {
          //     name: "山东省",
          //   },
          // ],
          data: this.data1,
          links: this.data2,
          // links: [
          //   {
          //     source: "设备网络速率",
          //     arget: "站点网络速率",
          //     value: 5,
          //   },
          //   {
          //     source: "设备网络速率",
          //     target: "北京市",
          //     value: 3,
          //   },
          //   {
          //     source: "设备网络速率",
          //     target: "天津市",
          //     value: 8,
          //   },
          //   {
          //     source: "站点网络速率",
          //     target: "河北省",
          //     value: 2,
          //   },
          //   {
          //     source: "站点网络速率",
          //     target: "山东省",
          //     value: 3,
          //   },
          // ],
        },
      }
      // console.log("optionsssssssssssss", option)
      let myechart = echarts.init(this.$refs.factor) //初始化一个echarts
      myechart.setOption(option)  //setOption 用this.option中的数据开始作图
    }, 1000)


  },
  methods: {
    GetData() {
      getnetworktraffic().then((res) => {
        // console.log(res.data[0])
        this.data1 = JSON.parse(JSON.stringify((res.data[0]).ratelist))
        this.data2 = JSON.parse(JSON.stringify((res.data[0]).linklist))
        //
        // this.$set(this.data, (res.data[0]).ratelist)
        // this.$set(this.links,(res.data[0]).linklist)
        // console.log(this.data1)
        // console.log(this.data2)
      })
    },
    Stopupdatedata() {
      this.interval = setTimeout(this.reload, 5000);
      this.$message ({
        type: 'success',
        message: '刷新'
      })
    }
  },

};
</script>
<style scoped>
h1, h2 {
  font-weight: normal;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}

a {
  color: #42b983;
}
</style>
