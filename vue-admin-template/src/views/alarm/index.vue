<template>
  <div>
    <br/>
    <el-dialog
      title="提示"
      :visible.sync="dialogVisible"
      width="30%"
      >
      <span>{{ this.tokenin }}</span>
      <span slot="footer" class="dialog-footer">
          <el-button @click="dialogVisible = false">取 消</el-button>
          <el-button type="primary" @click="dialogVisible = false">确 定</el-button>
        </span>
      </el-dialog>

      <el-button
      type="primary"
      style="margin-left: 20px"
      @click="getEquipmentAlarm(); dialogVisible = false"
      >点击获取告警信息列表({{SiteIdNum}})</el-button>
      <p> </p>

    <!--此处枚举出每个站点下设备告警数量-->
    <el-collapse v-for="(value,index) in SiteId" v-model="activeNames"  @change="handleChange(index)" accordion>

          <el-collapse-item   :title="index+1 +'、'+value" :name="index"  style="margin-left:20px;" >

            <div>设备总数：{{equipment["deviceTotalCount"]}}</div>
            <div>正常设备总数：{{equipment["normalDeviceCount"]}}</div>
            <div>提示设备总数：{{equipment["warningDeviceCount"]}}</div>
            <div>故障设备总数：{{equipment["faultyDeviceCount"]}}</div>
            <div>离线设备总数：{{equipment["offlineDeviceCount"]}}</div>
            <div>未注册设备总数：{{equipment["unregistedDeviceCount"]}}</div>
            <div>紧急告警总数：{{equipment["alarmCriticalCount"]}}</div>
            <div>严重告警总数：{{equipment["alarmMajorCount"]}}</div>
            <div>一般告警总数：{{equipment["alarmMinorCount"]}}</div>
            <div>提示告警总数：{{equipment["alarmWarningCount"]}}</div>
          </el-collapse-item>



    </el-collapse>


</div>
</template>

<script>
import {show_token} from "@/api/tok";
import {equipmentAlarm, getSiteId}from "@/api/EquipmentAlarm"

export default {
  data() {
    return {
      name: "index",
      tokenin: '',
      dialogVisible: false,
      dialogVisible3:true,
      activeNames: [],
      SiteId : [],
      equipment:{'deviceTotalCount': 0, 'normalDeviceCount': 0, 'warningDeviceCount': 0, 'faultyDeviceCount': 0, 'offlineDeviceCount': 0, 'unregistedDeviceCount': 0, 'alarmCriticalCount': 0, 'alarmMajorCount': 0, 'alarmMinorCount': 0, 'alarmWarningCount': 0},
      SiteIdNum : 0
    };
  },
  created() {
    console.log("here is nothing");
  },
  mounted() {
  },
  methods: {
    getEquipmentAlarm(){
      show_token().then((res) => {
        this.tokenin = res.token;
      });

      getSiteId().then((res)=>{
          console.log("getSiteId");
          console.log(res.data);
          console.log(res.totalRecords);
          this.SiteId = res.data;
          console.log(this.SiteId)
          this.SiteIdNum = res.totalRecords;
      })

    },
     handleChange(val) {
        console.log("选中的值", val);
        let p ={
          "id": parseInt(val)
        }
        // let q = JSON.stringify(p)
        // console.log(q)
        // console.log(typeof q)

       console.log(this.activeNames)
        equipmentAlarm(p).then((res)=>{
          console.log("---equipmentAlarm---");
          console.log("res.data", res.data);
          this.equipment = res.data;
          console.log("this.equipment", res.data);

      })

      }

  }
}
</script>



