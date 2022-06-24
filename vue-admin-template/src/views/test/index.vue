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
      </el-table-column>
      <el-table-column
        label="设备ESN号"
        prop="esn">
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
      </el-table-column>
      <el-table-column
        label="资产编号"
        prop="resourceId">
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
      </el-table-column>
      <el-table-column
        label="系统IP地址"
        prop="systemIp">
      </el-table-column>
      <el-table-column
        label="设备补丁版本"
        prop="patchVersion">
      </el-table-column>
      <el-table-column
        label="开局使能开关"
        prop="ztpConfirm">
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
      </el-table-column>

      <el-table-column
        prop="deletedevice">
        <template slot-scope="scope">
          <el-popconfirm
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
              type="danger"
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
import {createdevice, deletedevice, getdeviceinfo} from "@/api/devicemanage";

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
      tableData: [{
        id: "1befef7f-2114-4e07-b86d-131112c45e56",
        name: "AirEngine9700D_M7046D819",
        esn: "1019C0072655",
        deviceModel: "AirEngine9700D-M",
        deviceType: "AP",
        status: "0",
        siteId: null,
        mac: "84-46-FE-F8-0C-11",
        ip: "119.8.241.126",
        neType: "AirEngine9700D-M",
        version: "V200R020C10SPC100",
        vendor: "HUAWEI",
        description: "",
        resourceId: null,
        tenantId: "8b45c790a0fe46438a625616cf18dcfe",
        tenantName: "C4_huawei_qiankun",
        siteName: null,
        createTime: "2022-04-24 17:26:07",
        registerTime: "2022-04-24 17:37:28",
        modifyTime: null,
        startupTime: "2022-04-22 01:53:05",
        tags: null,
        systemIp: null,
        patchVersion: null,
        ztpConfirm: false,
        manageStatus: "NORMAL",
        manageStatusDownReason: [],
        role: [
          "ACC"
        ],
        performance: 0
      },
        {
          id: "b7efe28f-e368-4f5c-bbd7-67b2854a5acd",
          name: "2102351BTJ0000000665",
          esn: "2102351BTJ0000000665",
          deviceModel: "AR161EW",
          deviceType: "AR",
          status: "4",
          siteId: null,
          mac: null,
          ip: null,
          neType: "AR161EW",
          version: null,
          vendor: null,
          description: null,
          resourceId: null,
          tenantId: "8b45c790a0fe46438a625616cf18dcfe",
          tenantName: "C4_huawei_qiankun",
          siteName: null,
          createTime: "2022-06-10 22:44:31",
          registerTime: null,
          modifyTime: null,
          startupTime: null,
          tags: null,
          systemIp: null,
          patchVersion: null,
          ztpConfirm: false,
          manageStatus: "NORMAL",
          manageStatusDownReason: [],
          role: [
            "ACC"
          ],
          performance: 0
        },
        {
          id: "4c2b223f-284b-4a06-b19b-dfead0c81dbc",
          name: "AP",
          esn: "",
          deviceModel: "AP2050DN",
          deviceType: "AP",
          status: "4",
          siteId: "794e25a1-2400-488e-9d1a-33d863b975b8",
          mac: null,
          ip: null,
          neType: "AP2050DN",
          version: null,
          vendor: null,
          description: "AP",
          resourceId: null,
          tenantId: "8b45c790a0fe46438a625616cf18dcfe",
          tenantName: "C4_huawei_qiankun",
          siteName: "site",
          createTime: "2022-05-29 23:14:49",
          registerTime: null,
          modifyTime: null,
          startupTime: null,
          tags: null,
          systemIp: "",
          patchVersion: null,
          ztpConfirm: false,
          manageStatus: "NORMAL",
          manageStatusDownReason: [],
          role: [
            "AP"
          ],
          performance: 0
        },
        {
          id: "46384ccf-72fb-43d7-8f2d-763f515c8921",
          name: "AP1",
          esn: "2102351BTJ0000000699",
          deviceModel: "AD9430DN-12",
          deviceType: "AP",
          status: "4",
          siteId: "49f552e3-ebb2-4946-aa9a-d031dabc83d8",
          mac: null,
          ip: null,
          neType: "AD9430DN-12",
          version: null,
          vendor: null,
          description: "AP",
          resourceId: null,
          tenantId: "8b45c790a0fe46438a625616cf18dcfe",
          tenantName: "C4_huawei_qiankun",
          siteName: "site85",
          createTime: "2022-06-10 17:31:18",
          registerTime: null,
          modifyTime: null,
          startupTime: null,
          tags: null,
          systemIp: "192.168.56.1",
          patchVersion: null,
          ztpConfirm: false,
          manageStatus: "NORMAL",
          manageStatusDownReason: [],
          role: [
            "AP"
          ],
          performance: 0
        },
        {
          id: "5b5512e3-4202-4645-99d4-f405cfa8a367",
          name: "AP1",
          esn: "2102351BTJ0000000111",
          deviceModel: "AP2050DN",
          deviceType: "AP",
          status: "4",
          siteId: "794e25a1-2400-488e-9d1a-33d863b975b8",
          mac: null,
          ip: null,
          neType: "AP2050DN",
          version: null,
          vendor: null,
          description: "AP1",
          resourceId: null,
          tenantId: "8b45c790a0fe46438a625616cf18dcfe",
          tenantName: "C4_huawei_qiankun",
          siteName: "site",
          createTime: "2022-05-29 23:30:20",
          registerTime: null,
          modifyTime: null,
          startupTime: null,
          tags: null,
          systemIp: "192.168.1.103",
          patchVersion: null,
          ztpConfirm: false,
          manageStatus: "ABNORMAL",
          manageStatusDownReason: [],
          role: [
            "AP"
          ],
          performance: 0
        }]
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
        this.totalRecords = res.data[0].totalRecords
        this.$message({
          message: 'Success!',
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
  }
}
</script>
