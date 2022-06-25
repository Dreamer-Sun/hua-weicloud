<template>
  <div>
    <div>
      <el-button type="primary" @click="dialogVisible = true">
        创建设备
      </el-button>
    </div>
    <el-dialog
      title="创建设备"
      :visible.sync="dialogVisible"
      width="35%"
      :before-close="handleClose">
      <div>
        <el-input v-model="inputesn" placeholder="设备ESN号       示例值：2102351BTJ0000000666" type="text"
                  size="small "></el-input>
        <el-input v-model="inputname" placeholder="设备名称       示例值：测试设备1" type="text" size="small "></el-input>
        <el-input v-model="inputsiteID" placeholder="站点ID       示例值：84a5eb1d-0985-4c9a-b747-f7572f0e2fe5" type="text"
                  size="small "></el-input>
        <el-input v-model="inputdescription" placeholder="设备详情描述       示例值：AP1" type="text" size="small "></el-input>
        <el-input v-model="inputresourceId" placeholder="资产编号       示例值：HUAWEI" type="text" size="small "></el-input>
        <el-input v-model="inputdeviceModel" placeholder="设备款型       示例值：AP2050DN" type="text" size="small "></el-input>
        <el-input v-model="inputsystemIp" placeholder="系统IP地址       示例值：192.168.1.1" type="text"
                  size="small "></el-input>
        <el-input v-model="inputtags" placeholder="设备标签列表       示例值：	-" type="text" size="small "></el-input>
        <el-input v-model="inputztpConfirm" placeholder="用户确认开局使能开关       示例值：true" type="text"
                  size="small "></el-input>
        <el-input v-model="inputrole" placeholder="设备角色       示例值：['Gateway']" type="text" size="small "></el-input>
      </div>

      <span slot="footer" class="dialog-footer">
        <el-button @click="dialogVisible = false"> 取 消 </el-button>
        <el-button type="primary" @click="dialogVisible = false; CreateDevice()"> 确 定</el-button>
      </span>
    </el-dialog>
    <div>
      <el-backtop :bottom="100">
      </el-backtop>
    </div>
    <el-table
      ref="multipleTable"
      :data="tableData"
      style="width: 100%">
      <el-table-column type="expand">
        <template slot-scope="props">
          <el-form label-position="left" inline class="demo-table-expand">
            <el-form-item label="设备ID">
              <span>{{ props.row.id }}</span>
            </el-form-item>
            <el-form-item label="设备名称">
              <span>{{ props.row.name }}</span>
            </el-form-item>
            <el-form-item label="设备类型">
              <span>{{ props.row.deviceType }}</span>
            </el-form-item>
            <el-form-item label="设备MAC">
              <span>{{ props.row.mac }}</span>
            </el-form-item>
            <el-form-item label="设备IP">
              <span>{{ props.row.ip }}</span>
            </el-form-item>
            <el-form-item label="租户名称">
              <span>{{ props.row.tenantName }}</span>
            </el-form-item>
            <el-form-item label="创建时间">
              <span>{{ props.row.createTime }}</span>
            </el-form-item>
            <el-form-item label="设备首次注册时间">
              <span>{{ props.row.registerTime }}</span>
            </el-form-item>
            <el-form-item label="修改时间">
              <span>{{ props.row.modifyTime }}</span>
            </el-form-item>
            <el-form-item label="设备重启时间">
              <span>{{ props.row.startupTime }}</span>
            </el-form-item>
            <el-form-item label="系统IP地址">
              <span>{{ props.row.systemIp }}</span>
            </el-form-item>
            <el-form-item label="设备管理状态">
              <span v-if="props.row.manageStatus.indexOf('ABNORMAL') != -1" style="color: #FF5151">{{
                  'ABNORMAL'
                }}</span>
              <span v-else style="color: #67C23A;">{{ 'NORMAL' }}</span>
            </el-form-item>
          </el-form>

        </template>

      </el-table-column>
      <el-table-column
        label="设备 ID"
        prop="id">
      </el-table-column>
      <el-table-column
        label="设备名称"
        prop="name">
        <template slot-scope="scope">
          <div v-if="!scope.row.isEdit">{{ scope.row.name }}</div>
          <div v-else><el-input v-model="scope.row.name"></el-input></div>
        </template>
      </el-table-column>
      <el-table-column
        label="设备ESN号"
        prop="esn">
        <template slot-scope="scope">
          <div v-if="!scope.row.isEdit">{{ scope.row.esn }}</div>
          <div v-else><el-input v-model="scope.row.esn"></el-input></div>
        </template>
      </el-table-column>
      <el-table-column
        label="设备款型"
        prop="deviceModel">
      </el-table-column>
      <el-table-column
        label="设备类型"
        prop="deviceType">
      </el-table-column>
      <el-table-column
        label="设备状态"
        prop="status">
      </el-table-column>
      <el-table-column
        label="设备所属站点ID"
        prop="siteId">
        <template slot-scope="scope">
          <div v-if="!scope.row.isEdit">{{ scope.row.siteId }}</div>
          <div v-else><el-input v-model="scope.row.siteId"></el-input></div>
        </template>
      </el-table-column>
      <el-table-column
        label="设备MAC"
        prop="mac">
      </el-table-column>
      <el-table-column
        label="设备IP"
        prop="ip">
      </el-table-column>
      <el-table-column
        label="设备款型"
        prop="neType">
      </el-table-column>
      <el-table-column
        label="设备软件版本"
        prop="version">
      </el-table-column>
      <el-table-column
        label="设备制造商"
        prop="vendor">
      </el-table-column>
      <el-table-column
        label="设备备注信息"
        prop="description">
        <template slot-scope="scope">
          <div v-if="!scope.row.isEdit">{{ scope.row.description }}</div>
          <div v-else><el-input v-model="scope.row.description"></el-input></div>
        </template>
      </el-table-column>
      <el-table-column
        label="资产编号"
        prop="resourceId">
        <template slot-scope="scope">
          <div v-if="!scope.row.isEdit">{{ scope.row.resourceId }}</div>
          <div v-else><el-input v-model="scope.row.resourceId"></el-input></div>
        </template>
      </el-table-column>
      <el-table-column
        label="租户ID"
        prop="tenantId">
      </el-table-column>
      <el-table-column
        label="租户名称"
        prop="tenantName">
      </el-table-column>
      <el-table-column
        label="站点名称"
        prop="siteName">
      </el-table-column>
      <el-table-column
        label="创建时间"
        prop="createTime">
      </el-table-column>
      <el-table-column
        label="设备首次注册时间"
        prop="registerTime">
      </el-table-column>
      <el-table-column
        label="修改时间"
        prop="modifyTime">
      </el-table-column>
      <el-table-column
        label="设备重启时间"
        prop="startupTime">
      </el-table-column>
      <el-table-column
        label="设备标签列表"
        prop="tags">
        <template slot-scope="scope">
          <div v-if="!scope.row.isEdit">{{ scope.row.tags }}</div>
          <div v-else><el-input v-model="scope.row.tags"></el-input></div>
        </template>
      </el-table-column>
      <el-table-column
        label="系统IP地址"
        prop="systemIp">
        <template slot-scope="scope">
          <div v-if="!scope.row.isEdit">{{ scope.row.systemIp }}</div>
          <div v-else><el-input v-model="scope.row.systemIp"></el-input></div>
        </template>
      </el-table-column>
      <el-table-column
        label="设备补丁版本"
        prop="patchVersion">
      </el-table-column>
      <el-table-column
        label="开局使能开关"
        prop="ztpConfirm">
        <template slot-scope="scope">
          <div v-if="!scope.row.isEdit">{{ scope.row.ztpConfirm }}</div>
          <div v-else>
            <el-select v-model="value" placeholder="">
              <el-option
                v-for="item in options"
                :key="item.value"
                :label="item.label"
                :value="item.value">
              </el-option>
            </el-select>
          </div>
        </template>
      </el-table-column>
      <el-table-column
        label="设备管理状态"
        prop="manageStatus">
        <template slot-scope="scope">
          <div v-if="scope.row.manageStatus.indexOf('ABNORMAL') != -1" style="color: #FF5151">{{ 'ABNORMAL' }}</div>
          <div v-else style="color: #67C23A;">{{ 'NORMAL' }}</div>
        </template>
      </el-table-column>
      <el-table-column
        label="管理状态down原因"
        prop="manageStatusDownReason">
      </el-table-column>
      <el-table-column
        label="设备角色"
        prop="role">
<!--        <template slot-scope="scope">-->
<!--          <div v-if="!scope.row.isEdit">{{ scope.row.role }}</div>-->
<!--          <div v-else><el-input v-model="scope.row.role"></el-input></div>-->
<!--        </template>-->
      </el-table-column>
      <el-table-column
        prop="deletedevice" label="处理">
        <template slot-scope="scope">
          <el-button size="mini" @click="EditDev(scope.$index, scope.row)">
            {{ scope.row.isEdit ? "完成" : "编辑" }}
          </el-button>
          <el-popconfirm
            size="mini"
            confirm-button-text="确认"
            cancel-button-text="取消"
            icon="el-icon-info"
            icon-color="red"
            confirm-button-type="danger"
            title="确认删除吗?将无法撤回!"
            @onConfirm="DeleteDevice(scope.$index)"
          >
            <el-button
              slot="reference"
              style="margin-left: 10px"
              type="danger"
              size="mini"
              circle
              icon="el-icon-delete"
            ></el-button>
          </el-popconfirm>
        </template>
      </el-table-column>
    </el-table>
    <div class="block">
      <el-pagination
        @size-change="handleSizeChange"
        @current-change="handleCurrentChange"
        :current-page="currentPage"
        :page-sizes="[3, 5, 7, 10]"
        :page-size="3"
        layout="total, sizes, prev, pager, next, jumper"
        :total=this.totalRecords>
      </el-pagination>
    </div>
  </div>
</template>
<style>
.demo-table-expand {
  font-size: 0;
}

.demo-table-expand label {
  width: 100px;
  color: #99a9bf;
}

.demo-table-expand .el-form-item {
  margin-right: 0;
  margin-bottom: 0;
  width: 35%;
}
</style>


<script>
import {
  show_token
} from "@/api/tok";
import {createdevice, deletedevice, getdeviceinfo, changedevice} from "@/api/devicemanage";

export default {
  data() {
    return {
      totalRecords: 40,
      currentPage: 1,
      pageIndex: 1,
      pageSize: 3,
      dialogVisible: false,
      inputesn: '',
      inputname: '',
      inputsiteID: '',
      inputdescription: '',
      inputresourceId: '',
      inputdeviceModel: '',
      inputsystemIp: '',
      inputtags: '',
      inputztpConfirm: '',
      inputrole: '',
      tableData: [],
      options: [
        {
        value: '1',
        label: 'true'
         },
        {
          value: '2',
          label: 'false'
        }],
      value: ''
    }
  },
  created() {
    this.GetDeviceInfo()
  },
  mounted() {
  },
  methods: {
    GetDeviceInfo() {
      let p = {
        'pageIndex': this.pageIndex,
        'pageSize': this.pageSize,
      }
      // console.log(p)
      getdeviceinfo(p).then((res) => {
        // console.log(res.data[0])
        this.tableData = res.data[0].datainfo
        // console.log(this.tableData)
        for (let i = 0; i < this.tableData.length; i++) {
          if(this.tableData[i].tags == null) {
            // console.log("tags是空的")
          }
          else {
            this.tableData[i].tags = (this.tableData[i].tags).join(',')
          }
          if(this.tableData[i].role == null) {
            // console.log("role是空的")
          }
          else {
            this.tableData[i].role = (this.tableData[i].role).join(',')
          }
        }
        // console.log(this.tableData)
        this.totalRecords = res.data[0].totalRecords
        this.$message({
          message: 'Get data success!!',
          type: 'success'
        })
      })
    },
    handleSizeChange(val) {
      // console.log(`每页 ${val} 条`);
      this.pageSize = val;
      this.GetDeviceInfo();
    },
    handleCurrentChange(val) {
      // console.log(`当前页: ${val}`);
      this.pageIndex = val;
      this.GetDeviceInfo();
    },
    handleClose(done) {
      this.$confirm('确认关闭?')
        .then(_ => {
          done();
        })
        .catch(_ => {
        });
    },
    CreateDevice() {
      let p = {
        data: {
          devices:
            // [{
            //   esn: "",
            //   name: "测试设备1",
            //   siteId: "84a5eb1d-0985-4c9a-b747-f7572f0e2fe5",
            //   description: "AP1",
            //   resourceId: "",
            //   deviceModel: "AP2050DN",
            //   systemIp: "",
            //   tags: ['测试'],
            //   ztpConfirm: "true",
            //   role: [
            //     "AP"
            //   ]
            // }]
          [{
            esn: this.inputesn,
            name: this.inputname,
            siteId: this.inputsiteID,
            description: this.inputdescription,
            resourceId: this.inputresourceId,
            deviceModel: this.inputdeviceModel,
            systemIp: this.inputsystemIp,
            tags: [this.inputtags],
            ztpConfirm: this.inputztpConfirm,
            role: [
              this.inputrole
            ]
            }]
        }
      }
      // console.log(p)
      createdevice(p).then((res) => {
        // console.log(res)
        this.$message({
          message: '创建成功!',
          type: 'success'
        })
      })
    },
    DeleteDevice(index) {
      console.log(this.tableData[index].id)
      let p = {
        data: {
          deviceIds: [this.tableData[index].id],
          reset: "false",
        }

      }
      deletedevice(p).then((res) => {
        // console.log(res)
        this.GetDeviceInfo()
        this.$message({
          message: 'Success!',
          type: 'success'
        })
      })
    },
    EditDev(index, row) {
      // this.GetDeviceInfo();
      if (row.isEdit) {
        let p = {
            deviceid: this.tableData[index].id,
            data: {
              name: this.tableData[index].name,
              description: this.tableData[index].description,
              resourceId: this.tableData[index].resourceId,
              siteId: this.tableData[index].siteId,
              esn: this.tableData[index].esn,
              tags: [this.tableData[index].tags],
              systemIp: this.tableData[index].systemIp,
              ztpConfirm: JSON.stringify(this.tableData[index].ztpConfirm),
              role: [this.tableData[index].role]
            }
        };
        // console.log("这里是p的值" ,p)
        changedevice(p).then((res) => {
          console.log(res);
          if(res.data.errcode === "0"){
            this.$message({
            message: "Change Success!!!",
            type: "info",
            showClose: true,
            duration: 5000,
            onClose: this.GetDeviceInfo
          });
          }
          else {
            this.$message({
            message: res.data.errmsg,
            type: "info",
            showClose: true,
            duration: 6000,
          });
          }
        });
        this.$set(row, "isEdit", false);
      } else {
        // 设置为编辑状态
        this.$set(row, "isEdit", true);
      }
      },
  }
}
</script>
