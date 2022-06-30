<template>
  <div class="app-container">
    <el-button
      type="primary"
    >站点总数: {{ siteNum }}
    </el-button>

    <el-button
      type="primary"
      @click="dialogVisible = true"
    >站点删除
    </el-button>

    <el-button
      type="primary"
      @click="dialogVisible2 = true"
    >站点修改
    </el-button>

    <el-dialog
      title="删除站点 "
      :visible.sync="dialogVisible"
      width="30%"
    >
      <span>
        <el-select style="width:85%" multiple ref="searchSelect" @input.native="filterData" v-model="value1" filterable
                   placeholder="请选择">
          <el-option
            v-for="item in options"
            :key="item.value"
            :label="item.label"
            :value="item.value">
          </el-option>
        </el-select>
      </span>
      <span slot="footer" class="dialog-footer">
        <el-button @click="dialogVisible = false">取 消</el-button>
        <el-button type="primary" @click="DeleteSite ">确 定</el-button>
      </span>
    </el-dialog>

    <el-dialog
      title="修改站点"
      :visible.sync="dialogVisible2"
      width="100%"
    >
      <span>
        <el-form ref="form" :model="form" label-width="100px">
          <el-form-item label="站点id">
            <el-select style="width:85%"  ref="searchSelect" @input.native="filterData" v-model="value5" filterable
                       placeholder="请选择">
              <el-option
                v-for="item in options"
                :key="item.value"
                :label="item.label"
                :value="item.value">
              </el-option>
            </el-select>
          </el-form-item>
          <el-form-item label="站点名称">
            <el-input placeholder="示例值：site" v-model="form.name"></el-input>
          </el-form-item>
          <el-form-item label="站点描述">
            <el-input placeholder="示例值：site" v-model="form.description"></el-input>
          </el-form-item>

          <el-form-item label="	纬度">
            <el-input placeholder="示例值：50 纬度，北纬是正数，南纬是负数，比如北纬30.2度，传入30.2,；南纬50.76度，传入-50.76，纬度范围【-90，+90】"
                      v-model="form.latitude"></el-input>
          </el-form-item>
          <el-form-item label="经度">
            <el-input placeholder="示例值：111 经度，东经是正数，西经是负数，比如东经110度，传入110,；西经32.1度，传入-32.1，经度范围【-180，+180】"
                      v-model="form.longtitude"></el-input>
          </el-form-item>
          <el-form-item label="联系人">
            <el-input placeholder="示例值：David" v-model="form.contact"></el-input>
          </el-form-item>
          <el-form-item label="标签">
            <el-input placeholder='示例值：["abcd"]' v-model="form.tag"></el-input>
          </el-form-item>
          <el-form-item label="是否隔离">
            <el-select v-model="value3" placeholder="请选择">
                <el-option
                  v-for="item in options3"
                  :key="item.value"
                  :label="item.label"
                  :value="item.value">
                </el-option>
            </el-select>
          </el-form-item>
          <el-form-item label="邮箱">
            <el-input placeholder="示例值：tenant@huawei.com" v-model="form.email"></el-input>
          </el-form-item>
          <el-form-item label="电话号码">
            <el-input placeholder="示例值：15277431823" v-model="form.phone"></el-input>
          </el-form-item>
          <el-form-item label="邮编">
            <el-input placeholder="示例值：215000" v-model="form.postcode"></el-input>
          </el-form-item>
          <el-form-item label="地址">
            <el-input placeholder="示例值：66 JiangYun Road" v-model="form.address"></el-input>
          </el-form-item>


        </el-form>

      </span>
      <span slot="footer" class="dialog-footer">
        <el-button @click="dialogVisible2 = false">取 消</el-button>
        <el-button type="primary" @click="ChangeSite">确 定</el-button>
      </span>
    </el-dialog>


    <p></p>
    <el-input v-model="filterText" placeholder="Filter keyword" style="margin-bottom:30px;"/>

    <el-tree
      ref="tree2"
      :data="tableData"
      :props="defaultProps"
      :filter-node-method="filterNode"
      class="filter-tree"
      default-expand-all
    />

  </div>
</template>

<script>
import {getSiteData} from "@/api/getSiteData.js";
import {deleteSite} from "@/api/deleteSite";
import {updateSite} from "@/api/updateSite";

export default {

  data() {
    return {
      siteNum: '',
      filterText: '',
      dialogVisible: false,
      dialogVisible2: false,
      siteList: {"value": '', "label": ''},
      options: [],
      options2: [{
        value: 'AP',
        label: 'AP'
      }, {
        value: 'AR',
        label: 'AR'
      }, {
        value: 'FW',
        label: 'FW'
      }, {
        value: 'AC',
        label: 'AC'
      }, {
        value: 'LSW',
        label: 'LSW'
      }, {
        value: 'ONT',
        label: 'ONT'
      }, {
        value: 'OLT',
        label: 'OLT'
      }
      ],
      options3: [{
        value: 'true',
        label: 'true'
      }, {
        value: 'false',
        label: 'false'
      }],
      //value1修改站点时，选中的站点id, value2是指选择的站点类型
      value1: [],
      value2: [],
      //value3 是指isolated  value4是指cloneDevices  value5是指修改站点时，所选择id
      value3: '',
      value4: '',
      value5: '',
      tableData: [],
      //form是更新站点的表单
      form: {
        name: '',
        description: '',
        latitude: '',
        longtitude: '',
        contact: '',
        tag: '["abcd"]',
        isolated: "false",
        email: '',
        phone: '',
        postcode: '',
        address: ''
      },
      data2: [{
        id: 1,
        label: '设备id 1 ',
        children: [{
          id: 4,
          label: 'tenantId',
          children: [{
            id: 9,
            label: 'Level three 1-1-1'
          }, {
            id: 10,
            label: 'Level three 1-1-2'
          }]
        }]
      },
        {
          id: 2,
          label: '设备id 2',
          children: [{
            id: 5,
            label: 'Level two 2-1'
          }, {
            id: 6,
            label: 'Level two 2-2'
          }]
        },
        {
          id: 3,
          label: '设备id  3',
          children: [{
            id: 7,
            label: 'Level two 3-1'
          }, {
            id: 8,
            label: 'Level two 3-2'
          }]
        }],
      defaultProps: {
        children: 'children',
        label: 'label'
      }
    }
  },
  watch: {
    filterText(val) {
      this.$refs.tree2.filter(val)
    }
  },
  created() {
    this.GetData();
  },

  methods: {
    filterNode(value, data, node) {
      //查询显示当前节点
      /*if (!value) return true;
      return data.label.indexOf(value) !== -1;*/
      console.log(value, data, node)
      //如果共有三级菜单，查询显示当前节点及所有子节点
      if (!value) return true;
      let if_one = data.label.indexOf(value) !== -1;
      let if_two =
        node.parent &&
        node.parent.data &&
        node.parent.data.label &&
        node.parent.data.label.indexOf(value) !== -1;
      let if_three =
        node.parent &&
        node.parent.parent &&
        node.parent.parent.data &&
        node.parent.parent.data.label &&
        node.parent.parent.data.label.indexOf(value) !== -1;
      let result_one = false;
      let result_two = false;
      let result_three = false;
      if (node.level === 1) {
        result_one = if_one;
      } else if (node.level === 2) {
        result_two = if_one || if_two;
      } else if (node.level === 3) {
        result_three = if_one || if_two || if_three;
      }
      return result_one || result_two || result_three;
    },
    GetData() {
      getSiteData().then((res) => {
        console.log(res.data)
        this.tableData = res.data;
        this.siteNum = res.totalRecords;
        console.log(this.tableData);
        this.options = [];
        for (let i = 0; i < this.tableData.length; i++) {
          this.siteList = {"value": '', "label": ''}
          this.siteList["value"] = this.tableData[i]["label"]
          this.siteList["label"] = this.tableData[i]["label"]
          this.options.push(this.siteList)
        }
        console.log("options", this.options)
      });
    },
    DeleteSite() {
      this.dialogVisible = true;
      let site = []
      for(let i = 0;i<this.value1.length;i++){
          site.push(this.value1[i].substring(11,this.value1[i].length))
      }
      console.log("SelectSite", site)
      var formdata = new FormData();
      formdata.append('sites', JSON.stringify(site))
      deleteSite(formdata).then((res)=>{
        console.log("调用deleteSite成功");
        console.log(res.success)
        console.log(res.data);
        this.$message({
              message: '恭喜你，已成功删除站点{'+ res.success +'},请刷新页面',
              type: 'success'
        });
      })

    },
    ChangeSite() {
      this.siteId = this.value5;
      this.dialogVisible2 = false;
      let str = this.siteId.substring(11,this.siteId.length)
      console.log("this.siteId", str)
      console.log("this.form", this.form)
      var formdata = new FormData();
      formdata.append('siteId', JSON.stringify(str));
      formdata.append("form", JSON.stringify(this.form))
      updateSite(formdata).then((res)=>{
        console.log("updateSite调用成功")
        console.log(res.data)
        this.$message({
            message: '恭喜你，已成功更新站点',
            type: 'success'
        });
      })
    },
// 对输入字符串控制
    filterData() {
      var str = this.$refs.searchSelect.$data.selectedLabel;// 此属性得到输入的文字
      // 控制的js
      if (str.length > 20) {
        this.$refs.searchSelect.$data.selectedLabel = str.substr(0, 21)
      }
    }
  }
}
</script>

