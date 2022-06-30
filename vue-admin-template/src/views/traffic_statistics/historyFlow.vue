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
    <el-button type="primary" style="margin-left:10px;" @click="queryTag ">点击查询</el-button>


    <el-table
        :data="tableData"
        style="width: 100%">
        <el-table-column
          prop="siteId"
          label="siteId"
          width="360">
        </el-table-column>
        <el-table-column
          prop="tagId"
          label="tagId"
          width="360">
        </el-table-column>
        <el-table-column
          prop="tagName"
          label="tagName">
        </el-table-column>
    </el-table>


  </div>

</template>




<script>
    import {getSiteData} from "@/api/getSiteData";
    import {queryTag} from "@/api/traffic_statistics";

    export default {
    data() {
      return {
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
        }

    },
      created() {
      this.GetData();
    },
    methods: {
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
        console.log(this.siteId,this.pageIndex,this.pageSize)
        var formData = new FormData;
        formData.append('siteId', this.siteId.slice(9))
        formData.append('pageIndex', this.pageIndex)
        formData.append('pageSize',this.pageSize)
        queryTag(formData).then((res)=>{
          console.log("调用queryTag成功")
        })
      }

    }
  }
</script>
