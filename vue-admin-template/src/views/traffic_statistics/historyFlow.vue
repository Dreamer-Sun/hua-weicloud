<template>

  <div>
    <p></p>
      <div style="margin-left:10px;">
       获取设备tagId
      </div>
    <p></p>
    <el-button type="primary" @click="GetSiteId " style="margin-left:10px;">请选择站点ID</el-button>

    <el-select v-model="siteId" placeholder="请选择" filterable>
        <el-option
          v-for="item in options"
          :key="item.value"
          :label="item.label"
          :value="item.value">
        </el-option>
    </el-select>
    <el-button type="primary" style="margin-left:10px;">请选择分页大小</el-button>
    <el-input-number v-model="pageSize" @change="handleChange" :min="1" :max="1000" label="分页的大小"></el-input-number>
    <el-button type="primary" style="margin-left:10px;">请选择分页序号</el-button>
    <el-input-number v-model="pageIndex" @change="handleChange" :min="1" :max="1000" label="分页的序号"></el-input-number>
    <el-button type="primary" style="margin-left:10px;" @click="queryTag ">获取列表</el-button>


    <el-table
        :data="tableData"
        style="width: 100%">
        <el-table-column
            label="序号"
            width="100"
            align="center">
          <template scope="scope">
            <span>{{(scope.$index + 1)}} </span>
          </template>
        </el-table-column>

        <el-table-column
          prop="siteId"
          label="siteId"
          width="fixed">
        </el-table-column>

        <el-table-column
          prop="tagId"
          label="tagId"
          width="fixed">
        </el-table-column>

        <el-table-column
          prop="tagName"
          label="tagName"
          width="100">
        </el-table-column>

         <el-table-column
          label="timeSelect"
          prop="selectTime"
          width="fixed"
          align="center">
           <template scope="scope">
            <div class="block">
              <span class="demonstration"></span>
              <el-date-picker

                  value-format="timestamp"
                v-model="scope.row.selectTime"
                type="daterange"
                range-separator="至"
                start-placeholder="开始日期"
                end-placeholder="结束日期">
              </el-date-picker>
            </div>
          </template>
        </el-table-column>

      <el-table-column

          label="点击查询历史接入客户数量"
          width="fixed"
          align="center">

        <template scope="scope">
          <el-link type="primary" @click="queryHistory(scope.row.siteId, scope.row.tagId, scope.row.selectTime)">点击查询</el-link>

        </template>



      </el-table-column>

    </el-table>
    <!--此处是显示历史接入客户数量-->
      <div class="app-container">
        <el-dialog
          title="历史接入客户数量图表"
          :visible.sync="dialogVisible"
          width="60%"
          @open="open()"
           append-to-body
          >
          <div class="echart" id="main" style="width: 100%; height: 500px; padding-top:20px"></div>

          <span slot="footer" class="dialog-footer">
            <el-button @click="dialogVisible = false">取 消</el-button>
            <el-button type="primary" @click="dialogVisible = false">确 定</el-button>
          </span>
        </el-dialog>
      </div>
    </div>

</template>




<script>
    import {getSiteData} from "@/api/getSiteData";
    import {queryHistoryflow, queryTag} from "@/api/traffic_statistics";
    import * as echarts from 'echarts';

    export default {
    data() {
      return {
          dialogVisible:false,
          //option是获取所有站点ID,siteId为选中的id
          options: [],
          siteId: '',
          pageSize:20,
          pageIndex:1,
          //设备tagId列表
          tableData: [{
            siteId: '9dffc44b-1824-42a4-ac48-616e3f0eaa2a',
            tagId: '31f35021-e656-472a-8937-9c6d6da76e6e',
            tagName: 'test'
          }],
          //选中的日期
          selectTime:'',
          historyFlowNum:[]
        }

    },
    created() {
      this.GetData();
    },

    methods: {
      initEcharts(){
        var chartDom = document.getElementById('main');
        var myChart = echarts.init(chartDom);
        var option;

        option = {
          tooltip: {
            trigger: 'axis',
            axisPointer: {
              type: 'cross',
              crossStyle: {
                color: '#999'
              }
            }
          },
          toolbox: {
            feature: {
              dataView: { show: true, readOnly: false },
              magicType: { show: true, type: ['line', 'bar'] },
              restore: { show: true },
              saveAsImage: { show: true }
            }
          },
          legend: {
            data: ['historyFlow', 'historyFlowLine']
          },
          xAxis: [
            {
              type: 'category',
              data: ["REALTIME_HOUR_FLOW", "REALTIME_DAY_FLOW", "capture_rate", "passersby", "visitors", "connected",
                      "within_one_hr", "one_hr_to_six_hrs", "more_than_six_hrs", "average_staytime", "first_time",
                      "occasionally", "regularly", "frequently", "repeat_rate", "humanflow"],
              axisPointer: {
                type: 'shadow'
              }
            }
          ],
          yAxis: [
            {
              type: 'value',
              name: 'historyFlow',
              min: 0,
              max: 500,
              interval: 50,
              axisLabel: {
                formatter: '{value} 人'
              }
            },
            {
              type: 'value',
              name: 'historyFlowLine',
              min: 0,
              max: 500,
              interval: 50,
              axisLabel: {
                formatter: '{value} 人'
              }
            }
          ],
          series: [
            {
              name: 'historyFlow',
              type: 'bar',
              tooltip: {
                valueFormatter: function (value) {
                  return value + ' 人';
                }
              },
              data: [
                2.0, 4.9, 7.0, 23.2, 25.6, 76.7, 135.6, 162.2, 32.6, 20.0, 6.4, 3.3,50,80,40,30
              ]
            },
            {
              name: 'historyFlowLine',
              type: 'line',
              yAxisIndex: 1,
              tooltip: {
                valueFormatter: function (value) {
                  return value + ' °C';
                }
              },
              data: [
                2.0, 4.9, 7.0, 23.2, 25.6, 76.7, 135.6, 162.2, 32.6, 20.0, 6.4, 3.3,50,80,40,30
              ]
              }
          ]
        };

        option && myChart.setOption(option);


      },
      open(){
        this.$nextTick(() => {
        //  执行echarts方法
          this.initEcharts()
          console.log("初始化echarts完毕")
        })
      },
      GetData() {
        getSiteData().then((res) => {
          console.log(res.data)
          this.options = [];
          for (let i = 0; i < res.data.length; i++) {
            this.siteList = {"value": '', "label": ''}
            this.siteList["value"] = res.data[i]["label"]
            this.siteList["label"] = res.data[i]["label"]
            this.options.push(this.siteList)
          }
          console.log("options", this.options)
        });
      },
      GetSiteId(){
        console.log(this.siteId)
      },
      handleChange(){
        console.log(this.pageSize);
      },
      queryTag(){
        console.log(this.startTime)
        console.log(this.siteId,this.pageIndex,this.pageSize)
        this.tableData = []
        var formData = new FormData;
        formData.append('siteId', this.siteId.slice(9))
        formData.append('pageIndex', this.pageIndex)
        formData.append('pageSize',this.pageSize)
        queryTag(formData).then((res)=>{
          console.log("调用queryTag成功")
          console.log(res.data)
          let tmp ={}

          for(let i=0;i<res.data.length;i++){
            tmp["siteId"] = this.siteId.slice(9)
            tmp["tagId"] = res.data[i]["tagId"]
            tmp["tagName"] = res.data[i]["tagName"]
            this.tableData.push(tmp)
            tmp ={}
          }
        })
      },
      // 查询历史接入客户流量
      queryHistory(siteId, tagId, selectTime){
        this.dialogVisible = true
        console.log(siteId, tagId, selectTime)
        console.log(typeof selectTime[0])
        if(selectTime[1]-selectTime[0]>=31536000000){
            this.$message.error('查询失败，最大时间差不超过一年' );
            return;
        }
        if (typeof selectTime[0]  === "undefined" ){
            this.$message.error('查询失败，请选择时间且时间差不超过一年' );
            return;
        }

        var formData = new FormData;
        formData.append('siteId', siteId)
        formData.append('tagId', tagId)
        formData.append('selectTime',selectTime)
        queryHistoryflow(formData).then((res)=>{
          console.log("调用queryHistoryflow成功")
          console.log(res.data)
          this.historyFlowNum = []
          for(let i =0;i<res.data.length;i++){
            this.historyFlowNum.push(res.data[i]["counts"][0]["count"])
          }
          console.log(this.historyFlowNum)
          //再次实例化图表
          let previewChart = echarts.init(document.getElementById('main'))
          previewChart.setOption({
             series: [{
                data: this.historyFlowNum
             },{
               data: this.historyFlowNum
             }]
          })


        })


      }

    }
  }
</script>
